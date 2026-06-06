from Util import *
from character import Buff, Player
class Dummy(Player):
    def __init__(self,name):
        
        self.hhp = 10000
        self.hp = self.hhp
        super().__init__(name)
    