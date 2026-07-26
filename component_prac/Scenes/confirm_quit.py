import pygame
from Components.button import Button
import os

class Confirm_quit:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.base_path = os.path.dirname(__file__)
        self.backtitle = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_confirm_quit/endback.png"))
        self.backtitle = pygame.transform.scale(self.backtitle, (1920, 1080))


    def handle_event(self, event: pygame.event):
        pass
    
            
    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.backtitle, (0,0))

        
