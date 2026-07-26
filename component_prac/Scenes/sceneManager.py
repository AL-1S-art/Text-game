import pygame
from Scenes.intro import IntroScene
from Scenes.loading_to_main import Loading_To_Main
from Scenes.main import Main
from Scenes.game_mode_pick import Game_mode_pick
from Scenes.story_mode_pick import Story_mode_pick
from Scenes.character_dict import Character_dict


class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scene = None
        self.scenes = {
            "intro": IntroScene(screen),
            "loading_to_main": Loading_To_Main(screen),
            "main": Main(screen),
            "game_mode_pick": Game_mode_pick(screen),
            "story_mode_pick": Story_mode_pick(screen),
            "character_dict": Character_dict(screen),
        }

    def set_scene(self, name):
        self.scene = self.scenes[name]
            
    def handle_event(self, event: pygame.event):
        self.scene.handle_event(event)
        
        
    def update(self):
        self.scene.update()

        if self.scene.next_scene:
            self.set_scene(self.scene.next_scene)
            self.scene.next_scene = None


    def draw(self):
        self.scene.draw()
