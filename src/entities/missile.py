import pygame
from src.entities.projectile import ExplosiveProjectile
from src.entities.explosion import Explosion
from src.entities.entity_directions import DIRECTION_DOWN


class Missile(ExplosiveProjectile):
    RADIUS = 10
    SPEED = 200
    HP = 1
    BLAST_RADIUS = 64
    IMG_PATH = "assets/missile.png"

    def __init__(self, x, y, game_play, owner):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play, owner)
        self.radius = self.RADIUS
        self.speed = self.SPEED
        self.hp = self.HP
        self.blast_radius = self.BLAST_RADIUS
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
