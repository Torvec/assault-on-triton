import pygame
from src.entities.projectile import Projectile


class Shot(Projectile):

    RADIUS = 4

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play, owner)

        self.radius = self.RADIUS
        self.distance_traveled = 0
        self.max_range = 0
        self.speed = 0
        self.damage = 1
        self.sfx = None

    def sound(self):
        self.shoot_sound = pygame.mixer.Sound(self.sfx)
        self.shoot_sound.set_volume(0.5)
        self.shoot_sound.play()

    def handle_max_range(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.max_range:
            self.kill()

    def update(self, dt):
        super().update(dt)
        self.handle_max_range(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        shot_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, shot_rect)


class PlayerShot(Shot):

    shot_levels = {
        1: {
            "range": 512,
            "speed": 500,
            "damage": 1,
            "img_path": "assets/player_shot_lv1.png",
            "sfx": "assets/720118__baggonotes__player_shoot1.wav",
        },
        2: {
            "range": 768,
            "speed": 600,
            "damage": 2,
            "img_path": "assets/player_shot_lv2.png",
            "sfx": "assets/720118__baggonotes__player_shoot1.wav",
        },
        3: {
            "range": 1024,
            "speed": 700,
            "damage": 4,
            "img_path": "assets/player_shot_lv3.png",
            "sfx": "assets/720118__baggonotes__player_shoot1.wav",
        },
        4: {
            "range": 1024,
            "speed": 1000,
            "damage": 8,
            "img_path": "assets/player_shot_ov.png",
            "sfx": "assets/720118__baggonotes__player_shoot1.wav",
        },
    }

    def __init__(self, x, y, game_play, owner, power_level):
        self.img_path = self.shot_levels[power_level]["img_path"]
        super().__init__(x, y, game_play, owner)
        self.max_range = self.shot_levels[power_level]["range"]
        self.speed = self.shot_levels[power_level]["speed"]
        self.damage = self.shot_levels[power_level]["damage"]
        self.sfx = self.shot_levels[power_level]["sfx"]


class EnemyShot(Shot):

    RANGE = 512
    SPEED = 500
    DAMAGE = 2
    IMG_PATH = "assets/enemy_shot.png"
    SFX_PATH = "assets/720118__baggonotes__player_shoot1.wav"

    def __init__(self, x, y, game_play, owner):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play, owner)
        self.max_range = self.RANGE
        self.speed = self.SPEED
        self.damage = self.DAMAGE
        self.sfx = self.SFX_PATH
