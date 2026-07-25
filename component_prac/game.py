import os
import pygame
from Scenes.sceneManager import SceneManager



#디폴트
pygame.font.init()
smallpen = pygame.font.SysFont("malgungothic", 30, bold=True, italic=False)
between_sn = pygame.font.SysFont("malgungothic", 40, bold=True, italic=False)
normalpen = pygame.font.SysFont("malgungothic", 50, bold=True, italic=False)
between_nb = pygame.font.SysFont("malgungothic", 75, bold=True, italic=False)
bigpen = pygame.font.SysFont("malgungothic", 100, bold=True, italic=False)
screen = pygame.display.set_mode([1920, 1080])

# FPS 설정
clock = pygame.time.Clock()
FPS = 60

# sceneManager
sceneManager = SceneManager(screen)
sceneManager.set_scene("intro")

#반복해서 창 실행
running = True
while running:
    # event
    for event in pygame.event.get():
        if event.type == 256:
            running = False
        sceneManager.handle_event(event)

    # update
    sceneManager.update()

    # draw
    sceneManager.draw()
    pygame.display.flip()
    clock.tick(FPS)


pygame.quit()

# .\run_component_prac.cmd
