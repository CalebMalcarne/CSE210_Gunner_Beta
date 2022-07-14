import random
from constants import *

from game_.scripting.action import Action
from game_.casting.enemy import Enemy
from game_.casting.point import Point

from game_.casting.body import Body
from game_.casting.image import Image

class EnemySpawning(Action):

    def __init__(self, mouse_service, physics_service):
        self._physics_service = physics_service
        self._mouse_service = mouse_service
        self.delay = 0
        self.enemies_spawned = 0
        self.boss_spawn_threshold = 25
        self.enemy_amounts = 5

    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        enemys = cast.get_actors(ENEMEY_GROUP)
        
        if len(enemys) == 0:
            self.spawn_enemy(self.enemy_amounts, cast)
        
        for enemy in enemys:
            enemy_body = enemy.get_body()
            gunner_body = gunner.get_body()
            enemy_point_val = enemy.get_points()
            
            enemy_position = enemy_body.get_position()
            enemy_y = enemy_position.get_y()
            
            if enemy_y > 480:
                cast.remove_actor(ENEMEY_GROUP, enemy)
                gunner.take_damage(5)
                  
            if(self._mouse_service.is_button_pressed("left")) or self.delay > 0:
                if(self._physics_service.has_collided(gunner_body, enemy_body)):
                    cast.remove_actor(ENEMEY_GROUP, enemy)
                    gunner.add_points(enemy_point_val)
                    



    def spawn_enemy(self, amount_of_enemies, cast):
        for i in range(amount_of_enemies):
            x = random.randint(50, 600)
            y = random.randint(-400, -50)
            position = Point(x, y)
            vx = 0
            vy = random.randint(2,4)
            velocity = Point(vx,vy)
            size = Point(40,40)
            body = Body(position, size, velocity)
            image = Image(TEST_IMAGE)
            enemy = Enemy(body, image, False)
            cast.add_actor(ENEMEY_GROUP,enemy)

            self.enemies_spawned += 1
        #self.enemy_amounts += 1
    
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
