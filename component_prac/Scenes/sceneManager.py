import pygame
from Components.button import Button
from Scenes.intro import IntroScene
from Scenes.loading_to_main import Loading_To_Main
from Scenes.main import Main
from Scenes.game_mode_pick import Game_mode_pick
from Scenes.character_dict import Character_dict
from Scenes.home_setting import Home_setting
from Scenes.confirm_quit import Confirm_quit
from Scenes.PVP_game import PVP_Game
from Scenes.BOSS_game import BOSS_Game


class SceneManager:
    def __init__(self, screen):
        self.screen = screen
        self.scene = None
        self.alpha = 255
        self.delta_fadeinout = 5
        self.fade_surface = pygame.Surface((1920, 1080), pygame.SRCALPHA)
        self.matching = Button(self.screen, 800, 900, 320, 120, (0,0,0), "매칭 중", "b", (255,0,0),"y","n")
        self.scenes = {
            "intro": IntroScene(screen),
            "loading_to_main": Loading_To_Main(screen),
            "main": Main(screen),
            "game_mode_pick": Game_mode_pick(screen),
            "character_dict": Character_dict(screen),
            "home_setting": Home_setting(screen),
            "confirm_quit": Confirm_quit(screen),
            "PVP_game": PVP_Game(screen),
            "BOSS_game": BOSS_Game(screen)
        }

    def set_scene(self, name):
        self.scene = self.scenes[name]
            
    def handle_event(self, event: pygame.event):
        self.scene.handle_event(event)
        
        
    def update(self):
        self.scene.update()

        if self.scene.next_scene:
            if self.scene.next_scene == "game_quit":
                return "False"
            self.set_scene(self.scene.next_scene)
            self.scene.next_scene = None


    def draw(self):
        self.scene.draw()
        if self.scene.update() == "information":
            self.matching.draw()

        self.fade_surface.fill((0, 0, 0, 0))
        self.fade_surface.fill((0, 0, 0, self.alpha)) 
        self.screen.blit(self.fade_surface, (0, 0))