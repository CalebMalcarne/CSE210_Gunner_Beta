import random
from casting.boss import Boss
from game.constants import SCREEN_WIDTH
#draws the boss and everything to do with the boss 


class DrawBoss():

    def __init__(self):
        self.position_x = random.randint(SCREEN_WIDTH)
        self.position_y = 0
        self.velocity = 1


    def execute(self, cast, script, callback):
        

        pass 


