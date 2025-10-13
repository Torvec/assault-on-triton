import pygame
from src.entities.projectile import ExplosiveProjectile
from src.entities.explosion import Explosion
from src.entities.entity_directions import DIRECTION_DOWN
from src.data.settings import PROJECTILES
from src.data.assets import IMAGES


class Missile(ExplosiveProjectile):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["missile"]
        self.img_path = IMAGES["missile"]
        super().__init__(x, y, game_play, owner)
        self.radius = self.data["radius"]
        self.speed = self.data["speed"]
        self.hp = self.data["hp"]
        self.blast_radius = self.data["blast_radius"]
        self.score_value = self.hp

    def explode(self):
        self.remove_active_targets()
        Explosion(
            self.position.x,
            self.position.y,
            self.game_play,
            self.blast_radius,
            self.owner,
        )

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
