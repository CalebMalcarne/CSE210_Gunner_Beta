from game_.casting.enemy import Enemy
from constants import *

class Boss(Enemy):

    def __init__(self, body, animation, image):

        super().__init__(body, image, False)
        self.size = (80,70)
        # self.hitpoints = Enemy.set_hitpoints(Enemy) * 3
        # self.color = self.boss_color(self.hitpoints)

    def should_spawn():
        # Once there have been 25 enemies then it will spawn the boss
        number_of_enemies = 0
        if number_of_enemies == 25:
            return True
        else:
            number_of_enemies += 1
            return False
            
    def take_damage(self, damage):
        self.hitpoints -= damage
        self.change_color()




