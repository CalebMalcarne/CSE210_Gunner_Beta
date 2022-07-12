from constants import *
from game_.scripting.action import Action
from game_.scripting.DrawGunner import drawgunner


SHOOT = (0,218,255,255)

class ControllGunner(Action):
    def __init__(self, mouse_service, video_service, audio_service):
        self._mouse_service = mouse_service
        self._video_service = video_service
        self._audio_service = audio_service
        self.delay = 0
    
    def execute(self, cast, script, callback):
        fire_sound = GUNNER_SOUND
        gunner = cast.get_first_actor(GUNNER_GROUP)
        position = self._mouse_service.get_coordinates()
        body = gunner.get_body()
        self._mouse_service.hide_cursor()
        body.set_position(position)

        if(self._mouse_service.is_button_pressed("left")) or self.delay > 0:
            gunner.shoot = 1
            self.delay += 1
            if self.delay == 12:
                #self._audio_service.play_sound(fire_sound)
                self.delay = 0
                gunner.shoot = 0
