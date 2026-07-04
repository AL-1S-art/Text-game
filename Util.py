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


#모든 캐릭터 격투가 도박꾼 라이더 목수 보디빌더 엔지니어 음악가 자연술사 정치인 제빵사 체스선수 투수 해리포터 3회 독자 화학자 흑사병 보균자
