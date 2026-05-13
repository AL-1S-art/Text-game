import random
from Util import *



class Fighter:
    def __init__(self, name):
        self.name = name
        self.hhp = 2608
        self.hp = self.hhp
        self.ad = 128
        self.de = 113
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
        if self.uturn > 0:
            self.uturn -= 1
        self.turn += 1
        self.passive()

    
    def damageskill(self, target):
        if self.mp - 50 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
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
            if self.uturn > 0:
                self.uturn -= 1
            self.turn += 1
            self.passive()

    def buffdebuff(self, target):
        if self.mp - 80 < 0 :
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        elif self.hp > self.hhp/2 :
            slow_print('체력이 절반 이상이여서 사용 불가합니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        elif self.bdbturn > 0:
            slow_print('(디)버프 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
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
            self.turn += 1
            self.passive()
            
    def ultimate(self, target):
        if self.mp - 100 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        if self.uturn > 0:
            slow_print('궁극기 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        else:
            damm = int(((self.ad + self.ad + self.ad*0.55) * (100/(100+target.de)))*5)
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 궁극기 {self.ultimatename}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            slow_print(f'궁극기의 쿨타임이 돌기 시작해 두턴동안 궁극기를 쓰지 못합니다.')
            self.uturn += 2
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.turn += 1
            self.passive()

    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 턴이 지날수록 공격력이 증가하는 패시브입니다.')
        slow_print(f'[{self.normalname}]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 기본 스킬로 50%의 확률로 오른손이나 왼손을 사용하는 기본 스킬입니다.')
        slow_print(f'오른손의 대미지가 더 강력하며 왼손은 가끔 폐에 주먹을 꽃아 넣습니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 체력이 절반 이하일 시영구적으로 방어력과 공격력을 1.5배로 증가시키는 일회용 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 왼손과 오른손을 번갈아 가며 5번의 주먹을 꽃아 넣는 궁극기 입니다.')
        slow_print(f'(디)버프와 궁극기는 쿨타임이 존재합니다.')
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
        self.hhp = 2100
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
            self.uturn -= 1
        self.turn += 1
        self.passive()

    
    def damageskill(self, target):
        if self.mp - 60 < 0:
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        else:
            damm = int((((self.ad*2.5)*0.5) + 310) * (100/(100+target.de)))
            target.hp -= damm
            slow_print(f'{self.name}이/가 {target.name}에게 {self.damageskillname}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼 피해를 입혔습니다.')
            print()
            self.mp += self.rmp
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
        self.passive()

    
    def buffdebuff(self, target):
        if self.mp - 80 < 0 :
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        elif self.bdbturn > 0:
            slow_print('(디)버프 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        else:
            target.de = int(target.de * 0.3)
            slow_print(f'{self.name}이/가 {taget.name}에게 {self.buffdebuffname}을/를 사용합니다!')
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
            slow_print('사용 가능한 마나 없습니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        if self.uturn > 0:
            slow_print('궁극기 쿨타임 입니다.')
            slow_print('기본 공격으로 대체됩니다.')
            self.normal(target)
        else:
            damm = int(((((self.ad*2.5) * 0.9) + 400) * (100/(100+target.de)))/2)
            target.hp -= damm
            slow_print(f'{self.name}이/가 {self.target}에게 궁극기 {self.ultimatename}을/를 사용합니다!')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 피해를 2턴 동안 입힙니다.')
            slow_print(f'{self.name}이/가 {target.name}에게 {damm}만큼의 피해를 입혔습니다.')
            print()
            self.mp += self.rmp - 100
            slow_print(f'{self.name}의 마나가 100 감소되고 {self.rmp}만큼 재생되어 {self.mp} 남았습니다.')
            slow_print(f'궁극기의 쿨타임이 돌기 시작해 두턴동안 궁극기를 쓰지 못합니다.')
            self.uturn += 2
            print()
            if target.hp > 0:
                slow_print(f'{target.name}의 체력이 {target.hp} 남았습니다.')
            else:
                slow_print(f'{target.name}이/가 사망하였습니다!')
                return
            print()
            self.turn += 1
            self.passive()
            
    def explanation(self):
        slow_print(f'[{self.passivename}]은/는 2턴이 지날 때마다 체력을 회복하는 패시브입니다.')
        slow_print(f'[self.normalname]은/는 기본 공격입니다.')
        slow_print(f'[{self.damageskillname}]은/는 5만 년 치의 물의 침식 작용을 주는 기본 스킬입니다.')
        slow_print(f'[{self.buffdebuffname}]은/는 대상의 방어력은 1턴 동안 30%를 감소시키는 (디)버프 스킬입니다.')
        slow_print(f'[{self.ultimatename}]은/는 침식과 퇴적을 반복하는 퇴적층에 대상을 가두어 질식시키는 궁극기 입니다.')
        slow_print(f'(디)버프와 궁극기는 쿨타임이 존재합니다.')
        print()



