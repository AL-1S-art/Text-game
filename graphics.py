import pygame


#디폴트
pygame.font.init()
screen = pygame.display.set_mode([600, 600]) 


#글씨 및 이미지 부르기
font = pygame.font.SysFont("malgungothic", 30, bold=True, italic=False)
image = pygame.image.load("player1.bmp")
image2 = pygame.image.load("제목 없음.png")


#기본 위치 설정
x = 200
y = 200


#반복해서 창 실행
while True:

    #이벤트 입력 받을 때
    for event in pygame.event.get():
        print(event)

        if event.type == 256: #창 닫기
            break

        
        #방향키 조정
        if event.type == 768:
            if event.key == 1073741903:
                print("right")
                x += 10
            if event.key == 1073741904:
                print("left")
                x -= 10
            if event.key == 1073741906:
                print("up")
                y -= 10
            if event.key == 1073741905:
                print("down")
                y += 10
        

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
    text = font.render("안녕하세요! Pygame 테스트입니다.", True, (255, 255, 255))
    screen.blit(text, (100, 100))
    screen.blit(image, (x, y))
    screen.blit(image2, (0, 0))

    #화면에 띄우기
    pygame.display.flip()
