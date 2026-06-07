from Util import *
from character import Buff, Player



class ChessPlayer(Player):
    def __init__(self,name):
        
        self.hhp = 2000
        self.hp = self.hhp
        self.ad = 80
        self.de = 100
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 200
        self.mp = self.hmp
        self.rmp = 20
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 99999
        self.turn = 0
        self.passivename = '프로모션' #체스 플레이어는 공격을 직접 할 수 없으며, 체스 기물을 통해서만 할 수 있습니다. 기물은 폰으로 시작하며, 만약 체스 플레이어가 6회 행동한다면, 퀸으로 승진합니다. 승진 후에는 공격력이 2배로 증가하고 방어력이 1.5배로 증가하며, 체력이 2000 증가하고 모든 스킬이 강화됩니다. (강화된 스킬은 각각의 스킬 설명을 참고해주세요.)
        self.normalname = '1. d3' #폰을 전진시킵니다. 
        self.damageskillname = '1. d3' #폰을 전진시킵니다.
        self.buffdebuffname = '캐슬링' #캐슬링을 합니다. 체스 플레이어의 방어력이 50 상승하며, 체력을 잃은 체력에 비례해 회복합니다. 최대 1회 사용 가능합니다.
        self.ultimatename = '1. d3' #퀸 기물이 존재할때만 사용 가능합니다. 적의 방어력을 무시하고 공격하며, 적의 잃은 체력에 비례한 피해를 입힙니다. 
        self.piece = 'Pawn'
        self.actioncount = 0
        self.shield = 0
        self.castlingused = False
        self.square = 3
        self.classname = '체스선수'
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
        if self.square == 9 and self.piece == 'Pawn':
            self.piece = 'Queen'
            self.ad *= 2
            self.de = int(self.de*1.5)
            self.hhp += 2000
            self.hp += 2000
            self.passivename = '체크메이트'
            self.normalname = '평타'
            self.damageskillname = 'Qxe4+'
            self.ultimatename = '로얄 포크'
            self.uturn = 0
            slow_print(f'{self.name}이/가 체스보드의 끝에 도달해 승진하였습니다! 공격력이 2배로 증가하고 방어력이 1.5배로 증가하며, 최대 체력이 2000 증가하고 모든 스킬이 강화됩니다!')
            print()
            
        if self.piece == 'Queen':
            if target.hp <= target.hhp*0.1:
                slow_print(f'적이 빠져나갈곳이 없습니다!')
                time.sleep(0.5)
                moreslow_print('[체크메이트]')
                time.sleep(0.5)
                target.hp = -9999
                slow_print(f'\r{target.name}의 체력이 {target.hp} 남았습니다.')
                print()
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
    def normal(self, target):
        if self.piece == 'Pawn':
            slow_print(f'{self.name}이/가 폰을 1칸 전진시킵니다!')
            self.square += 1
            self.squarename = str(self.square-2)+'. d'+str(self.square)
            self.normalname = self.squarename
            self.damageskillname = self.squarename
            self.passive(target)
            print()
            self.mp += self.rmp
            slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
        else:
            damm = 400
            
            slow_print(f'{self.name}이/가 퀸으로 {target.name}에게 공격을 시도합니다!')
            slow_print(f'체크!')
            self.passive(target)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp
            slow_print(f'{self.name}의 마나가 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
        if self.uturn > 0:
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.actioncount += 1
        self.turn += 1
    def damageskill(self, target):
        if self.piece == 'Pawn':
            slow_print(f'{self.name}이/가 폰을 1칸 전진시킵니다!')
            self.square += 1
            self.squarename = str(self.square-2)+'. d'+str(self.square)
            self.normalname = self.squarename
            self.damageskillname = self.squarename
            self.passive(target)
            print()
            self.mp += self.rmp
            slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
        else:
            damm = 700
            
            slow_print(f'{self.name}이/가 퀸으로 {target.name}에게 공격을 시도합니다!')
            
            slow_print(f'체크!')
            self.passive(target)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 60
            slow_print(f'{self.name}의 마나가 60만큼 소모되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
        if self.uturn > 0:
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.actioncount += 1
        self.turn += 1
    def buffdebuff(self, target):
        if self.castlingused:
            slow_print('캐슬링은 최대 1회 사용 가능합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.de += 50
            self.hp += int((self.hhp-self.hp)*0.3)
            if self.hp > self.hhp:
                self.hp = self.hhp
            slow_print(f'{self.name}이/가 캐슬링을 합니다! 방어력이 50 상승하며, 체력을 잃은 체력에 비례하게 회복합니다.')
            print()
            self.mp += self.rmp - 40
            slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.castlingused = True
            if self.uturn > 0:
                self.uturn -= 1
            self.turn += 1
    def ultimate(self, target):
        if self.piece != 'Queen':
            slow_print('퀸 기물이 존재할 때만 사용할 수 있습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = 1000+int((target.hhp-target.hp)*0.3)
            
            slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다! 잃은 체력에 비례해 추가 피해를 입힙니다!')
            
            slow_print('체크!')
            self.passive(target)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다!')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.uturn += 3
    def explanation(self):
        if self.piece == 'Pawn':
            slow_print(f'[{self.passivename}]은/는 6회 행동 시 퀸으로 승진하는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 폰을 전진시키는 기본 스킬입니다.')
            slow_print(f'[{self.damageskillname}]은/는 폰을 전진시키는 기본 스킬입니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 캐슬링을 하는 (디)버프 스킬입니다. 캐슬링을 하면 방어력이 50 상승하며, 체력을 잃은 체력에 비례해 회복합니다. 최대 1회 사용 가능합니다.')
        else:
            slow_print(f'[{self.passivename}]은/는 적에게 고정 피해를 입히며, 적이 체력이 10% 이하로 떨어졌을 때 체크메이트가 발동하는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 퀸으로 적에게 공격하는 기본 스킬입니다.')
            slow_print(f'[{self.damageskillname}]은/는 퀸으로 적에게 공격하는 공격 스킬입니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 캐슬링을 하는 (디)버프 스킬입니다. 캐슬링을 하면 방어력이 50 상승하며, 체력을 잃은 체력에 비례해 회복합니다. 최대 1회 사용 가능합니다.')
            slow_print(f'[{self.ultimatename}]은/는 퀸으로 적에게 공격하는 궁극기입니다. 적의 잃은 체력에 비례한 피해를 입힙니다.')
        print()
