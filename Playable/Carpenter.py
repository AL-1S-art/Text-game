from Util import *
from character import Buff, Player
       
class Carpenter(Player):
    def __init__(self,name):
        
        self.hhp = 3000
        self.hp = self.hhp
        self.ad = 80
        self.de = 120
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 200
        self.mp = self.hmp
        self.rmp = 20
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '고된 업무' 
        self.normalname = '평타'         
        self.damageskillname = '못 박기' 
        self.buffdebuffname = '성경 읽기' 
        self.ultimatename = '아가페 탄생'  
        self.shield = 0
        self.ultimateon = 0
        self.passivecool = 0
        self.resurracting = False
        self.resurractingtime = 0
        self.ode = 120
        self.oad = 120
        self.bdbtime = 0
        self.line = ['그리스도께서 우리 죄를 위하여 죽으시고','장사 지낸 바 되셨다가','성경대로 사흘 만에 다시 살아나사']
        super().__init__(name)
        self.ultimatetarget = 'self'
        self.classname = '목수'
    def dealdamm(self, damage):
        if len(list(filter(lambda x: x.name == '그리스도의 부활',self.bufflist))) == 0:
            self.shield -= int(damage)
            if self.shield <= 0:
                self.hp += self.shield
                self.shield = 0
            if self.hp > 0:
                slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
            elif self.passivecool == 0 and len(list(filter(lambda x: x.name == '하나님의 아들',self.bufflist))) != 0:
                self.hp = 2
                slow_print(f'{self.name}이/가 사망하였습니다...?')
                self.bufflist.clear()
                self.bufflist.append(Buff('그리스도의 부활','resurraction',2,1,'Null',self))
                self.passivecool += 8
                self.damageskillname = '못 박기'
                self.passivename = '고된 업무'
            else:
                slow_print(f'{self.name}이/가 사망하였습니다!')
                return
        else:
            self.hp = 2
        print()                
                
    def passive(self, target):
        if len(list(filter(lambda x: x.name == '하나님의 아들',self.bufflist))) != 0:
            self.buffskilltarget = 'enemy'
            self.ultimateon -= 1
            self.shield += 300
            if self.shield > 700:
                self.shield = 700
            slow_print(f'{self.name}이/가 방어막을 획득합니다.')
        else:
            self.hp += 30
            self.buffskilltarget = 'self'
            if self.hp >= self.hhp:
                self.hp = self.hhp
            slow_print(f'{self.name}이가 고된 업무 후에 휴식을 취하며 체력을 30 재생했습니다.')
            if self.uturn > 0:
                self.uturn -= 1
            if self.bdbturn > 0:
                self.bdbturn -= 1
            if self.bdbtime == 1:
                self.de -= 50
                self.bdbtime = 0
            elif self.bdbtime == 2:
                target.de += 30
                target.ad += 30
                self.bdbtime = 0
            else:
                self.bdbtime -= 2
    def normal(self, target):
        if len(list(filter(lambda x: x.name == '하나님의 아들',self.bufflist))) == 0:
            slow_print(f'{self.name}이/가 {target.name}을/를 공격합니다.')
            damm = int(self.ad * (100/(target.de+100))*1.5)
        else:
            damm = int(self.ad * (100/(target.de+100))*2)
            moreslow_print('“원수를 사랑하라.”')
            slow_print(f'{self.name}이/가 {target.name}에게 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        self.passive(target)
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 마나가 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        self.turn += 1
    def damageskill(self, target):
        if len(list(filter(lambda x: x.name == '하나님의 아들',self.bufflist))) == 0:
            slow_print(f'{self.name}이/가 망치로 못을 박습니다!')
            damm = int(self.ad * (100/(target.de+100))*2)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        else:
            damm = int(self.ad * (100/(target.de+100))*3.5)
            moreslow_print(f'“아버지여, 저들을 사하여 주옵소서.”')
            slow_print(f'{self.name}이/가 {target.name}을/를 십자가에 매답니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        self.passive(target)
        print()
        self.mp += self.rmp - 60
        slow_print(f'{self.name}의 마나가 60만큼 소모되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        self.turn += 1
    def buffdebuff(self, target):
        if self.bdbturn > 0:
            slow_print('버프/디버프스킬이 아직 쿨타임입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.bdbturn += 5
            if self.ultimateon == 0:
                self.de += 50
                slow_print(f'{self.name}이/가 마음을 가다듬습니다! 방어력이 2턴동안 50 상승합니다.')
                self.bdbtime = 5
            else:
                moreslow_print('“화 있을진저, 외식하는 서기관들과 바리새인들이여”')
                slow_print(f'{self.name}이/가 {target.name}에게 설교를 해 공격력과 방어력을 2턴동안 30 감소시킵니다.')
                target.ad -= 30
                target.de -= 30
                self.bdbtime = 6
            print()
            self.mp += self.rmp - 40
            slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            return
    def ultimate(self, target):
        if self.mp < 70:
            slow_print('마나가 부족합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.hp > self.hhp * 0.5:
            slow_print('궁극기 발동 조건이 만족되지 않았습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            moreslow_print('“나는 길이요 진리요 생명이니”')
            slow_print(f'{self.name}이/가 예수로 각성합니다!')
            slow_print(f'{self.name}의 최대체력과 방어력이 절반으로 감소하지만, 공격력이 3배로 증가하며, 매 턴마다 보호막을 얻습니다!')
            self.passive(target)
            self.bufflist.append(Buff('하나님의 아들', 'statuschange','Null',1,{'de':(-1*self.de//2),'ad':(self.ad*2),'hhp':-1*(self.hhp//2)},self))
            self.passivename = '재림'
            self.damageskillname = '역지사지'
            print()
            self.mp += self.rmp - 70
            slow_print(f'{self.name}의 마나가 70 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.uturn += 5
    def explanation(self):
        if self.ultimateon == 0:
            slow_print(f'[{self.passivename}]은/는 턴마다 소량의 체력을 회복하는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 적에게 피해를 입히는 기본 스킬입니다.')
            slow_print(f'[{self.damageskillname}]은/는 못을 박아 적에게 피해를 입히는 기본 스킬입니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 마음을 가다듬어 방어력을 2턴동안 상승시키는 버프 스킬입니다.')
            slow_print(f'{self.ultimatename}은/는 체력이 최대체력의 50% 이하일시 사용 가능합니다. 예수로 각성하며 최대체력과 방어력이 절반 감소하지만, 공격력이 3배 상승하며 매 턴마다 보호막을 얻습니다. 또한 스킬이 모두 업그레이드 됩니다.')
        else:
            slow_print(f'[{self.passivename}]은/는 체력이 0에 도달시 3턴에 걸쳐 부활하는 패시브입니다(쿨타임 8턴).')
            slow_print(f'[{self.normalname}]은/는 적에게 공격하는 기본 스킬입니다.')
            slow_print(f'[{self.damageskillname}]은/는 적을 십자가에 매달아 방어력을 소량 무시해 피해를 입히는 공격 스킬입니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 2턴동안 적의 방어력과 공격력을 30 감소시키는 디버프 스킬입니다.')
        print()
