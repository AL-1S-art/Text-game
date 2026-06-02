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

player1 = character.Dummy('더미1')
player2 = character.Dummy('더미2')
player3 = character.Dummy('더미3')
player4 = character.Dummy('더미4')

def team1_pick():
    global player1
    global player2
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]','[화학자]','[체스선수]','[정치인]','[엔지니어]', '[음악가]', '[투수]','[목수]', '[보디빌더]']
    slow_print(f'{team1_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team1_name[0]}이/가 [{pick}]를 선택했습니다.')
    team1_character.append(f'{pick}')
    character_list.remove(f'{pick}')
    if pick == '격투가':
        player1 = character.Fighter(f'{team1_name[0]}')
    elif pick == '도박꾼':
        player1 = character.Gambler(f'{team1_name[0]}')
    elif pick == '자연술사':
        player1 = character.Naturalist(f'{team1_name[0]}')
    elif pick == '흑사병 보균자':
        player1 = character.Blackdeath(f'{team1_name[0]}')
    elif pick == '화학자':
        player1 = character.Chemist(f'{team1_name[0]}')
    elif pick == '체스선수':
        player1 = character.ChessPlayer(f'{team1_name[0]}')
    elif pick == '정치인':
        player1 = character.Politician(f'{team1_name[0]}')
    elif pick == '엔지니어':
        player1 = character.Engineer(f'{team1_name[0]}')
    elif pick == '음악가':
        player1 = character.Musician(f'{team1_name[0]}')
    elif pick == '투수':
        player1 = character.Pitcher(f'{team1_name[0]}')
    elif pick == '목수':
        player1 = character.Carpenter(f'{team1_name[0]}')
    elif pick == '보디빌더':
        player1 = character.Bodybuilder(f'{team1_name[0]}')
    print()


    slow_print(f'{team1_name[1]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team1_name[1]}이/가 [{pick}]를 선택했습니다.')
    team1_character.append(f'{pick}')
    character_list.remove(f'{pick}')
    if pick == '격투가':
        player2 = character.Fighter(f'{team1_name[1]}')
    elif pick == '도박꾼':
        player2 = character.Gambler(f'{team1_name[1]}')
    elif pick == '자연술사':
        player2 = character.Naturalist(f'{team1_name[1]}')
    elif pick == '흑사병 보균자':
        player2 = character.Blackdeath(f'{team1_name[1]}')
    elif pick == '화학자':
        player2 = character.Chemist(f'{team1_name[1]}')
    elif pick == '체스선수':
        player2 = character.ChessPlayer(f'{team1_name[1]}')
    elif pick == '정치인':
        player2 = character.Politician(f'{team1_name[1]}')
    elif pick == '엔지니어':
        player2 = character.Engineer(f'{team1_name[1]}')
    elif pick == '음악가':
        player2 = character.Musician(f'{team1_name[1]}')
    elif pick == '투수':
        player2 = character.Pitcher(f'{team1_name[1]}')
    elif pick == '목수':
        player2 = character.Carpenter(f'{team1_name[1]}')
    elif pick == '보디빌더':
        player2 = character.Bodybuilder(f'{team1_name[1]}')
    print()



def team2_pick():
    global player3
    global player4
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]','[화학자]','[체스선수]','[정치인]','[엔지니어]', '[음악가]', '[투수]', '[목수]', '[보디빌더]']
    slow_print(f'{team2_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team2_name[0]}이/가 [{pick}]를 선택했습니다.')
    team2_character.append(f'[{pick}]')
    character_list.remove(f'[{pick}]')
    if pick == '격투가':
        player3 = character.Fighter(f'{team2_name[0]}')
    elif pick == '도박꾼':
        player3 = character.Gambler(f'{team2_name[0]}')
    elif pick == '자연술사':
        player3 = character.Naturalist(f'{team2_name[0]}')
    elif pick == '흑사병 보균자':
        player3 = character.Blackdeath(f'{team2_name[0]}')
    elif pick == '화학자':
        player3 = character.Chemist(f'{team2_name[0]}')
    elif pick == '체스선수':
        player3 = character.ChessPlayer(f'{team2_name[0]}')
    elif pick == '정치인':
        player3 = character.Politician(f'{team2_name[0]}')
    elif pick == '엔지니어':
        player3 = character.Engineer(f'{team2_name[0]}')
    elif pick == '음악가':
        player3 = character.Musician(f'{team2_name[0]}')
    elif pick == '투수':
        player3 = character.Pitcher(f'{team2_name[0]}')
    elif pick == '목수':
        player3 = character.Carpenter(f'{team2_name[0]}')
    elif pick == '보디빌더':
        player3 = character.Bodybuilder(f'{team2_name[0]}')
    print()


    slow_print(f'{team2_name[1]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{team2_name[1]}이/가 [{pick}]를 선택했습니다.')
    team2_character.append(f'[{pick}]')
    character_list.remove(f'[{pick}]')
    if pick == '격투가':
        player4 = character.Fighter(f'{team2_name[1]}')
    elif pick == '도박꾼':
        player4 = character.Gambler(f'{team2_name[1]}')
    elif pick == '자연술사':
        player4 = character.Naturalist(f'{team2_name[1]}')
    elif pick == '흑사병 보균자':
        player4 = character.Blackdeath(f'{team2_name[1]}')
    elif pick == '화학자':
        player4 = character.Chemist(f'{team2_name[1]}')
    elif pick == '체스선수':
        player4 = character.ChessPlayer(f'{team2_name[1]}')
    elif pick == '정치인':
        player4 = character.Politician(f'{team2_name[1]}')
    elif pick == '엔지니어':
        player4 = character.Engineer(f'{team2_name[1]}')
    elif pick == '음악가':
        player4 = character.Musician(f'{team2_name[1]}')
    elif pick == '투수':
        player4 = character.Pitcher(f'{team2_name[1]}')
    elif pick == '목수':
        player4 = character.Carpenter(f'{team2_name[1]}')
    elif pick == '보디빌':
        player4 = character.Bodybuilder(f'{team2_name[1]}')
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
    print(f'{team1_name[i]}: {team1_character[i]}')
    print(f'체력: [ {players[i].hp} / {players[i].hhp} ], 마나: [ {players[i].mp} / {players[i].hmp} ] ')
    print(f'공격력 / 방어력: [ {players[i].ad} / {players[i].de} ]')
    print()


print()
print('2팀의 플레이어들')
for i in range(2):
    print(f'{team2_name[i]}: {team2_character[i]}')
    print(f'체력: [ {players[i+2].hp} / {players[i+2].hhp} ], 마나: [ {players[i+2].mp} / {players[i+2].hmp} ] ')
    print(f'공격력 / 방어력: [ {players[i+2].ad} / {players[i+2].de} ]')
    print()


time.sleep(10)




def player1_turn():
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
            if player3.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.normal(player4)
        if team2_name[1] in attact_target:
            player1.normal(player4)
            if player4.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.normal(player3)
    elif player1.damageskillname in attact_pick:
        if team2_name[0] in attact_target:
            player1.damageskill(player3)
            if player3.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.damageskill(player4)
        if team2_name[1] in attact_target:
            player1.damageskill(player4)
            if player4.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.damageskill(player3)
    elif player1.buffdebuffname in attact_pick:
        if team1_character[0] == '흑사병 보균자':
            if team2_name[0] in attact_target:
                player1.buffdebuff(player3, player2, player4)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.buffdebuff(player4, player2)
            if team2_name[1] in attact_target:
                player1.buffdebuff(player4, player2, player3)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.buffdebuff(player3, player2)
        else:
            if team2_name[0] in attact_target:
                player1.buffdebuff(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.buffdebuff(player4)
            if team2_name[1] in attact_target:
                player1.buffdebuff(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.buffdebuff(player3)
                
        slow_print(f'다시 {team1_name[0]}의 공격차례 입니다.')
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
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.normal(player4)
            if team2_name[1] in attact_target:
                player1.normal(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.normal(player3)
        elif player1.damageskillname in attact_pick:
            if team2_name[0] in attact_target:
                player1.damageskill(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.damageskill(player4)
            if team2_name[1] in attact_target:
                player1.damageskill(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.damageskill(player3)
        elif player1.ultimatename in attact_pick:
            if team2_name[0] in attact_target:
                player1.ultimate(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.ultimate(player4)
            if team2_name[1] in attact_target:
                player1.ultimate(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.ultimate(player3)

    elif player1.ultimatename in attact_pick:
        if team2_name[0] in attact_target:
            player1.ultimate(player3)
            if player3.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.ultimate(player4)
        if team2_name[1] in attact_target:
            player1.ultimate(player4)
            if player4.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.ultimate(player3)
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
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.normal(player4)
            if team2_name[1] in attact_target:
                player1.normal(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.normal(player3)
        elif player1.damageskillname in attact_pick:
            if team2_name[0] in attact_target:
                player1.damageskill(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.damageskill(player4)
            if team2_name[1] in attact_target:
                player1.damageskill(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.damageskill(player3)
        elif player1.buffdebuffname in attact_pick:
            if team1_character[0] == '흑사병 보균자':
                if team2_name[0] in attact_target:
                    player1.buffdebuff(player3, player2, player4)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.buffdebuff(player4, player2)
                if team2_name[1] in attact_target:
                    player1.buffdebuff(player4, player2, player3)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.buffdebuff(player3, player2)
            else:
                if team2_name[0] in attact_target:
                    player1.buffdebuff(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.ultimate(player4)
                if team2_name[1] in attact_target:
                    player1.buffdebuff(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.ultimate(player3)
                    
            slow_print(f'다시 {team1_name[0]}의 공격차례 입니다.')
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
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.normal(player4)
                if team2_name[1] in attact_target:
                    player1.normal(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.normal(player3)
            elif player1.damageskillname in attact_pick:
                if team2_name[0] in attact_target:
                    player1.damageskill(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.damageskill(player4)
                if team2_name[1] in attact_target:
                    player1.damageskill(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.damageskill(player3)
            elif player1.ultimatename in attact_pick:
                if team2_name[0] in attact_target:
                    player1.ultimate(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.ultimate(player4)
                if team2_name[1] in attact_target:
                    player1.ultimate(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player1.ultimate(player3)

        elif player1.ultimatename in attact_pick:
            if team2_name[0] in attact_target:
                player1.ultimate(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.ultimate(player4)
            if team2_name[1] in attact_target:
                player1.ultimate(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player1.ultimate(player3)

    if player3.hp <= 0 and player4.hp <= 0:
        slow_print(f'축하드립니다! 1팀의 승리입니다!')
        return

    player1.passive()
    player2.passive()
    player3.passive()
    player4.passive()
    
    print()
    print('1팀의 플레이어들')
    for i in range(2):
        print(f'{team1_name[i]}: {team1_character[i]}')
        print(f'체력: [ {players[i].hp} / {players[i].hhp} ], 마나: [ {players[i].mp} / {players[i].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i].ad} / {players[i].de} ]')
        if players[i].hp <= 0:
            print('사망 상태입니다.')
        print()


    print()
    print('2팀의 플레이어들')
    for i in range(2):
        print(f'{team2_name[i]}: {team2_character[i]}')
        print(f'체력: [ {players[i+2].hp} / {players[i+2].hhp} ], 마나: [ {players[i+2].mp} / {players[i+2].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i+2].ad} / {players[i+2].de} ]')
        if players[i+2].hp <= 0:
            print('사망 상태입니다.')
        print()







def player2_turn():
    slow_print(f'{team1_name[1]}의 공격차례 입니다.')
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
        
    slow_print(f'공격할 적을 골라주세요.')
    
    attact_target = input()
    
    if player2.normalname in attact_pick:
        if team2_name[0] in attact_target:
            player2.normal(player3)
            if player3.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player2.normal(player4)
        if team2_name[1] in attact_target:
            player2.normal(player4)
            if player4.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player1.normal(player3)
    elif player2.damageskillname in attact_pick:
        if team2_name[0] in attact_target:
            player2.damageskill(player3)
            if player3.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player2.damageskill(player4)
        if team2_name[1] in attact_target:
            player2.damageskill(player4)
            if player4.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player2.damageskill(player3)
    elif player2.buffdebuffname in attact_pick:
        if team1_character[1] == '흑사병 보균자':
            if team2_name[0] in attact_target:
                player2.buffdebuff(player3, player1, player4)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.buffdebuff(player4, player1)
            if team2_name[1] in attact_target:
                player2.buffdebuff(player4, player1, player3)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.buffdebuff(player3, player1)
        else:
            if team2_name[0] in attact_target:
                player2.buffdebuff(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.buffdebuff(player4)
            if team2_name[1] in attact_target:
                player2.buffdebuff(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.buffdebuff(player3)
                
        slow_print(f'다시 {team1_name[1]}의 공격차례 입니다.')
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

        slow_print(f'공격할 적을 골라주세요.')
    
        attact_target = input()
    
        if player2.normalname in attact_pick:
            if team2_name[0] in attact_target:
                player2.normal(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.normal(player4)
            if team2_name[1] in attact_target:
                player2.normal(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.normal(player3)
        elif player2.damageskillname in attact_pick:
            if team2_name[0] in attact_target:
                player2.damageskill(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.damageskill(player4)
            if team2_name[1] in attact_target:
                player2.damageskill(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.damageskill(player3)
        elif player2.ultimatename in attact_pick:
            if team2_name[0] in attact_target:
                player2.ultimate(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.ultimate(player4)
            if team2_name[1] in attact_target:
                player2.ultimate(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.ultimate(player3)

    elif player2.ultimatename in attact_pick:
        if team2_name[0] in attact_target:
            player2.ultimate(player3)
            if player3.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player2.ultimate(player4)
        if team2_name[1] in attact_target:
            player2.ultimate(player4)
            if player4.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player2.ultimate(player3)
    elif '설명' in attact_pick:
        player2.explanation()
        
        slow_print(f'{team1_name[1]}의 공격차례 입니다.')
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
            
        slow_print(f'공격할 적을 골라주세요.')
        
        attact_target = input()
        
        if player2.normalname in attact_pick:
            if team2_name[0] in attact_target:
                player2.normal(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.normal(player4)
            if team2_name[1] in attact_target:
                player2.normal(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.normal(player3)
        elif player2.damageskillname in attact_pick:
            if team2_name[0] in attact_target:
                player2.damageskill(player3)
                if player3.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.damageskill(player4)
            if team2_name[1] in attact_target:
                player2.damageskill(player4)
                if player4.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player2.damageskill(player3)
        elif player2.buffdebuffname in attact_pick:
            if team1_character[1] == '흑사병 보균자':
                if team2_name[0] in attact_target:
                    player2.buffdebuff(player3, player1, player4)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.buffdebuff(player4, player1)
                if team2_name[1] in attact_target:
                    player2.buffdebuff(player4, player1, player3)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.buffdebuff(player3, player1)
            else:
                if team2_name[0] in attact_target:
                    player2.buffdebuff(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.buffdebuff(player4)
                if team2_name[1] in attact_target:
                    player2.buffdebuff(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.buffdebuff(player3)
                    
            slow_print(f'다시 {team1_name[1]}의 공격차례 입니다.')
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

            slow_print(f'공격할 적을 골라주세요.')
        
            attact_target = input()
        
            if player2.normalname in attact_pick:
                if team2_name[0] in attact_target:
                    player2.normal(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.normal(player4)
                if team2_name[1] in attact_target:
                    player2.normal(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.normal(player3)
            elif player2.damageskillname in attact_pick:
                if team2_name[0] in attact_target:
                    player2.damageskill(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.damageskill(player4)
                if team2_name[1] in attact_target:
                    player2.damageskill(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.damageskill(player3)
            elif player2.ultimatename in attact_pick:
                if team2_name[0] in attact_target:
                    player2.ultimate(player3)
                    if player3.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.ultimate(player4)
                if team2_name[1] in attact_target:
                    player2.ultimate(player4)
                    if player4.hp <= 0:
                        slow_print('이미 사망한 적입니다!')
                        slow_print('타겟이 자동으로 지정됩니다.')
                        player2.ultimate(player3)
----------------------------------------------------------------------------------------------------------------------
        elif player2.ultimatename in attact_pick:
            if team2_name[0] in attact_target:
                player2.ultimate(player3)
            if team2_name[1] in attact_target:
                player2.ultimate(player4)

    if player3.hp <= 0 and player4.hp <= 0:
        slow_print(f'축하드립니다! 1팀의 승리입니다!')
        return

    player1.passive()
    player2.passive()
    player3.passive()
    player4.passive()
    
    print()
    print('1팀의 플레이어들')
    for i in range(2):
        print(f'{team1_name[i]}: {team1_character[i]}')
        print(f'체력: [ {players[i].hp} / {players[i].hhp} ], 마나: [ {players[i].mp} / {players[i].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i].ad} / {players[i].de} ]')
        if players[i].hp <= 0:
            print('사망 상태입니다.')
        print()


    print()
    print('2팀의 플레이어들')
    for i in range(2):
        print(f'{team2_name[i]}: {team2_character[i]}')
        print(f'체력: [ {players[i+2].hp} / {players[i+2].hhp} ], 마나: [ {players[i+2].mp} / {players[i+2].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i+2].ad} / {players[i+2].de} ]')
        if players[i+2].hp <= 0:
            print('사망 상태입니다.')
        print()












def player3_turn():
    slow_print(f'{team2_name[0]}의 공격차례 입니다.')
    slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

    if player3.bdbturn == 0:
        if player3.uturn == 0:
            slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}], [{player3.ultimatename}], [설명]')
        if player3.uturn > 0:
            slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}], [설명]')
    elif player3.bdbturn > 0:
        if player3.uturn == 0:
            slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.ultimatename}], [설명]')
        if player3.uturn > 0:
            slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [설명]')

    attact_pick = input()
        
    slow_print(f'공격할 적을 골라주세요.')
    
    attact_target = input()
    
    if player3.normalname in attact_pick:
        if team1_name[0] in attact_target:
            player3.normal(player1)
            if player1.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player3.damageskill(player2)
        if team1_name[1] in attact_target:
            player3.normal(player2)
            if player2.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player3.damageskill(player1)
    elif player3.damageskillname in attact_pick:
        if team1_name[0] in attact_target:
            player3.damageskill(player1)
            if player1.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player3.damageskill(player2)
        if team1_name[1] in attact_target:
            player3.damageskill(player2)
            if player2.hp <= 0:
                slow_print('이미 사망한 적입니다!')
                slow_print('타겟이 자동으로 지정됩니다.')
                player3.damageskill(player1)
    elif player3.buffdebuffname in attact_pick:
        if team2_character[0] == '흑사병 보균자':
            if team1_name[0] in attact_target:
                player3.buffdebuff(player1, player2, player4)
                if player1.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player3.damageskill(player2, player4)
            if team1_name[1] in attact_target:
                player3.buffdebuff(player2, player1, player4)
                if player2.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player3.damageskill(player1, player4)
        else:
            if team1_name[0] in attact_target:
                player3.buffdebuff(player3)
                if player1.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player3.damageskill(player2)
            if team1_name[1] in attact_target:
                player3.buffdebuff(player4)
                if player2.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player3.damageskill(player1)
                    
        slow_print(f'다시 {team2_name[0]}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player3.bdbturn == 0:
            if player3.uturn == 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}], [{player3.ultimatename}]')
            if player3.uturn > 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}]')
        elif player3.bdbturn > 0:
            if player3.uturn == 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.ultimatename}]')
            if player3.uturn > 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}]')

        attact_pick = input()

        slow_print(f'공격할 적을 골라주세요.')
    
        attact_target = input()
    
        if player3.normalname in attact_pick:
            if team1_name[0] in attact_target:
                player3.normal(player1)
                if player1.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player3.damageskill(player2)
            if team1_name[1] in attact_target:
                player3.normal(player2)
                if player1.hp <= 0:
                    slow_print('이미 사망한 적입니다!')
                    slow_print('타겟이 자동으로 지정됩니다.')
                    player3.damageskill(player2)
        elif player3.damageskillname in attact_pick:
            if team1_name[0] in attact_target:
                player3.damageskill(player1)
            if team1_name[1] in attact_target:
                player3.damageskill(player2)
        elif player3.ultimatename in attact_pick:
            if team1_name[0] in attact_target:
                player3.ultimate(player1)
            if team1_name[1] in attact_target:
                player3.ultimate(player2)

    elif player3.ultimatename in attact_pick:
        if team1_name[0] in attact_target:
            player3.ultimate(player1)
        if team1_name[1] in attact_target:
            player3.ultimate(player2)
    elif '설명' in attact_pick:
        player3.explanation()
        
        slow_print(f'{team2_name[0]}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player3.bdbturn == 0:
            if player3.uturn == 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}], [{player3.ultimatename}], [설명]')
            if player3.uturn > 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}], [설명]')
        elif player3.bdbturn > 0:
            if player3.uturn == 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.ultimatename}], [설명]')
            if player3.uturn > 0:
                slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [설명]')

        attact_pick = input()
            
        slow_print(f'공격할 적을 골라주세요.')
        
        attact_target = input()
        
        if player3.normalname in attact_pick:
            if team1_name[0] in attact_target:
                player3.normal(player1)
            if team1_name[1] in attact_target:
                player3.normal(player2)
        elif player3.damageskillname in attact_pick:
            if team1_name[0] in attact_target:
                player3.damageskill(player1)
            if team1_name[1] in attact_target:
                player3.damageskill(player2)
        elif player3.buffdebuffname in attact_pick:
            if team2_character[0] == '흑사병 보균자':
                if team1_name[0] in attact_target:
                    player3.buffdebuff(player1, player2, player4)
                if team1_name[1] in attact_target:
                    player3.buffdebuff(player2, player1, player4)
            else:
                if team1_name[0] in attact_target:
                    player3.buffdebuff(player3)
                if team1_name[1] in attact_target:
                    player3.buffdebuff(player4)
                    
            slow_print(f'다시 {team1_name[1]}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player3.bdbturn == 0:
                if player3.uturn == 0:
                    slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}], [{player3.ultimatename}]')
                if player3.uturn > 0:
                    slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.buffdebuffname}]')
            elif player3.bdbturn > 0:
                if player3.uturn == 0:
                    slow_print(f'[{player3.normalname}], [{player3.damageskillname}], [{player3.ultimatename}]')
                if player3.uturn > 0:
                    slow_print(f'[{player3.normalname}], [{player3.damageskillname}]')

            attact_pick = input()

            slow_print(f'공격할 적을 골라주세요.')
        
            attact_target = input()
        
            if player3.normalname in attact_pick:
                if team1_name[0] in attact_target:
                    player3.normal(player1)
                if team1_name[1] in attact_target:
                    player3.normal(player2)
            elif player3.damageskillname in attact_pick:
                if team1_name[0] in attact_target:
                    player3.damageskill(player1)
                if team1_name[1] in attact_target:
                    player3.damageskill(player2)
            elif player3.ultimatename in attact_pick:
                if team1_name[0] in attact_target:
                    player3.ultimate(player1)
                if team1_name[1] in attact_target:
                    player3.ultimate(player2)

        elif player3.ultimatename in attact_pick:
            if team1_name[0] in attact_target:
                player3.ultimate(player1)
            if team1_name[1] in attact_target:
                player3.ultimate(player2)

    if player1.hp <= 0 and player2.hp <= 0:
        slow_print(f'축하드립니다! 2팀의 승리입니다!')
        return


    player1.passive()
    player3.passive()
    player3.passive()
    player4.passive()
    
    print()
    print('1팀의 플레이어들')
    for i in range(2):
        print(f'{team1_name[i]}: {team1_character[i]}')
        print(f'체력: [ {players[i].hp} / {players[i].hhp} ], 마나: [ {players[i].mp} / {players[i].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i].ad} / {players[i].de} ]')
        if players[i].hp <= 0:
            print('사망 상태입니다.')
        print()


    print()
    print('2팀의 플레이어들')
    for i in range(2):
        print(f'{team2_name[i]}: {team2_character[i]}')
        print(f'체력: [ {players[i+2].hp} / {players[i+2].hhp} ], 마나: [ {players[i+2].mp} / {players[i+2].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i+2].ad} / {players[i+2].de} ]')
        if players[i+2].hp <= 0:
            print('사망 상태입니다.')
        print()
































def player4_turn():
    slow_print(f'{team2_name[1]}의 공격차례 입니다.')
    slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

    if player4.bdbturn == 0:
        if player4.uturn == 0:
            slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}], [{player4.ultimatename}], [설명]')
        if player4.uturn > 0:
            slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}], [설명]')
    elif player4.bdbturn > 0:
        if player4.uturn == 0:
            slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.ultimatename}], [설명]')
        if player4.uturn > 0:
            slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [설명]')

    attact_pick = input()
        
    slow_print(f'공격할 적을 골라주세요.')
    
    attact_target = input()
    
    if player4.normalname in attact_pick:
        if team1_name[0] in attact_target:
            player4.normal(player1)
        if team1_name[1] in attact_target:
            player4.normal(player2)
    elif player4.damageskillname in attact_pick:
        if team1_name[0] in attact_target:
            player4.damageskill(player1)
        if team1_name[1] in attact_target:
            player4.damageskill(player2)
    elif player4.buffdebuffname in attact_pick:
        if team2_character[1] == '흑사병 보균자':
            if team1_name[0] in attact_target:
                player4.buffdebuff(player1, player2, player3)
            if team1_name[1] in attact_target:
                player4.buffdebuff(player2, player1, player3)
        else:
            if team1_name[0] in attact_target:
                player4.buffdebuff(player4)
            if team1_name[1] in attact_target:
                player4.buffdebuff(player4)
                
        slow_print(f'다시 {team2_name[1]}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player4.bdbturn == 0:
            if player4.uturn == 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}], [{player4.ultimatename}]')
            if player4.uturn > 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}]')
        elif player4.bdbturn > 0:
            if player4.uturn == 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.ultimatename}]')
            if player4.uturn > 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}]')

        attact_pick = input()

        slow_print(f'공격할 적을 골라주세요.')
    
        attact_target = input()
    
        if player4.normalname in attact_pick:
            if team1_name[0] in attact_target:
                player4.normal(player1)
            if team1_name[1] in attact_target:
                player4.normal(player2)
        elif player4.damageskillname in attact_pick:
            if team1_name[0] in attact_target:
                player4.damageskill(player1)
            if team1_name[1] in attact_target:
                player4.damageskill(player2)
        elif player4.ultimatename in attact_pick:
            if team1_name[0] in attact_target:
                player4.ultimate(player1)
            if team1_name[1] in attact_target:
                player4.ultimate(player2)

    elif player4.ultimatename in attact_pick:
        if team1_name[0] in attact_target:
            player4.ultimate(player1)
        if team1_name[1] in attact_target:
            player4.ultimate(player2)
    elif '설명' in attact_pick:
        player4.explanation()
        
        slow_print(f'{team2_name[1]}의 공격차례 입니다.')
        slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

        if player4.bdbturn == 0:
            if player4.uturn == 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}], [{player4.ultimatename}], [설명]')
            if player4.uturn > 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}], [설명]')
        elif player4.bdbturn > 0:
            if player4.uturn == 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.ultimatename}], [설명]')
            if player4.uturn > 0:
                slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [설명]')

        attact_pick = input()
            
        slow_print(f'공격할 적을 골라주세요.')
        
        attact_target = input()
        
        if player4.normalname in attact_pick:
            if team1_name[0] in attact_target:
                player4.normal(player1)
            if team1_name[1] in attact_target:
                player4.normal(player2)
        elif player4.damageskillname in attact_pick:
            if team1_name[0] in attact_target:
                player4.damageskill(player1)
            if team1_name[1] in attact_target:
                player4.damageskill(player2)
        elif player4.buffdebuffname in attact_pick:
            if team2_character[1] == '흑사병 보균자':
                if team1_name[0] in attact_target:
                    player4.buffdebuff(player1, player2, player3)
                if team1_name[1] in attact_target:
                    player4.buffdebuff(player2, player1, player3)
            else:
                if team1_name[0] in attact_target:
                    player4.buffdebuff(player4)
                if team1_name[1] in attact_target:
                    player4.buffdebuff(player4)
                    
            slow_print(f'다시 {team2_name[1]}의 공격차례 입니다.')
            slow_print(f'다음 스킬들 중 하나를 선택하십시오.')

            if player4.bdbturn == 0:
                if player4.uturn == 0:
                    slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}], [{player4.ultimatename}]')
                if player4.uturn > 0:
                    slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.buffdebuffname}]')
            elif player4.bdbturn > 0:
                if player4.uturn == 0:
                    slow_print(f'[{player4.normalname}], [{player4.damageskillname}], [{player4.ultimatename}]')
                if player4.uturn > 0:
                    slow_print(f'[{player4.normalname}], [{player4.damageskillname}]')

            attact_pick = input()

            slow_print(f'공격할 적을 골라주세요.')
        
            attact_target = input()
        
            if player4.normalname in attact_pick:
                if team1_name[0] in attact_target:
                    player4.normal(player1)
                if team1_name[1] in attact_target:
                    player4.normal(player2)
            elif player4.damageskillname in attact_pick:
                if team1_name[0] in attact_target:
                    player4.damageskill(player1)
                if team1_name[1] in attact_target:
                    player4.damageskill(player2)
            elif player4.ultimatename in attact_pick:
                if team1_name[0] in attact_target:
                    player4.ultimate(player1)
                if team1_name[1] in attact_target:
                    player4.ultimate(player2)

        elif player4.ultimatename in attact_pick:
            if team1_name[0] in attact_target:
                player4.ultimate(player1)
            if team1_name[1] in attact_target:
                player4.ultimate(player2)

    if player1.hp <= 0 and player2.hp <= 0:
        slow_print(f'축하드립니다! 2팀의 승리입니다!')
        return

    player1.passive()
    player2.passive()
    player3.passive()
    player4.passive()
    
    print()
    print('1팀의 플레이어들')
    for i in range(2):
        print(f'{team1_name[i]}: {team1_character[i]}')
        print(f'체력: [ {players[i].hp} / {players[i].hhp} ], 마나: [ {players[i].mp} / {players[i].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i].ad} / {players[i].de} ]')
        if players[i].hp <= 0:
            print('사망 상태입니다.')

        print()


    print()
    print('2팀의 플레이어들')
    for i in range(2):
        print(f'{team2_name[i]}: {team2_character[i]}')
        print(f'체력: [ {players[i+2].hp} / {players[i+2].hhp} ], 마나: [ {players[i+2].mp} / {players[i+2].hmp} ] ')
        print(f'공격력 / 방어력: [ {players[i+2].ad} / {players[i+2].de} ]')
        if players[i+2].hp <= 0:
            print('사망 상태입니다.')
        print()















slow_print(f'게임을 시작합니다!')
print()
sequence = random.shuffle([team1_name[0], team1_name[1], team2_name[0], team2_name[1]])


slow_print(f'순서는 {sequence} 입니다.')
if sequence == [team1_name[0], team1_name[1], team2_name[0], team2_name[1]]:           # 1 2 3 4
    while True:
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[0], team1_name[1], team2_name[1], team2_name[0]]:           # 1 2 4 3
    while True:
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[0], team2_name[0], team1_name[1], team2_name[1]]:           # 1 3 2 4
    while True:
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[0], team2_name[0], team2_name[1], team1_name[1]]:           # 1 3 4 2
    while True:
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team1_name[0], team2_name[1], team1_name[1], team2_name[0]]:           # 1 4 2 3
    while True:
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[0], team2_name[1], team2_name[0], team1_name[1]]:           # 1 4 3 2
    while True:
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team1_name[1], team1_name[0], team2_name[0], team2_name[1]]:           # 2 1 3 4
    while True:
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[1], team1_name[0], team2_name[1], team2_name[0]]:           # 2 1 4 3
    while True:
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[1], team2_name[0], team1_name[0], team2_name[1]]:           # 2 3 1 4
    while True:
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[1], team2_name[0], team2_name[1], team1_name[0]]:           # 2 3 4 1
    while True:
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team1_name[1], team2_name[1], team1_name[0], team2_name[0]]:           # 2 4 1 3
    while True:
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team1_name[1], team2_name[1], team2_name[0], team1_name[0]]:           # 2 4 3 1
    while True:
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[0], team1_name[0], team1_name[1], team2_name[1]]:           # 3 1 2 4
    while True:
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team2_name[0], team1_name[0], team2_name[1], team1_name[1]]:           # 3 1 4 2
    while True:
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[0], team1_name[1], team1_name[0], team2_name[1]]:           # 3 2 1 4
    while True:
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team2_name[0], team1_name[1], team2_name[1], team1_name[0]]:           # 3 2 4 1
    while True:
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[0], team2_name[1], team1_name[0], team1_name[1]]:           # 3 4 1 2
    while True:
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[0], team2_name[1], team1_name[1], team1_name[0]]:           # 3 4 2 1
    while True:
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
    
if sequence == [team2_name[1], team1_name[0], team1_name[1], team2_name[0]]:           # 4 1 2 3
    while True:
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team2_name[1], team1_name[0], team2_name[0], team1_name[1]]:           # 4 1 3 2
    while True:
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[1], team1_name[1], team1_name[0], team2_name[0]]:           # 4 2 1 3
    while True:
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break

if sequence == [team2_name[1], team1_name[1], team2_name[0], team1_name[0]]:           # 4 2 3 1
    while True:
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[1], team2_name[0], team1_name[0], team1_name[1]]:           # 4 3 1 2
    while True:
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break

if sequence == [team2_name[1], team2_name[0], team1_name[1], team1_name[0]]:           # 4 3 2 1
    while True:
        player4_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player3_turn()
        if player1.hp <= 0 and player2.hp <= 0:
            break
        player2_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
        player1_turn()
        if player3.hp <= 0 and player4.hp <= 0:
            break
