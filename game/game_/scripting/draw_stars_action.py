from constants import *
from game_.scripting.action import Action

class DrawStars(Action):
    def __init__(self, video_service):
        self.video_service = video_service

    def execute(self, cast, script, callback):
        stars = cast.get_first_actor(STAR_GROUP)