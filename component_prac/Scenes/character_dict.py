import pygame
from Components.button import Button
import os

class Story_mode_pick:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.base_path = os.path.dirname(__file__)
        self.dict_name1 = Button(self.screen, 165, 0, 0, 0, (0,0,0), "직업", "nb", (255,255,255),"n")
        self.dict_name2 = Button(self.screen, 165, 0, 0, 0, (0,0,0), "사전", "nb", (255,255,255),"n")
      
        self.fighter_name = Button(self.screen, 360, 0, 0, 0, (0,0,0), "격투가", "s", (255,255,255),"n")
        self.gambler_name = Button(self.screen, 640, 0, 0, 0, (0,0,0), "도박꾼", "s", (255,255,255),"n")
        self.rider_name = Button(self.screen, 920, 0, 0, 0, (0,0,0), "라이더", "s", (255,255,255),"n")
        self.carpenter_name = Button(self.screen, 1200, 0, 0, 0, (0,0,0), "목수", "s", (255,255,255),"n")
        self.bodybuilder_name = Button(self.screen, 1480, 0, 0, 0, (0,0,0), "보디빌더", "s", (255,255,255),"n")
        self.engineer_name = Button(self.screen, 360, 0, 0, 0, (0,0,0), "엔지니어", "s", (255,255,255),"n")
        self.musician_name = Button(self.screen, 640, 0, 0, 0, (0,0,0), "음악가", "s", (255,255,255),"n")
        self.naturalist_name = Button(self.screen, 920, 0, 0, 0, (0,0,0), "자연술사", "s", (255,255,255),"n")
        self.politician_name = Button(self.screen, 1200, 0, 0, 0, (0,0,0), "정치가", "s", (255,255,255),"n")
        self.baker_name = Button(self.screen, 1480, 0, 0, 0, (0,0,0), "제빵사", "s", (255,255,255),"n")
        self.chessplayer_name = Button(self.screen, 360, 0, 0, 0, (0,0,0), "체스선수", "s", (255,255,255),"n")
        self.pitcher_name = Button(self.screen, 640, 0, 0, 0, (0,0,0), "투수", "s", (255,255,255),"n")
        self.harrypotter_name = Button(self.screen, 920, 0, 0, 0, (0,0,0), "해리포터 3회 독자", "s", (255,255,255),"n")
        self.chemist_name = Button(self.screen, 1200, 0, 0, 0, (0,0,0), "화학자", "s", (255,255,255),"n")
        self.blackdeath_name = Button(self.screen, 1480, 0, 0, 0, (0,0,0), "흑사병 보균자", "s", (255,255,255),"n")
      
        self.characterback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_character_dict/characterback.png"))
        self.characterback = pygame.transform.scale(self.backtitle, (1920, 1080))
        self.bookback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_character_dict/bookback.png"))
        self.bookback = pygame.transform.scale(self.bookback, (1700, 990))
        self.Naturalist_il = pygame.image.load(os.path.join(base_path, "Graphics/character_design/design_Naturalist.png"))
        self.Naturalist_il = pygame.transform.scale(self.Naturalist_il, (280, 250))

    def handle_event(self, event: pygame.event):
        pass
    
            
    def update(self):
        self.fighter_name.update()
        self.gambler_name.update()
        self.rider_name.update()
        self.carpenter_name.update()
        self.bodybuilder_name.update()
      
        self.engineer_name.update()
        self.musician_name.update()
        self.naturalist_name.update()
        self.politician_name.update()
        self.baker_name.update()

        self.chessplayer_name.update()
        self.pitcher_name.update()
        self.harrypotter_name.update()
        self.chemist_name.update()
        self.blackdeath_name.update()

    def draw(self):
        self.screen.blit(self.characterback, (0,0))
        self.screen.blit(self.bookback, (110,45))
        self.dict_name1.draw()
        self.dict_name2.draw()
      
        self.fighter_name.draw()
        self.gambler_name.draw()
        self.rider_name.draw()
        self.carpenter_name.draw()
        self.bodybuilder_name.draw()
      
        self.engineer_name.draw()
        self.musician_name.draw()
        self.naturalist_name.draw()
        self.screen.blit(self.naturalist_il, (0,0))
        self.politician_name.draw()
        self.baker_name.draw()

        self.chessplayer_name.draw()
        self.pitcher_name.draw()
        self.harrypotter_name.draw()
        self.chemist_name.draw()
        self.blackdeath_name.draw()
