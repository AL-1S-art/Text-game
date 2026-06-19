from Util import *
from character import Buff, Player
       

class Pitcher(Player):
    def __init__(self,name):
        
        self.hhp = 2200
        self.hp = self.hhp
        self.ad = 200
        self.de = 120
        self.originalde = self.de
        self.originalad = self.ad
        self.shield = 0
        self.hmp = 300
        self.mp = self.hmp
        self.rmp = 20
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '삼진아웃'
        self.normalname = '직구'
        self.damageskillname = '강속구'
        self.buffdebuffname = '너클볼'
        self.ultimatename = '스타디움의 지배자'
        self.strikelist = {}
        self.out = 0
        self.ultimateused = False
        super().__init__(name)
        self.buffskilltarget = 'enemy'
        self.ultimatetarget = 'self'
        self.classname = '투수'
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    
    def passive(self, target):
        if target not in self.strikelist.keys():
            self.strikelist[target] = 0
        self.strikelist[target] += 1
        slow_print(f'{target.name} {str(self.strikelist[target])} 스트라이크!')
        if self.strikelist[target] == 3:
            damm = int(300 +  self.ad * 0.5)
            
            slow_print(f'{target.name}이/가 삼진아웃되었습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 추가피해를 입힙니다.')
            target.dealdamm(damm)
            self.strikelist[target] = 0
            self.out += 1
            slow_print(f'{self.out} 아웃!')
        if self.bdbturn > 0:
            self.bdbturn -= 1

    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*1)
        slow_print(f'{self.name}이/가 직구를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        self.passive(target)
        
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()

    
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            slow_print(f'{self.name}이/가 {target.name}을 향해 {self.damageskillname}을/를 던집니다!')
            damm = int((self.ad * (100/(100+target.de)))*2)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            self.passive(target)
            
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.turn += 1

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
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 던집니다!')
            self.passive(target)
            damm =  int((self.ad * (100/(100+target.de)))*2)
            if len(list(filter(lambda buff : buff.name == '데드볼',target.bufflist))) == 0:
                target.bufflist.append(Buff('데드볼','statuschange','Null',1,{'de':10},target))
            else:
                list(filter(lambda buff : buff.name == '데드볼',target.bufflist))[3] += 1
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다. 또한 {target.name}의 방어력을 10만큼 감소시킵니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            self.bdbturn += 3
            print()

    
    def ultimate(self, target):
        if self.mp - 100 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.uturn > 0:
            slow_print('궁극기 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.ultimateused:
            slow_print('궁극기를 이미 사용했습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            slow_print(f'{self.name}이/가 궁극기를 사용합니다!')
            slow_print(f'타자를 아웃시킨 횟수가 {str(self.out)}회 입니다!')
            if self.out == 0:
                slow_print('관중들이 야유합니다!')
                slow_print(f'{self.name}의 공격력이 10 감소합니다.')
                self.ad -= 10
            elif self.out <= 2:
                slow_print('관중들이 환호합니다!')
                slow_print(f'{self.name}의 공격력과 방어력이 20 증가하며, 체력을 100 회복합니다!')
                self.ad += 20
                self.de += 20
                self.hp += 100
            elif self.out >2:
                slow_print(f'{self.name}이/가 스타디움을 지배하고 있습니다!!!')
                slow_print(f'관중들이 열광하고 있습니다!!')
                self.ad += self.out * 30
                self.de += self.out * 30
                self.hp += 100*self.out
                slow_print(f'{self.name}의 공격력과 방어력이 {str(self.out * 30)} 상승하며, 체력이 {str(self.out * 100)} 회복됩니다!')
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.ultimateused = True
            self.passive(target)

    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 적을 3번 공격할때마다 적을 아웃시키고 추가피해를 입히는 패시브입니다.')
        slow_print(f'[{self.normalname}]은/는 직구를 던지는 기본공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 강속구를 던지는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 포크볼을 던져 피해를 주고 방어력을 감소시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 아웃횟수에 따라 버프를 얻는 궁극기입니다. 최대 1회 사용 가능합니다.')
        print()