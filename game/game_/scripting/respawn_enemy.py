import random
from constants import *

from game_.scripting.action import Action
from game_.casting.enemy import Enemy
from game_.casting.point import Point

from game_.casting.body import Body
from game_.casting.image import Image

class Respawn_Enemy(Action):

    def __init__(self, cast):
        super().__init__(False)
        self.gunner = cast.get_first_actor(GUNNER_GROUP)
        self.gunner_hits = self.gunner.get_points
        self.enemies_spawned = 0
        self.boss_spawn_threshold = 25
    
    def spawn_enemy(self, amount_of_enemies):
        for i in range(amount_of_enemies):
            x = random.randint(1, 640)
            y = 480
            position = Point(x, y)
            vx = 0
            vy = 1
            velocity = Point(vx,vy)
            size = (10,10)
            body = Body(position, size, velocity)
            image = Image(TEST_IMAGE)
            enemy = Enemy(body, image, False)

            self.enemies_spawned += 1
    
    def spawn_boss(self):

        # Spawn the boss.
        if self.enemies_spawned == self.boss_spawn_threshold:

            # Reset the enemy counter and increase the threshold before the next boss.
            self.enemies_spawned = 0
            self.boss_spawn_threshold += self.boss_spawn_threshold
            return True
        
        # Don't spawn the boss.
        else:
            return False