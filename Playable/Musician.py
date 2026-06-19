from Util import *
from character import Buff, Player
       
class Musician(Player):
    def __init__(self,name):
        
        self.hhp = 1800
        self.hp = self.hhp
        self.ad = 100
        self.de = 100
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 300
        self.mp = self.hmp
        self.rmp = 20
        self.shield = 0
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '악기 전문가' #음악가는 악기를 2가지중 하나 선택할 수 있습니다. 피아노를 선택하면 최대체력이 2500, 방어력이 50 증가하며, 스킬사용시 체력을 회복합니다. 바이올린을 선택시 공격력이 100 증가하며, 스킬이 최대체력에 비례한 피해를 입힙니다.
        self.normalname = '평타' #음악가가 연주를 하여 적에게 피해를 입힙니다. 악기가 피아노일 시 체력을 50 회복하며, 악기가 바이올린일 시 적의 최대체력의 5%에 비례한 추가피해를 입힙니다.
        self.damageskillname = '세레나데' #음악가가 연주를 하여 적에게 피해를 입힙니다. 악기가 피아노일 시 체력을 100 회복하며, 악기가 바이올린일 시 적의 최대체력의 10%에 비례한 추가피해를 입힙니다.
        self.buffdebuffname = '조화로운 멜로디' #음악가가 아름다운 선율을 연주합니다. 악기가 피아노일 시 체력을 10% 회복하며, 악기가 바이올린일 시 공격력이 50 증가합니다. 공격력 증가는 2턴동안 유지되며, 최대 1회 사용 가능합니다.
        self.ultimatename = '피날레' #연주가 피날레에 들어갑니다! 악기가 피아노일 시 체력을 30% 회복하며, 방어력이 영구적으로 50 증가합니다. 악기가 바이올린일 시 적의 최대체력의 20%에 해당하는 고정피해를 입히며, 적의 방어력을 영구적으로 10% 감소시킵니다. 최대 1회 사용 가능합니다.
        self.instrument = ''
        self.ultimateused = False
        self.bdbtime = 0
        self.classname = '음악가'
        super().__init__(name)
        self.passive()
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    
    def passive(self):
        if self.instrument == '':
            print(f'{self.name}이/가 악기를 선택합니다!')
            while 1:
                slow_print('악기를 선택하세요 (피아노 / 바이올린)')
                self.instrument = input()
                if self.instrument not in ['피아노', '바이올린']:
                    print('잘못된 선택입니다. 다시 선택해주세요.')
                else:
                    break
            if self.instrument == '피아노':
                self.hhp += 2500
                self.originalhhp = self.hhp
                self.ultimatetarget = 'self'
                self.hp += 2500
                self.de += 50
                self.originalde = self.de
                self.passivename = '악기 전문가 - 피아노'
                self.normalname = '평타'
                self.damageskillname = '월광 소나타'
                self.buffdebuffname = '조화로운 멜로디'
                self.ultimatename = '피날레 - 라 캄파넬라'
                slow_print(f'{self.name}이/가 악기 전문가 패시브로 피아노를 선택하였습니다! 최대 체력이 200 증가하고, 방어력이 50 증가하며, 모든 스킬 사용 시 체력을 회복합니다!')
                print()
            elif self.instrument == '바이올린':
                self.ad += 100
                self.originalad = self.ad
                self.ultimatetarget = 'enemy'
                self.passivename = '악기 전문가 - 바이올린'
                self.normalname = '평타'
                self.damageskillname = '바이올린 협주곡 제1번'
                self.buffdebuffname = '조화로운 멜로디'
                self.ultimatename = '피날레 - 사계'
                slow_print(f'{self.name}이/가 악기 전문가 패시브로 바이올린을 선택하였습니다! 공격력이 100 증가하며, 모든 스킬이 적의 최대체력에 비례한 피해를 입힙니다!')
                print()
        if self.instrument == '바이올린':
            if self.bdbtime > 0:
                self.bdbtime -= 1
                if self.bdbtime == 0:
                    self.ad -= 50
                    slow_print(f'{self.name}의 조화로운 멜로디 버프가 끝났습니다. 공격력이 50 감소하여 {self.ad}가 되었습니다.')
                    print()
    def normal(self, target):
        if self.instrument == '피아노':
            heal = 50
            self.hp += heal
            if self.hp > self.hhp:
                self.hp = self.hhp
            damm = int((self.ad * (100/(100+target.de)))*2)
            
            slow_print(f'{self.name}이/가 잔잔한 선율을 연주합니다! 선율이 아름다워 체력이 {heal}만큼 회복됩니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
        elif self.instrument == '바이올린':
            damm = int((self.ad * (100/(100+target.de)))*2 + target.hhp*0.05)
            
            slow_print(f'{self.name}이/가 강렬한 선율을 쌓아올립니다! 적의 최대체력에 비례한 추가 피해를 입힙니다!')
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
        if self.instrument == '피아노':
            heal = 100
            self.hp += heal
            if self.hp > self.hhp:
                self.hp = self.hhp
            damm = int((self.ad * (100/(100+target.de)))*2.5)
            
            slow_print(f'{self.name}이/가 피아노를 연주합니다! 선율이 더욱 아름다워 체력이 {heal}만큼 회복됩니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
        elif self.instrument == '바이올린':
            damm = int((self.ad * (100/(100+target.de)))*2.5 + target.hhp*0.1)
            
            slow_print(f'{self.name}이/가 바이올린을 연주합니다! 적의 최대체력에 비례한 추가 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
        print()
        self.mp += self.rmp - 40
        slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()
        if self.uturn > 0: 
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.turn += 1
        self.passive()
    def buffdebuff(self, target):
        if self.instrument == '피아노':
            heal = int(self.hhp*0.1)
            self.hp += heal
            if self.hp > self.hhp:
                self.hp = self.hhp
            slow_print(f'{self.name}이/가 조화로운 멜로디를 피아노로 연주합니다! 선율이 조화로워 체력이 {heal}만큼 회복됩니다!')
        elif self.instrument ==  '바이올린':
            self.bufflist.append(Buff('조화로운 멜로디','statuschange','2',1,{'ad':50},self))
            self.bdbtime += 2
            slow_print(f'{self.name}이/가 조화로운 멜로디를 바이올린으로 연주합니다! 선율이 조화로워 공격력이 50 증가하여 {self.ad}가 되었습니다! 공격력 증가는 2턴동안 유지됩니다!')
        print()
        self.mp += self.rmp - 40
        slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()
        if self.uturn > 0: 
            self.uturn -= 1
        self.turn += 1
        self.bdbturn += 10000000000
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
            slow_print('피날레곡은 오직 한번만 연주됩니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            if self.instrument == '피아노':
                heal = int(self.hhp*0.3)
                self.hp += heal
                if self.hp > self.hhp:
                    self.hp = self.hhp
                self.de += 50
                slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다! 피날레에 들어갑니다! 선율이 절정에 달하여 체력이 {heal}만큼 회복되고, 방어력이 영구적으로 50 증가합니다!')
                print()
            elif self.instrument == '바이올린':
                damm = int(target.hhp*0.3)
                
                target.bufflist.append(Buff('장송곡','statuschange',1,{'de':int(target.de*0.3)},target))
                slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다! 피날레에 들어갑니다! 적의 최대체력의 20%에 해당하는 고정피해를 입히며, 적의 방어력을 영구적으로 10% 감소시킵니다!')
                slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다!')
                target.dealdamm(damm)
                print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.uturn += 10000000000
            self.ultimateused = True
        self.turn += 1
        self.passive()
    def explanation(self):
        if self.instrument == '피아노':
            slow_print(f'[{self.passivename}]은/는 최대체력이 2500, 방어력이 50 증가하며, 스킬사용시 체력을 회복하는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 피아노를 연주하여 적에게 피해를 입히는 기본 공격입니다. 기본공격시 체력을 50 회복합니다.')
            slow_print(f'[{self.damageskillname}]은/는 피아노로 아름다운 곡을 연주하여 적에게 피해를 입히는 공격 스킬입니다. 스킬사용시 체력을 100 회복합니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 조화로운 멜로디를 피아노로 연주하는 (디)버프 스킬입니다. 선율이 조화로워 체력이 10% 회복됩니다.')
            slow_print(f'[{self.ultimatename}]은/는 피날레를 피아노로 연주하는 궁극기입니다. 선율이 절정에 달하여 체력이 30% 회복되고, 방어력이 영구적으로 50 증가합니다. 최대 1회 사용 가능합니다.')
        elif self.instrument == '바이올린':
            slow_print(f'[{self.passivename}]은/는 공격력이 100 증가하며, 모든 스킬이 적의 최대체력에 비례한 피해를 입히는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 바이올린을 연주하여 적에게 피해를 입히는 기본 공격입니다. 또한 적의 최대체력의 5%에 비례한 추가 피해를 입힙니다.')
            slow_print(f'[{self.damageskillname}]은/는 바이올린으로 강렬한 곡을 연주하여 적에게 피해를 입히는 공격 스킬입니다. 또한 적의 최대체력의 10%에 비례한 추가 피해를 입힙니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 조화로운 멜로디를 바이올린으로 연주하는 버프 스킬입니다. 선율이 조화로워 공격력이 50 증가합니다. 공격력 증가는 2턴동안 유지되며, 최대 1회 사용 가능합니다.')
            slow_print(f'[{self.ultimatename}]은/는 피날레를 바이올린으로 연주하는 궁극기입니다. 적의 최대체력의 30%에 해당하는 고정피해를 입히며, 적의 방어력을 영구적으로 30% 감소시킵니다. 최대 1회 사용 가능합니다.')
