import pygame
import time
import os

#디폴트
pygame.font.init()
screen = pygame.display.set_mode([1920, 1080]) 


#화면 어둡게
fade = pygame.Surface((1920, 1080))
fade.fill((0, 0, 0))



# 장면
scene = 'intro'
clock = pygame.time.Clock()

# confirm_program_quit
y_confirm_program_quit = 490
x_main_pick = 235
x_game_mode_pick = 360
x_story_mode_pick = 360

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
mainback = pygame.image.load(os.path.join(base_path, "Graphics/mainback.png"))
mainback = pygame.transform.scale(mainback, (1920, 1080))
bookback = pygame.image.load(os.path.join(base_path, "Graphics/bookback.png"))
bookback = pygame.transform.scale(bookback, (1700, 990))
option_icon1 = pygame.image.load(os.path.join(base_path, "Graphics/option_icon1.png"))
option_icon1 = pygame.transform.scale(option_icon1, (150, 150))
home_settingback = pygame.image.load(os.path.join(base_path, "Graphics/home_settingback.png"))
home_settingback = pygame.transform.scale(home_settingback, (1920, 1080))
modeback = pygame.image.load(os.path.join(base_path, "Graphics/modeback.png"))
modeback = pygame.transform.scale(modeback, (1920, 1080))
endback = pygame.image.load(os.path.join(base_path, "Graphics/endback.png"))
endback = pygame.transform.scale(endback, (1920, 1080))


Naturalist = pygame.image.load(os.path.join(base_path, "Graphics/캐릭터 디자인/design_Naturalist.png"))
Naturalist = pygame.transform.scale(Naturalist, (280, 250))
# image2 = pygame.image.load("제목 없음.png")




fade_alpha = 255
fade_done = False
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
                    scene = "loading_to_main"

        if event.type == 256:
            running = False
























    #장면에 따른 선택같은 것들

    if scene == "main":
        if is_right_down == True:
            x_main_pick = min(1285, x_main_pick + 525)
            is_right_down = False

        if is_left_down == True:
            x_main_pick = max(235, x_main_pick - 525)
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
            if x_main_pick == 235:
                scene = "game_mode_pick"
            elif x_main_pick == 760:
                scene = "story_mode_pick"
            elif x_main_pick == 1285:
                scene = "character_pick"
            is_enter_down = False


        if is_mouse_down == True:
            if mouse_y >= 212.5 and mouse_y <= 1017.5:
                if 235 <= mouse_x and mouse_x <= 635:
                    scene = "game_mode_pick"
                if 760 <= mouse_x and mouse_x <= 1160:
                    scene = "story_mode_pick"
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
        if is_mouse_down == True:
            if mouse_x <= 100:
                if mouse_y >= 490 and mouse_y <= 590:
                    scene = "main"
            is_mouse_down = False

        if is_esc_down == True:
            scene = "main"
            is_esc_down = False



    if scene == "home_setting":
        if is_mouse_down == True:
            if mouse_y >= 900 and mouse_y <= 1034:
                if 797 <= mouse_x and mouse_x <= 1123:
                    scene = "confirm_program_quit"
            is_mouse_down = False

        if is_esc_down == True:
            scene = "main"
            is_esc_down = False




    if scene == "confirm_program_quit":
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
                scene = "home_setting"
            is_enter_down = False

        if is_mouse_down == True:
            if 845 < mouse_x and mouse_x < 1383.5:
                if 590 <= mouse_y and mouse_y <= 677:
                    scene = "home_setting"
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
            scene = "home_setting"
            is_esc_down = False



    if scene == "story_mode_pick":
        if is_right_down == True:
            x_story_mode_pick = min(1060, x_story_mode_pick + 700)
            is_right_down = False

        if is_left_down == True:
            x_story_mode_pick = max(360, x_story_mode_pick - 700)
            is_left_down = False

        if is_mouse_move == True:
            if mouse_y >= 212.5 and mouse_y <= 1017.5:
                if 360 <= mouse_x and mouse_x <= 860:
                    x_mode_pick = 360
                if 1060 <= mouse_x and mouse_x <= 1560:
                    x_mode_pick = 1060
            is_mouse_move = False


        if is_enter_down == True:
            if x_story_mode_pick == 360:
                scene = ""
            elif x_story_mode_pick == 1060:
                scene = ""
            is_enter_down = False


        # if is_mouse_down == True:
        #     if mouse_y >= 212.5 and mouse_y <= 1017.5:
        #         if 235 <= mouse_x and mouse_x <= 635:
        #             scene = "game_mode_pick"
        #         if 760 <= mouse_x and mouse_x <= 1160:
        #             scene = "story_mode_pick"
        #         if 1285 <= mouse_x and mouse_x <= 1685:
        #             scene = "character_pick"
        #     if mouse_y <= 150:
        #         if mouse_x >= 1770:
        #             scene = "home_setting"
        #     is_mouse_down = False




        if is_esc_down == True:
            scene = "main"
            is_esc_down = False




    if scene == "game_mode_pick":
        if is_right_down == True:
            x_game_mode_pick = min(1060, x_game_mode_pick + 700)
            is_right_down = False

        if is_left_down == True:
            x_game_mode_pick = max(360, x_game_mode_pick - 700)
            is_left_down = False

        if is_mouse_move == True:
            if mouse_y >= 212.5 and mouse_y <= 1017.5:
                if 360 <= mouse_x and mouse_x <= 860:
                    x_game_mode_pick = 360
                if 1060 <= mouse_x and mouse_x <= 1560:
                    x_game_mode_pick = 1060
            is_mouse_move = False


        if is_enter_down == True:
            if x_game_mode_pick == 360:
                scene = ""
            elif x_game_mode_pick == 1060:
                scene = ""
            is_enter_down = False


        # if is_mouse_down == True:
        #     if mouse_y >= 212.5 and mouse_y <= 1017.5:
        #         if 235 <= mouse_x and mouse_x <= 635:
        #             scene = "game_mode_pick"
        #         if 760 <= mouse_x and mouse_x <= 1160:
        #             scene = "story_mode_pick"
        #         if 1285 <= mouse_x and mouse_x <= 1685:
        #             scene = "character_pick"
        #     if mouse_y <= 150:
        #         if mouse_x >= 1770:
        #             scene = "home_setting"
        #     is_mouse_down = False

        if is_esc_down == True:
            scene = "main"
            is_esc_down = False












#배경

    screen.blit(backtitle, (0, 0))
    titlename = bigpen.render("세계 제일 직업 대회", True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (434.5, 75, 1055, 184))
    screen.blit(titlename, (509.5, 100))
    press_start = smallpen.render("PRESS BUTTON", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (850, 805, 220, 30))
    screen.blit(press_start, (850, 800))



    
    if scene == "confirm_program_quit":
        screen.blit(endback, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (450, 225, 1020, 550))
        pygame.draw.rect(screen, (255, 0, 0), (537.5, y_confirm_program_quit, 845, 87))
        realend = bigpen.render("종료하시겠습니까?", True, (255, 255, 255))
        yes = normalpen.render("예", True, (255, 255, 255))
        no = normalpen.render("아니요", True, (255, 255, 255))
        screen.blit(realend, (537.5, 300))
        screen.blit(yes, (935, 500))
        screen.blit(no, (885, 600))




    if scene == "home_setting":
        screen.blit(home_settingback, (0, 0))
        quit = between_nb.render("게임 종료", True, (255, 255, 255))
        opt = bigpen.render("설정", True, (255, 255, 255))
        screen.blit(quit, (797, 900))
        screen.blit(opt, (860, 50))



    if scene == "main":
        screen.blit(mainback, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1920, 150))
        pygame.draw.rect(screen, (0, 0, 0), (235, 212.5, 400, 805))
        pygame.draw.rect(screen, (0, 0, 0), (760, 212.5, 400, 805))
        pygame.draw.rect(screen, (0, 0, 0), (1285, 212.5, 400, 805))
        screen.blit(option_icon1, (1770, 0))
        titlename = bigpen.render("세계 제일 직업 대회", True, (255, 255, 255))
        pygame.draw.rect(screen, (255, 0, 0), (x_main_pick, 212.5, 400, 805))
        mainGAME1 = bigpen.render("게임", True, (255, 255, 255))
        mainGAME2 = bigpen.render("시작", True, (255, 255, 255))
        mainSTORY = bigpen.render("스토리", True, (255, 255, 255))
        mainLIST = bigpen.render("캐릭터", True, (255, 255, 255))
        screen.blit(titlename, (509.5, 8))
        screen.blit(mainGAME1, (335, 481))
        screen.blit(mainGAME2, (335, 615))
        screen.blit(mainSTORY, (810, 548))
        screen.blit(mainLIST, (1335, 548))














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
        fighter_name = smallpen.render("격투가", True, (255, 255, 255))
        gambler_name = smallpen.render("도박꾼", True, (255, 255, 255))
        rider_name = smallpen.render("라이더", True, (255, 255, 255))
        carpenter_name = smallpen.render("목수", True, (255, 255, 255))
        bodybuilder_name = smallpen.render("보디빌더", True, (255, 255, 255))
        engineer_name = smallpen.render("엔지니어", True, (255, 255, 255))
        musician_name = smallpen.render("음악가", True, (255, 255, 255))
        naturalist_name = smallpen.render("자연술사", True, (255, 255, 255))
        politician_name = smallpen.render("정치인", True, (255, 255, 255))
        baker_name = smallpen.render("제빵사", True, (255, 255, 255))
        chessplayer_name = smallpen.render("체스선수", True, (255, 255, 255))
        pitcher_name = smallpen.render("투수", True, (255, 255, 255))
        harrypotter_name = smallpen.render("해리포터 3회 독자", True, (255, 255, 255))
        chemist_name = smallpen.render("화학자", True, (255, 255, 255))
        blackdeath_name = smallpen.render("흑사병 보균자", True, (255, 255, 255))

        screen.blit(fighter_name, (455, 345)) # 90, 95
        screen.blit(gambler_name, (735, 345)) # 90, 95
        screen.blit(rider_name, (1015, 345)) # 90, 95
        screen.blit(carpenter_name, (1310, 345)) # 60, 110
        screen.blit(bodybuilder_name, (1560, 345)) # 120, 80

        screen.blit(engineer_name, (440, 645)) # 120, 80
        screen.blit(musician_name, (735, 645)) # 90, 95
        screen.blit(naturalist_name, (1000, 645)) # 120, 80
        screen.blit(Naturalist, (920, 385))
        screen.blit(politician_name, (1295, 645)) # 90, 95
        screen.blit(baker_name, (1575, 645)) # 90, 95

        screen.blit(chessplayer_name, (440, 945)) # 120, 80
        screen.blit(pitcher_name, (750, 945)) # 60, 110
        screen.blit(harrypotter_name, (935.5, 945)) # 249, 15.5
        screen.blit(chemist_name, (1295, 945)) # 90, 95
        screen.blit(blackdeath_name, (1524.5, 945)) # 191, 44.5





    if scene == "game_mode_pick":
        screen.blit(modeback, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (360, 90, 500, 900))
        pygame.draw.rect(screen, (0, 0, 0), (1060, 90, 500, 900))
        pygame.draw.rect(screen, (255, 0, 0), (x_game_mode_pick, 212.5, 400, 805))
        gamePVP = bigpen.render("PVP", True, (255, 255, 255))
        gameBOSS = bigpen.render("BOSS", True, (255, 255, 255))
        screen.blit(gamePVP, (515.5, 473))
        screen.blit(gameBOSS, (1180, 473))




    if scene == "story_mode_pick":
        screen.blit(modeback, (0, 0))
        screen.blit(modeback, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), (360, 90, 500, 900))
        pygame.draw.rect(screen, (0, 0, 0), (1060, 90, 500, 900))
        pygame.draw.rect(screen, (255, 0, 0), (x_story_mode, 212.5, 400, 805))
        storyMAIN1 = bigpen.render("메인", True, (255, 255, 255))
        storyMAIN2 = bigpen.render("스토리", True, (255, 255, 255))
        storySIDE1 = bigpen.render("사이드", True, (255, 255, 255))
        storySIDE2 = bigpen.render("스토리", True, (255, 255, 255))
        screen.blit(storyMAIN1, (510, 406))
        screen.blit(storyMAIN2, (460, 540))
        screen.blit(storySIDE1, (1160, 406))
        screen.blit(storySIDE2, (1160, 540))
        













    if scene == "loading_to_main":
        clock.tick(60)
        screen.blit(black, (0, 0))
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
        scene = "main"
        pygame.event.clear()
        is_left_down = False
        is_right_down = False
        is_enter_down = False
        is_esc_down = False

        
    if not fade_done:
            fade_alpha -= 5

    if fade_alpha <= 0:
        fade_alpha = 0
        fade_done = True

    fade.set_alpha(fade_alpha)
    screen.blit(fade, (0, 0))


    pygame.display.flip()
    clock.tick(60)


pygame.quit()

width = storyMAIN1.get_width()
height = storyMAIN1.get_height()
print(width, height)


# 누를때 768 땔때 769인 키들
# 윗키 1073741906
# 아랫키 1073741905
# 오른쪽키 1073741903
# 왼쪽키 1073741904
# 엔터키 13
# 스페이스바 32
# ESC키 27


# scene
# loading_to_main   시작화면에서 메인화면으로 갈 때 생기는 로딩 화면
# home_setting     main화면에서 설정화면 열 때 생기는 설정 화면
# main     character_dict,game_mode_pick, story_mode_pick 등 선택하여 가는 메인 로비 화면
# character_dict     캐릭터 사전으로 메인화면에서 갈 수 있으며, 각 캐릭터의 세부스탯을 살펴볼 수 있는 창
# character_pick     게임 시작 시 캐릭터 선택 리스트를 보여주며, 각 캐릭터의 간단한 스탯을 볼 수 있는 창
# game_mode_pick     PVP, BOSS 같은 게임 모드를 선택하는 화면
# story_mode_pick     메인 스토리, 사이드 스토리 같은 스토리 모드를 선택하는 화면
# side_story_pick     각 직업끼리의 사소한 서사 등을 담은 스토리 중 하나를 고르는 화면
# main_story_pick     주 스토리 중 하나를 고르는 화면
# PVP_
