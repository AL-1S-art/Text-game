import character
import random
from Util import *





slow_print('1팀의 플레이어들의 이름을 입력해 주세요.')
team1_name = []
for i in range(4):
    a = input()
    team1_name.append(a)
print()

slow_print('2팀의 플레이어들의 이름을 입력해 주세요.')
team2_name = []
for i in range(4):
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
player5 = character.Fighter(0)
player6 = character.Fighter(0)
player7 = character.Fighter(0)
player8 = character.Fighter(0)

def team1_pick():
    global player1
    global player2
    global player3
    global player4
    character_list = ['[기사]', '[무사]', '[격투가]']
    slow_print(f'{team1_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team1_name[0]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player1 = character.Knight(f'{team1_name[0]}')
    elif pick1 == '무사':
        player1 = character.Samurai(f'{team1_name[0]}')
    elif pick1 == '격투가':
        player1 = character.Fighter(f'{team1_name[0]}')
    print()


    slow_print(f'{team1_name[1]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team1_name[1]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player2 = character.Knight(f'{team1_name[1]}')
    elif pick1 == '무사':
        player2 = character.Samurai(f'{team1_name[1]}')
    elif pick1 == '격투가':
        player2 = character.Fighter(f'{team1_name[1]}')
    print()


    slow_print(f'{team1_name[2]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team1_name[2]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player3 = character.Knight(f'{team1_name[2]}')
    elif pick1 == '무사':
        player3 = character.Samurai(f'{team1_name[2]}')
    elif pick1 == '격투가':
        player3 = character.Fighter(f'{team1_name[2]}')
    print()


    slow_print(f'{team1_name[3]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team1_name[3]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player4 = character.Knight(f'{team1_name[3]}')
    elif pick1 == '무사':
        player4 = character.Samurai(f'{team1_name[3]}')
    elif pick1 == '격투가':
        player4 = character.Fighter(f'{team1_name[3]}')
    print()





def team2_pick():
    global player5
    global player6
    global player7
    global player8
    character_list = ['[기사]', '[무사]', '[격투가]']
    slow_print(f'{team2_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team2_name[0]}이/가 [{pick1}]를 선택했습니다.')
    team2_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player5 = character.Knight(f'{team2_name[0]}')
    elif pick1 == '무사':
        player5 = character.Samurai(f'{team2_name[0]}')
    elif pick1 == '격투가':
        player5 = character.Fighter(f'{team2_name[0]}')
    print()


    slow_print(f'{team2_name[1]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team2_name[1]}이/가 [{pick1}]를 선택했습니다.')
    team2_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player6 = character.Knight(f'{team2_name[1]}')
    elif pick1 == '무사':
        player6 = character.Samurai(f'{team2_name[1]}')
    elif pick1 == '격투가':
        player6 = character.Fighter(f'{team2_name[1]}')
    print()


    slow_print(f'{team2_name[2]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team2_name[2]}이/가 [{pick1}]를 선택했습니다.')
    team2_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player7 = character.Knight(f'{team2_name[2]}')
    elif pick1 == '무사':
        player7 = character.Samurai(f'{team2_name[2]}')
    elif pick1 == '격투가':
        player7 = character.Fighter(f'{team2_name[2]}')
    print()


    slow_print(f'{team1_name[3]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{team1_name[3]}이/가 [{pick1}]를 선택했습니다.')
    team1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player8 = character.Knight(f'{team1_name[3]}')
    elif pick1 == '무사':
        player8 = character.Samurai(f'{team1_name[3]}')
    elif pick1 == '격투가':
        player8 = character.Fighter(f'{team1_name[3]}')
    print()




slow_print(f'1팀의 캐릭터 선택 차례입니다.')
print()
team1_pick()
slow_print(f'2팀의 캐릭터 선택 차례입니다.')
print()
team2_pick()


slow_print(f'각 팀의 플레이어들과 캐릭터를 확인하세요!')
slow_print(f'1팀의 플레이어들')
for i in range(len(team1_name)):
    print(f'{team1_name[i]}: {team1_character[i]}')
print()
slow_print(f'2팀의 플레이어들')
for i in range(len(team2_name)):
    print(f'{team2_name[i]}: {team2_character[i]}')
print()
time.sleep(9)