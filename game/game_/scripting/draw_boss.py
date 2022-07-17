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
        boss = cast.get_first_actor(BOSS_GROUP) 

        body = boss.get_body()
        position = body.get_position()
        image = boss.get_image()
        self._video_service.draw_image(image, position)
        # boss_width = 80
        # boss_height = 70
        # boss_x = self.get_x_location()
        # boss_y = self.get_y_location()
        # boss_color = Boss.boss_color()


        self._video_service.draw_image(image, position)

    def get_x_location(self):
        return self.position_x

    def get_y_location(self):
        return self.position_y