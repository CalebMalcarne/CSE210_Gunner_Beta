from game_.casting.actor import Actor
from game_.casting.point import Point


class NukeExp(Actor):

    def __init__(self, body, animation, debug = False):

        self.shoot = 0

        super().__init__(debug)
        self._body = body
        self._animation = animation

    
    #-----------------------------------#

    def get_body(self):
        return self._body

    def get_animation(self):
        return self._animation