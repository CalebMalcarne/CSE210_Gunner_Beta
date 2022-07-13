<<<<<<< HEAD
from casting.boss import Boss
=======
from game_.casting.boss import Boss
#this deals with the movement of the boss, the volicity
>>>>>>> 8f0c2894f85075be6f0fe9e8a25b6dfe0627e601

#this deals with the movement of the boss
class ControlBoss():

    def __init__(self):
        self._position = Boss.get_y_location()
        self.velocity = 1
        
    def execute(self, cast, script, callback):
        self._position += self.velocity

