import random
import character
from Util import *



slow_print('게임 모드를 선택: [팀전] / [개인전]')
a = input()
if '팀' in a:
    slow_print('팀전 모드 1, 2, 3 중 하나를 골라주세요.')
    slow_print('[ 2 vs 2 ] / [ 3 vs 3 ] / [ 4 vs 4 ]')
    b = int(input())
    if b == 1:
        slow_print('[ 2 vs 2 ] 팀 게임을 시작합니다.')
        print()
        import mode2vs2
    if b == 2:
        slow_print('[ 3 vs 3 ] 팀 게임을 시작합니다.')
        print()
        import mode3vs3
    if b == 3:
        slow_print('[ 4 vs 4 ] 팀 게임을 시작합니다.')
        print()
        import mode4vs4
        
elif '개인' in a:
    slow_print('개인전 모드 1, 2, 3 중 하나를 골라주세요.')
    slow_print('[ 1 vs 1 ] / [ 1 vs 1 vs 1 ] / [ 1 vs 1 vs 1 vs 1 ]')
    b = int(input())
    if b == 1:
        slow_print('[ 1 vs 1 ] 팀 게임을 시작합니다.')
        print()
        import mode1vs1
    if b == 2:
        slow_print('[ 1 vs 1 vs 1 ] 팀 게임을 시작합니다.')
        print()
        import mode1vs1vs1
    if b == 3:
        slow_print('[ 1 vs 1 vs 1 vs 1 ] 팀 게임을 시작합니다.')
        print()
        import mode1vs1vs1vs1