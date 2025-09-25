import pygame
from src.entities.entity import Entity


class Explosion(Entity):

    INITIAL_RADIUS = 2
    EXPANSION_RATE = 192

    def __init__(self, x, y, blast_radius, game_play):
        super().__init__(x, y, game_play)
        self.radius = self.INITIAL_RADIUS
        self.exp_rate = self.EXPANSION_RATE
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
