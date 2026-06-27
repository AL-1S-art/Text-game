import pygame
import time
import os

#디폴트
pygame.font.init()
screen = pygame.display.set_mode([1920, 1080]) 

# 장면
scene = 'intro'
# scene = 'loading'

# confirm_program_quit
y_confirm_program_quit = 490

# 키 입력, 마우스 입력 이벤트 처리
key_down_manager = {chr(i): False for i in range(97, 122 + 1)}
is_left_down = False
is_right_down = False
is_top_down = False
is_bottom_down = False
is_enter_down = False
is_space_down = False
is_mouse_move = False
is_mouse_down = False


#글씨 및 이미지 부르기
base_path = os.path.dirname(__file__)
smallpen = pygame.font.SysFont("malgungothic", 30, bold=True, italic=False)
original = pygame.font.SysFont("malgungothic", 50, bold=True, italic=False)
title = pygame.font.SysFont("malgungothic", 100, bold=True, italic=False)
backtitle = pygame.image.load(os.path.join(base_path, "Graphics/backtitle.png"))
backtitle = pygame.transform.scale(backtitle, (1920, 1080))
black = pygame.image.load(os.path.join(base_path, "Graphics/black.png"))
black = pygame.transform.scale(black, (1920, 1080))
# image2 = pygame.image.load("제목 없음.png")









#반복해서 창 실행
running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == 768:
            if event.key == 27:  # 27 : ESC key
                scene = "confirm_program_quit"

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
                if event.key <= 122 and event.key >= 97 or event.key == 32 or event.key == 13:
                    scene = "loading"


































    # 이벤트로 인한 변화 처리(물리 이동, 공격 hp 감소라든지...)
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
                scene = "intro"
            is_enter_down = False

        if is_mouse_down == True:
            if y_confirm_program_quit == 490:
                running = False
            elif y_confirm_program_quit == 590:
                scene = "intro"
            is_mouse_down = False

        if is_mouse_move == True:
            if 845 < mouse_x and mouse_x < 1383.5:
                if 590 < mouse_y and mouse_y < 677:
                    y_confirm_program_quit = 590
                if 490 < mouse_y and mouse_y < 577:
                    y_confirm_program_quit = 490
            is_mouse_move = False
    


    if scene == "mode_pick":
        if is_top_down == True:
            y_mode_pick = max(490, y_confirm_program_quit - 100)
            is_top_down = False

        if is_bottom_down == True:
            y_mode_pick = min(490, y_confirm_program_quit - 100)
            is_bottom_down = False

        if is_enter_down == True:
            if y_mode_pick == 490:
                running = False
            elif y_mode_pick == 590:
                scene = "intro"
            is_enter_down = False
        
        if is_right_down == True:
            y_mode_pick = 490
            is_top_down = False

        if is_left_down == True:
            y_mode_pick = 590
            is_bottom_down = False

        if is_mouse_down == True:
            if y_mode_pick == 490:
                running = False
            elif y_mode_pick == 590:
                scene = "intro"
            is_mouse_down = False

        if is_mouse_move == True:
            if 845 < mouse_x and mouse_x < 1383.5:
                if 590 < mouse_y and mouse_y < 677:
                    y_mode_pick = 590
                if 490 < mouse_y and mouse_y < 577:
                    y_mode_pick = 490
            is_mouse_move = False



















    # 그리기
    screen.blit(backtitle, (0, 0))
    titlename = title.render("세계 제일 직업 대회", True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (434.5, 75, 1055, 184))
    screen.blit(titlename, (509.5, 100))
    press_start = smallpen.render("PRESS BUTTON", True, (255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 0), (850, 805, 220, 30))
    screen.blit(press_start, (850, 800))


    
    if scene == "confirm_program_quit":
        pygame.draw.rect(screen, (0, 0, 0), (450, 225, 1020, 550))
        pygame.draw.rect(screen, (255, 0, 0), (537.5, y_confirm_program_quit, 845, 87))
        realend = title.render("종료하시겠습니까?", True, (255, 255, 255))
        yes = original.render("예", True, (255, 255, 255))
        no = original.render("아니요", True, (255, 255, 255))
        screen.blit(realend, (537.5, 300))
        screen.blit(yes, (935, 500))
        screen.blit(no, (885, 600))




    if scene == "loading":
        time.sleep(0.25)
        screen.blit(black, (0, 0))
        pygame.display.flip()
        for i in range(3):
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
        scene = "character_pick"


    if scene == "mode_pick":
        modePVP = original.render("PVP", True, (255, 255, 255))
        modeBOSS = original.render("제빵사", True, (255, 255, 255))
        screen.blit(blackdeath, (789.5, 800))
        screen.blit(blackdeath, (789.5, 800))









    if scene == "character_pick":
        # 210 + 280 * (n - 1)
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
        chessplayer = smallpen.render("체스 선수", True, (255, 255, 255))
        pitcher = smallpen.render("투수", True, (255, 255, 255))
        harrypotter = smallpen.render("해리포터 3회 독자", True, (255, 255, 255))
        chemist = smallpen.render("화학자", True, (255, 255, 255))
        blackdeath = smallpen.render("흑사병 보균자", True, (255, 255, 255))
        screen.blit(fighter, (304.5, 800))
        screen.blit(gambler, (304.5, 800))
        screen.blit(rider, (304.5, 800))
        screen.blit(carpenter, (304.5, 800))
        screen.blit(bodybuilder, (304.5, 800))
        screen.blit(engineer, (304.5, 800))
        screen.blit(musician, (304.5, 800))
        screen.blit(naturalist, (304.5, 800))
        screen.blit(politician, (304.5, 800))
        screen.blit(baker, (304.5, 800))
        screen.blit(chessplayer, (304.5, 800))
        screen.blit(pitcher, (304.5, 800))
        screen.blit(harrypotter, (505.5, 800))
        screen.blit(chemist, (304.5, 800))
        screen.blit(blackdeath, (304.5, 800))








    pygame.display.flip()


pygame.quit()

width = harrypotter.get_width()
height = harrypotter.get_height()

print(width, height)


# 누를때 768 땔때 769인 키들
# 윗키 1073741906
# 아랫키 1073741905
# 오른쪽키 1073741903
# 왼쪽키 1073741904
# 엔터키 13
# 스페이스바 32
# ESC키 27

    #화면에 글씨 띄울 글씨 및 이미지 설정
    # pygame.draw.rect(screen, (255, 0, 0), (x, y, 200, 30))
    # title = title.render("세계 제일 직업 대회", True, (255, 255, 255))

    # text1 = original.render("격투가", True, (255, 255, 255))
    # text1 = original.render("격투가", True, (255, 255, 255))
    # text2 = original.render("도박꾼", True, (255, 255, 255))
    # text3 = original.render("자연술사", True, (255, 255, 255))
    # text4 = original.render("흑사병 보균자", True, (255, 255, 255))
    # screen.blit(title, (50, 50))
    # screen.blit(text1, (100, 200))
    # screen.blit(text2, (100, 300))
    # screen.blit(text3, (100, 400))
    # screen.blit(text4, (100, 500))
    # screen.blit(image, (x, y))
    # screen.blit(image2, (0, 0))
