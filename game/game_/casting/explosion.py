import random
import time
from constants import *
from game_.casting.actor import Actor
from game_.casting.point import Point

class Explosion(Actor):
    def __init__(self, body, animation, debug = False):        
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self.done = 0
        self.kill_delay = 0

    def get_animation(self):
        return self._animation

    def get_body(self):
        return self._body
    
    def set_done(self):
        self.done = 1
        
    def get_state(self):
        return self.done
    
    def kill(self, cast, exp):
        if self.kill_delay == 20:
            cast.remove_actor(EXPLOSION_GROUP, exp)
            self.kill_delay = 0
