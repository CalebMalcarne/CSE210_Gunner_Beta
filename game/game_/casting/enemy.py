import random
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point
from game.services.raylib.mouse_service import MouseService

class Enemy(Actor, point):

    ''' class for the enemy/ asteroids of the game gunner
    some attributes inherited from the actor and point classes 
    difficulty will climb as the game continues
    enemy will be affected by the actor at the mouse click
    animation will happen at the mouse click at the same location of the enemy. 
    
    
    ''' 
    def __init__(self):
        self.color = color(255,255,255)
        self.size = ,20
        self.position = random.randint
        self.velocity = #velocity will be set here and returned later in the class
        self.difficulty = #difficulty will be set here and returned later 


    def get_position(self):
        '''gets position for the enemies, will be randomized'''
        return position

    def get_velocity (self):
        '''velocity of the enemies at which they move on the screen'''
        return velocity

    def get_size(self):
        ''' for the size of the enemies'''
        return size
