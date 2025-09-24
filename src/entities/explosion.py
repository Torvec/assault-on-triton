import pygame
from src.entities.entity import Entity
from src.entities.entity_data import *


class Explosion(Entity):

    def __init__(self, x, y, blast_radius, game_play):
        super().__init__(x, y, game_play)
        self.radius = EXPLOSION_INITIAL_RADIUS
        self.exp_rate = EXPLOSION_EXPANSION_RATE
        self.blast_radius = blast_radius

    def sound(self):
        pass

    def update(self, dt):
        super().update(dt)
        if self.radius < self.blast_radius:
            self.radius += self.exp_rate * dt
            if self.radius >= self.blast_radius:
                self.kill()

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius
        )
