import random
import character
from Util import *

from Playable.Baker import *
from Playable.Blackdeath import *
from Playable.Bodybuilder import *
from Playable.Carpenter import *
from Playable.Chemist import *
from Playable.ChessPlayer import *
from Playable.Dummy import *
from Playable.Engineer import *
from Playable.Fighter import *
from Playable.Gambler import *
from Playable.Harrypotter import *
from Playable.Musician import *
from Playable.Naturalist import *
from Playable.Pitcher import *
from Playable.Politician import *


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

player1 = Fighter(f'{player1_name}')
player2 = Fighter(f'{player2_name}')
players = []

def player1_pick():
    global player1
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]','[화학자]','[체스선수]','[정치인]','[엔지니어]', '[음악가]', '[투수]','[목수]', '[보디빌더]']
    slow_print(f'{player1_name}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{player1_name}이/가 [{pick}]를 선택했습니다.')
    player1_character.append(f'{pick}')
    character_list.remove(f'[{pick}]')
    if pick == '도박꾼':
        player1 = Gambler(f'{player1_name}')
    elif pick == '격투가':
        player1 = Fighter(f'{player1_name}')
    elif pick == '자연술사':
        player1 = Naturalist(f'{player1_name}')
    elif pick == '흑사병 보균자':
        player1 = Blackdeath(f'{player1_name}')
    elif pick == '화학자':
        player1 = Chemist(f'{player1_name}')
    elif pick == '체스선수':
        player1 = ChessPlayer(f'{player1_name}')
    elif pick == '정치인':
        player1 = Politician(f'{player1_name}')
    elif pick == '엔지니어':
        player1 = Engineer(f'{player1_name}')
    elif pick == '음악가':
        player1 = Musician(f'{player1_name}')
    elif pick == '투수':
        player1 = Pitcher(f'{player1_name}')
    elif pick == '목수':
        player1 = Carpenter(f'{player1_name}')
    elif pick == '보디빌더':
        player1 = Bodybuilder(f'{player1_name}')
    print()
    players.append(player1)





def player2_pick():
    global player2
    character_list = ['[도박꾼]', '[격투가]', '[자연술사]', '[흑사병 보균자]','[화학자]','[체스선수]','[정치인]','[엔지니어]', '[음악가]', '[투수]', '[목수]', '[보디빌더]']
    slow_print(f'{player2_name}의 캐릭터 선택 시간입니다.')
    slow_print(f'캐릭터 리스트에 있는 캐릭터 중 원하는 캐릭터를 고르세요.')
    print()
    slow_print('캐릭터 리스트')
    for i in range(len(character_list)):
        print(character_list[i], end=' ')
    print()
    pick = input()
    slow_print(f'{player2_name}이/가 [{pick}]를 선택했습니다.')
    player2_character.append(f'{pick}')
    character_list.remove(f'[{pick}]')
    if pick == '도박꾼':
        player2 = Gambler(f'{player2_name}')
    elif pick == '격투가':
        player2 = Fighter(f'{player2_name}')
    elif pick == '자연술사':
        player2 = Naturalist(f'{player2_name}')
    elif pick == '흑사병 보균자':
        player2 = Blackdeath(f'{player2_name}')
    elif pick == '화학자':
        player2 = Chemist(f'{player2_name}')
    elif pick == '체스선수':
        player2 = ChessPlayer(f'{player2_name}')
    elif pick == '정치인':
        player2 = Politician(f'{player2_name}')
    elif pick == '엔지니어':
        player2 = Engineer(f'{player2_name}')
    elif pick == '음악가':
        player2 = Musician(f'{player2_name}')
    elif pick == '투수':
        player2 = Pitcher(f'{player2_name}')
    elif pick == '목수':
        player2 = Carpenter(f'{player2_name}')
    elif pick == '보디빌더':
        player2 = Bodybuilder(f'{player2_name}')
    players.append(player2)
    print()


random.shuffle(players)
team1 = []
team2 = []
teams = []
teams.append(team1)
teams.append(team2)
slow_print(f'{player1_name}의 캐릭터 선택 차례입니다.')
print()
player1_pick()
print()
slow_print(f'{player2_name}의 캐릭터 선택 차례입니다.')
print()
player2_pick()
print()
cnt = 0
teamlist = []
random.shuffle(teams)
for team in teams:
    teamlist.append('team'+str(cnt+1))
    cnt += 1
for x in range(len(players)):
    teams[x%(len(teams))].append(players[x])
    
for team in teams:
    for player in team:
        player.updateteam(team,teams,teamlist)








slow_print(f'각 플레이어와 캐릭터를 확인하세요!')
print()
print(f'{player1_name}: {player1_character[0]}')
print(f'체력/보호막: [ {player1.hp}({player1.hhp}) / {player1.shield} ], 마나: [ {player1.mp} / {player1.hmp} ] ')
print(f'공격력 / 방어력: [ {player1.ad} / {player1.de} ]')
print()
print(f'{player2_name}: {player2_character[0]}')
print(f'체력/보호막: [ {player2.hp}({player2.hhp}) / {player2.shield} ], 마나: [ {player2.mp} / {player2.hmp} ] ')
print(f'공격력 / 방어력: [ {player2.ad} / {player2.de} ]')
print()

time.sleep(5)










slow_print(f'게임을 시작합니다!')
print()
slow_print(f'순서는 {teamlist} 입니다.')
while 1:
    for x in range(len(teams[0])):
        for team in teams:
            team[x].startingturn()