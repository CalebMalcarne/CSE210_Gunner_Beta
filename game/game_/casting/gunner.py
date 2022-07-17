from game_.casting.actor import Actor
from game_.casting.point import Point


class Gunner(Actor):

    def __init__(self, body, image, debug = False):
        
        self._game_over = False

        self.shoot = 0
        self._health = 100
        self._wepon_damage = 5
        self._enemys_killed = 0
        self._points = 0
        self._diff_lvl = 0
        self._nukes = 0

        super().__init__(debug)
        self._body = body
        self._image = image

    def take_damage(self, damage):
        self._health -= damage

    def heal(self, health):
        self._health += health

    def add_wepon_damage(self, damage):
        self._wepon_damage += damage
    
    def add_kill(self):
        self._enemys_killed += 1

    def add_points(self, points):
        self._points += points
        
    def add_nuke(self):
        self._nukes += 1
        
    def remove_nuke(self):
        self._nukes = self._nukes - 1
    
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
        
    def set_game_over(self):
        self._game_over = True
        
    def set_nukes(self, nukes):
        self._nukes = nukes

    #-----------------------------------#
    def get_nukes(self):
        return self._nukes
    
    def get_diff(self):
        return self._diff_lvl
    
    def get_kills(self):
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
    
    def get_game_state(self):
        return self._game_over
        
