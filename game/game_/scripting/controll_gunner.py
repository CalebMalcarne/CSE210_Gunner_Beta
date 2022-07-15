from constants import *
from game_.scripting.action import Action
from game_.casting.sound import Sound
from game_.casting.text import Text
from game_.casting.point import Point
from game_.casting.label import Label


SHOOT = (0,218,255,255)

class ControllGunner(Action):
    def __init__(self, mouse_service, video_service, audio_service):
        self._mouse_service = mouse_service
        self._video_service = video_service
        self._audio_service = audio_service
        self.delay = 0
        self.warning_delay = 0
        
    
    def end_game(self, cast):
        gunner = cast.get_first_actor(GUNNER_GROUP)
        score = gunner.get_points()
        kills = gunner.get_kills()
        score = score + kills
        
        message = "GAME OVER"
        end = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        text_position = Point(570 , 200)
        label = Label(end, text_position)
        cast.add_actor(END_GAME_GROUP, label)
        
        message = f"Total Score:{score}"
        points = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        text_position = Point(580 , 300)
        label = Label(points, text_position)
        cast.add_actor(END_GAME_GROUP, label)
        
        message = f"Enemies Killed:{kills}"
        kill = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
        text_position = Point(590 , 400)
        label = Label(kill, text_position)
        cast.add_actor(END_GAME_GROUP, label)
    
    def execute(self, cast, script, callback):
        fire_sound = GUNNER_SOUND
        gunner = cast.get_first_actor(GUNNER_GROUP)
        position = self._mouse_service.get_coordinates()
        body = gunner.get_body()
        self._mouse_service.hide_cursor()
        body.set_position(position)
        gunner_hp = gunner.get_health()
        
        if(self._mouse_service.is_button_down("left")) and gunner.get_game_state() == False:
            self._audio_service.play_sound(Sound(LASER_SOUND))
        
        if gunner_hp > 20:
            self.warning_delay = 0
        else:
            if self.warning_delay > 300 and gunner.get_game_state() == False:
                self._audio_service.play_sound(Sound(GUNNER_WARNING))
                self.warning_delay  = 0
            else:
                self.warning_delay += 1
        
        if gunner.get_health() == 0:
            gunner.set_game_over()
            cast.clear_actors(ENEMEY_GROUP)
            self.end_game(cast)

        if(self._mouse_service.is_button_pressed("left")) or self.delay > 0:
            gunner.shoot = 1
            self.delay += 1
            if self.delay == 12:
                self.delay = 0
                gunner.shoot = 0
