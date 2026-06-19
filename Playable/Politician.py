
from Util import *
from character import Buff, Player

class Politician(Player):
    def __init__(self,name):
        
        self.hhp = 2200
        self.hp = self.hhp
        self.ad = 150
        self.de = 100
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 250
        self.mp = self.hmp
        self.shield = 0
        self.rmp = 20
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '대중의 지지' #정치인은 대중의 지지율에 따라 피해량이 바뀝니다. 지지율이 높을수록 피해량이 증가하며, 낮을수록 피해량이 감소합니다. 만약 지지율이 100% 이상이라면 즉시 승리하며, 0% 미만이라면 즉시 패배합니다.
        self.normalname = '평타' #정치인이 전국을 순회하여 연설을 합니다. 만약 입힌 피해량이 짝수이면, 지지율이 증가하며, 홀수시, 지지율이 감소합니다. (증가/감소량은 피해량의 10%입니다.)
        self.damageskillname = '후보 공격' #정치인이 상대 후보를 공격합니다. 만약 입힌 피해량이 홀수이면, 지지율이 증가하며, 짝수시, 지지율이 감소합니다. (증가/감소량은 피해량의 15%입니다.)
        self.buffdebuffname = '당의 지원' #당의 지원을 받아 방어력이 30 상승합니다. 또한 지지율이 50% 이상이면, 추가로 체력이 20% 회복됩니다. 최대 1회 사용 가능합니다.
        self.ultimatename = '대선 토론' #대선 토론을 엽니다. 다음 3턴동안 정치인의 공격이 방어력을 무시하며, 3턴 후 정치인이 입힌 피해량이 상대보다 많다면, 지지율을 40% 획득하며, 적보다 피해량이 적다면, 지지율을 40% 잃습니다. 
        self.popularity = 50
        self.prevhp = self.hp
        self.mytotaldamm = 0
        self.opptotaldamm = 0
        self.ultimateturn = 0
        self.supportused = False
        self.classname = '정치인'
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
        self.prevhp = self.hp
        if self.ultimateturn > 0:
            self.ultimateturn -= 1
            self.opptotaldamm += self.prevhp - self.hp
            if self.ultimateturn == 0:
                self.passivename = '대중의 지지'
                self.normalname = '평타' 
                self.damageskillname = '후보 공격'
                if self.mytotaldamm > self.opptotaldamm:
                    self.popularity += 40
                    slow_print(f'대선 토론에서 승리하여 지지율이 40% 증가하여 {self.popularity}%가 되었습니다.')
                elif self.mytotaldamm < self.opptotaldamm:
                    self.popularity -= 40
                    slow_print(f'대선 토론에서 패배하여 지지율이 40% 감소하여 {self.popularity}%가 되었습니다.')
                else:
                    slow_print('대선 토론에서 비겼습니다. 지지율에 변화가 없습니다.')
        if self.popularity >= 100:
            slow_print(f'{self.name}가 대중의 선택을 받았습니다!')
            target.hp = -9999
            slow_print(f'\r{target.name}의 체력이 {target.hp} 남았습니다.')
            print()
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        elif self.popularity <= 0:
            slow_print(f'{self.name}이/가 대중의 지지를 완전히 잃어버렸습니다.')
            self.hp = -9999
            slow_print(f'\r{self.name}의 체력이 {self.hp} 남았습니다.')
            print()
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
    def normal(self, target):
        if self.ultimateturn > 0:
            damm = int(self.ad*self.popularity/50)
            
            slow_print(f'{self.name}이/가 대선 토론에서 정책을 제안합니다! 공격이 방어력을 무시하며, 지지율에 비례한 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            if damm % 2 == 0:
                self.popularity += 10
                slow_print(f'정책 제안이 호응을 얻어 지지율이 {10}% 증가하여 {self.popularity}%가 되었습니다.')
            else:
                self.popularity -= 10
                slow_print(f'정책 제안이 비판을 받아 지지율이 {10}% 감소하여 {self.popularity}%가 되었습니다.')
        else:
            damm = int((self.ad * (100/(100+target.de)))*2*(self.popularity/100)*2)
            
            slow_print(f'{self.name}이/가 전국을 순회하며 연설을 합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            if damm % 2 == 0:
                self.popularity += 10
                slow_print(f'연설이 성공적으로 끝나 지지율이 {10}% 증가하여 {self.popularity}%가 되었습니다.')
            else:
                self.popularity -= 10
                slow_print(f'연설이 실망스럽게 끝나 지지율이 {10}% 감소하여 {self.popularity}%가 되었습니다.')
            print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.mytotaldamm += damm
        self.turn += 1
        self.passive(target)
    def damageskill(self, target):
        if self.ultimateturn > 0:
            damm = int(self.ad*self.popularity/50*2)
            
            slow_print(f'{self.name}이/가 대선 토론에서 상대 후보에게 반론을 제시합니다! 공격이 방어력을 무시하며, 지지율에 비례한 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            if damm % 2 == 1:
                self.popularity += 15
                slow_print(f'반론이 성공적으로 끝나 지지율이 {15}% 증가하여 {self.popularity}%가 되었습니다.')
            else:
                self.popularity -= 15
                slow_print(f'반론이 터무니없어서 지지율이 {15}% 감소하여 {self.popularity}%가 되었습니다.')
        else:
            damm = int((self.ad * (100/(100+target.de)))*2*(self.popularity/100)*2)
            
            slow_print(f'{self.name}이/가 상대 후보를 공격합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            if damm % 2 == 1:
                self.popularity += 15
                slow_print(f'공격이 호응을 얻어 지지율이 {15}% 증가하여 {self.popularity}%가 되었습니다.')
            else:
                self.popularity -= 15
                slow_print(f'공격이 비판을 받아 지지율이 {15}% 감소하여 {self.popularity}%가 되었습니다.')
            print()
        self.mp += self.rmp - 60
        slow_print(f'{self.name}의 마나가 60만큼 소모되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        self.mytotaldamm += damm
        self.turn += 1  
        self.passive(target)
    def buffdebuff(self, target):
        if self.supportused:
            slow_print('당의 지원은 최대 1회 사용 가능합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.bufflist.append(Buff('당의 지원','statuschange','Null',1,{'de':30},self))
            if self.popularity >= 50:
                heal = int((self.hhp-self.hp)*0.2)
                self.hp += heal
                if self.hp > self.hhp:
                    self.hp = self.hhp
                slow_print(f'{self.name}이/가 당의 지원을 받습니다! 방어력이 30 상승하며, 지지율이 50% 이상이므로 체력이 {heal}만큼 회복되어 {self.hp}가 되었습니다.')
            else:
                slow_print(f'{self.name}이/가 당의 지원을 받습니다! 방어력이 30 상승합니다.')
            print()
            self.mp += self.rmp - 40
            slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.supportused = True
            if self.uturn > 0:
                self.uturn -= 1
            if self.bdbturn > 0:
                self.bdbturn -= 1
            self.turn += 1
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
        else:
            self.normalname = '정책 제시'
            self.damageskillname = '반론 제기'
            slow_print(f'대선토론이 시작되었습니다! 다음 3턴동안 상대에게 피해를 더 준 플레이어가 대선토론에서 승리합니다.')
            slow_print(f'또한 다음 3턴동안 {self.name}이 입히는 피해가 방어력을 무시합니다.')
            print()
            self.ultimateturn += 3
            self.uturn += 6
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 지지율에 따라 피해량이 바뀌는 패시브입니다. 지지율이 높을수록 피해량이 증가하며, 낮을수록 피해량이 감소합니다. 만약 지지율이 100% 이상이라면 즉시 승리하며, 0% 미만이라면 즉시 패배합니다.')
        slow_print(f'[{self.normalname}]은/는 전국을 순회하며 연설을 하는 기본 스킬입니다. 입힌 피해량이 짝수이면 지지율이 증가하며, 홀수이면 지지율이 감소합니다. (증가/감소량은 피해량의 10%입니다.)')
        slow_print(f'[{self.damageskillname}]은/는 상대 후보를 공격하는 공격 스킬입니다. 입힌 피해량이 홀수이면 지지율이 증가하며, 짝수이면 지지율이 감소합니다. (증가/감소량은 피해량의 15%입니다.)')
        slow_print(f'[{self.buffdebuffname}]은/는 당의 지원을 받는 (디)버프 스킬입니다. 방어력이 30 상승하며, 지지율이 50% 이상이면 추가로 체력이 20% 회복됩니다. 최대 1회 사용 가능합니다.')
        slow_print(f'[{self.ultimatename}]은/는 대선 토론을 여는 궁극기입니다. 다음 3턴동안 공격이 방어력을 무시하며, 3턴 후 입힌 피해량에 따라 지지율이 변동합니다. 입힌 피해량이 상대보다 많다면 지지율을 40% 획득하며, 적보다 피해량이 적다면 지지율을 40% 잃습니다.')
        print()
