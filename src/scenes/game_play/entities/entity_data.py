import pygame

# === Direction Vector Constants ===
DIRECTION_UP = pygame.Vector2(0, -1)
DIRECTION_DOWN = pygame.Vector2(0, 1)
DIRECTION_LEFT = pygame.Vector2(-1, 0)
DIRECTION_RIGHT = pygame.Vector2(1, 0)
DIRECTION_UP_LEFT = pygame.Vector2(-1, -1).normalize()
DIRECTION_UP_RIGHT = pygame.Vector2(1, -1).normalize()
DIRECTION_DOWN_LEFT = pygame.Vector2(-1, 1).normalize()
DIRECTION_DOWN_RIGHT = pygame.Vector2(1, 1).normalize()

# === Entity Constants ===
HIT_TIMER = 0.1

# === Player Constants ===
PLAYER_RADIUS = 48
PLAYER_ACCELERATION = 600
PLAYER_SPEED = 350
PLAYER_LIVES = 3
PLAYER_SHIELD = 100
PLAYER_INVINCIBLE_TIME = 2
PLAYER_SHOOT_TIMER = 0.2
PLAYER_BOMB_AMMO = 3
PLAYER_BOMB_TIMER = 2.0
PLAYER_POWER_LEVEL = 1
PLAYER_BLAST_RADIUS = 128
PLAYER_IMG_PATH = "assets/player_spaceship.png"

# === Asteroid Constants ===
ASTEROID_SM_RADIUS = 16
ASTEROID_SM_SPEED = 120
ASTEROID_SM_HP = 2
ASTEROID_SM_IMG = "assets/asteroid_sm.png"

ASTEROID_MD_RADIUS = 32
ASTEROID_MD_SPEED = 100
ASTEROID_MD_HP = 4
ASTEROID_MD_IMG = "assets/asteroid_md.png"

ASTEROID_LG_RADIUS = 64
ASTEROID_LG_SPEED = 80
ASTEROID_LG_HP = 6
ASTEROID_LG_IMG = "assets/asteroid_lg.png"

ASTEROID_SPEED_RANGE = (80, 120)
ASTEROID_ROTATION_SPEED_RANGE = (-90, 90)

ASTEROID_SPLIT_ANGLE = 30
ASTEROID_SPLIT_VELOCITY_FACTOR = 1.2

# === EnemyDrone Constants ===
ENEMY_DRONE_RADIUS = 16
ENEMY_DRONE_SPEED = 300
ENEMY_DRONE_HP = 4
ENEMY_DRONE_BLAST_RADIUS = 32
ENEMY_DRONE_IMG_PATH = "assets/enemy_drone.png"

# === EnemyShip Constants ===
ENEMY_SHIP_RADIUS = 32
ENEMY_SHIP_SPEED = 200
ENEMY_SHIP_HP = 8
ENEMY_SHIP_BLAST_RADIUS = 48
ENEMY_SHIP_IMG_PATH = "assets/enemy_ship.png"

# === Missile Constants ===
MISSILE_RADIUS = 10
MISSILE_SPEED = 200
MISSILE_HP = 1
MISSILE_BLAST_RADIUS = 64
MISSILE_IMG_PATH = "assets/missile.png"

# === Shot Constants ===
SHOT_RADIUS = 4
SHOT_RANGE = 512
SHOT_SPEED = 500
SHOT_IMG_PATH = "assets/blaster_shot.png"
SHOT_SFX_PATH = "assets/720118__baggonotes__player_shoot1.wav"

# === Bomb Constants ===
BOMB_RADIUS = 8
BOMB_SPEED = 200
BOMB_BLAST_RADIUS = 256
BOMB_TRIGGER_DISTANCE = 256
BOMB_IMG_PATH = "assets/e_bomb.png"

# === Explosion Constants ===
EXPLOSION_INITIAL_RADIUS = 2
EXPLOSION_EXPANSION_RATE = 192
