from constants import *
from game_.scripting.action import Action
from game_.casting.sound import Sound
from game_.casting.nuke_exp import NukeExp
from game_.casting.point import Point
from game_.casting.body import Body
from game_.casting.animation import Animation



class ControlUpgrades(Action):
    def __init__(self, mouse_service, audio_service):
        self._mouse_service = mouse_service
        self._audio_service = audio_service
        
    def init_Nuke_exp(self, cast):
        position = Point(230,100)
        size = Point(40,40)
        velocity = Point(0,0)
        body = Body(position, size, velocity)
        animation = Animation(NUKE_EXP_ANIMATION)
        exp = NukeExp(body, animation, False)
        cast.add_actor(NUKE_EXP, exp)
        
            
            


    def execute(self,cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        healing_packs = cast.get_actors(HEALING_GROUP)
        nukes = cast.get_actors(NUKE_GROUP)
        for healing_pack in healing_packs:
            body = healing_pack.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            body.set_position(position)
            
            
        for nuke in nukes:
            body = nuke.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            body.set_position(position)
            
        if gunner.get_nukes() > 0:
            enemys = cast.get_actors(ENEMEY_GROUP)
            gunner = cast.get_first_actor(GUNNER_GROUP)
            if(self._mouse_service.is_button_pressed("right")):
                gunner.remove_nuke()
                for enemy in enemys:
                    gunner.add_points(enemy.get_points())
                    gunner.add_kill()
                cast.clear_actors(ENEMEY_GROUP)
                self._audio_service.play_sound(Sound(NUKE_SOUND))
                self.init_Nuke_exp(cast)
                