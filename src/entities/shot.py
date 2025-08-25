import pygame
from src.entities.entity import Entity
from src.data.global_consts import SHOT_RADIUS, SHOT_MAX_RANGE


class Shot(Entity):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, SHOT_RADIUS)
        self.start_position = pygame.Vector2(x, y)
        self.distance_traveled = 0

    def update(self, dt):
        super().update(dt)
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame

        if self.distance_traveled >= SHOT_MAX_RANGE:
            self.kill()

        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 0)
