import random
from Util import *
import time
from character import Buff, Player

class Gambler(Player):
    
    def __init__(self,name):
        self.hhp = random.randint(1670, 3388)
        self.hp = self.hhp
        self.ad = 0
        self.shield = 0
        self.de = random.randint(93, 126)
        self.originalde = self.de
        self.originalad = self.ad
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
        super().__init__(name)
        self.buffskilltarget = 'enemy'
        self.classname = '도박꾼'
    def dealdamm(self, damage):
        self.hp -= int(damage)
        if self.hp > 0:
            slow_print(f'{self.name}의 체력이 {self.hp} 남았습니다.')
        else:
            slow_print(f'{self.name}이/가 사망하였습니다!')
            return
        print()
    
    def normal(self, target):
        damm = random.randint(1, 2000)
        
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)

        
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
        
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
    

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
        
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)
    

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
        
        slow_print(f'{self.name}이/가  ??? 를  사용합니다!')
        slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입힙니다.')
        target.dealdamm(damm)

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
