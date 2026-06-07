
from Util import *
from character import Buff, Player


class Blackdeath(Player):
    def __init__(self):
        
        self.hhp = 4682
        self.hp = self.hhp
        self.shield = 0
        self.ad = 120
        self.de = 160
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 330
        self.mp = self.hmp
        self.rmp = 8
        self.bdbturn = 0
        self.uturn = 0
        self.usturn = 3
        self.turn = 0
        self.passivename = '보균' #흑사병에 걸려서 매턴 체력 감소
        self.normalname = '평타'
        self.damageskillname = '찌르기' #자신의 체력을 소비하여 대상을 찌름
        self.buffdebuffname = '기침' #패시브 보균을 자신의 주변과 대상의 주변으로 옮김
        self.ultimatename = '항생제' #대상을 지정해 흑사병을 치료(최대 3번)
        self.bdbtarget = []
        self.utarget = []
        super().__init__(self.name)
        self.classname = '흑사병 보균자'
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    def passive(self):
        damm = int((self.ad*2.63)*0.425 + 60)
        self.hp -= damm
        if len(self.bdbtarget) != 0:
            for i in range(len(self.bdbtarget)):
                self.bdbtarget[i].hp -= damm
   
    
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
        if self.hp - 100 < 0:
            slow_print('사용 가능한 체력이 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int((target.hp*0.3) * (100/(100+target.de)))
            
            self.hp -= 100
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.turn += 1
            self.passive()
   
   
    def buffdebuff(self, target, *args):
        if self.mp - 50 < 0:
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
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용했습니다!')
            slow_print(f'흑사병이 퍼져서 시전자의 앞, 뒤 플레이어 및 {target.name}의 앞, 뒤 플레이어가 {self.name}의 패시브를 가집니다.')
            print()
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbtarget.append(target)
            self.bdbtarget.append(args)
            self.bdbturn += 999999999999999999999999999999999999999999999999999999999999999
            
   
    def ultimate(self, target):
        if self.mp - 150 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif len(self.utarget) == 3:
            slow_print('궁극기 사용 횟수를 다하였습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif target not in self.bdbtarget:
            slow_print('대상은 현재 병을 가지고 있지 않습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.bdbtarget.remove(target)
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.ultimatename}를 사용합니다!')
            slow_print(f'{target.name}에게 부여된 {self.passivename} 상태를 해제했습니다.')
            print()
            self.mp += self.rmp - 150
            slow_print(f'{self.name}의 마나가 150 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.turn += 1
            self.usturn -= 1
            if self.usturn == 0:
                self.uturn += 3
            self.passive()
   
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 자신의 턴마다 자기 자신에게 고정 피해를 입히는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 체력을 소모하여 자신의 신체에서 떨어져 나온 뼈로 상대를 공격하는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 [{self.passivename}] 효과를 부여하여 시전자의 턴마다 피해를 입히는 (디)버프 스킬입니다.')
        slow_print(f'스킬의 대상은 시전자의 앞, 뒤 플레이어 및 대상자의 앞, 뒤 플레이어 입니다.')
        slow_print(f'[{self.ultimatename}]은/는 자신을 포함해 최대 세번 [{self.passivename}] 효과를 치유하는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다. 궁극기 사용은 최대 3번 입니다.')
        print()






