import pygame
from Components.button import Button
import os

class Home_setting:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None

        self.base_path = os.path.dirname(__file__)
        self.backtitle = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_home_setting/home_settingback.png"))
        self.backtitle = pygame.transform.scale(self.backtitle, (1920, 1080))


    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key <= 122 and event.key >= 97:
                self.next_scene = "loading_to_main"
    
            
    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.backtitle, (0,0))

        
