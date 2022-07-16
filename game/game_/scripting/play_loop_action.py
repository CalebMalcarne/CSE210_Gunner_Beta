from constants import *
from game_.scripting.action import Action
from game_.casting.sound import Sound


class PlayLoopAction(Action):

    def __init__(self, audio_service, filename):
        self._audio_service = audio_service
        self._filename = filename
        self.timer = 10920
        
    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        game_over = gunner.get_game_state()
        sound = Sound(self._filename)
        sound.set_volume(.5)
        
        if game_over == True:
            self._audio_service.pause_sound(sound)
        
        if self.timer == 10920 and game_over == False:
            self._audio_service.play_sound(sound)
            self.timer = 0
        else:
            self.timer += 1
        #script.remove_action(OUTPUT, self)