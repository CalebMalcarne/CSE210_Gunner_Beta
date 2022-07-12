from constants import *
from game_.scripting.end_drawing_action import EndDrawingAction
from game_.scripting.initialize_devices_action import InitializeDevicesAction
from game_.scripting.load_assets_action import LoadAssetsAction
from game_.scripting.release_devices_action import ReleaseDevicesAction
from game_.scripting.start_drawing_action import StartDrawingAction
from game_.scripting.unload_assets_action import UnloadAssetsAction
from game_.scripting.controll_gunner import ControllGunner

from game_.directing.director import Director
from game_.casting.cast import Cast
from game_.scripting.script import Script
from game_.casting.point import Point
from game_.services.raylib.raylib_audio_service import RaylibAudioService
from game_.services.raylib.raylib_video_service import RaylibVideoService
from game_.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game_.services.raylib.raylib_mouse_service import RaylibMouseService
from game_.casting.rectangle import Rectangle
from game_.casting.gunner import Gunner
from game_.casting.body import Body
from game_.casting.image import Image
from game_.scripting.DrawGunner import drawgunner

def testObjs(cast):
    x = SCREEN_WIDTH / 4
    y = SCREEN_HEIGHT / 4
    position = Point(x,y)
    size = Point(20,20)
    velocity = Point(0,0)
    body = Body(position, size, velocity)
    image = Image(TEST_IMAGE)
    test = Gunner(body, image, False)
    cast.add_actor(TEST_GROUP,test)   

def main():

    # create the services that we need
    audio_service = RaylibAudioService()
    video_service = RaylibVideoService()
    keyboard_service = RaylibKeyboardService()
    mouse_service = RaylibMouseService()
    # TODO: create any other services we need

    # create the cast and actors we need
    cast = Cast()
    testObjs(cast)

    
    # TODO: create any actors that we need
    # TODO: add the actors to tche cast in the appropriate group

    # create the script and actions we need
    script = Script()
    
    initialize_devices_action = InitializeDevicesAction(audio_service, video_service)
    load_assets_action = LoadAssetsAction(audio_service, video_service)
   
    # TODO: create any input phase actions
    # TODO: create any update phase actions
    controll_gunner = ControllGunner(mouse_service, video_service)

    start_drawing_action = StartDrawingAction(video_service)
    draw_test = drawgunner(video_service, mouse_service)
    # TODO: create any other output phase actions
    end_drawing_action = EndDrawingAction(video_service)
    unload_assets_action = UnloadAssetsAction(audio_service, video_service)
    release_devices_action = ReleaseDevicesAction(audio_service, video_service)
    
    script.add_action(INITIALIZE, initialize_devices_action)
    script.add_action(LOAD, load_assets_action)
    # TODO: add any input phase actions
    script.add_action(INPUT, controll_gunner)
    # TODO: add any update phase actions
    script.add_action(OUTPUT, start_drawing_action)
    script.add_action(OUTPUT, draw_test)
    # TODO: add any other output phase actions
    script.add_action(OUTPUT, end_drawing_action)
    script.add_action(UNLOAD, unload_assets_action)
    script.add_action(RELEASE, release_devices_action)

    # start the game
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()