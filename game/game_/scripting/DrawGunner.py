import time
from game_.scripting.action import Action
from game_.casting.color import Color
from game_.casting.rectangle import Rectangle
from constants import *

TEST_GROUP = "test"
SHOOT = (0,218,255,255)
WHITE = (255,255,255,255)

class drawgunner(Action):
    def __init__(self, video_service, mouse_service):
        self._mouse_service = mouse_service
        self._video_service = video_service
        self._line_color = WHITE
    

    def draw_Lines(self, C, body):
        position = body.get_position()
        line_start_x = position.get_x()
        line_start_y = position.get_y()

        line_end_x_a = 640
        line_end_y_a = 480
        line_end_x_b = 0
        self._video_service.draw_line(line_start_x, line_start_y, line_end_x_a, line_end_y_a, C, C)
        self._video_service.draw_line(line_start_x, line_start_y, line_end_x_b, line_end_y_a, C, C)
    
    def set_Line_Color(self, line_color):
        self._line_color = line_color

    def execute(self, cast, script, callback):
        gunner = cast.get_first_actor(GUNNER_GROUP)

        body = gunner.get_body()

        if  gunner.is_debug():
            rectangle = Rectangle(body.get_position(), body.get_size())
            self._video_service.draw_rectangle(rectangle, Color(255,255,255,255))
        
        if gunner.shoot == 1:
            self.set_Line_Color(SHOOT)
        else:
            self.set_Line_Color(WHITE)

        
        image =  gunner.get_image()
        position = body.get_position()
        self.draw_Lines(self._line_color, body)
        
        #self._video_service.draw_image(image, position)

            