from Util import *
from character import Buff, Player
import time
        
class Bodybuilder(Player):
    def __init__(self,name):
        
        self.shield = 0
        self.hhp = 3000
        self.hp = self.hhp
        self.ad = 100
        self.de = 130
        self.originalde = self.de
        self.originalad = self.ad
        self.hmp = 295
        self.mp = self.hmp
        self.rmp = 8
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.damageincrease = 1
        self.passivename = '체력이 곧 힘!'
        self.normalname = '평타'
        self.damageskillname = '죽음의 데드리프트'
        self.buffdebuffname = '준비운동'
        self.ultimatename = '벌크업'
        self.warmingup = True
        self.warminuplist = []
        self.ad = self.ad + self.hhp // 60
        self.utime = 0
        self.wtime = 0
        super().__init__(name)
        self.buffskilltarget = 'self'
        self.ultimatetarget = 'self'
        self.classname = '보디빌더'
        self.onstartpassive = True
        self.bufflist.append(Buff('체력이 곧 힘!', 'statuschange','Null',1,{'ad':1},self))
    def addhhpbuff(self,target,amount):
        for player in target:
            if len(list(filter(lambda buff : buff.name == '트레이닝의 결실',player.bufflist))) == 0:
                player.bufflist.append(Buff('트레이닝의 결실','statuschange','Null',0,{'hhp':1},player))
            list(filter(lambda buff : buff.name == '트레이닝의 결실',player.bufflist))[0].stack += amount
            self.hp += amount
            if player == self:
                self.updatead()
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
        self.addhhpbuff([self],damage//10)
        print(f'\r{self.name}이/가 피해를 받아 최대체력이 {0} 증가하였습니다.', end='')
        for i in range(damage//10 + 1):
            print(f'\r{self.name}이/가 피해를 받아 최대체력이 {i} 증가하였습니다.', end='')
            time.sleep(0.07)
        time.sleep(0.7)
        print()
    
    def passive(self, damm):
        if damm > 0:
            print(f'\r{self.name}이/가 운동을 하여 체력이 {0} 증가합니다!', end='')
            for i in range(damm//5):
                print(f'\r{self.name}이/가 운동을 하여 체력이 {i+1} 증가합니다!', end='')
                time.sleep(0.02)
            self.addhhpbuff([self], damm//5)
            print()
        if not self.warmingup:
            self.buffdebuffname = '웨이트 트레이닝'
            self.buffskilltarget = 'teamall'
        if self.bdbturn > 0:
            self.bdbturn -= 1
        if self.uturn > 0:
            self.uturn -= 1
        self.updatead()
    def updatead(self):
        list(filter(lambda buff : buff.name == '체력이 곧 힘!',self.bufflist))[0].buffdo(self)
    def startpassive(self):
        slow_print('트레이닝 시간입니다!')
        moreslow_print('하나! 둘! 하나! 둘!')
        increase = self.hhp // 100
        slow_print_with_end(f'\r팀원 모두가 최대체력이 {0} 증가합니다!')
        for i in range(increase+1):
            print(f'\r팀원 모두가 최대체력이 {i} 증가합니다!', end='')
            time.sleep(0.06)
        time.sleep(0.7)
        print()
        self.addhhpbuff(self.team, increase)
    def normal(self, target):
        self.warmingup = False
        damm = int((self.ad * (100/(100+target.de)))*2 * self.damageincrease)
        
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힘니다.')
        target.dealdamm(damm)
        print()
        self.passive(damm)
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
            self.warmingup = False
            slow_print(f'{self.name}이/가 200kg 바벨을 휘두릅니다!')
            damm = int((self.ad + 140 + (target.hp/100)*(1+(self.ad*0.03)) + (self.ad*0.55)) * (100/(100+target.de)))
            
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
            target.dealdamm(damm)
            print()
            self.passive(damm)
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()

    def buffdebuff(self, target):
        if self.warmingup:
            slow_print(f'{self.name}이/가 몸을 풉니다!')
            slow_print_with_end(f'\r최대체력이 {0} 증가합니다!')
            for i in range(101):
                print(f'\r최대체력이 {i} 증가합니다!', end='')
                time.sleep(0.02)
            print()
            self.addhhpbuff([self],100)
            self.wtime += 1
            if self.wtime == 5:
                slow_print(f'{self.name}이/가 몸풀기를 끝냈습니다!')
                slow_print('최대체력이 추가로 500 증가합니다!')
                self.addhhpbuff([self], 500)
                self.warmingup = False
                self.buffdebuffname = '웨이트 트레이닝'
                self.buffskilltarget = 'team'
        else:
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
                slow_print(f'{self.name}이/가 아군을 모두 웨이트 트레이닝 시킵니다!')
                increase = self.hhp // 70
                for i in self.team:
                    self.addhhpbuff(i,increase)
                    slow_print_with_end(f'{i.name}이/가 트레이닝의 결과로 영구적으로 최대체력이 {0} 증가합니다!')
                    for x in range(increase+1):
                        print(f'\r{i.name}이/가 트레이닝의 결과로 영구적으로 최대체력이 {x} 증가합니다!', end='')
                        time.sleep(0.02)
                    time.sleep(0.7)
                    print()
                self.bdbturn += 5
                
                

    
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
            self.warmingup = False
            slow_print(f'{self.name}이/가 벌크업 합니다!')
            slow_print_with_end(f'\r{self.name}의 최대체력이 3턴동안 0 증가합니다!')
            for x in range(101):
                print(f'\r{self.name}의 최대체력이 3턴동안 {x*30} 증가합니다!', end='')
                time.sleep(0.04)
            time.sleep(0.7)
            print()
            self.bufflist.append(Buff('벌크업!','statuschange',3,1,{'hhp':3000},self))
            self.hp += 3000
            self.passive(0)
            self.mp += self.rmp - 100
            self.uturn += 6
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            print()

    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 공격력이 최대체력에 비해 증가하며, 입거나 입히는 피해에 비례해 최대체력이 증가하는 패시브 입니다.')
        slow_print(f'[{self.normalname}]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 바벨을 적에게 휘둘러 피해를 주는 공격 스킬입니다.')
        if self.warmingup:
            slow_print(f'[{self.buffdebuffname}]은/는 공격을 시작하기 전에 몸을 풀어 최대체력을 증가시키는 버프 스킬입니다.')
        else:
            slow_print(f'[{self.buffdebuffname}]은/는 팀 전체를 운동시켜 영구적으로 최대체력을 증가시키는 버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]의 기본지속효과는 턴이 돌아올 때마다 팀의 최대체력을 증가시키는 효과입니다.')
        slow_print(f'[{self.ultimatename}]은/는 벌크업을 하여 3턴동안 최대체력을 3000 증가시키는 궁극기입니다.')
        print()