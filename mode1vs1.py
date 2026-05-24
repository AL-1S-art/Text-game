import random
import character
from Util import *

slow_print('플레이어 1의 이름을 입력해 주세요.')
player1_name = input()
print()

slow_print('플레이어 2의 이름을 입력해 주세요.')
player2_name = input()
print()






slow_print(f'각 플레이어들의 이름을 확인하세요')
slow_print(f'{player1_name}, {player2_name}')
print()
print()




player1_character = []
player2_character = []

player1 = character.Fighter(f'{player1_name}')
player2 = character.Fighter(f'{player2_name}')

def player1_pick():
    global player1
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]']
    slow_print(f'{player1_name}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{player1_name}이/가 [{pick}]를 선택했습니다.')
    player1_character.append(f'[{pick}]')
    character_list.remove(f'[{pick}]')
    if pick == '도박꾼':
        player1 = character.Gambler(f'{player1_name}')
    elif pick == '격투가':
        player1 = character.Fighter(f'{player1_name}')
    elif pick == '자연술사':
        player1 = character.Naturalist(f'{player1_name}')
    elif pick == '흑사병 보균자':
        player1 = character.Blackdeath(f'{player1_name}')
    print()





def player2_pick():
    global player2
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]']
    slow_print(f'{player2_name}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{player2_name}이/가 [{pick}]를 선택했습니다.')
    player2_character.append(f'[{pick}]')
    character_list.remove(f'[{pick}]')
    if pick == '도박꾼':
        player2 = character.Gambler(f'{player2_name}')
    elif pick == '격투가':
        player2 = character.Fighter(f'{player2_name}')
    elif pick == '자연술사':
        player2 = character.Naturalist(f'{player2_name}')
    elif pick == '흑사병 보균자':
        player2 = character.Blackdeath(f'{player2_name}')
    print()






slow_print(f'{player1_name}의 캐릭터 선택 차례입니다.')
print()
player1_pick()
print()
slow_print(f'{player2_name}의 캐릭터 선택 차례입니다.')
print()
player2_pick()
print()




slow_print(f'각 플레이어와 캐릭터를 확인하세요!')
print()
print(f'{player1_name}: {player1_character[0]}')
print(f'체력: [ {player1.hp} / {player1.hhp} ], 마나: [ {player1.mp} / {player1.hmp} ] ')
print(f'공격력 / 방어력: [ {player1.ad} / {player1.de} ]')
print()
print(f'{player2_name}: {player2_character[0]}')
print(f'체력: [ {player2.hp} / {player2.hhp} ], 마나: [ {player2.mp} / {player2.hmp} ] ')
print(f'공격력 / 방어력: [ {player2.ad} / {player2.de} ]')
print()

time.sleep(5)







slow_print(f'게임을 시작합니다!')
print()
sequence = random.shuffle([player1_name, player2_name])

if sequence == 'player1':
    slow_print(f'순서는 {sequence} 입니다.')
    print()
    while True:
        slow_print(f'{player1_name}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player1.bdbturn == 0:
            if player1.uturn == 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}], [{player1.ultimatename}], [설명]')
            if player1.uturn > 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}], [설명]')
        elif player1.bdbturn > 0:
            if player1.uturn == 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}], [설명]')
            if player1.uturn > 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [설명]')

        attact_pick = input()

        if player1.normalname in attact_pick:
            player1.normal(player2)
        elif player1.damageskillname in attact_pick:
            player1.damageskill(player2)
        elif player1.buffdebuffname in attact_pick:
            player1.buffdebuff(player2)

            slow_print(f'다시 {player1_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player1.uturn == 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}]')
            if player1.uturn > 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}]')

            attact_pick = input()

            if player1.normalname in attact_pick:
                player1.normal(player2)
            elif player1.damageskillname in attact_pick:
                player1.damageskill(player2)
            elif player1.ultimatename in attact_pick:
                    player1.ultimate(player2)

        elif player1.ultimatename in attact_pick:
            player1.ultimate(player2)
        elif '설명' in attact_pick:
            player1.explanation()

            slow_print(f'{player1_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player1.bdbturn == 0:
                if player1.uturn == 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}], [{player1.ultimatename}]')
                if player1.uturn > 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}]')
            elif player1.bdbturn > 0:
                if player1.uturn == 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}]')
                if player1.uturn > 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}]')

            attact_pick = input()

            if player1.normalname in attact_pick:
                player1.normal(player2)
            elif player1.damageskillname in attact_pick:
                player1.damageskill(player2)
            elif player1.buffdebuffname in attact_pick:
                player1.buffdebuff(player2)

                slow_print(f'다시 {player1_name}의 공격차례 입니다.')
                slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                if player1.uturn == 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}]')
                if player1.uturn > 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}]')

                attact_pick = input()

                if player1.normalname in attact_pick:
                    player1.normal(player2)
                elif player1.damageskillname in attact_pick:
                    player1.damageskill(player2)
                elif player1.ultimatename in attact_pick:
                        player1.ultimate(player2)
            
            elif player1.ultimatename in attact_pick:
                player1.ultimate(player2)


        if '흑사병 보균자' in player1_character:
            player1.passive()
        elif '흑사병 보균자' in player2_character:
            player2.passive()
        
        if player2.hp <= 0:
            slow_print(f'축하드립니다! {player1_name}의 승리입니다!')
            break

        print(f'{player1_name}, {player2_name}의 현재 상태')
        print()
        print(f'{player1_name}: {player1_character[0]}')
        print(f'체력: [ {player1.hp} / {player1.hhp} ], 마나: [ {player1.mp} / {player1.hmp} ] ')
        print(f'공격력 / 방어력: [ {player1.ad} / {player1.de} ]')
        print()
        print(f'{player2_name}: {player2_character[0]}')
        print(f'체력: [ {player2.hp} / {player2.hhp} ], 마나: [ {player2.mp} / {player2.hmp} ] ')
        print(f'공격력 / 방어력: [ {player2.ad} / {player2.de} ]')
        print()






        slow_print(f'{player2_name}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player2.bdbturn == 0:
            if player2.uturn == 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}], [{player2.ultimatename}], [설명]')
            if player2.uturn > 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}], [설명]')
        elif player2.bdbturn > 0:
            if player2.uturn == 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}], [설명]')
            if player2.uturn > 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [설명]')

        attact_pick = input()

        if player2.normalname in attact_pick:
            player2.normal(player1)
        elif player2.damageskillname in attact_pick:
            player2.damageskill(player1)
        elif player2.buffdebuffname in attact_pick:
            player2.buffdebuff(player1)
            
            slow_print(f'다시 {player2_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player2.uturn == 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}]')
            if player2.uturn > 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}]')

            attact_pick = input()

            if player2.normalname in attact_pick:
                player2.normal(player1)
            elif player2.damageskillname in attact_pick:
                player2.damageskill(player1)
            elif player2.buffdebuffname in attact_pick:
                player2.buffdebuff(player1)
            elif player2.ultimatename in attact_pick:
                player2.ultimate(player1)

        elif player2.ultimatename in attact_pick:
            player2.ultimate(player1)
        elif '설명' in attact_pick:
            player2.explanation()

            slow_print(f'{player2_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player2.bdbturn == 0:
                if player2.uturn == 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}], [{player2.ultimatename}]')
                if player2.uturn > 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}]')
            elif player2.bdbturn > 0:
                if player2.uturn == 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}]')
                if player2.uturn > 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}]')

            attact_pick = input()

            if player2.normalname in attact_pick:
                player2.normal(player1)
            elif player2.damageskillname in attact_pick:
                player2.damageskill(player1)
            elif player2.buffdebuffname in attact_pick:
                player2.buffdebuff(player1)

                slow_print(f'다시 {player2_name}의 공격차례 입니다.')
                slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                if player2.uturn == 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}]')
                if player2.uturn > 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}]')

                attact_pick = input()

                if player2.normalname in attact_pick:
                    player2.normal(player1)
                elif player2.damageskillname in attact_pick:
                    player2.damageskill(player1)
                elif player2.ultimatename in attact_pick:
                    player2.ultimate(player1)

            elif player2.ultimatename in attact_pick:
                player2.ultimate(player1)

        if '흑사병 보균자' in player1_character:
            player1.passive()
        elif '흑사병 보균자' in player2_character:
            player2.passive()
        
        if player1.hp <= 0:
            slow_print(f'축하드립니다! {player2_name}의 승리입니다!')
            break

        print(f'{player1_name}, {player2_name}의 현재 상태')
        print()
        print(f'{player1_name}: {player1_character[0]}')
        print(f'체력: [ {player1.hp} / {player1.hhp} ], 마나: [ {player1.mp} / {player1.hmp} ] ')
        print(f'공격력 / 방어력: [ {player1.ad} / {player1.de} ]')
        print()
        print(f'{player2_name}: {player2_character[0]}')
        print(f'체력: [ {player2.hp} / {player2.hhp} ], 마나: [ {player2.mp} / {player2.hmp} ] ')
        print(f'공격력 / 방어력: [ {player2.ad} / {player2.de} ]')
        print()





elif sequence == 'player2':
    slow_print(f'순서는 {sequence} 입니다.')
    print()
    while True:
        slow_print(f'{player2_name}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player2.bdbturn == 0:
            if player2.uturn == 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}], [{player2.ultimatename}], [설명]')
            if player2.uturn > 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}], [설명]')
        elif player2.bdbturn > 0:
            if player2.uturn == 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}], [설명]')
            if player2.uturn > 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [설명]')

        attact_pick = input()

        if player2.normalname in attact_pick:
            player2.normal(player1)
        elif player2.damageskillname in attact_pick:
            player2.damageskill(player1)
        elif player2.buffdebuffname in attact_pick:
            player2.buffdebuff(player1)

            slow_print(f'다시 {player2_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player2.uturn == 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}]')
            if player2.uturn > 0:
                slow_print(f'[{player2.normalname}], [{player2.damageskillname}]')

            attact_pick = input()

            if player2.normalname in attact_pick:
                player2.normal(player1)
            elif player2.damageskillname in attact_pick:
                player2.damageskill(player1)
            elif player2.ultimatename in attact_pick:
                player2.ultimate(player1)

        elif player2.ultimatename in attact_pick:
            player2.ultimate(player2)
        elif '설명' in attact_pick:
            player2.explanation()

            slow_print(f'{player2_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')
            
            if player2.bdbturn == 0:
                if player2.uturn == 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}], [{player2.ultimatename}]')
                if player2.uturn > 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.buffdebuffname}]')
            elif player2.bdbturn > 0:
                if player2.uturn == 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}]')
                if player2.uturn > 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}]')

            attact_pick = input()

            if player2.normalname in attact_pick:
                player2.normal(player1)
            elif player2.damageskillname in attact_pick:
                player2.damageskill(player1)
            elif player2.buffdebuffname in attact_pick:
                player2.buffdebuff(player1)

                slow_print(f'다시 {player2_name}의 공격차례 입니다.')
                slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                if player2.uturn == 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}], [{player2.ultimatename}]')
                if player2.uturn > 0:
                    slow_print(f'[{player2.normalname}], [{player2.damageskillname}]')

                attact_pick = input()

                if player2.normalname in attact_pick:
                    player2.normal(player1)
                elif player2.damageskillname in attact_pick:
                    player2.damageskill(player1)
                elif player2.ultimatename in attact_pick:
                    player2.ultimate(player1)

        
            elif player2.ultimatename in attact_pick:
                player2.ultimate(player1)

        if '흑사병 보균자' in player1_character:
            player1.passive()
        elif '흑사병 보균자' in player2_character:
            player2.passive()

        if player2.hp <= 0:
            slow_print(f'축하드립니다! {player1_name}의 승리입니다!')
            break

        print(f'{player1_name}, {player2_name}의 현재 상태')
        print()
        print(f'{player1_name}: {player1_character[0]}')
        print(f'체력: [ {player1.hp} / {player1.hhp} ], 마나: [ {player1.mp} / {player1.hmp} ] ')
        print(f'공격력 / 방어력: [ {player1.ad} / {player1.de} ]')
        print()
        print(f'{player2_name}: {player2_character[0]}')
        print(f'체력: [ {player2.hp} / {player2.hhp} ], 마나: [ {player2.mp} / {player2.hmp} ] ')
        print(f'공격력 / 방어력: [ {player2.ad} / {player2.de} ]')
        print()






        slow_print(f'{player1_name}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player1.bdbturn == 0:
            if player1.uturn == 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}], [{player1.ultimatename}], [설명]')
            if player1.uturn > 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}], [설명]')
        elif player1.bdbturn > 0:
            if player1.uturn == 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}], [설명]')
            if player1.uturn > 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [설명]')

        attact_pick = input()

        if player1.normalname in attact_pick:
            player1.normal(player2)
        elif player1.damageskillname in attact_pick:
            player1.damageskill(player2)
        elif player1.buffdebuffname in attact_pick:
            player1.buffdebuff(player2)
            
            slow_print(f'다시 {player1_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player1.uturn == 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}]')
            if player1.uturn > 0:
                slow_print(f'[{player1.normalname}], [{player1.damageskillname}]')

            attact_pick = input()

            if player1.normalname in attact_pick:
                player1.normal(player2)
            elif player1.damageskillname in attact_pick:
                player1.damageskill(player2)
            elif player1.ultimatename in attact_pick:
                player1.ultimae(player2)

        elif player1.ultimatename in attact_pick:
            player1.ultimate(player2)
        elif '설명' in attact_pick:
            player1.explanation()

            slow_print(f'{player1_name}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player1.bdbturn == 0:
                if player1.uturn == 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}], [{player1.ultimatename}]')
                if player1.uturn > 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.buffdebuffname}]')
            elif player1.bdbturn > 0:
                if player1.uturn == 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}]')
                if player1.uturn > 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}]')

            attact_pick = input()

            if player1.normalname in attact_pick:
                player1.normal(player2)
            elif player1.damageskillname in attact_pick:
                player1.damageskill(player2)
            elif player1.buffdebuffname in attact_pick:
                player1.buffdebuff(player2)

                slow_print(f'다시 {player1_name}의 공격차례 입니다.')
                slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

                if player1.uturn == 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}], [{player1.ultimatename}]')
                if player1.uturn > 0:
                    slow_print(f'[{player1.normalname}], [{player1.damageskillname}]')

                attact_pick = input()

                if player1.normalname in attact_pick:
                    player1.normal(player2)
                elif player1.damageskillname in attact_pick:
                    player1.damageskill(player2)
                elif player1.ultimatename in attact_pick:
                        player1.ultimate(player2)

            
            elif player1.ultimatename in attact_pick:
                player1.ultimate(player2)

        if '흑사병 보균자' in player1_character:
            player1.passive()
        elif '흑사병 보균자' in player2_character:
            player2.passive()
        
        if player1.hp <= 0:
            slow_print(f'축하드립니다! {player2_name}의 승리입니다!')
            break

        print(f'{player1_name}, {player2_name}의 현재 상태')
        print()
        print(f'체력: [ {player1.hp} / {player1.hhp} ], 마나: [ {player1.mp} / {player1.hmp} ] ')
        print(f'공격력 / 방어력: [ {player1.ad} / {player1.de} ]')
        print()
        print(f'{player2_name}: {player2_character[0]}')
        print(f'체력: [ {player2.hp} / {player2.hhp} ], 마나: [ {player2.mp} / {player2.hmp} ] ')
        print(f'공격력 / 방어력: [ {player2.ad} / {player2.de} ]')
        print()
