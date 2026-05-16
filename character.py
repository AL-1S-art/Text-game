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
            self.turn += 4
        if self.turn > 0:
            self.hp = self.hhp
            self.turn -= 1
            
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
            self.turn += 4
        if self.turn > 0:
            self.hp = self.hhp
            self.turn -= 1
            
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
            self.turn += 4
        if self.turn > 0:
            self.hp = self.hhp
            self.turn -= 1

    
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
            self.turn += 4
        if self.turn > 0:
            self.hp = self.hhp
            self.turn -= 1
            
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
            damm = int((((self.ad*8.98)*0.5) + 310) * (100/(100+target.de)))
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
            damm = int((((self.ad*8.98) * 0.9) + 400) * (100/(100+target.de)))
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
        self.uutrun = 3
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
            self.uuturn -= 1
            if self.uuturn == 0:
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
        self.hhp =
        self.hp = self.hhp
        self.ad =
        self.de =
        self.hmp =
        self.mp = self.hmp
        self.rmp =
        self.passiveturn = 0
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.passivename = '바이크' #매 라운드가
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
            damm = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de))*2)
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
                break
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
                break
            print()
   
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 매턴 마다 자기 자신에게 피해를 입히는 패시브입니다.')
        slow_print(f'[{self.damageskillname}]은/는 오토바이로 대상의 발가락을 밟고가 골절 시키는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 2턴 동안 방어력이 0.5배가 증가하고 공격력을 2배로 증가시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 속력에 비례해 상대방에게 들이 박고 3턴 동안 휠체어를 타 방어력을 높이는 궁극기 입니다.')
        slow_print(f'여러 턴에 걸쳐 피해 및 (디)버프를 거는 스킬은 해당 스킬의 효과가 끝날 때 까지 재사용이 불가능 합니다.')
        print()



