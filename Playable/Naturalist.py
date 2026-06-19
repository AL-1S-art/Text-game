from Util import *
from character import Buff, Player


class Naturalist(Player):
    def __init__(self,name):
        self.hhp = 2109
        self.hp = self.hhp
        self.ad = 89
        self.de = 104
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 365
        self.mp = self.hmp
        self.rmp = 11
        self.shield = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '자연 치유'
        self.normalname = '평타'
        self.damageskillname = '침식'
        self.buffdebuffname = '덩굴조작'
        self.ultimatename = '퇴적층 생성'
        self.bdbtarget = []
        self.utarget = []        
        super().__init__(name)
        self.classname = '자연술사'
        self.buffskilltarget = 'enemy'
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    def passive(self):
        if self.turn%2 == 0:
            self.hp += self.hhp*(23/1000)
    
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
            self.utarget[0].hp -= int((((self.ad*8.98) * 0.9) + 400) * (100/(100+target.de)))
            self.uturn -= 1
            if self.uturn == 0:
                self.utarget[0].remove()
        if self.bdbturn > 0:
            self.bdbturn -= 1
            if self.bdbturn == 0:
                self.bdbtarget[0].de = self.bdbtarget[0].de / 0.3
                self.bdbtarget[0].remove()
        self.turn += 1
        self.passive()

    
    def damageskill(self, target):
        if self.mp - 60 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int((((self.ad*8.98)*0.8) + 310) * (100/(100+target.de)))
            
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 60
            slow_print(f'{self.name}의 마나가 60 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            if self.uturn > 0:
                self.utarget[0].hp -= int((((self.ad*8.98) * 0.9) + 400) * (100/(100+target.de)))
                self.uturn -= 1
                if self.uturn == 0:
                    self.utarget[0].remove()
            if self.bdbturn > 0:
                self.bdbturn -= 1
                if self.bdbturn == 0:
                    self.bdbtarget[0].de = self.bdbtarget[0].de / 0.3
                    self.bdbtarget[0].remove()
            self.turn += 1
            self.passive()

    
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
            target.bufflist.append(Buff('물의 침식','statuschange',1,1,{'de':int(target.de*0.3)},target))
            slow_print(f'{self.name}이/가 {target.name}에게 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}의 방어력을 30%를 감소시킵니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 1
            self.turn += 1
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
            damm = int((((self.ad*8.98) * 0.75) + 400) * (100/(100+target.de)))
            
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.ultimatename}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 피해를 2턴 동안 입힙니다.')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 피해를 입힙니다.')
            target.bufflist.append(Buff('질식','cc',2,1,'Null',target))
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            if self.bdbturn > 0:
                self.bdbturn -= 1
                if self.bdbturn == 0:
                    self.bdbtarget[0].de = self.bdbtarget[0].de / 0.3
                    self.bdbtarget[0].remove()
            self.turn += 1
            self.uturn += 1
            self.passive()

    
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 자신의 2턴이 지날 때마다 체력을 회복하는 패시브입니다.')
        slow_print(f'[self.normalname]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 5만 년 치의 물의 침식 작용을 주는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 바로 다음 공격이 대상의 방어력을 30% 무시시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 침식과 퇴적을 반복하는 퇴적층에 대상을 가두어 질식시키는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()

