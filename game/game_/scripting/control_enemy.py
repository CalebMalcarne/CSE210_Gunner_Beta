from constants import *
from game_.scripting.action import Action
from game_.scripting.DrawGunner import drawgunner


SHOOT = (0,218,255,255)

class ControlEnemy(Action):
    def __init__(self, video_service, audio_service):
        self._video_service = video_service
        self._audio_service = audio_service