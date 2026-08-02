import pygame
from Components.button import Button
import os

class Character_dict:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        self.base_path = os.path.dirname(__file__)
        self.menu = Button(self.screen, 0, 0, 1920, 150, (0,0,0), "다양한 직업들", "b", (255,255,255),"n")
        #좌표 규칙
        #양옆 공백 100, 캐릭터 사전 사이즈 1720, 990
        #한 캐릭터 당 한 칸 가로 길이 320, 세로 길이 370(그림 320, 글씨 50)
        #한 캐릭터 끼리의 공백은 양옆 20, 위아래 20
        #가로 2줄, 세로 5줄
        #(a,b)에 있는 글씨의 좌표 위치는 (280 + (a-1)*340, 515 + (b-1)*390)
        #(a,b)에 있는 그림의 좌표 위치는 (180 + (a-1)*340, 170 + (b-1)*390)
        self.fighter_name = Button(self.screen, 280, 515, 0, 0, (0,0,0), "격투가", "s", (255,255,255),"n")
        self.gambler_name = Button(self.screen, 620, 515, 0, 0, (0,0,0), "도박꾼", "s", (255,255,255),"n")
        self.rider_name = Button(self.screen, 960, 515, 0, 0, (0,0,0), "라이더", "s", (255,255,255),"n")
        self.carpenter_name = Button(self.screen, 1300, 515, 0, 0, (0,0,0), "목수", "s", (255,255,255),"n")
        self.bodybuilder_name = Button(self.screen, 1640, 515, 0, 0, (0,0,0), "보디빌더", "s", (255,255,255),"n")
        self.engineer_name = Button(self.screen, 280, 905, 0, 0, (0,0,0), "엔지니어", "s", (255,255,255),"n")
        self.musician_name = Button(self.screen, 620, 905, 0, 0, (0,0,0), "음악가", "s", (255,255,255),"n")
        self.naturalist_name = Button(self.screen, 960, 905, 0, 0, (0,0,0), "자연술사", "s", (255,255,255),"n")
        self.politician_name = Button(self.screen, 1300, 905, 0, 0, (0,0,0), "정치가", "s", (255,255,255),"n")
        self.baker_name = Button(self.screen, 1640, 905, 0, 0, (0,0,0), "제빵사", "s", (255,255,255),"n")
        # self.chessplayer_name = Button(self.screen, 280, 995, 0, 0, (0,0,0), "체스선수", "s", (255,255,255),"n")
        # self.pitcher_name = Button(self.screen, 620, 995, 0, 0, (0,0,0), "투수", "s", (255,255,255),"n")
        # self.harrypotter_name = Button(self.screen, 960, 995, 0, 0, (0,0,0), "해리포터 3회 독자", "s", (255,255,255),"n")
        # self.chemist_name = Button(self.screen, 1300, 995, 0, 0, (0,0,0), "화학자", "s", (255,255,255),"n")
        # self.blackdeath_name = Button(self.screen, 1640, 995, 0, 0, (0,0,0), "흑사병 보균자", "s", (255,255,255),"n")
      
        self.characterback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_mode/modeback.png"))
        self.characterback = pygame.transform.scale(self.characterback, (1920, 1080))
        self.bookback = pygame.image.load(os.path.join(self.base_path, "Graphics/scene_mode/bookback.png"))
        self.bookback = pygame.transform.scale(self.bookback, (1720, 930))
        self.Naturalist_il = pygame.image.load(os.path.join(self.base_path, "Graphics/character_design/design_Naturalist.png"))
        self.Naturalist_il = pygame.transform.scale(self.Naturalist_il, (200, 320))

    def handle_event(self, event: pygame.event):
        if event.type == 768:
            if event.key == 27:
                self.next_scene = 'main'
    
            
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

        # self.chessplayer_name.update()
        # self.pitcher_name.update()
        # self.harrypotter_name.update()
        # self.chemist_name.update()
        # self.blackdeath_name.update()

    def draw(self):
        self.screen.blit(self.characterback, (0,0))
        self.screen.blit(self.bookback, (100,150))
        self.menu.draw()

        self.fighter_name.draw()
        self.gambler_name.draw()
        self.rider_name.draw()
        self.carpenter_name.draw()
        self.bodybuilder_name.draw()
      
        self.engineer_name.draw()
        self.musician_name.draw()
        self.naturalist_name.draw()
        self.screen.blit(self.Naturalist_il, (860,560))
        self.politician_name.draw()
        self.baker_name.draw()

        # self.chessplayer_name.draw()
        # self.pitcher_name.draw()
        # self.harrypotter_name.draw()
        # self.chemist_name.draw()
        # self.blackdeath_name.draw()