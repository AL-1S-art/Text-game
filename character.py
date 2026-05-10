import random
from Util import *

class Fighter:    #int(((self.ad + self.ad + self.ad*0.55) / (100/(100+target.de)))*5)
    def __init__(self, name):
        self.name = name
        self.hhp = 2608
        self.hp = self.hhp
        self.ad = 128
        self.de = 113
        self.hmp = 295
        self.mp = self.hmp
        self.rmp = 10
        self.bdbturn = 0
        self.uturn = 0
        self.turn = 0
        self.normalname = '평타'
        self.damageskillname = '훅'
        self.buffdebuffname = '배면기'
        self.ultimatename = '오라러쉬'

    def passive(self):
        self.ad += self.turn * 2
        
    def normal(self, target):
        global passive
        slow_print(f'{self.name}이/가 공격을 시도합니다!')
        damm = int((self.ad * (100/(100+target.de)))*2)
        target.hp -= damm
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        print()
        self.mp += self.rmp
        slow_print(f'{self.name}의 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
        print()
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
        print()
        if self.uturn > 0:
            self.uturn -= 1
        self.turn += 1
        passive()

    
    def damageskill(self, target):
        global passive
        global normal
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            normal(self, target)
        else:
            a = random.choice(['r', 'l'])
            if a == 'r':
                damm = int((self.ad + 140 + (target.hp/100)*(1+(self.ad*0.03)) + (self.ad*0.55)) * (100/(100+target.de)))
                target.hp -= damm
                slow_print(f'{self.name}이/가 [오른손]으로 강력한 훅을 날렸습니다!')
                slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            elif a == 'l':
                b = random.randint(1, 100)
                if b < 90:
                    damm = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de))
                    target.hp -= damm
                    slow_print(f'{self.name}이/가 [왼손]으로 강력한 훅을 날렸습니다!')
                    slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
                else:
                    a = int((self.ad + 50 + (target.hp/100)*(1+(self.ad*0.03))) * (100/(100+target.de))*2)
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
            print()
            if self.uturn > 0:
                self.uturn -= 1
            self.turn += 1
            passive()

    def buffdebuff(self, target):
        global passive
        global normal
        if self.mp - 40 < 0 :
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            normal(self, target)
        elif self.hp > self.hhp/2 :
            slow_print('체력이 절반 이상이여서 사용 불가합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            normal(self, target)
        elif self.bdbturn > 0:
            slow_print('(디)버프 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            normal(self, target)
        else:
            self.de *= 1.5
            self.ad *= 2
            slow_print(f'{self.name}이/가 영구적으로 방어력과 공격력이 1.5배로 증가합니다.')
            print()
            self.mp += self.rmp - 80
            slow_print(f'{self.name}의 마나가 80 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            print()
            slow_print(f'한번 더 공격할 수 있습니다.')
            print()
            self.bdbturn += 999999999999999999999999999999999999999999999999999999999999999
            self.turn += 1
            passive()
            
    def ultimate(self, target):
        global passive
        global normal
        if self.mp - 100 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            normal(self, target)
        if self.uturn > 0:
            slow_print('궁극기 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            normal(self, target)
        else:
            damm = int(((self.ad + self.ad + self.ad*0.55) * (100/(100+target.de)))*5)
            slow_print(f'{self.name}이/가 양손 모두 사용해 상대를 공격합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            slow_print(f'궁극기의 쿨타임이 돌기 시작해 두턴동안 궁극기를 쓰지 못합니다.')
            self.turn += 2
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
            print()
            self.turn += 1
            passive()

    def explanation(self):
        slow_print('[패시브]는 턴이 지날수록 공격력이 증가합니다.')
        slow_print('[평타]는 기본 공격입니다.')
        slow_print('[훅]은 기본 스킬로 50%의 확률로 오른손이나 왼손을 사용하는 기본 스킬입니다.')
        slow_print('오른손의 대미지가 더 강력하며 왼손은 가끔 폐에 주먹을 꽃아 넣습니다.')
        slow_print('[배면기]는 방어력과 공격력을 1.5배로 증가시키는 (디)버프 스킬입니다.')
        slow_print('[오라러쉬]는 왼손과 오른손을 번갈아 가며 5번의 주먹을 꽃아 넣는 궁극기 입니다.')
        slow_print('(디)버프와 궁극기는 쿨타임이 존재합니다.')
        print()




class Gambler:
    def __init__(self, name):
        self.name = name
        self.hhp = random.randint(1670, 3388)
        self.hp = self.hhp
        self.de = random.randint(93, 126)
        self.turn = 0
        self.normalname = '???'
        self.damageskillname = '???'
        self.buffdebuffname = '???'
        self.ultimatename = '???'

    def normal(self, target):
        damm = random.choice(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가 ??? 을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
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
        damm = random.choice(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가 ??? 을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
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
        damm = random.choice(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가 ??? 을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
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
        damm = random.choice(1, 2000)
        target.hp -= damm
        slow_print(f'{self.name}이/가 ??? 을 시도합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
        if target.hp > 0:
            slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
        else:
            slow_print(f'{target.name}이/가 사망하였습니다!')
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









