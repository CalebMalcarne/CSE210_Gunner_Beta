from game_.casting.actor import Actor
from game_.casting.point import Point


class Gunner(Actor):

    def __init__(self, body, image, debug = False):

        self.shoot = 0
        self._health = 100
        self._wepon_damage = 5

        super().__init__(debug)
        self._body = body
        self._image = image

    def take_damage(self, damage):
        self._health -= damage

    def heal(self, health):
        self._health += health

    def add_wepon_damage(self, damage):
        self._wepon_damage += damage
    
    #-----------------------------------#
    def set_health(self, health):
        self.health = health

    def set_wepon_damage(self, damage):
        self._wepon_damage = damage

    #-----------------------------------#
    def get_health(self):
        return self._health
    
    def get_wepon_damage(self):
        return self._wepon_damage

    def get_body(self):
        return self._body

    def get_image(self):
        return self._image
        
