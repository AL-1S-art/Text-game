from Util import *
from character import Buff, Player

class Chemist(Player):
    def __init__(self,name):
        
        self.hhp = 2500
        self.hp = self.hhp
        self.ad = 200
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
        self.passivename = '화학 반응' #스킬 사용시 화합물을 저장합니다. 화합물은 최대 7개까지 저장 가능합니다.
        self.normalname = '나트륨 투척' #나트륨 플라스크를 던져 적에게 피해를 입힙니다. 화합물에 나트륨을 저장합니다
        self.damageskillname = '수소 투척' #수소 플라스크를 던져 적에게 피해를 입힙니다. 화합물에 수소를 저장합니다.
        self.buffdebuffname = '산소 투척' #산소 플라스크를 던져 적에게 피해를 입히고 화합물에 산소를 저장합니다. 산소는 상대를 부식시켜 방어력을 영구적으로 4 감소시킵니다.
        self.ultimatename = '연쇄반응' #저장된 화합물을 모두 반응시킵니다. 
        self.compoundlist = []
        self.reactionlist = ['O2 + H2', 'H2O + Na']
        self.productlist = {'O2 + H2':'H2O', 'H2O + Na':'H2'}
        self.classname = '화학자'
        super().__init__(name)
        self.buffskilltarget = 'enemy'
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    def passive(self, target):
        if len(self.compoundlist) > 7:
            self.compoundlist.pop(0)
    
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        
        slow_print(f'{self.name}이/가 나트륨 플라스크를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        self.compoundlist.append('Na')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.turn += 1
        self.passive(target)
    def damageskill(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2.5)
        
        slow_print(f'{self.name}이/가 수소 플라스크를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
        self.compoundlist.append('H2')
        print()
        self.mp += self.rmp - 40
        slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        if self.bdbturn > 0:
            self.bdbturn -= 1
        self.turn += 1
        self.passive(target)
    def buffdebuff(self, target):
        damm = int((self.ad * (100/(100+target.de)))*1.5)
        
        if len(list(filter(lambda buff: buff.name == '침식', target.bufflist))) == 0:
            target.bufflist.append(Buff('부식','statuschange','Null',1,{'de':-4},target))
        else:
            list(filter(lambda buff: buff.name == '침식', target.bufflist))[0].stack += 1
        target.statusrenewal()
        slow_print(f'{self.name}이/가 산소 플라스크를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다. 또한 {target.name}의 방어력이 4 감소합니다.')
        target.dealdamm(damm)
        self.compoundlist.append('O2')
        print()
        self.mp += self.rmp - 40
        slow_print(f'{self.name}의 마나가 40 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        self.bdbturn += 1
        self.turn += 1
        self.passive(target)
    def ultimate(self, target, *args):
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
            if len(self.compoundlist) == 0:
                slow_print('저장된 화합물이 없습니다.')
                slow_print('기본 공격으로 대체됩니다.')
                print()
                self.normal(target)
                return
            totaldamm = 0
            slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다!')
            while (self.compoundlist.count('H2O') > 0 and self.compoundlist.count('Na')>0) or (self.compoundlist.count('O2') > 0 and self.compoundlist.count('H2') > 0):
                for i in self.reactionlist:
                    if i.split(' + ')[0] in self.compoundlist and i.split(' + ')[1] in self.compoundlist:
                        self.compoundlist.append(self.productlist[i])
                        self.compoundlist.remove(i.split(' + ')[0])
                        self.compoundlist.remove(i.split(' + ')[1])
                        totaldamm += int((self.ad * (100/(100+target.de)))*3)
                        slow_print(f'{self.name}이/가 {i.split(" + ")[0]}과 {i.split(" + ")[1]}을/를 반응시켜 {self.productlist[i]}을/를 생성하여 모든적에게 {int((self.ad * (100/(100+target.de)))*3)}만큼 피해를 입힙니다!')
                     
            
            slow_print(f'{self.name}이/가 저장된 화합물을 모두 반응시켜 {target.name}에게 총 {totaldamm}만큼 피해를 입힙니다!')
            target.dealdamm(totaldamm, args)
            print()
            self.compoundlist = []
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            
            self.uturn += 3
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 스킬 사용시 화합물을 저장하는 패시브입니다. 화합물은 최대 7개까지 저장 가능합니다.')
        slow_print(f'[{self.normalname}]은/는 나트륨 플라스크를 던져 적에게 피해를 입히는 기본 스킬입니다. 화합물에 나트륨을 저장합니다.')
        slow_print(f'[{self.damageskillname}]은/는 수소 플라스크를 던져 적에게 피해를 입히는 기본 스킬입니다. 화합물에 수소를 저장합니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 산소 플라스크를 던져 적에게 피해를 입히고 방어력을 감소시키며, 화합물에 산소를 저장하는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 저장된 화합물을 모두 반응시키는 궁극기 입니다. 화합물의 종류에 따라 다른 반응이 일어나며, 반응이 일어날 때마다 적에게 피해를 입힙니다.')
        print()