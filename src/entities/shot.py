import pygame
from src.entities.projectile import Projectile
from src.config.settings import PROJECTILES
from src.config.assets import IMAGES, SOUNDS


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

    def __init__(self, x, y, game_play, owner, power_level):
        self.config = PROJECTILES["player_shot"][power_level]
        if power_level == 4:
            image_key = "player_shot_ov"
        else:
            image_key = f"player_shot_lv{power_level}"
        self.img_path = IMAGES[image_key]
        super().__init__(x, y, game_play, owner)
        self.max_range = self.config["range"]
        self.speed = self.config["speed"]
        self.damage = self.config["damage"]
        self.sfx = SOUNDS["player_shoot"]


class EnemyShot(Shot):

    def __init__(self, x, y, game_play, owner):
        self.config = PROJECTILES["enemy_shot"]
        self.img_path = IMAGES["enemy_shot"]
        super().__init__(x, y, game_play, owner)
        self.max_range = self.config["range"]
        self.speed = self.config["speed"]
        self.damage = self.config["damage"]
        self.sfx = SOUNDS["player_shoot"]
