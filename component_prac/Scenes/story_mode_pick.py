import pygame
from Components.button import Button
import os

class Story_mode_pick:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.base_path = os.path.dirname(__file__)
        self.characterback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_character_dict/characterback.png"))
        self.characterback = pygame.transform.scale(self.backtitle, (1920, 1080))


    def handle_event(self, event: pygame.event):
        pass
    
            
    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.characterback, (0,0))
