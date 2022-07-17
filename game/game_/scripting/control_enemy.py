from constants import *
from game_.scripting.action import Action
from game_.casting.point import Point



class ControlEnemy(Action):
    def __init__(self):
        #self._video_service = video_service
        #self._audio_service = audio_service
        pass

    def execute(self,cast, script, callback):
        enemys = cast.get_actors(ENEMEY_GROUP)
        for enemy in enemys:
            body = enemy.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            body.set_position(position)
