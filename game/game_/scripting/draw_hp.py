from constants import *
from game_.scripting.action import Action


class DrawHPAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        gunner_hp = cast.get_first_actor(GUNNER_HP_GROUP)
        text = gunner_hp.get_text()
        health = gunner.get_health()
        disp_health = f"HP:{health}"
        text.set_value(disp_health)
        position = gunner_hp.get_position()
        self._video_service.draw_text(text, position)