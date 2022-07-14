from constants import *
from game_.scripting.action import Action


class DrawStats(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def draw_HP(self, cast):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        gunner_hp = cast.get_first_actor(GUNNER_HP_GROUP)
        text = gunner_hp.get_text()
        health = gunner.get_health()
        disp_health = f"HP:{health}"
        text.set_value(disp_health)
        position = gunner_hp.get_position()
        self._video_service.draw_text(text, position)
        
    def draw_Points(self, cast):   
        gunner = cast.get_first_actor(GUNNER_GROUP)
        gunner_points = cast.get_first_actor(GUNNER_POINTS_GROUP)
        text = gunner_points.get_text()
        points = gunner.get_points()
        disp_points = f"Points:{points}"
        text.set_value(disp_points)
        position = gunner_points.get_position()
        self._video_service.draw_text(text, position)
        
    def execute(self, cast, script, callback):
        self.draw_HP(cast)