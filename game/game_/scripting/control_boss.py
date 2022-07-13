from game_.casting.boss import Boss

#this deals with the movement of the boss
class ControlBoss():

    def __init__(self):
        self._position = Boss.get_y_location()
        self.velocity = 1
        
    def execute(self, cast, script, callback):
        self._position += self.velocity
