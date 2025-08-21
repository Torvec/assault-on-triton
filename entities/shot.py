import pygame
from entities.entity import Entity
from global_consts import SHOT_RADIUS, SHOT_MAX_RANGE


class Shot(Entity):
    def __init__(self, game, x, y):
        super().__init__(game, x, y, SHOT_RADIUS)
        self.start_position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 0)

    def update(self, dt):
        distance_traveled = self.position.distance_to(self.start_position)
        if distance_traveled >= SHOT_MAX_RANGE:
            self.kill()
        self.position += self.velocity * dt
