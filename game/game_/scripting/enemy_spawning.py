import random
import math
from constants import *

from game_.scripting.action import Action
from game_.casting.enemy import Enemy
from game_.casting.point import Point
from game_.casting.boss import Boss
from game_.casting.explosion import Explosion

from game_.casting.body import Body
from game_.casting.image import Image
from game_.casting.sound import Sound

from game_.casting.animation import Animation

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
        self.kill_delay = 0


    def execute(self, cast, script, callback):
        self.enemy_amounts = math.floor(4 + self.difficulty_level)
        gunner = cast.get_first_actor(GUNNER_GROUP)
        enemys = cast.get_actors(ENEMEY_GROUP)
        gunner.set_diff(math.floor(self.difficulty_level))
        
        if len(enemys) == 0 and gunner.get_game_state() == False:
            self.spawn_enemy(self.enemy_amounts, cast)
        
        for enemy in enemys:
            enemy_body = enemy.get_body()
            gunner_body = gunner.get_body()
            enemy_point_val = enemy.get_points()
            
            enemy_position = enemy_body.get_position()
            enemy_y = enemy_position.get_y()
            enemy_x = enemy_position.get_x()
            
            
            if enemy_y > 800:
                cast.remove_actor(ENEMEY_GROUP, enemy)
                gunner.take_damage(5)
                  
            if(self._mouse_service.is_button_pressed("left")) or self.delay > 0:
                if(self._physics_service.has_collided(gunner_body, enemy_body)):
                    enemy_y = enemy_position.get_y()
                    enemy_x = enemy_position.get_x()
                    self._audio_service.play_sound(Sound(EXPLOSION))
                    #enemy.set_animation(Animation(EXPLOSION_ANIMATION))
                    #enemy_body.set_position(Point(enemy_x-40, enemy_y-80))
                    self.init_explosion((enemy_x-40), (enemy_y-80), cast)
                    cast.remove_actor(ENEMEY_GROUP, enemy)
                    gunner.add_points(enemy_point_val)
                    gunner.add_kill()
                    


    def init_explosion(self, x, y, cast):
        position = Point(x,y)
        size = Point(40,40)
        velocity = Point(0,0)
        body = Body(position, size, velocity)
        animation = Animation(EXPLOSION_ANIMATION)
        exp = Explosion(body, animation, False)
        cast.add_actor(EXPLOSION_GROUP, exp)


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
                
                animation = Animation(ENEMY_ANIMATIONS[random.randint(0,3)])
                
                enemy = Enemy(body, image, animation, False)
                cast.add_actor(ENEMEY_GROUP,enemy)

                self.enemies_spawned += 1
            self.increase_difficulty(.1)
            
            print(self.enemy_amounts)
            print(self.difficulty_level)
    
    def spawn_boss(self, cast):

        # Spawn the boss.
        if self.enemies_spawned >= self.boss_spawn_threshold * self.difficulty_level:
            x = random.randint(10, 1050)
            y = random.randint(-400, -50)
            position = Point(x,y)
            size = Point(40,40)
            velocity = Point(0,0)
            body = Body(position, size, velocity)
            image = Image(TEST_IMAGE)
            boss = Boss(body, image, False)
            cast.add_actor(BOSS_GROUP, boss)
        
        # Don't spawn the boss.
        else:
            return False

    def increase_difficulty(self, amount):
        self.difficulty_level += .1