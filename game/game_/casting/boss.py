from game_.casting.enemy import Enemy
from constants import *

class Boss(Enemy):

    def __init__(self, body, image, debug):
        animation = "null"

        super().__init__(body, image, animation, debug)
        self.size = (80,70)

            
    def take_damage(self, damage):
        self.hitpoints -= damage
        #self.change_color()




