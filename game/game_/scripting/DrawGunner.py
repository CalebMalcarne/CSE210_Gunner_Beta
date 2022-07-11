from game_.scripting.action import Action
from game_.casting.color import Color
from game_.casting.rectangle import Rectangle
from constants import *

TEST_GROUP = "test"
BLUE = 0

class drawgunner(Action):
    def __init__(self, video_service):
        self._video_service = video_service

    def draw_Lines(self, C, body):
        position = body.get_position()
        line_start_x = position.get_x()
        line_start_y = position.get_y()

        line_end_x_a = 640
        line_end_y_a = 480
        line_end_x_b = 0
        self._video_service.draw_line(line_start_x, line_start_y, line_end_x_a, line_end_y_a, C, C)
        self._video_service.draw_line(line_start_x, line_start_y, line_end_x_b, line_end_y_a, C, C)


    def execute(self, cast, script, callback):
        testobj = cast.get_first_actor(TEST_GROUP)
        body = testobj.get_body()

        if  testobj.is_debug():
            rectangle = Rectangle(body.get_position(), body.get_size())
            self._video_service.draw_rectangle(rectangle, Color(255,255,255,255))
        
        image =  testobj.get_image()
        position = body.get_position()
        self.draw_Lines((255,255,255,255), body)
        #self._video_service.draw_image(image, position)
            