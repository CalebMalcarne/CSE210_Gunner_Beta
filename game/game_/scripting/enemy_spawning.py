import random
import math
from constants import *

from game_.scripting.action import Action
from game_.casting.enemy import Enemy
from game_.casting.point import Point
from game_.casting.boss import Boss

from game_.casting.body import Body
from game_.casting.image import Image
from game_.casting.sound import Sound

class EnemySpawning(Action):

    def __init__(self, mouse_service, physics_service, audio_service):
        self._physics_service = physics_service
        self._mouse_service = mouse_service
        self._audio_service = audio_service
        
        self.delay = 0
        self.enemies_spawned = 0
        self.boss_spawn_threshold = 25
        self.difficulty_level = 0
        self.enemy_amounts = 0


    def execute(self, cast, script, callback):
        self.enemy_amounts = math.floor(5 + self.difficulty_level)
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
            
            if enemy_y > 800:
                cast.remove_actor(ENEMEY_GROUP, enemy)
                gunner.take_damage(5)
                  
            if(self._mouse_service.is_button_pressed("left")) or self.delay > 0:
                if(self._physics_service.has_collided(gunner_body, enemy_body)):
                    self._audio_service.play_sound(Sound(EXPLOSION))
                    cast.remove_actor(ENEMEY_GROUP, enemy)
                    gunner.add_points(enemy_point_val)
                    



    def spawn_enemy(self, amount_of_enemies, cast):
        # boss_check = spawn_boss(self)
        boss_check = False
        boss_present = False
        if boss_check == True and boss_present == False:
            boss_present = True
            # spawn boss command.
        elif boss_check == False and boss_present == False:
            for i in range(amount_of_enemies):
                x = random.randint(10, 1050)
                y = random.randint(-400, -50)
                position = Point(x, y)
                vx = 0
                vy = random.randint(3,6)
                velocity = Point(vx,vy)
                size = Point(40,40)
                body = Body(position, size, velocity)
                image = Image(TEST_IMAGE)
                enemy = Enemy(body, image, False)
                cast.add_actor(ENEMEY_GROUP,enemy)

                self.enemies_spawned += 1
            self.increase_difficulty(.1)
            print(self.enemy_amounts)
            print(self.difficulty_level)
    
    def spawn_boss(self):

        # Spawn the boss.
        if self.enemies_spawned >= self.boss_spawn_threshold * self.difficulty_level:
            return True
        
        # Don't spawn the boss.
        else:
            return False

    def increase_difficulty(self, amount):
        self.difficulty_level += .1