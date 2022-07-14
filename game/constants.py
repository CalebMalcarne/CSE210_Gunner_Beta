import pathlib
from game_.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Gunner"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 680
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
TEST_IMAGE = "game/assets/images/blue.png"
GUNNER_HP_GROUP = "gunner_hp"
GUNNER_POINTS_GROUP = "gunner_points"
GUNNER_SOUND = "game/assets/sounds/Laser_Gun.MP3"

#BOSS
BOSS_GROUP = "boss"
TEST_IMAGE = "game/assets/images/blue.png"
BOSS_HP_GROUP = "boss_hp"
BOSS_SOUND = "game/assets/sounds/"

#enemys
ENEMEY_GROUP = "enemys"
ENEMEY_IMAGE = "game/assets/images"
ENEMY_SOUND = "game/assets/sounds/" 

