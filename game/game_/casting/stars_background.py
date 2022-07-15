import random
from constants import *
from game_.casting.actor import Actor
from game_.casting.point import Point

class StarsBackground(Actor):
    def __init__(self, body, animation, debug = False):        
        super().__init__(debug)
        self._body = body
        self._animation = animation

    def get_animation(self):
        return self._animation

    def get_body(self):
        return self._body
