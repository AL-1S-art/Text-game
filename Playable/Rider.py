from Util import *
from character import Buff, Player

class Rider(Player):
    def __init__(self,name):
        
        self.classname = '라이더'
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
        self.shield = 0
        self.passivename = '바이크' #매 라운드가 지날 때 마다 속력 획득, 속력에 비례해 스킬딜량 증가
        self.normalname = '평타'
        self.damageskillname = '발가락 골절' #상대를 밟고 간다
        self.buffdebuffname = '윌리' #앞바퀴를 들어올려 방어력을 낮추고 공격력을 높임
        self.ultimatename = '준자살' #교통사고 속력 비례 대미지 입히고 3턴동안 휠체어를 타서 방어력을 높인다
        super().__init__(name)
    def dealdamm(self, damage):
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
            self.de *= 1.5
            self.ad *= 1.5
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 영구적으로 방어력과 공격력이 1.5배로 증가합니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 2
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
        slow_print(f'[{self.passivename}]은/는 매턴 마다 자기 자신에게 피해를 입히는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 오토바이로 대상의 발가락을 밟고가 골절 시키는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 2턴 동안 방어력이 0.5배가 증가하고 공격력을 2배로 증가시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 속력에 비례해 상대방에게 들이 박고 3턴 동안 휠체어를 타 방어력을 높이는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()

