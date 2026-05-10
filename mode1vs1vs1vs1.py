import random
import character
from Util import *





slow_print('플레이어 1의 이름을 입력해 주세요.')
player1_name = input()
print()

slow_print('플레이어 2의 이름을 입력해 주세요.')
player2_name = input()
print()

slow_print('플레이어 3의 이름을 입력해 주세요.')
player3_name = input()
print()

slow_print('플레이어 4의 이름을 입력해 주세요.')
player4_name = input()
print()


slow_print(f'각 플레이어들의 이름을 확인하세요')
slow_print(f'{player1_name}, {player2_name}, {player3_name}, {player4_name}')
print()
print()




player1_character = []
player2_character = []
player3_character = []
player4_character = []

player1 = character.Fighter(f'{player1_name}')
player2 = character.Fighter(f'{player2_name}')
player3 = character.Fighter(f'{player3_name}')
player4 = character.Fighter(f'{player4_name}')

def player1_pick():
    global player1
    character_list = ['[기사]', '[무사]', '[격투가]']
    slow_print(f'{player1_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{player1_name[0]}이/가 [{pick1}]를 선택했습니다.')
    player1_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player1 = character.Knight(f'{player1_name}')
    elif pick1 == '무사':
        player1 = character.Samurai(f'{player1_name}')
    elif pick1 == '격투가':
        player1 = character.Fighter(f'{player1_name}')
    print()





def player2_pick():
    global player2
    character_list = ['[기사]', '[무사]', '[격투가]']
    slow_print(f'{player2_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{player2_name[0]}이/가 [{pick1}]를 선택했습니다.')
    player2_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player2 = character.Knight(f'{player2_name}')
    elif pick1 == '무사':
        player2 = character.Samurai(f'{player2_name}')
    elif pick1 == '격투가':
        player2 = character.Fighter(f'{player2_name}')
    print()





def player3_pick():
    global player3
    character_list = ['[기사]', '[무사]', '[격투가]']
    slow_print(f'{player3_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{player3_name[0]}이/가 [{pick1}]를 선택했습니다.')
    player3_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player3 = character.Knight(f'{player3_name}')
    elif pick1 == '무사':
        player3 = character.Samurai(f'{player3_name}')
    elif pick1 == '격투가':
        player3 = character.Fighter(f'{player3_name}')
    print()






def player4_pick():
    character_list = ['[기사]', '[무사]', '[격투가]']
    slow_print(f'{player4_name[0]}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick1 = input()
    slow_print(f'{player4_name[0]}이/가 [{pick1}]를 선택했습니다.')
    player3_character.append(f'[{pick1}]')
    character_list.remove(f'[{pick1}]')
    if pick1 == '기사':
        player4 = character.Knight(f'{player4_name}')
    elif pick1 == '무사':
        player4 = character.Samurai(f'{player4_name}')
    elif pick1 == '격투가':
        player4 = character.Fighter(f'{player4_name}')
    print()





slow_print(f'{player1_name}의 캐릭터 선택 차례입니다.')
print()
player1_pick()
print()
slow_print(f'{player2_name}의 캐릭터 선택 차례입니다.')
print()
player2_pick()
print()
slow_print(f'{player3_name}의 캐릭터 선택 차례입니다.')
print()
player3_pick()
print()
slow_print(f'{player4_name}의 캐릭터 선택 차례입니다.')
print()
player4_pick()
print()


slow_print(f'각 플레이어들과 캐릭터를 확인하세요!')
print(f'{player1_name}: {player1_character[0]}')
print(f'{player2_name}: {player2_character[0]}')
print(f'{player3_name}: {player3_character[0]}')
print(f'{player4_name}: {player4_character[0]}')
time.sleep(5)

