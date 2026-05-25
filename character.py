import random
from Util import *



class Fighter:
    def __init__(self, name):
        self.name = name
        self.hhp = 4908
        self.hp = self.hhp
        self.ad = 407
        self.de = 163
        self.hmp = 295
        self.mp = self.hmp
        self.rmp = 8
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '투기장의 투기'
        self.normalname = '평타'
        self.damageskillname = '훅'
        self.buffdebuffname = '배면기'
        self.ultimatename = '오라러쉬'

    def passive(self):
        self.ad = self.ad + (self.turn * 2)

    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()
        self.turn += 1
        self.passive()

    
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용합니다!')
            a = random.choice(['r', 'l'])
            if a == 'r':
                damm = int((self.ad + 140 + (target.hp/100)*(1+(self.ad*0.03)) + (self.ad*0.55)) * (100/(100+target.de)))
                target.hp -= damm
                slow_print(f'{self.name}이/가 [오른손]으로 강력한 훅을 날렸습니다!')
                slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            elif a == 'l':
                b = random.randint(1, 100)
                if b < 90:
                    damm = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de)))
                    target.hp -= damm
                    slow_print(f'{self.name}이/가 [왼손]으로 강력한 훅을 날렸습니다!')
                    slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
                else:
                    damm = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de))*2)
                    target.hp -= damm
                    slow_print(f'{self.name}이/가 [왼손]으로 [폐]를 강타했습니다!')
                    slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.turn += 1
            self.passive()

    def buffdebuff(self, target):
        if self.mp - 80 < 0 :
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.hp > self.hhp/2 :
            slow_print('체력이 절반 이상이여서 사용 불가합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif self.bdbturn > 0:
            slow_print('(디)버프 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.de *= 1.5
            self.ad *= 1.5
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 영구적으로 방어력과 공격력이 1.5배로 증가합니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 999999999999999999999999999999999999999999999999999999999999999
            self.passive()

    
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
            damm = int(((self.ad + self.ad + self.ad*0.55) * (100/(100+target.de)))*5)
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.ultimatename}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.passive()

    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 턴이 지날수록 공격력이 증가하는 패시브입니다.')
        slow_print(f'[{self.normalname}]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 기본 스킬로 50%의 확률로 오른손이나 왼손을 사용하는 기본 스킬입니다.')
        slow_print(f'오른손의 대미지가 더 강력하며 왼손은 가끔 폐에 주먹을 꽃아 넣습니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 체력이 절반 이하일 시영구적으로 방어력과 공격력을 1.5배로 증가시키는 일회용 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 왼손과 오른손을 번갈아 가며 5번의 주먹을 꽃아 넣는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()









class Gambler:
    def __init__(self, name):
        self.name = name
        self.hhp = random.randint(1670, 3388)
        self.hp = self.hhp
        self.ad = 0
        self.de = random.randint(93, 126)
        self.hmp = 0
        self.mp = 0
        self.rmp = 0
        self.pturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.normalname = '???'
        self.damageskillname = '???'
        self.buffdebuffname = '???'
        self.ultimatename = '???'

    def normal(self, target):
        damm = random.randint(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()

        
        moreslow_print(f'료이키텐카이... [ 좌 살 박 도 ]')
        
        chars = "0123456789"

        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.01)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.02)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.05)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.1)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.2)
        time.sleep(0.3)
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        print(f'\r {a} {b} {c}')
        if a == b and b == c and c == a:
            slow_print(f'{self.name}이/가 잭팟을 터트립니다!!!')
            slow_print(f'{self.name}이/가 4턴 동안 계속하여 체력을 최대로 회복합니다!')
            self.pturn += 4
        if self.pturn > 0:
            self.hp = self.hhp
            self.pturn -= 1
        print()
        
            
    def damageskill(self, target):
        damm = random.randint(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()

        moreslow_print(f'료이키텐카이... [ 좌 살 박 도 ]')
        
        chars = "0123456789"

        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.01)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.02)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.05)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.1)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.2)
        time.sleep(0.3)
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        print(f'\r {a} {b} {c}')
        if a == b and b == c and c == a:
            slow_print(f'{self.name}이/가 잭팟을 터트립니다!!!')
            slow_print(f'{self.name}이/가 4턴 동안 계속하여 체력을 최대로 회복합니다!')
            self.pturn += 4
        if self.pturn > 0:
            self.hp = self.hhp
            self.pturn -= 1
        print()

    
    def buffdebuff(self, target):
        damm = random.randint(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()

        moreslow_print(f'료이키텐카이... [ 좌 살 박 도 ]')
        
        chars = "0123456789"

        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.01)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.02)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.05)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.1)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.2)
        time.sleep(0.3)
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        print(f'\r {a} {b} {c}')
        if a == b and b == c and c == a:
            slow_print(f'{self.name}이/가 잭팟을 터트립니다!!!')
            slow_print(f'{self.name}이/가 4턴 동안 계속하여 체력을 최대로 회복합니다!')
            self.pturn += 4
        if self.pturn > 0:
            self.hp = self.hhp
            self.pturn -= 1
        print()
        
    
    def ultimate(self, target):
        damm = random.randint(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()

        moreslow_print(f'료이키텐카이... [ 좌 살 박 도 ]')
        
        chars = "0123456789"

        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.01)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.02)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.05)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.1)
        for _ in range(10):
            text = " ".join(random.choice(chars) for _ in range(3))
            print(f"\r {text}", end="  ", flush=True)
            time.sleep(0.2)
        time.sleep(0.3)
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        print(f'\r {a} {b} {c}')
        if a == b and b == c and c == a:
            slow_print(f'{self.name}이/가 잭팟을 터트립니다!!!')
            slow_print(f'{self.name}이/가 4턴 동안 계속하여 체력을 최대로 회복합니다!')
            self.pturn += 4
        if self.pturn > 0:
            self.hp = self.hhp
            self.pturn -= 1
        print()
        
    def explanation(self):
        slow_print('모든걸 운에 거세요!')
        print()









class Naturalist:
    def __init__(self, name):
        self.name = name
        self.hhp = 2109
        self.hp = self.hhp
        self.ad = 89
        self.de = 104
        self.hmp = 365
        self.mp = self.hmp
        self.rmp = 11
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '자연 치유'
        self.normalname = '평타'
        self.damageskillname = '침식'
        self.buffdebuffname = '덩굴조작'
        self.ultimatename = '퇴적층 생성'
        self.bdbtarget = []
        self.utarget = []        
    
    def passive(self):
        if self.turn%2 == 0:
            self.hp += self.hhp*(23/1000)

    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()
        if self.uturn > 0:
            self.utarget[0].hp -= int((((self.ad*8.98) * 0.9) + 400) * (100/(100+target.de)))
            self.uturn -= 1
            if self.uturn == 0:
                self.utarget[0].remove()
        if self.bdbturn > 0:
            self.bdbturn -= 1
            if self.bdbturn == 0:
                self.bdbtarget[0].de = self.bdbtarget[0].de / 0.3
                self.bdbtarget[0].remove()
        self.turn += 1
        self.passive()

    
    def damageskill(self, target):
        if self.mp - 60 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int((((self.ad*8.98)*0.8) + 310) * (100/(100+target.de)))
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 60
            slow_print(f'{self.name}의 마나가 60 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            if self.uturn > 0:
                self.utarget[0].hp -= int((((self.ad*8.98) * 0.9) + 400) * (100/(100+target.de)))
                self.uturn -= 1
                if self.uturn == 0:
                    self.utarget[0].remove()
            if self.bdbturn > 0:
                self.bdbturn -= 1
                if self.bdbturn == 0:
                    self.bdbtarget[0].de = self.bdbtarget[0].de / 0.3
                    self.bdbtarget[0].remove()
            self.turn += 1
            self.passive()

    
    def buffdebuff(self, target):
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
            target.de = int(target.de * 0.3)
            slow_print(f'{self.name}이/가 {target.name}에게 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}의 방어력을 30%를 감소시킵니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 1
            self.turn += 1
            self.passive()

    
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
            damm = int((((self.ad*8.98) * 0.75) + 400) * (100/(100+target.de)))
            target.hp -= damm
            slow_print(f'{self.name}이/가 {self.target}에게 궁극기 {self.ultimatename}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 피해를 2턴 동안 입힙니다.')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            if self.bdbturn > 0:
                self.bdbturn -= 1
                if self.bdbturn == 0:
                    self.bdbtarget[0].de = self.bdbtarget[0].de / 0.3
                    self.bdbtarget[0].remove()
            self.turn += 1
            self.uturn += 1
            self.passive()

    
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 자신의 2턴이 지날 때마다 체력을 회복하는 패시브입니다.')
        slow_print(f'[self.normalname]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 5만 년 치의 물의 침식 작용을 주는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 바로 다음 공격이 대상의 방어력을 30% 무시시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 침식과 퇴적을 반복하는 퇴적층에 대상을 가두어 질식시키는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()









class Blackdeath:
    def __init__(self, name):
        self.name = name
        self.hhp = 4682
        self.hp = self.hhp
        self.ad = 120
        self.de = 160
        self.hmp = 330
        self.mp = self.hmp
        self.rmp = 8
        self.bdbturn = 0
        self.uturn = 0
        self.ustrun = 3
        self.turn = 0
        self.passivename = '보균' #흑사병에 걸려서 매턴 체력 감소
        self.normalname = '평타'
        self.damageskillname = '찌르기' #자신의 체력을 소비하여 대상을 찌름
        self.buffdebuffname = '기침' #패시브 보균을 자신의 주변과 대상의 주변으로 옮김
        self.ultimatename = '항생제' #대상을 지정해 흑사병을 치료(최대 3번)
        self.bdbtarget = []
        self.utarget = []
   
    def passive(self):
        damm = int((self.ad*2.63)*0.425 + 60)
        self.hp -= damm
        if len(self.bdbtarget) != 0:
            for i in range(len(self.bdbtarget)):
                self.bdbtarget[i].hp -= damm
   
   
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
        print()
        self.turn += 1
        self.passive()

    
    def damageskill(self, target):
        if self.hp - 100 < 0:
            slow_print('사용 가능한 체력이 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int((target.hp*0.3) * (100/(100+target.de)))
            target.hp -= damm
            self.hp -= 100
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.turn += 1
            self.passive()
   
   
    def buffdebuff(self, target, *args):
        if self.mp - 50 < 0:
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
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용했습니다!')
            slow_print(f'흑사병이 퍼져서 시전자의 앞, 뒤 플레이어 및 {target.name}의 앞, 뒤 플레이어가 {self.name}의 패시브를 가집니다.')
            print()
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbtarget.append(target)
            self.bdbtarget.append(args)
            self.bdbturn += 999999999999999999999999999999999999999999999999999999999999999
            
   
    def ultimate(self, target):
        if self.mp - 150 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif len(self.utarget) == 3:
            slow_print('궁극기 사용 횟수를 다하였습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        elif target not in self.bdbtarget:
            slow_print('대상은 현재 병을 가지고 있지 않습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            self.bdbtarget.remove(target)
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.ultimatename}를 사용합니다!')
            slow_print(f'{target.name}에게 부여된 {self.passivename} 상태를 해제했습니다.')
            print()
            self.mp += self.rmp - 150
            slow_print(f'{self.name}의 마나가 150 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.turn += 1
            self.usturn -= 1
            if self.usturn == 0:
                self.uturn += 3
            self.passive()
   
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 자신의 턴마다 자기 자신에게 고정 피해를 입히는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 체력을 소모하여 자신의 신체에서 떨어져 나온 뼈로 상대를 공격하는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 [{self.passivename}] 효과를 부여하여 시전자의 턴마다 피해를 입히는 (디)버프 스킬입니다.')
        slow_print(f'스킬의 대상은 시전자의 앞, 뒤 플레이어 및 대상자의 앞, 뒤 플레이어 입니다.')
        slow_print(f'[{self.ultimatename}]은/는 자신을 포함해 최대 세번 [{self.passivename}] 효과를 치유하는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다. 궁극기 사용은 최대 3번 입니다.')
        print()










class Rider:
    def __init__(self, name):
        self.namee = name
        self.hhp = 4410
        self.hp = self.hhp
        self.ad = 421
        self.de = 124
        self.hmp = 280
        self.mp = self.hmp
        self.rmp = 7
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '바이크' #매 라운드가 지날 때 마다 속력 획득, 속력에 비례해 스킬딜량 증가
        self.normalname = '평타'
        self.damageskillname = '발가락 골절' #상대를 밟고 간다
        self.buffdebuffname = '윌리' #앞바퀴를 들어올려 방어력을 낮추고 공격력을 높임
        self.ultimatename = '준자살' #교통사고 속력 비례 대미지 입히고 3턴동안 휠체어를 타서 방어력을 높인다
   
    def passive(self, target):
        self.passiveturn += 1
        self.ad += self.passiveturn * 2
        
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
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
         selself.bdbturn -= 1
        self.turn += 1
        self.passive()
   
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int(() * (100/(100+target.de)))
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            if self.uturn > 0:
                self.uturn -= 1
   
    def buffdebuff(self, target):
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
            self.de *= 1.5
            self.ad *= 1.5
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 영구적으로 방어력과 공격력이 1.5배로 증가합니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 2
            self.turn += 1
            self.passive()
   
    def ultimate(self, target):
        if self.mp - 50 < 0:
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
            damm = int()
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
   
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 매턴 마다 자기 자신에게 피해를 입히는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 오토바이로 대상의 발가락을 밟고가 골절 시키는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 2턴 동안 방어력이 0.5배가 증가하고 공격력을 2배로 증가시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 속력에 비례해 상대방에게 들이 박고 3턴 동안 휠체어를 타 방어력을 높이는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()







class Harrypotter:
    def __init__(self, name):
        self.namee = name
        self.hhp = 4410
        self.hp = self.hhp
        self.ad = 421
        self.de = 124
        self.hmp = 280
        self.mp = self.hmp
        self.rmp = 7
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '현실자각' #체력이 낮아질 수록 공/방 증가
        self.normalname = '평타'
        self.damageskillname = '슈투포파이' #마법피해 입히기
        self.buffdebuffname = '프루타이고' #3턴 동안 마법 보호막 생성해서 데미지 감소
        self.ultimatename = '아부다카다브라' #1턴 마비
   
    def passive(self, target):
        self.passiveturn += 1
        self.ad += self.passiveturn * 2
        
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
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
         selself.bdbturn -= 1
        self.turn += 1
        self.passive()
   
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나가 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            print()
            self.normal(target)
        else:
            damm = int(() * (100/(100+target.de)))
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            if self.uturn > 0:
                self.uturn -= 1
   
    def buffdebuff(self, target):
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
            self.de *= 1.5
            self.ad *= 1.5
            slow_print(f'{self.name}이/가 {self.buffdebuffname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 영구적으로 방어력과 공격력이 1.5배로 증가합니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            self.bdbturn += 2
            self.turn += 1
            self.passive()
   
    def ultimate(self, target):
        if self.mp - 50 < 0:
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
            damm = int()
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.damageskillname}을/를 사용했습니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 50
            slow_print(f'{self.name}의 마나가 50 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
   
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 체력이 낮아질 수록 공격력과 방어력이 증가하는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 해리포터 책으로 학습한 공격 마법으로 공격하는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 해리포터 책으로 학습한 방어 마법으로 보호막을 펼쳐 3턴간 대미지를 감소시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 대상에게 죽음의 공포를 선사하여 피해를 입히고 마비를 시키는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()





class Chemist:
    def __init__(self, name):
        self.name = name
        self.hhp = 2500
        self.hp = self.hhp
        self.ad = 200
        self.de = 100
        self.hmp = 300
        self.mp = self.hmp
        self.rmp = 20
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
    def passive(self, target):
        if len(self.compoundlist) > 7:
            self.compoundlist.pop(0)
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 나트륨 플라스크를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        self.compoundlist.append('Na')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
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
        self.passive(target)
    def damageskill(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2.5)
        target.hp -= damm
        slow_print(f'{self.name}이/가 수소 플라스크를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        self.compoundlist.append('H2')
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
        self.passive(target)
    def buffdebuff(self, target):
        damm = int((self.ad * (100/(100+target.de)))*1.5)
        target.hp -= damm
        target.de -= 4
        slow_print(f'{self.name}이/가 산소 플라스크를 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다. 또한 {target.name}의 방어력이 4 감소합니다.')
        self.compoundlist.append('O2')
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
        self.bdbturn += 1
        self.turn += 1
        self.passive(target)
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
                        slow_print(f'{self.name}이/가 {i.split(" + ")[0]}과 {i.split(" + ")[1]}을/를 반응시켜 {self.productlist[i]}을/를 생성하여 {target.name}에게 {int((self.ad * (100/(100+target.de)))*3)}만큼 피해를 입혔습니다!')
                     
            target.hp -= totaldamm
            slow_print(f'{self.name}이/가 저장된 화합물을 모두 반응시켜 {target.name}에게 총 {totaldamm}만큼 피해를 입혔습니다!')
            print()
            self.compoundlist = []
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.uturn += 3
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 스킬 사용시 화합물을 저장하는 패시브입니다. 화합물은 최대 7개까지 저장 가능합니다.')
        slow_print(f'[{self.normalname}]은/는 나트륨 플라스크를 던져 적에게 피해를 입히는 기본 스킬입니다. 화합물에 나트륨을 저장합니다.')
        slow_print(f'[{self.damageskillname}]은/는 수소 플라스크를 던져 적에게 피해를 입히는 기본 스킬입니다. 화합물에 수소를 저장합니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 산소 플라스크를 던져 적에게 피해를 입히고 방어력을 감소시키며, 화합물에 산소를 저장하는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 저장된 화합물을 모두 반응시키는 궁극기 입니다. 화합물의 종류에 따라 다른 반응이 일어나며, 반응이 일어날 때마다 적에게 피해를 입힙니다.')
        print()

class ChessPlayer:
    def __init__(self, name):
        self.name = name
        self.hhp = 2000
        self.hp = self.hhp
        self.ad = 80
        self.de = 100
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
        self.castlingused = False
        self.square = 3
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
            target.hp -= damm
            slow_print(f'{self.name}이/가 퀸으로 {target.name}에게 공격을 시도합니다!')
            slow_print(f'체크!')
            self.passive(target)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp
            slow_print(f'{self.name}의 마나가 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
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
            target.hp -= damm
            slow_print(f'{self.name}이/가 퀸으로 {target.name}에게 공격을 시도합니다!')
            slow_print(f'체크!')
            self.passive(target)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 60
            slow_print(f'{self.name}의 마나가 60만큼 소모되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
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
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
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
            target.hp -= damm
            slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다! 잃은 체력에 비례해 추가 피해를 입힙니다!')
            slow_print('체크!')
            self.passive(target)
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다!')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
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


class Politician:
    def __init__(self, name):
        self.name = name
        self.hhp = 2200
        self.hp = self.hhp
        self.ad = 150
        self.de = 100
        self.hmp = 250
        self.mp = self.hmp
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
            target.hp -= damm
            slow_print(f'{self.name}이/가 대선 토론에서 정책을 제안합니다! 공격이 방어력을 무시하며, 지지율에 비례한 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            if damm % 2 == 0:
                self.popularity += 10
                slow_print(f'정책 제안이 호응을 얻어 지지율이 {10}% 증가하여 {self.popularity}%가 되었습니다.')
            else:
                self.popularity -= 10
                slow_print(f'정책 제안이 비판을 받아 지지율이 {10}% 감소하여 {self.popularity}%가 되었습니다.')
        else:
            damm = int((self.ad * (100/(100+target.de)))*2*(self.popularity/100)*2)
            target.hp -= damm
            slow_print(f'{self.name}이/가 전국을 순회하며 연설을 합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
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
        self.mytotaldamm += damm
        self.turn += 1
        self.passive(target)
    def damageskill(self, target):
        if self.ultimateturn > 0:
            damm = int(self.ad*self.popularity/50*2)
            target.hp -= damm
            slow_print(f'{self.name}이/가 대선 토론에서 상대 후보에게 반론을 제시합니다! 공격이 방어력을 무시하며, 지지율에 비례한 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            if damm % 2 == 1:
                self.popularity += 15
                slow_print(f'반론이 성공적으로 끝나 지지율이 {15}% 증가하여 {self.popularity}%가 되었습니다.')
            else:
                self.popularity -= 15
                slow_print(f'반론이 터무니없어서 지지율이 {15}% 감소하여 {self.popularity}%가 되었습니다.')
        else:
            damm = int((self.ad * (100/(100+target.de)))*2*(self.popularity/100)*2)
            target.hp -= damm
            slow_print(f'{self.name}이/가 상대 후보를 공격합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
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
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
            return
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
            self.de += 30
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
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
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

class Engineer:
    def __init__(self, name):
        self.name = name
        self.hhp = 2400
        self.hp = self.hhp
        self.ad = 120
        self.de = 100
        self.hmp = 200
        self.mp = self.hmp
        self.rmp = 20
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '장비 업그레이드' #엔지니어는 3턴마다 부품을 획득합니다. 부품은 버프스킬을 사용해 스탯 또는 스킬 업그레이드에 사용할 수 있다. 
        self.normalname = '평타' # 스패너를 적에게 던집니다.
        self.damageskillname = '레이저 용접' #엔지니어가 용접용 레이저를 적에게 발사합니다.
        self.buffdebuffname = '업그레이드!' #드론을 소환합니다.
        self.ultimatename = '로켓 발사' #.메가와트급 레이저를 적에게 발사합니다.
        self.parts = 0
        self.upgradelist = ['공격력 20 증가', '방어력 20 증가', '평타+', '레이저 용접+', '로켓 발사+', '설명']
    def passive(self, target):
        if self.turn % 3 == 0:
            self.parts += 1
            slow_print(f'{self.name}이/가 부품을 획득하여 현재 {self.parts}개입니다!')
    def normal(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 스패너를 적에게 던집니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if self.normalname != '평타':
            slow_print(f'{self.name}이/가 스패너에 맞아 방어력이 5 감소합니다!')
            target.de -= 5
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
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
        self.passive(target)
    def damageskill(self, target):
        damm = int((self.ad * (100/(100+target.de)))*2.5)
        target.hp -= damm
        slow_print(f'{self.name}이/가 용접용 레이저를 적의 위치에 발사합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if self.damageskillname != '레이저 용접':
            slow_print(f'{target.name} 주변의 지면이 온도가 급격히 높아져 폭발합니다!')
            target.hp -= damm
            slow_print(f'{target.name}이/가 폭발에 휘말려 {int(damm*1.1)}만큼 피해를 입었습니다!')
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
            
            target.hp -= damm
            slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다!')
            
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            if self.ultimatename == '로켓 발사+':
                extradamm = int((self.hhp-self.hp)*0.3)
                slow_print(f'로켓이 폭발했습니다! 폭발이 적이 잃은 체력에 비례한 추가 고정 피해를 입힙니다!')
                target.hp -= extradamm
                slow_print(f'{self.name}이/가 {extradamm}만큼 피해를 입혔습니다!')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
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
        
class Musician:
    def __init__(self, name):
        self.name = name
        self.hhp = 1800
        self.hp = self.hhp
        self.ad = 100
        self.de = 100
        self.hmp = 300
        self.mp = self.hmp
        self.rmp = 20
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
        self.passive()
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
                self.hp += 2500
                self.de += 50
                self.passivename = '악기 전문가 - 피아노'
                self.normalname = '평타 - 피아노'
                self.damageskillname = '세레나데 - 피아노'
                self.buffdebuffname = '조화로운 멜로디 - 피아노'
                self.ultimatename = '피날레 - 피아노'
                slow_print(f'{self.name}이/가 악기 전문가 패시브로 피아노를 선택하였습니다! 최대 체력이 200 증가하고, 방어력이 50 증가하며, 모든 스킬 사용 시 체력을 회복합니다!')
                print()
            elif self.instrument == '바이올린':
                self.ad += 100
                self.passivename = '악기 전문가 - 바이올린'
                self.normalname = '평타 - 바이올린'
                self.damageskillname = '세레나데 - 바이올린'
                self.buffdebuffname = '조화로운 멜로디 - 바이올린'
                self.ultimatename = '피날레 - 바이올린'
                slow_print(f'{self.name}이/가 악기 전문가 패시브로 바이올린을 선택하였습니다! 공격력이 100 증가하며, 모든 스킬이 적의 최대체력에 비례한 피해를 입힙니다!')
                print()
        if self.buffdebuffname == '조화로운 멜로디 - 바이올린':
            if self.bdbturn > 0:
                self.bdbturn -= 1
                if self.bdbturn == 0:
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
            target.hp -= damm
            slow_print(f'{self.name}이/가 다장조 C를 피아노로 연주합니다! 선율이 아름다워 체력이 {heal}만큼 회복됩니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        elif self.instrument == '바이올린':
            damm = int((self.ad * (100/(100+target.de)))*2 + target.hhp*0.05)
            target.hp -= damm
            slow_print(f'{self.name}이/가 다장조 C를 바이올린으로 연주합니다! 적의 최대체력에 비례한 추가 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
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
    def damageskill(self, target):
        if self.instrument == '피아노':
            heal = 100
            self.hp += heal
            if self.hp > self.hhp:
                self.hp = self.hhp
            damm = int((self.ad * (100/(100+target.de)))*2.5)
            target.hp -= damm
            slow_print(f'{self.name}이/가 가단조 A를 피아노로 연주합니다! 선율이 더욱 아름다워 체력이 {heal}만큼 회복됩니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        elif self.instrument == '바이올린':
            damm = int((self.ad * (100/(100+target.de)))*2.5 + target.hhp*0.1)
            target.hp -= damm
            slow_print(f'{self.name}이/가 가단조 A를 바이올린으로 연주합니다! 적의 최대체력에 비례한 추가 피해를 입힙니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
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
        if self.buffdebuffname == '조화로운 멜로디 - 피아노':
            heal = int(self.hhp*0.1)
            self.hp += heal
            if self.hp > self.hhp:
                self.hp = self.hhp
            slow_print(f'{self.name}이/가 조화로운 멜로디를 피아노로 연주합니다! 선율이 조화로워 체력이 {heal}만큼 회복됩니다!')
        elif self.buffdebuffname == '조화로운 멜로디 - 바이올린':
            self.ad += 50
            self.bdbturn += 2
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
            slow_print('피날레는 오직 한번만 연주됩니다.')
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
                damm = int(target.hhp*0.2)
                target.hp -= damm
                target.de = int(target.de*0.9)
                slow_print(f'{self.name}이/가 궁극기 {self.ultimatename}을/를 사용합니다! 피날레에 들어갑니다! 적의 최대체력의 20%에 해당하는 고정피해를 입히며, 적의 방어력을 영구적으로 10% 감소시킵니다!')
                slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다!')
                print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.uturn += 10000000000
            self.ultimateused = True
        self.turn += 1
        self.passive()
    def explanation(self):
        if self.instrument == '피아노':
            slow_print(f'[{self.passivename}]은/는 최대체력이 2500, 방어력이 50 증가하며, 스킬사용시 체력을 회복하는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 다장조 C를 피아노로 연주하여 적에게 피해를 입히는 기본 공격입니다. 기본공격시 체력을 50 회복합니다.')
            slow_print(f'[{self.damageskillname}]은/는 가단조 A를 피아노로 연주하여 적에게 피해를 입히는 공격 스킬입니다. 스킬사용시 체력을 100 회복합니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 조화로운 멜로디를 피아노로 연주하는 (디)버프 스킬입니다. 선율이 조화로워 체력이 10% 회복됩니다.')
            slow_print(f'[{self.ultimatename}]은/는 피날레를 피아노로 연주하는 궁극기입니다. 선율이 절정에 달하여 체력이 30% 회복되고, 방어력이 영구적으로 50 증가합니다. 최대 1회 사용 가능합니다.')
        elif self.instrument == '바이올린':
            slow_print(f'[{self.passivename}]은/는 공격력이 100 증가하며, 모든 스킬이 적의 최대체력에 비례한 피해를 입히는 패시브입니다.')
            slow_print(f'[{self.normalname}]은/는 다장조 C를 바이올린으로 연주하여 적에게 피해를 입히는 기본 공격입니다. 또한 적의 최대체력의 5%에 비례한 추가 피해를 입힙니다.')
            slow_print(f'[{self.damageskillname}]은/는 가단조 A를 바이올린으로 연주하여 적에게 피해를 입히는 공격 스킬입니다. 또한 적의 최대체력의 10%에 비례한 추가 피해를 입힙니다.')
            slow_print(f'[{self.buffdebuffname}]은/는 조화로운 멜로디를 바이올린으로 연주하는 버프 스킬입니다. 선율이 조화로워 공격력이 50 증가합니다. 공격력 증가는 2턴동안 유지되며, 최대 1회 사용 가능합니다.')
            slow_print(f'[{self.ultimatename}]은/는 피날레를 바이올린으로 연주하는 궁극기입니다. 적의 최대체력의 20%에 해당하는 고정피해를 입히며, 적의 방어력을 영구적으로 10% 감소시킵니다. 최대 1회 사용 가능합니다.')


        

