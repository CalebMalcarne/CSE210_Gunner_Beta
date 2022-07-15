from constants import *
from game_.scripting.action import Action



class ControlUpgrades(Action):
    def __init__(self):
        #self._video_service = video_service
        #self._audio_service = audio_service
        pass

    def execute(self,cast, script, callback):
        healing_packs = cast.get_actors(HEALING_GROUP)
        for healing_pack in healing_packs:
            body = healing_pack.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            body.set_position(position)