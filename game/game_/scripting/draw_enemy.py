from constants import *
from game_.scripting.action import Action



class DrawEnemy(Action):
    def __init__(self, video_service):
        self._video_service = video_service
        #self._audio_service = audio_service
        pass

    def execute(self, cast, script, callback):
        enemys = cast.get_actors(ENEMEY_GROUP)
        for enemy in enemys:
            body = enemy.get_body()
            position = body.get_position()

            image = enemy.get_image()

            animation = enemy.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)


    

    





