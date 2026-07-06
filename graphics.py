import pygame
import time
import os

#디폴트
pygame.font.init()
screen = pygame.display.set_mode([1920, 1080]) 

# 장면
scene = 'intro'
# scene = 'loading'
effect = 'nothing'
character_opt = False


# confirm_program_quit
y_confirm_program_quit = 490
x_mode_pick = 235

# 키 입력, 마우스 입력 이벤트 처리
key_down_manager = {chr(i): False for i in range(97, 122 + 1)}
is_left_down = False
is_right_down = False
is_top_down = False
is_bottom_down = False
is_enter_down = False
is_space_down = False
is_esc_down = False
is_mouse_move = False
is_mouse_down = False


#글씨 및 이미지 부르기
base_path = os.path.dirname(__file__)
smallpen = pygame.font.SysFont("malgungothic", 30, bold=True, italic=False)
between_sn = pygame.font.SysFont("malgungothic", 40, bold=True, italic=False)
normalpen = pygame.font.SysFont("malgungothic", 50, bold=True, italic=False)
between_nb = pygame.font.SysFont("malgungothic", 75, bold=True, italic=False)
bigpen = pygame.font.SysFont("malgungothic", 100, bold=True, italic=False)



backtitle = pygame.image.load(os.path.join(base_path, "Graphics/backtitle.png"))
backtitle = pygame.transform.scale(backtitle, (1920, 1080))
black = pygame.image.load(os.path.join(base_path, "Graphics/black.png"))
black = pygame.transform.scale(black, (1920, 1080))
modeback = pygame.image.load(os.path.join(base_path, "Graphics/modeback.png"))
modeback = pygame.transform.scale(modeback, (1920, 1080))
bookback = pygame.image.load(os.path.join(base_path, "Graphics/bookback.png"))
bookback = pygame.transform.scale(bookback, (1700, 990))
option_icon1 = pygame.image.load(os.path.join(base_path, "Graphics/opt_icon.png"))
option_icon1 = pygame.transform.scale(option_icon1, (150, 150))
home_settingback = pygame.image.load(os.path.join(base_path, "Graphics/settingback.png"))
home_settingback = pygame.transform.scale(home_settingback, (1920, 1080))
back_icon = pygame.image.load(os.path.join(base_path, "Graphics/back_icon.png"))
back_icon = pygame.transform.scale(back_icon, (100, 100))
# image2 = pygame.image.load("제목 없음.png")






#반복해서 창 실행
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == 768:
            if event.key == 27:  # 27 : ESC key
                is_esc_down = True

            elif event.key == 13:  # enter
                is_enter_down = True
            # 방향키
            elif event.key == 1073741906:  # top
                is_top_down = True

            elif event.key == 1073741905:  # bottom
                is_bottom_down = True

            elif event.key == 1073741903:  # right
                is_right_down = True

            elif event.key == 1073741904:  # left
                is_left_down = True
            
            elif event.key == 32:  # space
                is_space_down = True
            
            #알파벳
            if event.key <= 122 and event.key >= 97:
                key_down_manager[chr(event.key)] = True


        if event.type == 1024:
            is_mouse_move = True
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
        
        if event.type == 1025:
            is_mouse_down = True
            
        if scene == "intro":
            if event.type == 768:
                if event.key <= 122 and event.key >= 97 or event.key == 32:
                    scene = "loading"

        if event.type == 256:
            running = False
































    # 화면 위에 덮어 씌워지는 효과들
    if effect == "confirm_program_quit":
        if is_top_down == True:
            y_confirm_program_quit = max(490, y_confirm_program_quit - 100)
            is_top_down = False

        if is_bottom_down == True:
            y_confirm_program_quit = min(590, y_confirm_program_quit + 100)
            is_bottom_down = False

        if is_enter_down == True:
            if y_confirm_program_quit == 490:
                running = False
            elif y_confirm_program_quit == 590:
                effect = "nothing"
            is_enter_down = False

        if is_mouse_down == True:
            if 845 < mouse_x and mouse_x < 1383.5:
                if 590 <= mouse_y and mouse_y <= 677:
                    effect = "nothing"
                if 490 <= mouse_y and mouse_y <= 577:
                    running = False
            is_mouse_down = False

        if is_mouse_move == True:
            if 845 < mouse_x and mouse_x < 1383.5:
                if 590 <= mouse_y and mouse_y <= 677:
                    y_confirm_program_quit = 590
                if 490 <= mouse_y and mouse_y <= 577:
                    y_confirm_program_quit = 490
            is_mouse_move = False

        if is_esc_down == True:
            effect = "nothing"
            is_esc_down = False
























    #장면에 따른 선택같은 것들

    if scene == "mode_pick":
        if is_right_down == True:
            x_mode_pick = min(1285, x_mode_pick + 525)
            is_right_down = False

        if is_left_down == True:
            x_mode_pick = max(235, x_mode_pick - 525)
            is_left_down = False

        if is_mouse_move == True:
            if mouse_y >= 212.5 and mouse_y <= 1017.5:
                if 235 <= mouse_x and mouse_x <= 635:
                    x_mode_pick = 235
                if 760 <= mouse_x and mouse_x <= 1160:
                    x_mode_pick = 760
                if 1285 <= mouse_x and mouse_x <= 1685:
                    x_mode_pick = 1285
            is_mouse_move = False

        if is_enter_down == True:
            if x_mode_pick == 235:
                scene = ""
            elif x_mode_pick == 760:
                scene = ""
            elif x_mode_pick == 1285:
                scene = "character_pick"
            is_enter_down = False


        if is_mouse_down == True:
            if mouse_y >= 212.5 and mouse_y <= 1017.5:
                if 235 <= mouse_x and mouse_x <= 635:
                    scene = ""
                if 760 <= mouse_x and mouse_x <= 1160:
                    scene = ""
                if 1285 <= mouse_x and mouse_x <= 1685:
                    scene = "character_pick"
            if mouse_y <= 150:
                if mouse_x >= 1770:
                    scene = "home_setting"
            is_mouse_down = False

        if is_esc_down == True:
            scene = "home_setting"
            is_esc_down = False


    if scene == "character_pick":
        if is_esc_down == True:
            scene = "mode_pick"
            is_esc_down = False

        if is_mouse_move == True:
            if mouse_x <= 100:
                character_opt = True
            else:
                character_opt = False
        
        if is_mouse_down == True:
            if mouse_x <= 100:
                if mouse_y >= 490 and mouse_y <= 590:
                    scene = "mode_pick"



    if scene == "home_setting":
        if is_mouse_down == True:
            if mouse_y >= 900 and mouse_y <= 1034:
                if 797 <= mouse_x and mouse_x <= 1123:
                    effect = "confirm_program_quit"
            is_mouse_down = False

        if is_esc_down == True:
            scene = "mode_pick"
            is_esc_down = False























#배경

    screen.blit(backtitle, (0, 0))
    titlename = bigpen.render("세계 제일 직업 대회", True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (434.5, 75, 1055, 184))
    screen.blit(titlename, (509.5, 100))
    press_start = smallpen.render("PRESS BUTTON", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (850, 805, 220, 30))
    screen.blit(press_start, (850, 800))

    

    if scene == "loading":
        time.sleep(0.25)
        screen.blit(black, (0, 0))
        pygame.display.flip()
        for i in range(1):
            pygame.display.flip()
            loading_ment = smallpen.render("다양한 직업들 모으는 중.", True, (255, 255, 255))
            screen.blit(loading_ment, (789.5, 800))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(black, (0, 0))
            loading_ment = smallpen.render("다양한 직업들 모으는 중..", True, (255, 255, 255))
            screen.blit(loading_ment, (785.5, 800))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(black, (0, 0))
            loading_ment = smallpen.render("다양한 직업들 모으는 중...", True, (255, 255, 255))
            screen.blit(loading_ment, (781.5, 800))
            pygame.display.flip()
            time.sleep(0.5)
            screen.blit(black, (0, 0))
            loading_ment = smallpen.render("다양한 직업들 모으는 중.", True, (255, 255, 255))
            screen.blit(loading_ment, (789.5, 800))
        scene = "mode_pick"


    if scene == "home_setting":
        screen.blit(home_settingback, (0, 0))
        quit = between_nb.render("게임 종료", True, (255, 255, 255))
        opt = bigpen.render("설정", True, (255, 255, 255))
        screen.blit(quit, (797, 900))
        screen.blit(opt, (860, 50))


    if scene == "mode_pick":
        screen.blit(modeback, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1920, 150))
        pygame.draw.rect(screen, (0, 0, 0), (235, 212.5, 400, 805))
        pygame.draw.rect(screen, (0, 0, 0), (760, 212.5, 400, 805))
        pygame.draw.rect(screen, (0, 0, 0), (1285, 212.5, 400, 805))
        screen.blit(option_icon1, (1770, 0))
        pygame.draw.rect(screen, (255, 0, 0), (x_mode_pick, 212.5, 400, 805))
        modeGAME1 = bigpen.render("게임", True, (255, 255, 255))
        modeGAME2 = bigpen.render("시작", True, (255, 255, 255))
        modeSTORY = bigpen.render("스토리", True, (255, 255, 255))
        modeLIST = bigpen.render("캐릭터", True, (255, 255, 255))
        screen.blit(modeGAME1, (335, 481))
        screen.blit(modeGAME2, (335, 615))
        screen.blit(modeSTORY, (810, 548))
        screen.blit(modeLIST, (1335, 548))



    if scene == "character_pick":
        # 가로 360 + 280 * (n - 1)
        # 세로 90 + 300 * (n - 1)
        # 모든 smallpen 글씨는 세로 40 차지
        # 세로 중 차지하는 정도: 그림 250, 글씨 50
        # 가로길이, 140-(가로길이/2)
        screen.blit(modeback, (0, 0))
        screen.blit(bookback, (110, 45))
        pygame.draw.rect(screen, (255, 0, 0), (310, 45, 50, 990))
        pygame.draw.rect(screen, (255, 0, 0), (1760, 45, 50, 990))
        character_li = between_nb.render("직업", True, (255, 255, 255))
        character_st = between_nb.render("사전", True, (255, 255, 255))
        screen.blit(character_li, (135, 435))
        screen.blit(character_st, (135, 545))
        fighter = smallpen.render("격투가", True, (255, 255, 255))
        gambler = smallpen.render("도박꾼", True, (255, 255, 255))
        rider = smallpen.render("라이더", True, (255, 255, 255))
        carpenter = smallpen.render("목수", True, (255, 255, 255))
        bodybuilder = smallpen.render("보디빌더", True, (255, 255, 255))
        engineer = smallpen.render("엔지니어", True, (255, 255, 255))
        musician = smallpen.render("음악가", True, (255, 255, 255))
        naturalist = smallpen.render("자연술사", True, (255, 255, 255))
        politician = smallpen.render("정치인", True, (255, 255, 255))
        baker = smallpen.render("제빵사", True, (255, 255, 255))
        chessplayer = smallpen.render("체스선수", True, (255, 255, 255))
        pitcher = smallpen.render("투수", True, (255, 255, 255))
        harrypotter = smallpen.render("해리포터 3회 독자", True, (255, 255, 255))
        chemist = smallpen.render("화학자", True, (255, 255, 255))
        blackdeath = smallpen.render("흑사병 보균자", True, (255, 255, 255))

        screen.blit(fighter, (455, 345)) # 90, 95
        screen.blit(gambler, (735, 345)) # 90, 95
        screen.blit(rider, (1015, 345)) # 90, 95
        screen.blit(carpenter, (1310, 345)) # 60, 110
        screen.blit(bodybuilder, (1560, 345)) # 120, 80

        screen.blit(engineer, (440, 645)) # 120, 80
        screen.blit(musician, (735, 645)) # 90, 95
        screen.blit(naturalist, (1000, 645)) # 120, 80
        screen.blit(politician, (1295, 645)) # 90, 95
        screen.blit(baker, (1575, 645)) # 90, 95

        screen.blit(chessplayer, (440, 945)) # 120, 80
        screen.blit(pitcher, (750, 945)) # 60, 110
        screen.blit(harrypotter, (935.5, 945)) # 249, 15.5
        screen.blit(chemist, (1295, 945)) # 90, 95
        screen.blit(blackdeath, (1524.5, 945)) # 191, 44.5
        if character_opt == True:
            pygame.draw.rect(screen, (0, 0, 0), (0, 0, 100, 1080))
            screen.blit(back_icon, (0, 490))









#위에 최종적으로 걸쳐지는 것
    if effect == "confirm_program_quit":
        pygame.draw.rect(screen, (0, 0, 0), (450, 225, 1020, 550))
        pygame.draw.rect(screen, (255, 0, 0), (537.5, y_confirm_program_quit, 845, 87))
        realend = bigpen.render("종료하시겠습니까?", True, (255, 255, 255))
        yes = normalpen.render("예", True, (255, 255, 255))
        no = normalpen.render("아니요", True, (255, 255, 255))
        screen.blit(realend, (537.5, 300))
        screen.blit(yes, (935, 500))
        screen.blit(no, (885, 600))


    pygame.display.flip()


pygame.quit()


# 누를때 768 땔때 769인 키들
# 윗키 1073741906
# 아랫키 1073741905
# 오른쪽키 1073741903
# 왼쪽키 1073741904
# 엔터키 13
# 스페이스바 32
# ESC키 27



# 글러브


# 찢어진 트럼프 카드
# [도박꾼]이 들고 다니는 카드로 카드 게임에 널리 쓰이는 카드의 한 종류입니다.
# '가프덱', '기믹덱', 앞면만 백지인 '블랭크 페이스', 뒷면만 백지인 '블랭크 백',
# 양면이 백지인 '더블 블랭크' 등 다양한 종류의 카드가 존재합니다.

# 과연 도박을 위해 들고 다니는 것이 카드 뿐일까요...?


# 수리가 필요한 오토바이
# [라이더]가 타고 다니는 이동수단 입니다.
# 경량화가 가능하여 적은 출력으로도 높은 속도를 얻을 수 있고
# 구조가 비교적 단순하며, 유지 관리 비용이 적게 든다는 장점이 있지만
# 차체가 가벼워 경미한 접촉사고에도 크게 파손되고, 상당한 수리 비용이 발생할 수 있습니다.

# 대회에 참가한 라이더가 타는 기종은 엄청난 속도를 자랑하는 '스포츠 바이크'라고 합니다.


# 십자가
# [목수]가 들고 다니는 기독교의 상징입니다.
# 예수 그리스도의 십자가형을 통한 희생 및 완전한 순종과 자격을 상징하며
# 그리스도의 고난에 동참하고 그 가르침을 따르겠다는 신앙적 고백과 실천의 의미를 담습니다.

# 이번에는 어떤 용도로 사용하려고 하는걸까요?


# 아령
# [보디빌더]가 주로 들고 다니는 스포츠 용품의 일종입니다.
# 근비대, 근력 향상 등을 목적으로 무게를 통해 훈련하는 방법인 웨이트 트레이닝을 할 때
# 결코 빼놓을 수 없는 중요한 운동 기구입니다.

# '덤벨 컬'을 할때 쓰던 50kg짜리 아령은 두고 왔다고 하네요.


# 스패너/렌치
# [엔지니어]가 들고 다니는 공구 중 하나입니다.
# 영국, 호주, 뉴질랜드 같은 나라들은 스패너, 미국식 영어로는 렌치라고 한답니다.
# 너트와 볼트를 죄고 풀며 물체를 조립하고 분해할 때 사용하는 도구로
# 단어가 가진 뜻은 '비틀다'라고 하네요.


# 용접용 레이저
# [엔지니어]가 들고 다니는 공구 중 하나입니다.
# 다른 기술과 달리 뛰어난 정밀성을 자랑하는 용접용 레이저는 대형 공작기계로 쓰여왔으나
# 최근에는 중소 기업에서도 사용할 만한 제품들이 출시되고 있다네요.

# 매우 위험하니 사람을 향하여 사용하지 마세요!


# 피아노
# [음악가]가 들고 다니는 '유건 타현악기'입니다.
# 정식 명칭은 '피아노포르테'라고 하며 현재는 악기의 황제로 불린다고 하네요.
# '어쿠스틱 피아노', '전기 피아노', '전자 피아노' 등 다양한 피아노가 존재합니다.

# 대회에 이 피아노를 어떻게 들고 오는 걸까요?


# 피 묻은 바이올린
# [음악가]가 들고 다니는 '찰현악기'입니다.
# '에라스모'라는 사람이 양의 창자를 말려두고 있을 때 널어둔 창자 사이로 소리가 나는 것을 듣고
# 거기에서 영감을 받아 '르네상스 피들'이라는 악기를 제작 후 그것이 개량되어 나왔답니다.

# [음악가]의 손을 자세히 보면 노력의 상처가 남아있습니다.


# 지팡이
# 

# 누군가에게서 뺏은 판사봉
#

# 제빵사
#

# 체스판
#

# 타자에 의해 터져버린 야구공
#

# 닳고 닳은 해리포터 책
#

# 수상하고 위험한 샘플
#

# 썩어 문드러진 살점
# [흑사병 보균자]에게서 떨어진 살점입니다.



























