from game_.casting.enemy import Enemy
from game_.services.raylib.raylib_video_service import RaylibVideoService
'''the class that will be responsible for spawning of the enemy.'''
class draw_enemy(Enemy):
   
   def __init__(self, enemy, debug = False):
    self._enemy = enemy
    self._debug = debug
     


    def _execute(self, cast, script, callback):
        self._video_service = RaylibVideoService()
        self._video_service.set_title("Enemy")
        self._video_service.set_width(640)
        self._video_service.set_height(480)
        self._video_service.health_bar(self._enemy.get_hitpoints())
        self._video_service.health_bar_size(self._enemy.get_size())
        self.points = self._enemy.get_points()

    

    





