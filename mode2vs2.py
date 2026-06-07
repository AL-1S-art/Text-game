import random
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


slow_print(f'각 플레이어들의 이름을 확인하세요')
slow_print(f'{team1_name}')
slow_print(f'{team2_name}')
print()
print()



team1_character = []
team2_character = []

player1 = Dummy('더미1')
player2 = Dummy('더미2')
player3 = Dummy('더미3')
player4 = Dummy('더미4')

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
    print()
    team1_character.append(f'{pick}')
    character_list.remove(f'[{pick}]')
    if pick == '격투가':
        player1 = Fighter(f'{team1_name[0]}')
    elif pick == '도박꾼':
        player1 = Gambler(f'{team1_name[0]}')
    elif pick == '자연술사':
        player1 = Naturalist(f'{team1_name[0]}')
    elif pick == '흑사병 보균자':
        player1 = Blackdeath(f'{team1_name[0]}')
    elif pick == '화학자':
        player1 = Chemist(f'{team1_name[0]}')
    elif pick == '체스선수':
        player1 = ChessPlayer(f'{team1_name[0]}')
    elif pick == '정치인':
        player1 = Politician(f'{team1_name[0]}')
    elif pick == '엔지니어':
        player1 = Engineer(f'{team1_name[0]}')
    elif pick == '음악가':
        player1 = Musician(f'{team1_name[0]}')
    elif pick == '투수':
        player1 = Pitcher(f'{team1_name[0]}')
    elif pick == '목수':
        player1 = Carpenter(f'{team1_name[0]}')
    elif pick == '보디빌더':
        player1 = Bodybuilder(f'{team1_name[0]}')
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
    print()
    team1_character.append(f'{pick}')
    character_list.remove(f'[{pick}]')
    if pick == '격투가':
        player2 = Fighter(f'{team1_name[1]}')
    elif pick == '도박꾼':
        player2 = Gambler(f'{team1_name[1]}')
    elif pick == '자연술사':
        player2 = Naturalist(f'{team1_name[1]}')
    elif pick == '흑사병 보균자':
        player2 = Blackdeath(f'{team1_name[1]}')
    elif pick == '화학자':
        player2 = Chemist(f'{team1_name[1]}')
    elif pick == '체스선수':
        player2 = ChessPlayer(f'{team1_name[1]}')
    elif pick == '정치인':
        player2 = Politician(f'{team1_name[1]}')
    elif pick == '엔지니어':
        player2 = Engineer(f'{team1_name[1]}')
    elif pick == '음악가':
        player2 = Musician(f'{team1_name[1]}')
    elif pick == '투수':
        player2 = Pitcher(f'{team1_name[1]}')
    elif pick == '목수':
        player2 = Carpenter(f'{team1_name[1]}')
    elif pick == '보디빌더':
        player2 = Bodybuilder(f'{team1_name[1]}')
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
    print()
    team2_character.append(f'{pick}')
    character_list.remove(f'[{pick}]')
    if pick == '격투가':
        player3 = Fighter(f'{team2_name[0]}')
    elif pick == '도박꾼':
        player3 = Gambler(f'{team2_name[0]}')
    elif pick == '자연술사':
        player3 = Naturalist(f'{team2_name[0]}')
    elif pick == '흑사병 보균자':
        player3 = Blackdeath(f'{team2_name[0]}')
    elif pick == '화학자':
        player3 = Chemist(f'{team2_name[0]}')
    elif pick == '체스선수':
        player3 = ChessPlayer(f'{team2_name[0]}')
    elif pick == '정치인':
        player3 = Politician(f'{team2_name[0]}')
    elif pick == '엔지니어':
        player3 = Engineer(f'{team2_name[0]}')
    elif pick == '음악가':
        player3 = Musician(f'{team2_name[0]}')
    elif pick == '투수':
        player3 = Pitcher(f'{team2_name[0]}')
    elif pick == '목수':
        player3 = Carpenter(f'{team2_name[0]}')
    elif pick == '보디빌더':
        player3 = Bodybuilder(f'{team2_name}')
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
    print()
    team2_character.append(f'{pick}')
    character_list.remove(f'[{pick}]')
    if pick == '격투가':
        player4 = Fighter(f'{team2_name[1]}')
    elif pick == '도박꾼':
        player4 = Gambler(f'{team2_name[1]}')
    elif pick == '자연술사':
        player4 = Naturalist(f'{team2_name[1]}')
    elif pick == '흑사병 보균자':
        player4 = Blackdeath(f'{team2_name[1]}')
    elif pick == '화학자':
        player4 = Chemist(f'{team2_name[1]}')
    elif pick == '체스선수':
        player4 = ChessPlayer(f'{team2_name[1]}')
    elif pick == '정치인':
        player4 = Politician(f'{team2_name[1]}')
    elif pick == '엔지니어':
        player4 = Engineer(f'{team2_name[1]}')
    elif pick == '음악가':
        player4 = Musician(f'{team2_name[1]}')
    elif pick == '투수':
        player4 = Pitcher(f'{team2_name[1]}')
    elif pick == '목수':
        player4 = Carpenter(f'{team2_name[1]}')
    elif pick == '보디빌':
        player4 = Bodybuilder(f'{team2_name[1]}')
    print()



slow_print(f'1팀의 캐릭터 선택 차례입니다.')
print()
team1_pick()
slow_print(f'2팀의 캐릭터 선택 차례입니다.')
print()
team2_pick()


players = []
players.append(player1)
players.append(player2)
players.append(player3)
players.append(player4)


team1 = []
team2 = []
teams = []
teams.append(team1)
teams.append(team2)


teamlist = {}
cnt = 0
for team in teams:
    teamlist['team'+str(cnt)] = team
    cnt += 1
teamnamelist = list(teamlist.keys())




for x in range(len(players)):
    teams[x%(len(teams))].append(players[x])
for i in team1:
    i.updateteam(team1, team2, teamlist)
for i in team2:
    i.updateteam(team2, team1, teamlist)


slow_print(f'각 팀의 플레이어들과 캐릭터를 확인하세요!')
print()
print('1팀의 플레이어들')
for i in range(2):
    print(f'{team1_name[i]}: {team1_character[i]}')
    print(f'체력: [ {players[i].hp} / {players[i].hhp} ], 마나: [ {players[i].mp} / {players[i].hmp} ] ')
    print(f'공격력 / 방어력: [ {players[i].ad} / {players[i].de} ]')
    print()
print()

print()
print('2팀의 플레이어들')
for i in range(2):
    print(f'{team2_name[i]}: {team2_character[i]}')
    print(f'체력: [ {players[i+2].hp} / {players[i+2].hhp} ], 마나: [ {players[i+2].mp} / {players[i+2].hmp} ] ')
    print(f'공격력 / 방어력: [ {players[i+2].ad} / {players[i+2].de} ]')
    print()
print()

time.sleep(10)



slow_print(f'게임을 시작합니다!')
print()
random.shuffle(teamnamelist)
slow_print(f'순서는 {teamnamelist} 입니다.')
print()
while True:
    for team in teams:
        for player in team:
            player.startingturn()
