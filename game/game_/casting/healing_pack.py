from game_.casting.actor import Actor
from game_.casting.point import Point


class HealingPack(Actor):

    def __init__(self, body, image, debug = False):

        self.shoot = 0
        self._health_gain = 10

        super().__init__(debug)
        self._body = body
        self._image = image

    
    #-----------------------------------#
    def set_health_gain(self, health):
        self._health_gain = health


    #-----------------------------------#
    def get_health_gain(self):
        return self._health_gain
    
    def get_body(self):
        return self._body

    def get_image(self):
        return self._image