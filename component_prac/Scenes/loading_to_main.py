import pygame
import time
from Components.button import Button
import os

class Loading_To_Main:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.loading_count = 0
        self.loading1 = Button(self.screen, 960, 800, 0, 0, (0,0,0), "다양한 직업들 모으는 중.", "s", (255,255,255),"n")
        self.loading2 = Button(self.screen, 960, 800, 0, 0, (0,0,0), "다양한 직업들 모으는 중..", "s", (255,255,255),"n")
        self.loading3 = Button(self.screen, 960, 800, 0, 0, (0,0,0), "다양한 직업들 모으는 중...", "s", (255,255,255),"n")
        self.base_path = os.path.dirname(__file__)
        self.black = pygame.image.load(os.path.join(self.base_path, "Graphics/black.png"))
        self.black = pygame.transform.scale(self.black, (1920, 1080))

    def handle_event(self, event: pygame.event):
        if self.loading_count == 3:
            self.next_scene = "main"
            

    def update(self):
        pass

    def draw(self):
        for i in range(1):
            self.screen.blit(self.black, (0, 0))
            self.loading1.draw()
            pygame.display.flip()
            time.sleep(0.5)
            self.screen.blit(self.black, (0, 0))
            self.loading2.draw()
            pygame.display.flip()
            time.sleep(0.5)
            self.screen.blit(self.black, (0, 0))
            self.loading3.draw()
            pygame.display.flip()
            time.sleep(0.5)
        self.loading_count = 3
            
