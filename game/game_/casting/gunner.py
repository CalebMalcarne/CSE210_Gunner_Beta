from game_.casting.actor import Actor
from game_.casting.point import Point


class Gunner(Actor):

    def __init__(self, body, image, debug = False):

        self.shoot = 0
        self._health = 100
        self._wepon_damage = 5
        self._enemys_killed = 0
        self._points = 0
        self._diff_lvl = 0

        super().__init__(debug)
        self._body = body
        self._image = image

    def take_damage(self, damage):
        self._health -= damage

    def heal(self, health):
        self._health += health

    def add_wepon_damage(self, damage):
        self._wepon_damage += damage
    
    def add_kill(self, kill):
        self._enemys_killed += kill

    def add_points(self, points):
        self._points += points
    
    #-----------------------------------#
    def set_health(self, health):
        self.health = health

    def set_wepon_damage(self, damage):
        self._wepon_damage = damage

    def set_kills(self, kills):
        self._enemys_killed = kills

    def set_points(self, points):
        self._points = points
    
    def set_diff(self, lvl):
        self._diff_lvl = lvl

    #-----------------------------------#
    def get_diff(self):
        return self._diff_lvl
    
    def get_killed(self):
        return self._enemys_killed

    def get_health(self):
        return self._health

    def get_points(self):
        return self._points
    
    def get_wepon_damage(self):
        return self._wepon_damage

    def get_body(self):
        return self._body

    def get_image(self):
        return self._image
        
