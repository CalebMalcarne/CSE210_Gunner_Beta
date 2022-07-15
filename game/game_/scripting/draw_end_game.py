from constants import *
from game_.scripting.action import Action


class DrawEndGame(Action):

    def __init__(self, video_service):
        self._video_service = video_service

        
    def execute(self, cast, script, callback):
        end_game = cast.get_actors(END_GAME_GROUP)
        gunner = cast.get_first_actor(GUNNER_GROUP)
        
        for stat in end_game:
            text = stat.get_text()
            position = stat.get_position()
            self._video_service.draw_text(text, position)