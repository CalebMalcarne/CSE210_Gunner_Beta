import random
import math
from constants import *

from game_.scripting.action import Action
from game_.casting.enemy import Enemy
from game_.casting.point import Point
from game_.casting.boss import Boss
from game_.casting.explosion import Explosion
from game_.scripting.draw_explosion import DrawExplosion
from game_.casting.nuke_exp import NukeExp

from game_.casting.body import Body
from game_.casting.image import Image
from game_.casting.sound import Sound

from game_.casting.animation import Animation

from game_.scripting.script import Script


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
        self.minion_delay = 3

        self.boss_hp_bost = 0

        self.boss_check = True
        self.boss_present = False


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
                if enemy.get_boss_state():
                    gunner.take_damage(20)
                    self.boss_present = False
                else:
                    gunner.take_damage(5)
                  
            if(self._mouse_service.is_button_pressed("left")) or self.delay > 0:
                if(self._physics_service.has_collided(gunner_body, enemy_body)):
                    if enemy.get_boss_state() and enemy.get_boss_hp() > 0:
                        enemy.damage_boss(gunner.get_wepon_damage())
                        boss_y = enemy_position.get_y() + random.randint(0,100)
                        boss_x = enemy_position.get_x() + random.randint(0,100) 
                        self.init_explosion((boss_x), (boss_y), cast) 
                        self._audio_service.play_sound(Sound(EXPLOSION))
                        if self.minion_delay == 3:
                            self.spawn_boss_minions(cast, enemy_position)
                            self.minion_delay = 0
                        else:
                            self.minion_delay += 1

                    elif enemy.get_boss_hp() <= 0 and enemy.get_boss_state():
                        boss_y = enemy_position.get_y()
                        boss_x = enemy_position.get_x()    
                        self._audio_service.play_sound(Sound(NUKE_SOUND))   
                        self.init_Nuke_exp(cast, Point(boss_x - 150, boss_y - 150))  
                        cast.remove_actor(ENEMEY_GROUP, enemy)
                        gunner.add_points(10000)
                        gunner.add_kill()       
                        self.boss_present = False
                        self.boss_hp_bost += 20
                                 
                    else:
                        enemy_y = enemy_position.get_y()
                        enemy_x = enemy_position.get_x()
                        self._audio_service.play_sound(Sound(EXPLOSION))
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


    def spawn_boss_minions(self, cast, position):
        for i in range(4):
            boss_x = position.get_x()
            boss_y = position.get_y()
            position = Point(boss_x + random.randint(0,100),boss_y + random.randint(0,100))
            vx = 0
            vy = random.randint(3,5)
            velocity = Point(vx,vy)
            size = Point(40,40)
            body = Body(position, size, velocity)
            image = Image(TEST_IMAGE)
                
            animation = Animation(ENEMY_ANIMATIONS[random.randint(0,3)])
                
            enemy = Enemy(body, image, animation,0 , False, False)
            cast.add_actor(ENEMEY_GROUP,enemy)        

    def spawn_enemy(self, amount_of_enemies, cast):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        if self.boss_check == True and self.boss_present == False and gunner.get_kills() >= self.boss_spawn_threshold:
            self.boss_spawn_threshold += 100
            print(self.boss_spawn_threshold)
            self.spawn_boss(cast)
            self._audio_service.play_sound(Sound(MOTHERSHIP))
        elif self.boss_present == False:
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
                
                enemy = Enemy(body, image, animation, 0, False, False)
                cast.add_actor(ENEMEY_GROUP,enemy)

                self.enemies_spawned += 1
            self.increase_difficulty(.1)
            
    
    def spawn_boss(self, cast):

        x = random.randint(100, 800)
        y = -300
        position = Point(x, y)
        vx = 0
        vy = .5
        velocity = Point(vx,vy)
        size = Point(200,300)
        body = Body(position, size, velocity)
        image = Image(TEST_IMAGE)
                
        animation = Animation(ENEMY_ANIMATIONS[4])
                
        enemy = Enemy(body, image, animation, self.boss_hp_bost, True, False)
        cast.add_actor(ENEMEY_GROUP,enemy)
        self.boss_present = True

    def increase_difficulty(self, amount):
        self.difficulty_level += .1

    def init_Nuke_exp(self, cast, position):
        size = Point(40,40)
        velocity = Point(0,0)
        body = Body(position, size, velocity)
        animation = Animation(NUKE_EXP_ANIMATION)
        exp = NukeExp(body, animation, False)
        cast.add_actor(NUKE_EXP, exp)