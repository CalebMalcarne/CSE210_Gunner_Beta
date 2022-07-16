import pathlib
from game_.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Gunner"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 800
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "game/assets/fonts/pixel.ttf"
FONT_SMALL = 25
FONT_LARGE = 30

# SOUND
LASER_SOUND = "game/assets/sounds/laser2.mp3"
EXPLOSION = "game/assets/sounds/explosion1.mp3"
END_SONG = "game/assets/sounds/Game_over_music.wav"
END_VOICE = "game/assets/sounds/Game_over_voice.wav"
#BACKGROUND = "game/assets/sounds/background.mp3"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0, 0)
WHITE = Color(255, 255, 255, 255)
PURPLE = Color(255, 0, 255, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space"
ENTER = "enter"
PAUSE = "p"

# LEVELS
LEVEL_FILE = "batter/assets/data/level-{:03}.txt"
BASE_LEVELS = 5

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GUNNER
GUNNER_GROUP = "gunner_group"
GUNNER_TEST_IMAGE = "game/assets/images/blue.png"
GUNNER_HP_GROUP = "gunner_hp"
GUNNER_POINTS_GROUP = "gunner_points"
GUNNER_NUKE_GROUP = "gunner_nukes"
GUNNER_SOUND = "game/assets/sounds/Laser_Gun.MP3"
GUNNER_WARNING = "game/assets/sounds/LowHP.wav"

#BOSS
BOSS_GROUP = "boss"
TEST_IMAGE = "game/assets/images/Turtle.png"
BOSS_HP_GROUP = "boss_hp"
BOSS_SOUND = "game/assets/sounds/"

#ENEMYS
ENEMEY_GROUP = "enemys"
ENEMEY_IMAGE = "game/assets/images"
ENEMY_SOUND = "game/assets/sounds/" 
ENEMY_ANIMATIONS = [[f"game/assets/images/Ship1/Dove{n}.png" for n in range(1,5)], 
                    [f"game/assets/images/Ship2/Ligher{n}.png" for n in range(1,5)],
                    [f"game/assets/images/Ship3/Lightning{n}.png" for n in range(1,5)],
                    ["game/assets/images/Turtle.png"]]
EXPLOSION_ANIMATION = [f"game/assets/images/Explosion/explotion{n}.png" for n in range(0,19)]
EXPLOSION_GROUP = "explosion"

#UPGRADES
HEALING_GROUP = "healing"
HEALING_IMAGE = "game/assets/images/healing.png"
HEALING_SOUND = "game/assets/sounds/powerUp.wav"
NUKE_ANIMATION = [f"game/assets/images/nuke/frame_{n}_delay-0.07s.gif" for n in range(0,31)]
NUKE_EXP_ANIMATION = [f"game/assets/images/nuke_exp/frame_{n}_delay-0.1s.gif" for n in range(0,7)]
NUKE_IMAGE = "game/assets/images/nuke/frame_1_delay-0.07s.gif"
NUKE_GROUP = "nukes"
NUKE_SOUND = "game/assets/sounds/nuke.wav"
NUKE_EXP = "nuke_exp"

#BACKGROUND
STAR_GROUP = "stars"
STAR_ANIMATION = [f"game/assets/images/stars/Stars{n}.png" for n in range(1,7)]
END_GAME_GROUP = "end"
MAIN_LOOP = "game/assets/sounds/Loop.mp3"


