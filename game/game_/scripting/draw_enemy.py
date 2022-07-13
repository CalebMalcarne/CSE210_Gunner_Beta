from game_.scripting.action import Action
from game_.casting.color import Color
from game_.casting.rectangle import Rectangle
from constants import *
'''the class that will be responsible for spawning of the enemy.'''
class draw_enemy(Action):

   
   def __init__(self, video_service, mouse_service):
    self._mouse_service = mouse_service
    self._video_service = video_service
     


    def execute(self, cast, script, callback):
        enemys = cast.get_actors(ENEMEY_GROUP)

        for enemy in enemys:
            body = enemy.get_body()
            position = body.get_position()

            image = enemy.get_image()

            self._video_service.draw_image(image, position)


            #self._video_service.health_bar(self._enemy.get_hitpoints())
            #self._video_service.health_bar_size(self._enemy.get_size())
            self.points = self._enemy.get_points()

    

    





