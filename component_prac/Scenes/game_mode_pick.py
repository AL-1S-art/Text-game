import pygame
from Components.button import Button
import os

class Game_mode_pick:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.menu = Button(self.screen, 0, 0, 1920, 150, (0,0,0), "게임 모드 선택", "b", (255,255,255),"n")
        self.gamePVP = Button(self.screen, 360, 215, 500, 800, (0,0,0), "PVP", "b", (255,255,255),"y")
        self.gameBOSS = Button(self.screen, 1060, 215, 500, 800, (0,0,0), "BOSS", "b", (255,255,255),"y")
        self.base_path = os.path.dirname(__file__)
        self.characterback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_mode/modeback.png"))
        self.characterback = pygame.transform.scale(self.characterback, (1920, 1080))


    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key == 27:
                self.next_scene = 'main'

        if self.gamePVP.handle_event(event) == "next":
            self.next_scene = "PVP_game"

        if self.gameBOSS.handle_event(event) == "next":
            self.next_scene = "BOSS_game"
            
    def update(self):
        self.menu.update()
        self.gamePVP.update()
        self.gameBOSS.update()

    def draw(self):
        self.screen.blit(self.characterback, (0,0))
        self.menu.draw()
        self.gamePVP.draw()
        self.gameBOSS.draw()

