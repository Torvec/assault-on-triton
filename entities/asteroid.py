import random
import pygame
from entities.entity import Entity
from global_consts import ASTEROID_MIN_RADIUS


class Asteroid(Entity):
    def __init__(self, game, x, y, radius):
        super().__init__(game, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "wheat4", self.position, self.radius, 2)

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a_velocity = self.velocity.rotate(random_angle)
        b_velocity = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(self.game, self.position.x, self.position.y, new_radius)
        asteroid_a.velocity = a_velocity * 1.2
        asteroid_b = Asteroid(self.game, self.position.x, self.position.y, new_radius)
        asteroid_b.velocity = b_velocity * 1.2
