from constants import *
from game_.scripting.action import Action

class DrawStars(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def execute(self, cast, script, callback):
        stars = cast.get_first_actor(STAR_GROUP)
        body = stars.get_body()
        
        animation = stars.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)