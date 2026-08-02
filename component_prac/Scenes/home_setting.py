import pygame
from Components.button import Button
import os

class Home_setting:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None

        self.base_path = os.path.dirname(__file__)
        self.home_settingback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_home_setting/home_settingback.png"))
        self.home_settingback = pygame.transform.scale(self.home_settingback, (1920, 1080))
        self.menu = Button(self.screen, 960, 117, 0, 0, (0,0,0), "설정", "b", (255,255,255),"n")
        self.quit = Button(self.screen, 960, 950, 0, 0, (0,0,0), "게임 종료", "nb", (255,255,255),"y")


    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key == 27:
                self.next_scene = "main"

        if self.quit.handle_event(event) == "next":
           self.next_scene = "confirm_quit"
    
            
    def update(self):
        self.quit.update()

    def draw(self):
        self.screen.blit(self.home_settingback, (0,0))
        self.menu.draw()
        self.quit.draw()