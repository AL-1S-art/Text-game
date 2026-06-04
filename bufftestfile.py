import character
a = character.Fighter('nae')

a.bufflist.append(character.Buff('화상', 'dot', 5, 10, -10, 'hp'))
a.bufflist.append(character.Buff('기절', 'cc', 5, 1, 'Null', 'Null'))
while True:
    a.startingturn()