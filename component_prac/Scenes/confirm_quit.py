import pygame
from Components.button import Button
import os

class Confirm_quit:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.real_quit = Button(self.screen, 0, 0, 1920, 150, (0,0,0), "종료하시겠습니까?", "b", (255,255,255),"n")
        self.yes = Button(self.screen, 537.5, 490, 845, 87, (0,0,0), "예", "b", (255,255,255),"y")
        self.no = Button(self.screen, 537.5, 590, 845, 87, (0,0,0), "아니요", "b", (255,255,255),"y")
        self.base_path = os.path.dirname(__file__)
        self.endback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_confirm_quit/endback.png"))
        self.endback = pygame.transform.scale(self.backtitle, (1920, 1080))
        self.black = pygame.image.load(os.path.join(self.base_path, "Graphics/black.png"))
        self.black = pygame.transform.scale(self.black, (1020, 550))


    def handle_event(self, event: pygame.event):
        pass
    
            
    def update(self):
        pass

    def draw(self):
        self.screen.blit(self.endback, (0,0))
        self.screen.blit(self.black, (450,225))

        
