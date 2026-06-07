from Util import *
from character import Buff, Player

class Harrypotter(Player):
    def __init__(self,name):
        
        self.hhp = 4410
        self.hp = self.hhp
        self.ad = 421
        self.de = 124
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 280
        self.mp = self.hmp
        self.rmp = 7
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '현실자각' #체력이 낮아질 수록 공/방 증가
        self.normalname = '평타'
        self.damageskillname = '슈투포파이' #마법피해 입히기
        self.buffdebuffname = '프루타이고' #3턴 동안 마법 보호막 생성해서 데미지 감소
        self.ultimatename = '아부다카다브라' #1턴 마비
        self.shield = 0
        self.classname = '해리포터'
        super().__init__(name)
    def dealdamm(self, damage):
        if self.shield > 0:
            slow_print(f'마법 보호막이 피해를 대신 받았습니다!')
            self.shield -= damage
            if self.shield <= 0:
                slow_print('마법 보호막이 파괴되었습니다!')
        else:    
            self.hp -= int(damage)
            if self.hp > 0:
                slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
            else:
                slow_print(f'{self.name}이/가 사망하였습니다!')
                return
        print()
    def passive(self, target):
        self.passiveturn += 1
        self.ad += self.passiveturn * 2
        
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.turn += 1
        self.passive()
   
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int(() * (100/(100+target.de)))
            
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            if self.uturn > 0:
                self.uturn -= 1
   
    def buffdebuff(self, target):
        if self.mp - 80 < 0 :
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.bdbturn > 0:
            slow_print('(디)버프 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.shield += 1000
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 최대 1000까지의 피해를 막아줍니다. 초과 피해량은 사라집니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 4
            self.turn += 1
            self.passive()
   
    def ultimate(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        if self.uturn > 0:
            slow_print('궁극기 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int()
            
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
   
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 체력이 낮아질 수록 공격력과 방어력이 증가하는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 해리포터 책으로 학습한 공격 마법으로 공격하는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 해리포터 책으로 학습한 방어 마법으로 보호막을 펼쳐 3턴간 대미지를 감소시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 대상에게 죽음의 공포를 선사하여 피해를 입히고 마비를 시키는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()

