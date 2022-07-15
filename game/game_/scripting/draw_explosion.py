from constants import *
from game_.scripting.action import Action

class DrawExplosion(Action):
    def __init__(self, video_service):
        self._video_service = video_service
        self.kill_delay = 0

    def execute(self, cast, script, callback):
        explosion = cast.get_actors(EXPLOSION_GROUP)
        
        for exp in explosion:
            body = exp.get_body()
            animation = exp.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
            exp.kill(cast, exp)
            self.kill_delay += 1
            if self.kill_delay == 30:
                cast.remove_actor(EXPLOSION_GROUP, exp)
                self.kill_delay = 0