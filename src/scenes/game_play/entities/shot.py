import pygame
from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.entity_data import *


class Shot(Entity):

    def __init__(self, x, y, game_play, owner):
        self.img_path = SHOT_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = SHOT_RADIUS
        self.distance_traveled = 0
        self.max_range = SHOT_RANGE
        self.speed = SHOT_SPEED
        self.sfx = SHOT_SFX_PATH
        self.owner = owner

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
