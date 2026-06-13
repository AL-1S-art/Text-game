import pygame


#디폴트
pygame.font.init()
screen = pygame.display.set_mode([1920, 1080]) 


#글씨 및 이미지 부르기
original = pygame.font.SysFont("malgungothic", 50, bold=True, italic=False)
title = pygame.font.SysFont("malgungothic", 100, bold=True, italic=False)
background = pygame.image.load("Graphics/background1.jpg")
background = pygame.transform.scale(background, (1920, 1080))
# image2 = pygame.image.load("제목 없음.png")



#반복해서 창 실행
running = True
y = 490
while running:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        
        if event.type == 1025:
            print(event)

        if event.type == pygame.QUIT:
            running = False
        if event.type == 768:
            if event.key == 27:
                running1 = True
                while running1:
                    
                    pygame.draw.rect(screen, (0, 0, 0), (450, 225, 1020, 550))
                    pygame.draw.rect(screen, (255, 0, 0), (537.5, y, 845, 87))
                    end = title.render("종료하시겠습니까?", True, (255, 255, 255))
                    yes = original.render("예", True, (255, 255, 255))
                    no = original.render("아니요", True, (255, 255, 255))
                    screen.blit(end, (537.5, 300))
                    screen.blit(yes, (935, 500))
                    screen.blit(no, (885, 600))
                    pygame.display.flip()

                    for event in pygame.event.get():
                        if event.type == 768:
                            if event.key == 27:
                                running = False
                                running1 = False
                            if event.key == 1073741906:
                                if y == 590:
                                    y -= 100
                            if event.key == 1073741905:
                                if y == 490:
                                    y += 100
                    





pygame.quit()

width = end.get_width()
height = end.get_height()
print(width, height)
width = yes.get_width()
height = yes.get_height()
print(width, height)
width = no.get_width()
height = no.get_height()
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
