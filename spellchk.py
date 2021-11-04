import os
import glob
import sys
import json
import argparse
from collections import Counter

import docx2txt

def debug(k, v):
    if _dbg_:
        print(f'#DEBUG# {k}: {v}')
        input()

def main(infile):
    debug('infile', infile)
    
    try:
        text = read_manuscript(infile)
    except PermissionError:
        print(f"Failed!!! Please close {infile} and retry...", file=sys.stderr)
        sys.exit()
    
    path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "ko_spelling_rules.json"
    )
    with open(path) as json_file:
        rules = ruletable(json.load(json_file))
    
    global warnings_counter
    warnings_counter = Counter()
    
    for paragraph in text.split('\n'):
        lines = paragraph.split(". ")
        if len(lines) > 1:
            for line in lines[:-1]:
                check(rules, line + '.')
        check(rules, lines[-1])
    
    display_summary()

def ruletable(obj):
    table = []
    for rule in obj:
        caselist = []
        for rc in rule['cases']:
            if len(rc[0]) > 4 and rc[0][:4] in ['~은/는', '~이/가', '~을/를']:
                caselist.append(('~' + rc[0][1] + rc[0][4:], rc[1]))
                caselist.append(('~' + rc[0][3] + rc[0][4:], rc[1]))
            else:
                caselist.append((rc[0], rc[1]))
        table.append((rule['kind'], rule['name'], rule['desc'], caselist, rule['exception']))
    return table

def read_manuscript(infile):
    if infile.endswith('.docx'):
        text = docx2txt.process(infile)
    elif infile.endswith('.txt'):
        text = open(textfile).read()
    else:
        sys.exit('Unable to parse file!')
    return text

def check(rules, line):

    # avoid false positive on rule108
    if not korean(line):
        return None
    
    for rule in rules:
        kind, name, desc, cases, exceptions = rule
        for cs in cases:
            bad, good = cs[0], cs[1]
            
            bad_root = bad
            if bad.startswith('~'):
                bad_root = bad.lstrip('~')
            if bad.endswith(')') and korean(bad.rstrip(')').rsplit('(', 1)[1]):
                bad_root = bad_root.rsplit('(', 1)[0]
            
            debug('line', line)
            debug('bad_root', bad_root)
            
            if bad_root in line:
                loc = line.find(bad_root)
                skip = False
                for ex in exceptions:
                    beg, end = 0, -1
                    sz = 10
                    if loc > sz:
                        beg = loc - sz
                    if len(line) - loc > 10:
                        end = loc + sz
                    window = line[beg:end]
                    
                    if ex in window:
                        skip = True
                    
                if not skip:
                    cl = carret_loc(line, loc)
                    print('* ' + line)
                    print('  ' + ' ' * cl + '^')
                    message(kind, name, bad, good, desc)
                    warnings_counter[name] += 1

def carret_loc(s, loc):
    for c in s[:loc]:
        if korean(c):
            loc += 1
    return loc

def korean(s):
    assert isinstance(s, str)
    if len(s) == 1:
        return '가' < s < '힣'
    elif len(s) > 1:
        for ch in s:
            if korean(ch):
                break
        else:
            return False
        return True
    

def message(kind, name, bad, good, desc):
    if bad.startswith(". "):  # do not use lstrip() because it works differently
        bad = bad[2:]
    guide = " → ".join(filter(None, [bad, good]))
    ref = " : ".join(filter(None, [name, desc]))
    print(f'  => {guide}\t ({ref})\n\n')

def display_summary():
    print('=== Summary ===')
    for ele in sorted(warnings_counter):
        print(f'{ele} ==> count: {warnings_counter[ele]}')

def latest():
    return max(glob.glob('*.docx'), key=os.path.getctime)


if __name__ == '__main__':
    global _dbg_
    _dbg_ = False
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="filename", default=latest(), type=str)
    args = parser.parse_args()
    
    main(args.filename)
