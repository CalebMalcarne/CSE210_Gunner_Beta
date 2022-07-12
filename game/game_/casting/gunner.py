from game_.casting.actor import Actor
from game_.casting.point import Point


class Gunner(Actor):

    def __init__(self, body, image, debug = False):

        self.shoot = 0

        super().__init__(debug)
        self._body = body
        self._image = image

    def get_body(self):
        return self._body

    def get_image(self):
        return self._image
        
