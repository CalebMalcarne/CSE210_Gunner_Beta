from constants import *
from game_.scripting.action import Action

class Respawn_Enemy(Action):

    def __init__(self, body, image):
        super().__init__(body, image, False)