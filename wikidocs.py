#!/usr/bin/python3
import urllib.request
from bs4 import BeautifulSoup
import sys


cmd = sys.argv[1]

if cmd == "toc":
    url = 'https://wikidocs.net/book/' + sys.argv[2]
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('.list-group-item > span')
    for title in titles[1:]:
         s = title.select('span')[0].text.strip()
         print(s)

elif cmd == "content":
    url = 'https://wikidocs.net/' + sys.argv[2]
    with urllib.request.urlopen(url) as f:
        html = f.read().decode('utf-8')
    
    soup = BeautifulSoup(html, 'html.parser')
    for content in soup.select('div.page-content'):
        print(content.text)
