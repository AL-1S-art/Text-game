import pygame
from Components.button import Button
import os

class Main_story:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.menu = Button(self.screen, 0, 0, 1920, 150, (0,0,0), "스토리", "b", (255,255,255),"n")
        self.storyMAIN = Button(self.screen, 360, 215, 500, 800, (0,0,0), "메인", "b", (255,255,255),"y")
        self.storySIDE = Button(self.screen, 1060, 215, 500, 800, (0,0,0), "사이드", "b", (255,255,255),"y")
        self.base_path = os.path.dirname(__file__)
        self.characterback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_mode/modeback.png"))
        self.characterback = pygame.transform.scale(self.characterback, (1920, 1080))


    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key == 27:
                self.next_scene = 'main'

        if self.storyMAIN.handle_event(event) == "next":
            self.next_scene = "main_story"

        if self.storySIDE.handle_event(event) == "next":
            self.next_scene = "side_story"
    
            
    def update(self):
        self.storyMAIN.update()
        self.storySIDE.update()

    def draw(self):
        self.screen.blit(self.characterback, (0,0))
        self.storyMAIN.draw()
        self.storySIDE.draw()