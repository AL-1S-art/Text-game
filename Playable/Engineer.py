from Util import *
from character import Buff, Player


class Engineer(Player):
    def __init__(self,name):
        self.hhp = 2343
        self.hp = self.hhp
        self.ad = 101
        self.de = 90
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 385
        self.mp = self.hmp
        self.rmp = 8
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
        self.upgradelist = ['출력 강화', '장갑 강화', '내구력 강화','스패너 업그레이드', '레이저 업그레이드', '로켓 업그레이드', '설명']
        super().__init__(name)
        self.classname = '엔지니어'
        self.skill_choose_options = 'buffdebuffskill' # 선택 후 추가행동 옵션
        self.choice = ''
        self.upgradecost = {'출력 강화':1,'장갑 강화':1,'내구력 강화':1,'스패너 업그레이드':1,'레이저 업그레이드':2,'로켓 강화':3}
    def dealdamm(self, damage):
        self.hp -= int(damage)*(1-len(self.findbuff == 1)*0.5)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    
    def passive(self, target):
        if len(self.findbuff('첨단기술의 총집합체')) == 1:
            self.hp += 300
            if self.hp > self.hhp:
                self.hp = self.hhp
            slow_print(f'{self.name}이/가 첨단의료기술의 힘으로 체력을 300 회복합니다.')
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        if len(self.findbuff('부품')) == 0:
            self.addbuff('부품','stack','Null',1,'Null',self)
        else:
            self.findbuff('부품')[0].stack += 1
        slow_print(f'{self.name}이/가 부품을 획득하여 현재 {self.findbuff('부품')[0].stack}개입니다!')
    def chooseoption(self):
        slow_print(f'업그레이드 메뉴: {self.upgradelist}')
        while 1:
            choice = input('업그레이드할 항목을 입력해주세요: ')
            if choice not in self.upgradelist:
                slow_print('올바른 항목을 입력해주세요.')
            elif self.upgradecost(choice) > self.findbuff('부품')[0].stack:
                slow_print('부품이 부족합니다!')
            elif choice == '설명':
                slow_print('업그레이드 메뉴 설명:')
                slow_print(' - 출력 강화: 공격력이 70 상승합니다. 부품을 1개 소모합니다.')
                slow_print(' - 장갑 강화: 방어력이 50 상승합니다. 부품을 1개 소모합니다.') 
                slow_print(' - 내구력 강화: 최대체력이 300 상승합니다. 부품을 1개 소모합니다.')
                slow_print(' - 스패너 강화: 평타가 상대의 방어력을 영구적으로 5 감소시킵니다. 부품을 1개 소모합니다.')
                slow_print(' - 레이저 강화: 스킬의 마나소모량이 대폭 증가하는 대신, 피해량이 대폭 증가하며, 추가로 레이저 용접이 지면을 폭발시켜 추가피해를 입힙니다. 부품을 2개 소모합니다.')
                slow_print(' - 로켓 강화: 로켓 발사가 상대의 방어력을 50% 무시하며, 또한 잃은 체력에 비례하는 추가피해를 입힙니다. 부품을 3개 소모합니다.')
                if '첨단기술의 총집합체' in self.upgradelist:
                    slow_print(' - 첨단기술의 총집합체: 엔지니어가 받는 모든 피해가 50% 감소하며, 가하는 모든 피해가 300% 증가하고, 매턴 체력이 300씩 회복되며 방어력과 공격력이 100, 최대마나가 1000, 최대체력이 4000 증가합니다. 부품을 소모하지 않습니다.')
            else:
                self.findbuff('부품')[0].stack -= self.upgradecost(choice)
                
                return choice
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)*(1+(len(self.findbuff('첨단기술의 총집합체') == 1)))
        if len(self.findbuff('스패너 업그레이드')) == 0:
            slow_print(f'{self.name}이/가 스패너를 적에게 던집니다!')
        else:
            slow_print_with_end(f'{self.name}이/가 매우 크고 아름다운 스패너를 적에게 던집니다!')
            moreslow_print('깡!')
            slow_print(f'{target.name}의 방어력이 추가로 5 감소합니다!')
            if len(target.findbuff('골절')) == 0:
                target.addbuff('골절','statuschange','Null',1,{'de':5},target)
            else:
                target.findbuff('골절')[0].stack += 1
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)    
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        self.passive(target)
    def damageskill(self, target):
        
        if len(self.findbuff('레이저 업그레이드')) == 0:
            damm = int((self.ad * (100/(100+target.de)))*1.5)*(1+(len(self.findbuff('첨단기술의 총집합체') == 1)*2))
            slow_print(f'{self.name}이/가 용접용 레이저를 적의 위치에 발사합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 40
            slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        else:
            slow_print_with_end(f'{self.name}이/가 10페타와트급 레이저를 적의 위치에 발사합니다! ')
            damm = int((self.ad * (100/(100+target.de)))*3.5)*(1+(len(self.findbuff('첨단기술의 총집합체') == 1)))
            moreslow_print('지이이이이잉!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            slow_print(f'{target.name} 주변의 지면이 온도가 급격히 높아져 폭발합니다!')
            moreslow_print('쾅----!')
            slow_print(f'{target.name}이/가 폭발에 휘말려 {int(damm*1.1*(1+(len(self.findbuff('첨단기술의 총집합체') == 1)*2)))}만큼 피해를 입힙니다!')
            target.dealdamm(damm)
            print()
            self.mp += self.rmp - 150
            slow_print(f'{self.name}의 마나가 150 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        self.passive(target)
    def buffdebuff(self, target):
        if self.findbuff('부품')[0].stack <= 0:
            slow_print('부품이 부족하여 스킬을 사용할 수 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            slow_print(f'{self.name}이/가 {self.choice} 업그레이드를 선택하였습니다! 남은 부품은 {self.findbuff('부품')[0].stack}개입니다!')
            if self.choice == '출력 강화':
                if len(self.findbuff('공격력 모듈')) == 0:
                    self.addbuff('출력 강화','statuschange','Null',1,{'ad':70},self)
                else:
                    self.findbuff('출력 강화')[0].stack += 1
                self.statusrenewal()
                slow_print(f'{self.name}의 공격력이 70 증가하여 {self.ad}가 되었습니다!')
            elif self.choice == '장갑 강화':
                if len(self.findbuff('장갑 강화')) == 0:
                    self.addbuff('장갑 강화','statuschange','Null',1,{'de':50},self)
                else:
                    self.findbuff('장갑 강화')[0].stack += 1
                self.statusrenewal()
                slow_print(f'{self.name}의 방어력이 50 증가하여 {self.de}가 되었습니다!')
            elif self.choice == '스패너 업그레이드':
                self.normalname = '초대형 스패너'
                self.addbuff('스패너 업그레이드','stack','Null',1,'Null',self)
                slow_print(f'{self.name}의 스패너가 업그레이드 되었습니다! 스패너가 상대의 방어력을 영구적으로 5 감소시킵니다!')
                self.upgradelist.remove('스패너 업그레이드')
            elif self.choice == '레이저 업그레이드':
                self.damageskillname = '초강력 레이저+'
                self.addbuff('레이저 업그레이드','stack','Null',1,'Null',self)
                self.upgradelist.remove('레이저 업그레이드')
                slow_print(f'{self.name}의 레이저가 업그레이드 되었습니다! 마나 소모량이 대폭 증가하지만, 레이저의 피해량이 대폭 증가하며, 레이저 용접이 지면을 폭발시켜 추가피해를 입힙니다!')
            elif self.choice == '로켓 업그레이드':
                self.ultimatename = '스페이스Y'
                self.addbuff('로켓 업그레이드','stack','Null',1,'Null',self)
                self.upgradelist.remove('로켓 업그레이드')
                slow_print(f'{self.name}의 로켓 발사가 업그레이드 되었습니다! 로켓 발사가 상대의 방어력을 무시하며, 또한 잃은 체력에 비례하는 추가피해를 입힙니다!')
            elif self.choice == '첨단기술의 총집합체':
                self.addbuff('첨단기술의 총집합체','statuschange','Null',1,{'ad':100,'de':100,'hhp':4000,'hmp':1000},self)
                self.upgradelist.remove('첨단기술의 총집합체')
                self.normalname = '초대형 스패너+++'
                self.damageskillname = '초강력 레이저+++'
                self.ultimatename = '스페이스Y+++'
                slow_print(f'{self.name}의 걸작이 완성이 되었습니다.')
            print()
            self.mp += self.rmp - 40
            slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if len(self.findbuff('출력 강화'))*len(self.findbuff('장갑 강화'))*len(self.findbuff('스패너 강화'))*len(self.findbuff('레이저 강화'))*len(self.findbuff('로켓 강화')) != 0:
                moreslow_print('모든 업그레이드를 완료했습니다!')
                time.sleep(0.3)
                moreslow_print('마지막 업그레이드를 진행할 수 있습니다.')
                self.upgradelist.append['첨단기술의 총집합체']
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
            
            
            
            slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다!')
            if len(self.findbuff('로켓 업그레이드')) == 0:
                damm = int((self.ad * (100/(100+target.de/2)))*3)*(1+(len(self.findbuff('첨단기술의 총집합체') == 1))*2)
                slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
                target.dealdamm(damm)
            else:
                damm = int((self.ad * (100/(100+target.de/2)))*6 + (self.hhp-self.hp)*0.3)*(1+(len(self.findbuff('첨단기술의 총집합체') == 1))*2)
                slow_print_with_end(f'\r로켓 발사! 목표지점 도달까지 ')
                time.sleep(2)
                for i in range(5,0,-1):
                    print(f'\r로켓 발사! 목표지점 도달까지 {i}', end='')
                    time.sleep(1)
                time.sleep(1)
                print()
                moreslow_print('붐--------------!')
                slow_print(f'{self.name}이/가 {damm}만큼 피해를 입힙니다!')
                target.dealdamm(damm)
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.uturn += 3
        self.passive(target)
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 매턴마다 부품을 획득하는 패시브입니다. 부품은 버프스킬을 사용해 스탯 또는 스킬 업그레이드에 사용할 수 있습니다.')
        slow_print(f'[{self.normalname}]은/는 스패너를 적에게 던지는 기본 공격입니다. 평타가 업그레이드되면, 상대의 방어력을 영구적으로 5 감소시킵니다.')
        slow_print(f'[{self.damageskillname}]은/는 용접용 레이저를 적에게 발사하는 공격 스킬입니다. 레이저 용접이 업그레이드되면 마나소모량과 피해량이 대폭 증가하며 지면을 폭발시켜 추가피해를 입힙니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 업그레이드 메뉴를 여는 (디)버프 스킬입니다. 부품을 사용하여 스탯을 증가시키거나, 스킬을 업그레이드할 수 있습니다. 모든 업그레이드를 완료하면 마지막 궁극의 업그레이드를 진행할 수 있습니다.')
        slow_print(f'[{self.ultimatename}]은/는 로켓을 적에게 발사하는 궁극기입니다. 로켓 발사가 업그레이드되면, 상대의 방어력을 무시하며, 또한 잃은 체력에 비례하는 추가피해를 입힙니다.')
        print()
