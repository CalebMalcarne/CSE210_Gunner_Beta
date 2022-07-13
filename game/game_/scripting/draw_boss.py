import random

from pyray import draw_rectangle
from casting.boss import Boss
from game.constants import SCREEN_WIDTH
#draws the boss and everything to do with the boss 


class DrawBoss():

    def draw_body(self):

        boss_width = 80
        boss_height = 70
        boss_x = Boss.get_x_location()
        boss_y = Boss.get_y_location()
        boss_color = Boss.boss_color()


        draw_rectangle(boss_x, boss_y, boss_width, boss_height)
