import pygame
from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.explosion import Explosion
from src.scenes.game_play.entities.entity_data import *


class Missile(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = MISSILE_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = MISSILE_RADIUS
        self.speed = MISSILE_SPEED
        self.hp = MISSILE_HP
        self.blast_radius = MISSILE_BLAST_RADIUS
        self.score_value = self.hp

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def track_player(self):
        direction = self.game_play.player.position - self.position
        return DIRECTION_DOWN.angle_to(direction)

    def update(self, dt):
        super().update(dt)
        forward = DIRECTION_DOWN.rotate(self.rotation)
        self.position += forward * self.speed * dt
        self.rotation = self.track_player()

    def draw(self, screen):
        super().draw(screen)
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        missile_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, missile_rect)
