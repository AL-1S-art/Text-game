import pygame
from Components.button import Button
import os

class PVP_Game:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.menu = Button(self.screen, 0, 0, 1920, 150, (0,0,0), "게임 로비 창", "b", (255,255,255),"n","n")
        self.prepare = Button(self.screen, 800, 900, 320, 120, (0,0,0), "매칭", "b", (255,255,255),"y","y")
        self.base_path = os.path.dirname(__file__)
        self.characterback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_mode/modeback.png"))
        self.characterback = pygame.transform.scale(self.characterback, (1920, 1080))


    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key == 27:
                self.next_scene = 'main'
                
        if self.prepare.handle_event(event) == "information":
            return "information"
            
    def update(self):
        self.prepare.update()

    def draw(self):
        self.screen.blit(self.characterback, (0,0))
        self.prepare.draw()
        self.menu.draw()