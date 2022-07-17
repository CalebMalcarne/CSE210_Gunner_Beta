from constants import *
from game_.scripting.action import Action

class DrawNukeExp(Action):
    def __init__(self, video_service):
        self._video_service = video_service
        self.kill_delay = 0

    def execute(self, cast, script, callback):
        explosion = cast.get_actors(NUKE_EXP)
        
        for exp in explosion:
            body = exp.get_body()
            animation = exp.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
            self.kill_delay += 1
            if self.kill_delay == 30:
                cast.remove_actor(NUKE_EXP, exp)
                self.kill_delay = 0