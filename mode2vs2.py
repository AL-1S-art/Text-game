import random
import character
from Util import *





slow_print('1팀의 플레이어들의 이름을 입력해 주세요.')
team1_name = []
for i in range(2):
    a = input()
    team1_name.append(a)
print()

slow_print('2팀의 플레이어들의 이름을 입력해 주세요.')
team2_name = []
for i in range(2):
    a = input()
    team2_name.append(a)
print()
print()





team1_character = []
team2_character = []

player1 = character.Fighter(0)
player2 = character.Fighter(0)
player3 = character.Fighter(0)
player4 = character.Fighter(0)

def team1_pick():
    global player1
    global player2
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]']
    slow_print(f'{team1_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team1_name[0]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick == '격투가':
        player1 = character.Fighter(f'{team2_name[0]}')
    elif pick == '도박꾼':
        player1 = character.Gambler(f'{team2_name[0]}')
    elif pick == '자연술사':
        player1 = character.Naturalist(f'{team2_name[0]}')
    elif pick == '흑사병 보균자':
        player1 = character.Blackdeath(f'{team2_name[0]}')
    print()


    slow_print(f'{team1_name[1]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team1_name[1]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick == '격투가':
        player2 = character.Fighter(f'{team2_name[0]}')
    elif pick == '도박꾼':
        player2 = character.Gambler(f'{team2_name[0]}')
    elif pick == '자연술사':
        player2 = character.Naturalist(f'{team2_name[0]}')
    elif pick == '흑사병 보균자':
        player2 = character.Blackdeath(f'{team2_name[0]}')
    print()



def team2_pick():
    global player3
    global player4
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]']
    slow_print(f'{team2_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team2_name[0]}이/가 [{pick1}]를 선택했습니다.')
    team2_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick == '격투가':
        player3 = character.Fighter(f'{team2_name[0]}')
    elif pick == '도박꾼':
        player3 = character.Gambler(f'{team2_name[0]}')
    elif pick == '자연술사':
        player3 = character.Naturalist(f'{team2_name[0]}')
    elif pick == '흑사병 보균자':
        player3 = character.Blackdeath(f'{team2_name[0]}')
    print()


    slow_print(f'{team2_name[1]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team2_name[1]}이/가 [{pick1}]를 선택했습니다.')
    team2_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick == '격투가':
        player4 = character.Fighter(f'{team2_name[0]}')
    elif pick == '도박꾼':
        player4 = character.Gambler(f'{team2_name[0]}')
    elif pick == '자연술사':
        player4 = character.Naturalist(f'{team2_name[0]}')
    elif pick == '흑사병 보균자':
        player4 = character.Blackdeath(f'{team2_name[0]}')
    print()



slow_print(f'1팀의 캐릭터 선택 차례입니다.')
print()
team1_pick()
slow_print(f'2팀의 캐릭터 선택 차례입니다.')
print()
team2_pick()

players = [player1, player2, player3, player4]

slow_print(f'각 팀의 플레이어들과 캐릭터를 확인하세요!')
print()
print('1팀의 플레이어들')
for i in range(2):
    print(f'{team1_name[i]}: {player1_character[i]}')
    print(f'체력: [ {players[i+1].hp} / {players[i+1].hhp} ], 마나: [ {players[i+1].mp} / {players[i+1].hmp} ] ')
    print(f'공격력 / 방어력: [ {players[i+1].ad} / {players[i+1].de} ]')


print()
print('2팀의 플레이어들')
for i in range(2):
    print(f'{team2_name[i]}: {player2_character[i]}')
    print(f'체력: [ {players[i+3].hp} / {players[i+3].hhp} ], 마나: [ {players[i+3].mp} / {players[i+3].hmp} ] ')
    print(f'공격력 / 방어력: [ {players[i+3].ad} / {players[i+3].de} ]')




slow_print(f'게임을 시작합니다!')
print()
sequence = random.shuffle([team1_name[0], team1_name[1], team2_name[0], team2_name[1]])

if sequence == [team1_name[0], team1_name[1], team2_name[0], team2_name[1]]:
    slow_print(f'순서는 {sequence} 입니다.')
    print()
    while True:
        if player1.hp >= 0:
            slow_print(f'{team1_name[0]}의 공격차례 입니다.')
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
                
            slow_print(f'공격할 적을 골라주세요.')
            
            attact_target = input()
            
            if player1.normalname in attact_pick:
                if team2_name[0] in attact_target:
                    player1.normal(player3)
                if team2_name[1] in attact_target:
                    player1.normal(player4)
            elif player1.damageskillname in attact_pick:
                if team2_name[0] in attact_target:
                    player1.damageskill(player3)
                if team2_name[1] in attact_target:
                    player1.damageskill(player4)
            elif player1.buffdebuffname in attact_pick:
                if '흑사병 보균자' in team1_character[0]:
                    if team2_name[0] in attact_target:
                        player1.buffdebuff(player2, player3, player4)
                    if team2_name[1] in attact_target:
                        player1.buffdebuff(player2, player3, player4)
                elif:
                    if team2_name[0] in attact_target:
                        player1.buffdebuff(player3)
                    if team2_name[1] in attact_target:
                        player1.buffdebuff(player4)
                        
                slow_print(f'다시 {player1_name}의 공격차례 입니다.')
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
    
                slow_print(f'공격할 적을 골라주세요.')
            
                attact_target = input()
            
                if player1.normalname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.normal(player3)
                    if team2_name[1] in attact_target:
                        player1.normal(player4)
                elif player1.damageskillname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.damageskill(player3)
                    if team2_name[1] in attact_target:
                        player1.damageskill(player4)
                elif player1.ultimatename in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.ultimate(player3)
                    if team2_name[1] in attact_target:
                        player1.ultimate(player4)
    
            elif player1.ultimatename in attact_pick:
                if team2_name[0] in attact_target:
                    player1.ultimate(player3)
                if team2_name[1] in attact_target:
                    player1.ultimate(player4)
            elif '설명' in attact_pick:
                player1.explanation()
                
                slow_print(f'{team1_name[0]}의 공격차례 입니다.')
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
                    
                slow_print(f'공격할 적을 골라주세요.')
                
                attact_target = input()
                
                if player1.normalname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.normal(player3)
                    if team2_name[1] in attact_target:
                        player1.normal(player4)
                elif player1.damageskillname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.damageskill(player3)
                    if team2_name[1] in attact_target:
                        player1.damageskill(player4)
                elif player1.buffdebuffname in attact_pick:
                    if '흑사병 보균자' in team1_character[0]:
                        if team2_name[0] in attact_target:
                            player1.buffdebuff(player2, player3, player4)
                        if team2_name[1] in attact_target:
                            player1.buffdebuff(player2, player3, player4)
                    elif:
                        if team2_name[0] in attact_target:
                            player1.buffdebuff(player3)
                        if team2_name[1] in attact_target:
                            player1.buffdebuff(player4)
                            
                    slow_print(f'다시 {player1_name}의 공격차례 입니다.')
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
        
                    slow_print(f'공격할 적을 골라주세요.')
                
                    attact_target = input()
                
                    if player1.normalname in attact_pick:
                        if team2_name[0] in attact_target:
                            player1.normal(player3)
                        if team2_name[1] in attact_target:
                            player1.normal(player4)
                    elif player1.damageskillname in attact_pick:
                        if team2_name[0] in attact_target:
                            player1.damageskill(player3)
                        if team2_name[1] in attact_target:
                            player1.damageskill(player4)
                    elif player1.ultimatename in attact_pick:
                        if team2_name[0] in attact_target:
                            player1.ultimate(player3)
                        if team2_name[1] in attact_target:
                            player1.ultimate(player4)
        
                elif player1.ultimatename in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.ultimate(player3)
                    if team2_name[1] in attact_target:
                        player1.ultimate(player4)
    
            if '흑사병 보균자' in player1_character:
                player1.passive()
            elif '흑사병 보균자' in player2_character:
                player2.passive()
            
            if player3.hp <= 0 and player4.hp <= 0:
                slow_print(f'축하드립니다! 1팀의 승리입니다!')
                break









        if player1.hp >= 0:
            slow_print(f'{team1_name[0]}의 공격차례 입니다.')
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
                
            slow_print(f'공격할 적을 골라주세요.')
            
            attact_target = input()
            
            if player1.normalname in attact_pick:
                if team2_name[0] in attact_target:
                    player1.normal(player3)
                if team2_name[1] in attact_target:
                    player1.normal(player4)
            elif player1.damageskillname in attact_pick:
                if team2_name[0] in attact_target:
                    player1.damageskill(player3)
                if team2_name[1] in attact_target:
                    player1.damageskill(player4)
            elif player1.buffdebuffname in attact_pick:
                if '흑사병 보균자' in team1_character[0]:
                    if team2_name[0] in attact_target:
                        player1.buffdebuff(player2, player3, player4)
                    if team2_name[1] in attact_target:
                        player1.buffdebuff(player2, player3, player4)
                elif:
                    if team2_name[0] in attact_target:
                        player1.buffdebuff(player3)
                    if team2_name[1] in attact_target:
                        player1.buffdebuff(player4)
                        
                slow_print(f'다시 {player1_name}의 공격차례 입니다.')
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
    
                slow_print(f'공격할 적을 골라주세요.')
            
                attact_target = input()
            
                if player1.normalname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.normal(player3)
                    if team2_name[1] in attact_target:
                        player1.normal(player4)
                elif player1.damageskillname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.damageskill(player3)
                    if team2_name[1] in attact_target:
                        player1.damageskill(player4)
                elif player1.ultimatename in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.ultimate(player3)
                    if team2_name[1] in attact_target:
                        player1.ultimate(player4)
    
            elif player1.ultimatename in attact_pick:
                if team2_name[0] in attact_target:
                    player1.ultimate(player3)
                if team2_name[1] in attact_target:
                    player1.ultimate(player4)
            elif '설명' in attact_pick:
                player1.explanation()
                
                slow_print(f'{team1_name[0]}의 공격차례 입니다.')
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
                    
                slow_print(f'공격할 적을 골라주세요.')
                
                attact_target = input()
                
                if player1.normalname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.normal(player3)
                    if team2_name[1] in attact_target:
                        player1.normal(player4)
                elif player1.damageskillname in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.damageskill(player3)
                    if team2_name[1] in attact_target:
                        player1.damageskill(player4)
                elif player1.buffdebuffname in attact_pick:
                    if '흑사병 보균자' in team1_character[0]:
                        if team2_name[0] in attact_target:
                            player1.buffdebuff(player2, player3, player4)
                        if team2_name[1] in attact_target:
                            player1.buffdebuff(player2, player3, player4)
                    elif:
                        if team2_name[0] in attact_target:
                            player1.buffdebuff(player3)
                        if team2_name[1] in attact_target:
                            player1.buffdebuff(player4)
                            
                    slow_print(f'다시 {player1_name}의 공격차례 입니다.')
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
        
                    slow_print(f'공격할 적을 골라주세요.')
                
                    attact_target = input()
                
                    if player1.normalname in attact_pick:
                        if team2_name[0] in attact_target:
                            player1.normal(player3)
                        if team2_name[1] in attact_target:
                            player1.normal(player4)
                    elif player1.damageskillname in attact_pick:
                        if team2_name[0] in attact_target:
                            player1.damageskill(player3)
                        if team2_name[1] in attact_target:
                            player1.damageskill(player4)
                    elif player1.ultimatename in attact_pick:
                        if team2_name[0] in attact_target:
                            player1.ultimate(player3)
                        if team2_name[1] in attact_target:
                            player1.ultimate(player4)
        
                elif player1.ultimatename in attact_pick:
                    if team2_name[0] in attact_target:
                        player1.ultimate(player3)
                    if team2_name[1] in attact_target:
                        player1.ultimate(player4)
    
            if '흑사병 보균자' in player1_character:
                player1.passive()
            elif '흑사병 보균자' in player2_character:
                player2.passive()
            
            if player3.hp <= 0 and player4.hp <= 0:
                slow_print(f'축하드립니다! 1팀의 승리입니다!')
                break







