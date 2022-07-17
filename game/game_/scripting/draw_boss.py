import random

# from casting.boss import Boss // you use the cast.get_actors(GROUP) to do this
from game_.scripting.action import Action 
from game_.casting.boss import Boss
from constants import *
# draws the boss and everything to do with the boss 


class DrawBoss(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        # self.position_x = random.randint(0,SCREEN_WIDTH)
        # self.position_y = 0
        # self.velocity = 1


    def execute(self, cast, script, callback):
        boss_ = cast.get_actors(BOSS_GROUP)
        
        for boss in boss_:
            body = boss.get_body()
            position = body.get_position()

            image = boss.get_image()

            self._video_service.draw_image(image, position)