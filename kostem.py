from utils import joinseq


"""Korean Stems"""

## A: Adjective (removed final consonant which will be dropped during conjugatation)
# can be conjugated to                  # VS            AS       ASL     ASN     AVC          AVM     AVN   
KS_Aa = '나ㅃ|바ㅃ'                     # +ㅏ지다       +ㅡ+다   +ㅡ+ㄹ  +ㅡ+ㄴ  +ㅏ서        +ㅡ+게  +ㅡ+지 
KS_Ab = '귀여|더|무서|쉬|차가|추|해로'  # +워지다       +ㅂ+다   +울     +운     +워서        +ㅂ+게  +ㅂ+지 
KS_Ac = '많|맑|않|작|좁'                # +아지다       +다      +을     +은     +아서        +게     +지    
KS_Ad = '다'            # sweet         # +ㄹ+아지다    +ㄹ+다   +ㄹ     +ㄴ     +ㄹ+아서     +ㄹ+게  +ㄹ+지 
KS_Ae = '예ㅃ|ㅋ'                       # +ㅓ지다       +ㅡ+다   +ㅡ+ㄹ  +ㅡ+ㄴ  +ㅓ서        +ㅡ+게  +ㅡ+지 
KS_Af = '다'            # different     # +ㄹ+라지다    +르+다   +를     +른     +ㄹ+라서     +르+게  +르+지 
KS_Ah = '깔끔|긴요|매끈|복잡|비슷|섬세|장대|장렬|졸렬|중요|지저분|진부|착|참신'
                                        # +해지다       +하다    +할     +한     +해서        +하게   +하지
KS_Ai = '붉'                            # +어지다       +다      +을     +은     +어서        +게     +지    
KS_Aj = '같|괜찮|낮|높|좋'              # +아지다       +다      +을     +은     +아서        +게     +지    
KS_Ak = '모'                            # x             +르다    +를     +르는   +ㄹ+라서     +르게   +르지  
KS_Al = '섣부'                          # x             +르다    +를     +른     +ㄹ+러서     +르게   +르지  
KS_Am = '맛있'                          # +어지다       +다      +을     +는     +어서        +게     +지    
KS_An = '낯서|머'                       # +ㄹ+어지다    +ㄹ+다   +ㄹ     +ㄴ     +ㄹ+어서     +ㄹ+게  +ㄹ+지 
KS_Ao = '넓'                            # +어지다       +다      +을     +은     +어서        +게     +지    
KS_Ap = '희'                            # +어지다       +다      +ㄹ     +ㄴ     +어서        +게     +지    
KS_Ar = '이로|평화로'                   # +와지다       +ㅂ+다   +울     +운     +와서        +ㅂ+게  +ㅂ+지 
KS_As = '나'                            # +아지다       +ㅅ+다   +을     +은     +아서        +ㅅ+게  +ㅅ+지 
KS_Aw = '고'                            # +와지다       +ㅂ+다   +울     +운     +와서        +ㅂ+게  +ㅂ+지 
KS_Ay = '못ㄷ'                          # +ㅚ+어+지다   +ㅚ+다,  +ㅚ+ㄹ  +ㅚ+ㄴ  +ㅚ+어ㅙ+서  +ㅚ+게  +ㅚ+지 ('ㅚ+어' can be shortend to 'ㅙ')

# '쓰다(bitter)' is not included because it is ambiguous with '쓰다(write)'



## roots of verb

### Both(intransives can conjugate to transive)
#                                   # intransive                        transive                             
#                                   # no-tense  past         present    no-tense     past         intension
KS_VCg = "숨"                       # 숨+다     숨+었+다     숨+는+다   숨+ㄱ+ㅣ+다  숨+ㄱ+였+다  숨+ㄱ+ㅣ+ㄹ
KS_VCi = "먹|죽"                    # 먹+다     먹+었+다     먹+는+다   먹+이+다     먹+여+ㅆ+다  먹+일
KS_VCj = "속"                       # 속+다     속+았+다     속+는+다   속+이+다     속+였+다     속+일
KS_VCl = "사" # '살'                # 사+ㄹ+다  사+ㄹ+았+다  사+ㄴ+다   사+ㄹ+리+다  사+ㄹ+렸+다  사+ㄹ+릴
KS_VCr = "주" # '줄'                # 주+ㄹ+다  주+ㄹ+었+다  주+ㄴ+다   주+ㄹ+이+다  주+ㄹ+였+다  주+ㄹ+일

### Intransive
#                                   # no-tense    past           present
KS_VIa = "가"                       # 가+다       가+ㅆ+다       가+ㄴ+다
KS_VIe = "야물|여물"                # 여무+ㄹ+다  여무+ㄹ+었+다  여무+ㄴ+다
KS_VIy = "숨죽ㅇ|생ㄱ|쓰러ㅈ|해ㅈ"  # 생ㄱ+ㅣ+다  생ㄱ+ㅕ+ㅆ+다  생ㄱ+ㅣ+ㄴ+다
KS_VIl = "조"                       # 조+ㄹ+다    조+ㄹ+았+다    조+ㄴ+다
KS_VIs = "잘나"                     # 잘나+다     잘나+ㅆ+다

### Transive
#                                   # active                            passive
#                                   # no-tense   present    past        no-tense      present          past            
KS_VTg = "박|붙잡|잡"               # +다        +는+다     +았+다      +히+다        +힌+다           +혔+다        
KS_VTh = "먹|읽|찍"                 # +다        +는+다     +었+다      +ㅎ+ㅣ+다     +ㅎ+ㅣ+ㄴ+다     +ㅎ+ㅕ+ㅆ+다
KS_VTi = "보|쪼"                    # +다        +ㄴ+다     +았+다      +ㅇ+ㅣ+다     +ㅇ+ㅣ+ㄴ+다     +ㅇ+ㅕ+ㅆ+다
KS_VTl = "가" # grind               # +ㄹ+다     +ㄴ+다     +ㄹ+았+다   +ㄹ+ㄹ+ㅣ+다  +ㄹ+ㄹ+ㅣ+ㄴ+다  +ㄹ+ㄹ+ㅕ+ㅆ+다 
KS_VTm = "거|드|미"                 # +ㄹ+다     +ㄴ+다     +ㄹ+었+다   +ㄹ+ㄹ+ㅣ+다  +ㄹ+ㄹ+ㅣ+ㄴ+다  +ㄹ+ㄹ+ㅕ+ㅆ+다  
KS_VTn = "빠" # wash                # +ㄹ+다     +ㄴ+다     +ㄹ+았+다   +ㄹ+ㄹ+ㅣ+다  +ㄹ+ㄹ+ㅣ+ㄴ+다  +ㄹ+ㄹ+ㅕ+ㅆ+다  
KS_VTy = "나ㄴ"                     # +ㅜ+다     +ㅜ+ㄴ+다  +ㅝ+ㅆ+다   +ㅟ+다        +ㅟ+ㄴ+다        +ㅟ+었+다      

### Active
KS_VAd = "내밀|넣|말|받들|빼|재|쳐들|허물"  # ~다(da)
KS_VAh = "가까이"                   # 가까이+하+다  가까이+했+다  가까이+한+다 x
KS_VAi = "내ㅊ|당ㄱ|[되]?[돌살]ㄹ|망ㅊ|숨ㄱ|외ㅊ|[드]높|되뇌|죽|[보]살ㅍ" # ~ㅣ다(ida)
KS_VAl = "[되][돌살]|[쳐]올|[내때]"  # ~리다(lida)
KS_VAu = "ㅊ|낮ㅊ|늦ㅊ"             # +ㅜ+다     +ㅜ+ㄴ+다  +ㅝ+ㅆ+다        
KS_VAw = "[치채]"  # ~우다(wuda)

