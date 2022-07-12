from constants import *
from game_.scripting.action import Action
from game_.scripting.DrawGunner import drawgunner
import time

SHOOT = (0,218,255,255)

class ControllGunner(Action):
    def __init__(self, mouse_service, video_service):
        self._mouse_service = mouse_service
        self._video_service = video_service
    
    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(TEST_GROUP)
        position = self._mouse_service.get_coordinates()
        body = gunner.get_body()
        self._mouse_service.hide_cursor()
        body.set_position(position)

        if(self._mouse_service.is_button_released("left")):
            gunner.shoot = 1
