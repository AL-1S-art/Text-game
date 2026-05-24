import pygame


#디폴트
pygame.font.init()
screen = pygame.display.set_mode([600, 600]) 


#글씨 및 이미지 부르기
font = pygame.font.SysFont("malgungothic", 20, bold=True, italic=False)
font1 = pygame.font.SysFont("malgungothic", 40, bold=True, italic=False)
# image = pygame.image.load("player1.bmp")
# image2 = pygame.image.load("제목 없음.png")


#기본 위치 설정
x = 100
y = 200


#반복해서 창 실행
while True:

    #이벤트 입력 받을 때
    for event in pygame.event.get():
        print(event)

        if event.type == 256: #창 닫기
            break

        
        #방향키 위아래에 y좌표 변경
        if event.type == 768:
            if event.key == 1073741906:
                if y != 200:
                    y -= 100
            if event.key == 1073741905:
                if y != 500:
                    y += 100
        
        # #방향키 조정
        # if event.type == 768:
        #     if event.key == 1073741903:
        #         print("right")
        #         x += 10
        #     if event.key == 1073741904:
        #         print("left")
        #         x -= 10
        #     if event.key == 1073741906:
        #         print("up")
        #         y -= 10
        #     if event.key == 1073741905:
        #         print("down")
        #         y += 10
        


        #마우스 위치에 따른 결과값 출력
        if event.type == 1025:
            mouse_x, mouse_y = pygame.mouse.get_pos() #마우스 위치 부르기
            if mouse_x > 100 and mouse_x < 200:
                if mouse_y > 100 and mouse_y < 200:
                    print(1111111111)


    if event.type == 256: #창 닫기
        break


    screen.fill((0, 0, 0)) #화면 전부 까맣게


    #화면에 글씨 띄울 글씨 및 이미지 설정
    pygame.draw.rect(screen, (255, 0, 0), (x, y, 200, 30))
    title = font1.render("세계 제일 직업 대회", True, (255, 255, 255))
    subtitle = font1.render("직업을 선택해 주세요.", True, (255, 255, 255))
    text1 = font.render("격투가", True, (255, 255, 255))
    text2 = font.render("도박꾼", True, (255, 255, 255))
    text3 = font.render("자연술사", True, (255, 255, 255))
    text4 = font.render("흑사병 보균자", True, (255, 255, 255))
    screen.blit(title, (50, 50))
    screen.blit(subtitle, (50, 100))
    screen.blit(text1, (100, 200))
    screen.blit(text2, (100, 300))
    screen.blit(text3, (100, 400))
    screen.blit(text4, (100, 500))
    # screen.blit(image, (x, y))
    # screen.blit(image2, (0, 0))

    #화면에 띄우기
    pygame.display.flip()


# 누를때 768 땔때 769인 키들
# 윗키 1073741906
# 아랫키 1073741905
# 오른쪽키 1073741903
# 왼쪽키 1073741904
# 엔터키 13
# 스페이스바 32
