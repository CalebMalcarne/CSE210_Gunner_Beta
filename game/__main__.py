from constants import *
import random
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
from game_.casting.animation import Animation

from game_.services.raylib.raylib_audio_service import RaylibAudioService
from game_.services.raylib.raylib_video_service import RaylibVideoService
from game_.services.raylib.raylib_keyboard_service import RaylibKeyboardService
from game_.services.raylib.raylib_mouse_service import RaylibMouseService
from game_.services.raylib.raylib_physics_service import RaylibPhysicsService

from game_.casting.gunner import Gunner
from game_.scripting.DrawGunner import drawgunner
from game_.scripting.controll_gunner import ControllGunner
from game_.scripting.draw_stats import DrawStats

from game_.casting.boss import Boss
from game_.scripting.draw_boss import DrawBoss
from game_.scripting.control_boss import ControlBoss

from game_.casting.enemy import Enemy
from game_.scripting.control_enemy import ControlEnemy
from game_.scripting.draw_enemy import DrawEnemy
from game_.scripting.enemy_spawning import EnemySpawning

from game_.casting.stars_background import StarsBackground
from game_.scripting.draw_stars_action import DrawStars

from game_.scripting.upgrade_spawning import UpgradeSpawning
from game_.scripting.draw_upgrades import DrawUpgrades
from game_.scripting.control_upgrades import ControlUpgrades

from game_.casting.body import Body
from game_.casting.image import Image
from game_.casting.text import Text
from game_.casting.label import Label

startGame = 1

def init_Gunner(cast):
    x = SCREEN_WIDTH / 4
    y = SCREEN_HEIGHT / 4
    position = Point(x,y)
    size = Point(20,20)
    velocity = Point(0,0)
    body = Body(position, size, velocity)
    image = Image(GUNNER_TEST_IMAGE)
    gunner = Gunner(body, image, False)
    cast.add_actor(GUNNER_GROUP,gunner)

    message = 100
    hp = Text(message, FONT_FILE, FONT_SMALL, ALIGN_CENTER)
    text_position = Point(550, 740)
    label = Label(hp, text_position)
    cast.add_actor(GUNNER_HP_GROUP, label)
    
    message = 0
    points = Text(message, FONT_FILE, 20, ALIGN_CENTER)
    text_position = Point(590, 10)
    label = Label(points, text_position)
    cast.add_actor(GUNNER_POINTS_GROUP, label)
    

def init_Background(cast):
    x = 0
    y = 0
    position = Point(x,y)
    size = Point(40,40)
    velocity = Point(0,0)
    body = Body(position, size, velocity)
    animation = Animation(STAR_ANIMATION)
    stars = StarsBackground(body, animation, False)
    cast.add_actor(STAR_GROUP, stars)

def init_Boss(cast):
    x = SCREEN_WIDTH / 4
    y = SCREEN_HEIGHT / 4
    position = Point(x,y)
    size = Point(40,40)
    velocity = Point(0,0)
    body = Body(position, size, velocity)
    image = Image(TEST_IMAGE)
    boss = Boss(body, image, False)
    cast.add_actor(BOSS_GROUP, boss)

def init_enemys(cast):
    for i in range(5):
        x = random.randint(10, 1050)
        y = random.randint(-400, -50)
        position = Point(x, y)
        vx = 0
        vy = random.randint(2,4)
        velocity = Point(vx,vy)
        size = Point(40,40)
        body = Body(position, size, velocity)
        image = Image(TEST_IMAGE)
        enemy = Enemy(body, image, False)
        cast.add_actor(ENEMEY_GROUP,enemy)

def main():

    # create the services that we need
    audio_service = RaylibAudioService()
    video_service = RaylibVideoService()
    keyboard_service = RaylibKeyboardService()
    mouse_service = RaylibMouseService()
    audio_service = RaylibAudioService()
    physics_service = RaylibPhysicsService()
    # TODO: create any other services we need

    # create the cast and actors we need
    cast = Cast()
    init_Gunner(cast)
    init_enemys(cast)
    init_Background(cast)
    
    # TODO: create any actors that we need
    # TODO: add the actors to tche cast in the appropriate group

    # create the script and actions we need
    script = Script()
    
    initialize_devices_action = InitializeDevicesAction(audio_service, video_service)
    load_assets_action = LoadAssetsAction(audio_service, video_service)
   
    # TODO: create any input phase actions
    # TODO: create any update phase actions
    controll_gunner = ControllGunner(mouse_service, video_service, audio_service)
    draw_gunner = drawgunner(video_service, mouse_service)

    control_enemy = ControlEnemy()
    draw_enemy = DrawEnemy(video_service)
    enemy_spawning = EnemySpawning(mouse_service, physics_service, audio_service)
    
    control_upgrades = ControlUpgrades()
    draw_upgrades = DrawUpgrades(video_service)
    upgrade_spawning = UpgradeSpawning(mouse_service, physics_service, audio_service, keyboard_service)
    
    control_boss = ControlBoss()
    draw_boss = DrawBoss(video_service)
    
    # TODO: create any other output phase actions
    start_drawing_action = StartDrawingAction(video_service)
    end_drawing_action = EndDrawingAction(video_service)
    unload_assets_action = UnloadAssetsAction(audio_service, video_service)
    release_devices_action = ReleaseDevicesAction(audio_service, video_service)
    draw_stats = DrawStats(video_service)
    draw_stars = DrawStars(video_service)
    

    if startGame == 1:
        script.add_action(INITIALIZE, initialize_devices_action)
        script.add_action(LOAD, load_assets_action)
        # TODO: add any input phase actions
        script.add_action(INPUT, controll_gunner)
        script.add_action(INPUT, control_enemy)
        script.add_action(INPUT, control_upgrades)
        # TODO: add any update phase actions
        script.add_action(OUTPUT, draw_stars)
        script.add_action(OUTPUT, draw_enemy)
        script.add_action(OUTPUT, draw_upgrades)
        script.add_action(OUTPUT, start_drawing_action)
        script.add_action(OUTPUT, draw_gunner)
        script.add_action(OUTPUT, draw_stats)
        script.add_action(OUTPUT, enemy_spawning)
        script.add_action(OUTPUT, upgrade_spawning)
        # TODO: add any other output phase actions
        script.add_action(OUTPUT, end_drawing_action)
        script.add_action(UNLOAD, unload_assets_action)
        script.add_action(RELEASE, release_devices_action)

    # start the game
    director = Director(video_service)
    director.start_game(cast, script)

if __name__ == "__main__":
    main()