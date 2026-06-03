import character
a = character.Fighter('nae')
a.bufflist = ['기절/2/1/Null/True/Null', '화상/2/4/100/True/hp','방어력감소/2/1/20/True/de']
while 1:
    a.buffdo()
    a.bufftimerenewal()