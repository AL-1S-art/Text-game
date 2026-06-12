import random
from Util import *
from character import Buff, Player

class Fighter(Player):
    def __init__(self,name):
        self.hhp = 4908
        self.hp = self.hhp
        self.ad = 407
        self.de = 163
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 295
        self.mp = self.hmp
        self.rmp = 8
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '투기장의 투기'
        self.normalname = '평타'
        self.damageskillname = '훅'
        self.buffdebuffname = '배면기'
        self.classname = '격투가'
        self.ultimatename = '오라러쉬'
        super().__init__(name)
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    
    def passive(self):
        self.ad = self.ad + (self.turn * 2)

    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        self.passive()

    
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용합니다!')
            a = random.choice(['r', 'l'])
            if a == 'r':
                damm = int((self.ad + 140 + (target.hp/100)*(1+(self.ad*0.03)) + (self.ad*0.55)) * (100/(100+target.de)))
                
                slow_print(f'{self.name}이/가 [오른손]으로 강력한 훅을 날렸습니다!')
                slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
                target.dealdamm(damm)
            elif a == 'l':
                b = random.randint(1, 100)
                if b < 90:
                    damm = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de)))
                    
                    slow_print(f'{self.name}이/가 [왼손]으로 강력한 훅을 날렸습니다!')
                    slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
                    target.dealdamm(damm)
                else:
                    damm = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de))*2)
                    
                    slow_print(f'{self.name}이/가 [왼손]으로 [폐]를 강타했습니다!')
                    slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
                    target.dealdamm(damm)
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.turn += 1
            self.passive()

    def buffdebuff(self, target):
        if self.mp - 80 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.hp > self.hhp/2:
            slow_print('체력이 절반 이상이여서 사용 불가합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.bdbturn > 0:
            slow_print('(디)버프 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.bufflist.append(Buff('배면기','statuschange','Null','1',{'ad':int(self.ad*0.5),'de':int(self.de*0.5)},self))
            self.statusrenewal()
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 영구적으로 방어력과 공격력이 1.5배로 증가합니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 999999999999999999999999999999999999999999999999999999999999999
            self.passive()

    
    def ultimate(self, target):
        if self.mp - 100 < 0:
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
            damm = int(((self.ad + self.ad + self.ad*0.55) * (100/(100+target.de)))*3)
            
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.ultimatename}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.passive()

    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 턴이 지날수록 공격력이 증가하는 패시브입니다.')
        slow_print(f'[{self.normalname}]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 기본 스킬로 50%의 확률로 오른손이나 왼손을 사용하는 기본 스킬입니다.')
        slow_print(f'오른손의 대미지가 더 강력하며 왼손은 가끔 폐에 주먹을 꽃아 넣습니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 체력이 절반 이하일 시영구적으로 방어력과 공격력을 1.5배로 증가시키는 일회용 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 왼손과 오른손을 번갈아 가며 5번의 주먹을 꽃아 넣는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()
