import random
from constants import *
from game_.casting.actor import Actor
from game_.casting.point import Point
# from game_.services.raylib.mouse_service import MouseService
class Enemy(Actor):

    ''' class for the enemy/ asteroids of the game gunner
    some attributes inherited from the actor and point classes 
    difficulty will climb as the game continues
    enemy will be affected by the actor at the mouse click
    animation will happen at the mouse click at the same location of the enemy. 
    ''' 
    # def __init__(self):
    #     # self.color = color(255,255,255)
    #     # self.size = ,20
    #     # self.position = random.randint
    #     # self.velocity = #velocity will be set here and returned later in the class
    #     self.difficulty = #difficulty will be set here and returned later 
    #     self.points = #points will be set here and returned later
    #     self.hitpoints = 50
    '''pay no attention to the code above this line, that was written during class'''

    def __init__(self, body, image, animation, debug = False):

        super().__init__(debug)
        self._body = body
        self.size = random.randint(20,50)
        self._image = image
        self._point_value = 50
        self.hitpoints = random.randint(50,100)
        self.dead = 0
        self._animation = animation
        #self.color = self.get_color(self.hitpoints)
        
    def set_animation(self, new_animation):
        self._animation = new_animation
        
    def get_death_state(self):
        return self.dead
    
    def get_points(self):
        return self._point_value
    
    def set_points(self, points):
        self._point_value = points
    
    def get_body(self):
        return self._body

    def get_image(self):
        return self._image

    def get_size(self):
        ''' for the size of the enemies'''
        return self.size
    def get_animation(self):
        return self._animation

    def set_hitpoints(self):
        ''' for the hitpoints of the enemies(this will be the difficulty), this will be used to determine the color of the enemy
        random number will be generated for the hitpoints of the enemies'''
        
        return self.hitpoints

''' if the enemy is hit by the gunner, the hitpoints will be reduced by the gunner's damage

get in the director mindset'''
    