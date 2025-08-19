import pygame
from entities.circleshape import CircleShape
from global_consts import SHOT_RADIUS, SHOT_MAX_RANGE

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.start_position = pygame.Vector2(x, y)

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 0)

    def update(self, dt):
        distance_traveled = self.position.distance_to(self.start_position)
        if distance_traveled >= SHOT_MAX_RANGE:
            self.kill()
        self.position += self.velocity * dt