from constants import *
from game_.scripting.action import Action


class DrawHPAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        gunner_hp = cast.get_first_actor(GUNNER_HP_GROUP)
        text = gunner_hp.get_text()
        position = gunner_hp.get_position()
        self._video_service.draw_text(text, position)