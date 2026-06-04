import time

def slow_print(text, delay = 0.02):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)
    print()

def moreslow_print(text, delay = 0.1):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)
    print()

def slow_print_with_end(text,delay=0.02):
    for char in text:
        print(char, end='', flush = True)
        time.sleep(delay)


#모든 캐릭터 [도박꾼, 격투가, 자연술사, 흑사병 보균자, 화학자, 체스선수, 정치인, 엔지니어, 음악가, 투수, 목수, 보디빌더

    
#범위기: 흑사병 (디)버프 (자신 앞뒤, 대상 앞뒤), 체스선수 궁 (모든적), 엔지니어 스킬 (대상 앞뒤), 화학자 궁 (모든 적)
#대결상태: 정치인 궁 (대상과 1vs1) 
#아군대상: 
