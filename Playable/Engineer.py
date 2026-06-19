from Util import *
from character import Buff, Player


class Engineer(Player):
    def __init__(self,name):
        
        self.hhp = 2400
        self.hp = self.hhp
        self.ad = 120
        self.de = 100
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 200
        self.mp = self.hmp
        self.rmp = 20
        self.passiveturn = 0
        self.bdbturn = 0
        self.shield = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '장비 업그레이드' #엔지니어는 3턴마다 부품을 획득합니다. 부품은 버프스킬을 사용해 스탯 또는 스킬 업그레이드에 사용할 수 있다. 
        self.normalname = '평타' # 스패너를 적에게 던집니다.
        self.damageskillname = '레이저 용접' #엔지니어가 용접용 레이저를 적에게 발사합니다.
        self.buffdebuffname = '업그레이드!' #드론을 소환합니다.
        self.ultimatename = '로켓 발사' #.메가와트급 레이저를 적에게 발사합니다.
        self.parts = 0
        self.upgradelist = ['공격력 20 증가', '방어력 20 증가', '평타+', '레이저 용접+', '로켓 발사+', '설명']
        super().__init__(name)
        self.classname = '엔지니어'
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    
    def passive(self, target):
        if self.turn % 3 == 0:
            self.parts += 1
            slow_print(f'{self.name}이/가 부품을 획득하여 현재 {self.parts}개입니다!')
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        
        slow_print(f'{self.name}이/가 스패너를 적에게 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        if self.normalname != '평타':
            slow_print(f'{self.name}이/가 스패너에 맞아 방어력이 5 감소합니다!')
            if len(list(filter(lambda buff : buff.name == '골절',target.bufflist))) == 0:
                target.bufflist.append(Buff('골절','statuschange','Null',1,{'de':4},target))
            else:
                list(filter(lambda buff : buff.name == '골절',target.bufflist))[3] += 1
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0: 
            self.uturn -= 1
        self.turn += 1
        self.passive(target)
    def damageskill(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2.5)
        
        slow_print(f'{self.name}이/가 용접용 레이저를 적의 위치에 발사합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        if self.damageskillname != '레이저 용접':
            slow_print(f'{target.name} 주변의 지면이 온도가 급격히 높아져 폭발합니다!')
            
            slow_print(f'{target.name}이/가 폭발에 휘말려 {int(damm*1.1)}만큼 피해를 입힙니다!')
            target.dealdamm(damm)
        print()
        self.mp += self.rmp - 40
        slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0: 
            self.uturn -= 1
        self.turn += 1
        self.passive(target)
    def buffdebuff(self, target):
        if self.parts < 1:
            slow_print('부품이 부족하여 스킬을 사용할 수 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            slow_print(f'업그레이드 메뉴: {self.upgradelist}')
            while 1:
                choice = input('업그레이드할 항목을 입력해주세요: ')
                if choice not in self.upgradelist:
                    slow_print('올바른 항목을 입력해주세요.')
                elif choice == '설명':
                    slow_print('업그레이드 메뉴 설명:')
                    slow_print(' - 공격력 20 증가: 공격력이 20 상승합니다.')
                    slow_print(' - 방어력 20 증가: 방어력이 20 상승합니다.')
                    slow_print(' - 평타+: 평타가 상대의 방어력을 영구적으로 5 감소시킵니다.')
                    slow_print(' - 레이저 용접+: 레이저 용접이 지면을 폭발시켜 추가피해를 입힙니다.')
                    slow_print(' - 로켓 발사+: 로켓 발사가 상대의 방어력을 50% 무시하며, 또한 잃은 체력에 비례하는 추가피해를 입힙니다.')
                else:
                    break
            self.parts -= 1
            slow_print(f'{self.name}이/가 {choice} 업그레이드를 선택하였습니다! 남은 부품은 {self.parts}개입니다!')
            if choice == '공격력 20 증가':
                self.ad += 20
                slow_print(f'{self.name}의 공격력이 20 증가하여 {self.ad}가 되었습니다!')
            elif choice == '방어력 20 증가':
                self.de += 20
                slow_print(f'{self.name}의 방어력이 20 증가하여 {self.de}가 되었습니다!')
            elif choice == '평타+':
                self.normalname = '평타+'
                slow_print(f'{self.name}의 평타가 업그레이드 되었습니다! 평타가 상대의 방어력을 영구적으로 5 감소시킵니다!')
            elif choice == '레이저 용접+':
                self.damageskillname = '레이저 용접+'
                slow_print(f'{self.name}의 레이저 용접이 업그레이드 되었습니다! 레이저 용접이 지면을 폭발시켜 추가피해를 입힙니다!')
            elif choice == '로켓 발사+':
                self.ultimatename = '로켓 발사+'
                slow_print(f'{self.name}의 로켓 발사가 업그레이드 되었습니다! 로켓 발사가 상대의 방어력을 무시하며, 또한 잃은 체력에 비례하는 추가피해를 입힙니다!')
            print()
            self.mp += self.rmp - 40
            slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
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
        else:
            damm = int((self.ad * (100/(100+target.de/2)))*3)
            
            
            slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다!')
            
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            if self.ultimatename == '로켓 발사+':
                extradamm = int((self.hhp-self.hp)*0.3)
                slow_print(f'로켓이 폭발했습니다! 폭발이 적이 잃은 체력에 비례한 추가 고정 피해를 입힙니다!')
                
                slow_print(f'{self.name}이/가 {extradamm}만큼 피해를 입힙니다!')
                target.dealdamm(extradamm, self.name)
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.uturn += 3
        self.turn += 1
        self.passive(target)
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 3턴마다 부품을 획득하는 패시브입니다. 부품은 버프스킬을 사용해 스탯 또는 스킬 업그레이드에 사용할 수 있습니다.')
        slow_print(f'[{self.normalname}]은/는 스패너를 적에게 던지는 기본 공격입니다. 평타가 업그레이드되면, 상대의 방어력을 영구적으로 5 감소시킵니다.')
        slow_print(f'[{self.damageskillname}]은/는 용접용 레이저를 적에게 발사하는 공격 스킬입니다. 레이저 용접이 업그레이드되면, 지면을 폭발시켜 추가피해를 입힙니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 업그레이드 메뉴를 여는 (디)버프 스킬입니다. 부품을 사용하여 공격력 또는 방어력을 증가시키거나, 스킬을 업그레이드할 수 있습니다.')
        slow_print(f'[{self.ultimatename}]은/는 로켓을 적에게 발사하는 궁극기입니다. 로켓 발사가 업그레이드되면, 상대의 방어력을 무시하며, 또한 잃은 체력에 비례하는 추가피해를 입힙니다.')
        print()