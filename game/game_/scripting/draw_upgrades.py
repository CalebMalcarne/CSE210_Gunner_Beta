from constants import *
from game_.scripting.action import Action



class DrawUpgrades(Action):
    def __init__(self, video_service):
        self._video_service = video_service
        
    def draw_Healing(self, cast):
        healing_packs = cast.get_actors(HEALING_GROUP)
        
        for healing_pack in healing_packs:
            body = healing_pack.get_body()
            position = body.get_position()

            image = healing_pack.get_image()

            self._video_service.draw_image(image, position)
            
    def draw_Nuke(self, cast):
        nukes = cast.get_actors(NUKE_GROUP)      
        for nuke in nukes:
            body = nuke.get_body()
            position = body.get_position()

            animation = nuke.get_animation()
            image = animation.next_image()
            position = body.get_position()
            self._video_service.draw_image(image, position)
            
    def draw_Nuke_explosion(self, cast):
        pass
            
    def execute(self,cast, script, callback):
        self.draw_Healing(cast)
        self.draw_Nuke(cast)
            