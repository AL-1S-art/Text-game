import random
from Util import *
import time



class Buff:
    def __init__(self, name, bufftype, duration, stack, value, variant):
        self.name = name
        self.type = bufftype
        self.duration = duration
        self.stack = stack
        self.value = value
        self.variant = variant
        self.bufftype = bufftype
    def buffrenewal(self):
        self.duration -= 1
    def buffdo(self, target):
        slow_print(f'{target.name}이/가 {self.name} 상태입니다!')
        if self.bufftype == 'cc':
            pass
        elif self.bufftype == 'dot':
            slow_print_with_end(f'\r{target.name}이/가 {abs(int(self.value))}만큼 피해를 입습니다!')
            time.sleep(0.1)
            for x in range(self.stack):
                print(f'\r{target.name}이/가 {abs(int(self.value))} x {x+1} 만큼 피해를 입습니다!', end='', flush=True)
                target.dealdamm(self.value)
                time.sleep(0.1)
            time.sleep(0.3)
            print()
        elif self.bufftype == 'statischange':
            eval(f'target.self.variant = target.self.variant{self.value}')
        self.buffrenewal()
        
class Player:
    def __init__(self, name):
        self.name = name
        self.team = []
        self.shield = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.bufflist = []
        self.skipturn = False
    def updateteam(self, team):
        self.team = team
    
    def endingturn(self,target):
        self.turn += 1
        global teams
        for team in teams:
            print(f'{team}')
            for player in team:
                print(f'{player.name}, {player.name}의 현재 상태')
                print()
                print(f'{player.name}: {player.character[0]}')
                print(f'체력/보호막: [ {player.hp}({player.hhp}) / {player.shield} ], 마나: [ {player.mp} / {player.hmp} ] ')
                print(f'공격력 / 방어력: [ {player.ad} / {player.de} ]')
                print()
    def startingturn(self):
        self.skipturn = False
        for buff in self.bufflist:
            if buff.duration > 0:
                if buff.type == 'cc':
                    self.skipturn = True
                buff.buffdo(self)
            else:
                slow_print(f'{self.name}의 {buff.name} 상태가 해제되었습니다!')
                self.bufflist.remove(buff)           
                    
        if self.skipturn:
            slow_print(f'{self.name}이/가 군중 제어 상태로 인해 행동할 수 없습니다!')
            slow_print(f'{self.name}의 턴이 넘어갑니다...')
            print()
            return
        slow_print(f'{self.name}의 차례 입니다.')
        if self.__class__.__name__ == ['목수'] and self.resurracting:
            self.passive(self)
        
        else:
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if self.bdbturn == 0:
                if self.uturn == 0:
                    slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.buffdebuffname}], [{self.ultimatename}], [설명]')
                if self.uturn > 0:
                    slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.buffdebuffname}], [설명]')
            elif self.bdbturn > 0:
                if self.uturn == 0:
                    slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.ultimatename}], [설명]')
                if self.uturn > 0:
                    slow_print(f'[{self.normalname}], [{self.damageskillname}], [설명]')

            attact_pick = input()

            if self.normalname in attact_pick:
                self.normal(self)
            elif self.damageskillname in attact_pick:
                self.damageskill(self)
            elif self.buffdebuffname in attact_pick:
                self.buffdebuff(self)
                if not '[보디빌더]' in self.__class__.__name__ or not self.warmingup:
                    slow_print(f'다시 {self.name}의 차례 입니다.')
                    slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                    if self.uturn == 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.ultimatename}]')
                    if self.uturn > 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}]')

                    attact_pick = input()

                    if self.normalname in attact_pick:
                        self.normal(self)
                    elif self.damageskillname in attact_pick:
                        self.damageskill(self)
                    elif self.ultimatename in attact_pick:
                        self.ultimate(self)

            elif self.ultimatename in attact_pick:
                self.ultimate(self)
            elif '설명' in attact_pick:
                self.explanation()

                slow_print(f'{self.name}의 차례 입니다.')
                slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                if self.bdbturn == 0:
                    if self.uturn == 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.buffdebuffname}], [{self.ultimatename}]')
                    if self.uturn > 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.buffdebuffname}]')
                elif self.bdbturn > 0:
                    if self.uturn == 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.ultimatename}]')
                    if self.uturn > 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}]')

                attact_pick = input()

                if self.normalname in attact_pick:
                    self.normal(self)
                elif self.damageskillname in attact_pick:
                    self.damageskill(self)
                elif self.buffdebuffname in attact_pick:
                    self.buffdebuff(self)

                    slow_print(f'다시 {self.name}의 차례 입니다.')
                    slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                    if self.uturn == 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}], [{self.ultimatename}]')
                    if self.uturn > 0:
                        slow_print(f'[{self.normalname}], [{self.damageskillname}]')

                    attact_pick = input()

                    if self.normalname in attact_pick:
                        self.normal(self)
                    elif self.damageskillname in attact_pick:
                        self.damageskill(self)
                    elif self.ultimatename in attact_pick:
                        self.ultimate(self)
                
                elif self.ultimatename in attact_pick:
                    self.ultimate(self)
                    return

        if self.hp <= 0:
            slow_print(f'축하드립니다! {self.name}의 승리입니다!')
        if '흑사병 보균자' in self.__class__.__name__:
            self.passive()
        elif '흑사병 보균자' in self.__class__.__name__:
            self.passive()
        self.endingturn
                