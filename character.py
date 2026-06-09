import random
from Util import *
import time


class Buff:
    def __init__(self, name, bufftype, duration, stack, variation,target,*args):
        self.name = name
        self.type = bufftype
        self.duration = duration
        self.stack = stack
        self.variation = variation
        self.bufftype = bufftype
        self.target = target
    def buffrenewal(self):
        if self.duration != 'Null':
            self.duration -= 1
    def applybuff(self):
        if self.bufftype == 'statuschange':
            for x in range(self.stack):
                if 'de' in self.variation.keys():
                    self.target.de += self.varaion['de']
                if 'ad' in self.variation.keys():
                    self.target.ad += self.variation['ad']
                if 'hhp' in self.variation.keys():
                        self.target.hhp += self.variation['hhp']       
    def buffdo(self, target):
        if self.bufftype == 'cc':
            pass
        if self.bufftype == 'resurraction':
            target.hp = 2
            moreslow_print(self.args[self.duration])
            self.buffrenewal()
        else:
            if self.bufftype != 'statuschange' and self.bufftype != 'stack':
                slow_print(f'{target.name}이/가 {self.name} 상태입니다!')
            elif self.bufftype == 'dot':
                slow_print_with_end(f'\r{target.name}이/가 {abs(int(self.value))}만큼 피해를 입습니다!')
                time.sleep(0.1)
                for x in range(self.stack):
                    print(f'\r{target.name}이/가 {abs(int(self.value))} x {x+1} 만큼 피해를 입습니다!', end='', flush=True)
                    target.dealdamm(self.value)
                    time.sleep(0.1)
                time.sleep(0.3)
                print()
            elif self.bufftype == 'statuschange':
                for x in range(self.stack):
                    if 'de' in self.variation.keys():
                        self.target.de += self.varaion['de']
                    if 'ad' in self.variation.keys():
                        self.target.ad += self.variation['ad']
                    if 'hhp' in self.variation.keys():
                        self.target.hhp += self.variation['hhp']
                        
                        
            elif self.bufftype == 'stack':
                pass
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
        self.normaltarget = 'enemy'
        self.damageskilltarget = 'enemy'
        self.buffskilltarget = 'self'
        self.ultimatetarget = 'enemy'
        self.onstartpassive = False
        self.originalhhp = self.hhp
        self.startturn = True
    def updateteam(self, team,teams,teamlist):
        self.team = team
        self.teams = teams
        self.teamlist = teamlist
    def endingturn(self):
        self.ad, self.de = self.originalad, self.originalde
        self.hhp = self.originalhhp
        self.statusrenewal()
        self.turn += 1
        for team in self.teams:
            print(f'{self.teamlist[self.teams.index(team)]}')
            for player in team:
                print(f'{player.name}: {player.classname}')
                print(f'체력/보호막: [ {player.hp}({player.hhp}) / {player.shield} ], 마나: [ {player.mp} / {player.hmp} ] ')
                print(f'공격력 / 방어력: [ {player.ad} / {player.de} ]')
                for x in player.bufflist:
                    if x.stack > 1:
                        print(f'[{x.name}]*{x.stack}',end=' ')
                    else:
                        print(f'[{x.name}]',end=' ')
                print()
            print()
                
    def statusrenewal(self):
        for buff in self.bufflist:
            buff.applybuff()
    def settarget(self, targetrange):
        targetname = []
        if targetrange == 'self':
            return self
        elif targetrange == 'team':
            slow_print('스킬 사용 대상을 지정해 주십시오')
            for teammate in self.team:
                slow_print_with_end(f'[{teammate.name}] ')
                targetname.append(f'{teammate.name}')
            print()
            while 1:
                target = input()
                if target in targetname:
                    return self.team[targetname.index(target)]
        elif targetrange == 'enemy':
            targets = []
            self.teamlist1 = self.teamlist.copy()
            self.teams1 = self.teams.copy()
            del self.teamlist1[self.teams1.index(self.team)]
            self.teams1.remove(self.team)
            slow_print('스킬 사용 대상을 지정해 주십시오')
            for team in self.teams1:
                slow_print_with_end(f'{self.teamlist1[self.teams1.index(team)]}: ')
                for enemy in team:
                    slow_print_with_end(f'[{enemy.name}] ')
                    targetname.append(f'{enemy.name}')
                    targets.append(enemy)
            print()
            while 1:
                target = input()
                if target in targetname:
                    return targets[targetname.index(target)]
    def startingturn(self):
        slow_print(f'{self.name}의 차례 입니다.')
        if len(list(filter(lambda x: x.name == '그리스도의 부활',self.bufflist))) > 0:
            self.startturn = False
            self.res = list(filter(lambda x: x.name == '그리스도의 부활',self.bufflist))[0]
            self.res.buffdo(self)
            if self.res.duration == 0:
                slow_print(f'{self.name}이/가 부활하였습니다!')
                self.bufflist.clear()
                self.startturn = True
                self.statusrenewal()
        if self.startturn:
            self.skipturn = False
            self.ad = self.originalad
            self.de = self.originalde
            self.hhp = self.originalhhp
            if self.onstartpassive:
                self.startpassive()
            for buff in self.bufflist:
                if buff.duration == 'Null' or buff.duration > 0:
                    if buff.type == 'cc':
                        self.skipturn = True
                    buff.buffdo(self)
                else:
                    slow_print(f'{self.name}의 {buff.name} 상태가 해제되었습니다!')
                    self.bufflist.remove(buff)           
                    if self.hp > self.hhp:
                        self.hp = self.hhp

                        
            if self.skipturn:
                slow_print(f'{self.name}이/가 군중 제어 상태로 인해 행동할 수 없습니다!')
                slow_print(f'{self.name}의 턴이 넘어갑니다...')
                print()
                return
            
            
            else:
                self.skillturn()
            if self.hp <= 0:
                slow_print(f'축하드립니다! {self.name}의 승리입니다!')
            if '흑사병 보균자' in self.classname:
                self.passive()
        self.endingturn()
    
    
    def skillturn(self):
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')
        self.skills = [self.normalname, self.damageskillname, self.buffdebuffname, self.ultimatename]
        if self.bdbturn > 0:
            self.skills.remove(self.buffdebuffname)
        if self.uturn > 0:
            self.skills.remove(self.ultimatename)
        for skill in self.skills:
            slow_print_with_end(f'[{skill}], ')
        slow_print('[설명]')

        attact_pick = input()
        if self.normalname in attact_pick:
            self.normal(self.settarget(self.normaltarget))
        elif self.damageskillname in attact_pick:
            
            self.damageskill(self.settarget(self.damageskilltarget))
        elif self.buffdebuffname in attact_pick:
            self.buffdebuff(self.settarget(self.buffskilltarget))
            if self.classname != '보디빌더' or not self.warmingup:
                slow_print_with_end(f'다시 ')
                self.skillturn()

        elif self.ultimatename in attact_pick:
            self.ultimate(self.settarget(self.ultimatetarget))
        elif '설명' in attact_pick:
            self.explanation()
            self.skillturn()

        
                
