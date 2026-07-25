import pygame
from Components.button import Button
import os

class Main:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.menu = Button(self.screen, 0, 0, 1920, 150, (0,0,0), "세계 제일 직업 대회", "b", (255,255,255),"n")
        self.game = Button(self.screen, 235, 212.5, 400, 805, (0,0,0), "시작", "b", (255,255,255),"y")
        self.story = Button(self.screen, 760, 212.5, 400, 805, (0,0,0), "스토리", "b", (255,255,255),"y")
        self.character = Button(self.screen, 1285, 212.5, 400, 805, (0,0,0), "캐릭터", "b", (255,255,255),"y")
        self.base_path = os.path.dirname(__file__)
        self.mainback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_main/mainback.png"))
        self.mainback = pygame.transform.scale(self.mainback, (1920, 1080))
        self.option_icon = pygame.image.load(os.path.join(self.base_path, "Graphics/option_icon1.png"))
        self.option_icon = pygame.transform.scale(self.option_icon, (150, 150))

    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key == 27:
                self.next_scene = "home_setting"
        if event.type == 1024:
            if self.game.handle_event(event) == "next":
                self.next_scene = "game_mode_pick"
    
            
    def update(self):
        self.menu.update()
        self.game.update()
        self.story.update()
        self.character.update()

    def draw(self):
        self.screen.blit(self.mainback, (0,0))
        self.menu.draw()
        self.game.draw()
        self.story.draw()
        self.character.draw()
        self.screen.blit(self.option_icon, (1770,0))
        
