import random
import math
from constants import *

from game_.scripting.action import Action
from game_.casting.healing_pack import HealingPack
from game_.casting.point import Point
from game_.casting.boss import Boss

from game_.casting.body import Body
from game_.casting.image import Image
from game_.casting.sound import Sound

class UpgradeSpawning(Action):
    
    def approx(self, pos1, pos2):
        pos1_x = pos1.get_x()
        pos1_y = pos1.get_y()

        pos2_x = pos2.get_x()
        pos2_y = pos2.get_y()
        
        x_dist = abs((pos1_x - pos2_x))
        y_dist = abs((pos1_y - pos2_y))
        
        print(x_dist, ' ', y_dist)
        
        if x_dist <= 45 and y_dist <= 45:
            return True
        
        
    def __init__(self, mouse_service, physics_service, audio_service, keyboard_service):
        self._physics_service = physics_service
        self._mouse_service = mouse_service
        self._audio_service = audio_service
        self._keyboard_service = keyboard_service
        
        self.delay = 0


    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        enemys = cast.get_actors(ENEMEY_GROUP)
        healing_packs = cast.get_actors(HEALING_GROUP)
        difficulty = gunner.get_diff()
        
        if self.delay == 1000 - difficulty * 15 and gunner.get_game_state() == False:
            self.spawn_health_pack(cast, difficulty * 5)
            self.delay = 0;
        else:
            self.delay += 1
            
        for healing_pack in healing_packs:
            healing_body = healing_pack.get_body()
            gunner_body = gunner.get_body()
            healing_val = healing_pack.get_health_gain()
            
            healing_position = healing_body.get_position()
            gunner_position = gunner_body.get_position()
                  
            if(self._mouse_service.is_button_pressed("left")):
                if(self._physics_service.has_collided(gunner_body, healing_body)):
                    self._audio_service.play_sound(Sound(HEALING_SOUND))
                    cast.remove_actor(HEALING_GROUP, healing_pack)
                    gunner.heal(healing_val)
        
                    
    def spawn_health_pack(self, cast, difficulty):
        random_pick = random.randint(0,1)
        x_vals = [-100,1100]
        x = x_vals[random_pick]
        y = random.randint(150,1000)
        position = Point(x,y)
        if random_pick == 1:
            vx = (random.randint(1,2) * -1)
        else:
            vx = random.randint(1,2) 
        vy = (random.randint(0,3) * -1)
        velocity = Point(vx, vy)
        size = Point(40,40)
        body = Body(position, size, velocity)
        image = Image(HEALING_IMAGE)
        healing = HealingPack(body, image, False)
        healing.set_health_gain(10+difficulty)
        cast.add_actor(HEALING_GROUP, healing)
    
    def spawn_nuke(cast):
        pass
        