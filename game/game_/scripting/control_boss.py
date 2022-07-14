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
        self._position += self.velocity