from game_.casting.boss import Boss
from game_.scripting.draw_boss import DrawBoss

from constants import *
from game_.scripting.action import Action

#this deals with the movement of the boss
class ControlBoss(Action):

    def __init__(self):
        # self._position = DrawBoss.get_y_location(DrawBoss)
        # self.velocity = 1
        pass
        
    def execute(self, cast, script, callback):
        boss_ = cast.get_actors(BOSS_GROUP)
        for boss in boss_:
            body = boss.get_body()
            position = body.get_position()

            velocity = body.get_velocity()
            position = body.get_position()
            position = position.add(velocity)
            body.set_position(position)