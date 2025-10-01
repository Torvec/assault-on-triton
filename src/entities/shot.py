import pygame
from src.entities.projectile import Projectile


class Shot(Projectile):

    RADIUS = 4
    RANGE = 512
    SPEED = 500
    IMG_PATH = "assets/blaster_shot.png"
    SFX_PATH = "assets/720118__baggonotes__player_shoot1.wav"

    def __init__(self, x, y, game_play, owner):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play, owner)

        self.radius = self.RADIUS
        self.distance_traveled = 0
        self.max_range = self.RANGE
        self.speed = self.SPEED
        self.sfx = self.SFX_PATH

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
    pass

class EnemyShot(Shot):
    pass