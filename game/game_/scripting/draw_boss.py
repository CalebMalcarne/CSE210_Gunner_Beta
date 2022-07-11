from casting.enemy import Enemy
from casting.cast import Stat

class Boss(Enemy):
    #still need to put in values just making a skeleton 
    def __init__(self,):

        self.color =''
        self.size = ''
        self.position = ''
        self.velocity = ''
        self.difficulty = ''

    def get_position(self):
        '''gets position for the boss, will be randomized'''
        position = 0 
        return position

    def get_size(self):
        ''' for the size of the boss'''
        size = 0
        return size
    