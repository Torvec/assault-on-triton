import pygame
from src.entities.entity import Entity
from src.entities.entity_layer_flags import (
    PLAYER,
    ENEMY,
    ALLY,
    NEUTRAL,
    EXPLOSIVE,
    EXPLOSION,
)
from src.config.settings import EXPLOSIONS


class Explosion(Entity):

    layer = EXPLOSION

    def __init__(self, x, y, game_play, blast_radius, owner):
        self.config = EXPLOSIONS
        super().__init__(x, y, game_play)
        self.blast_radius = blast_radius
        self.owner = owner
        self.radius = self.config["initial_radius"]
        self.exp_rate = self.config["expansion_rate"]
        self.damage = self.config["damage"]

    @property
    def mask(self):
        if self.owner.layer == PLAYER:
            return ENEMY | EXPLOSIVE | NEUTRAL
        elif self.owner.layer == ENEMY:
            return PLAYER | ALLY | NEUTRAL | EXPLOSIVE
        elif self.owner.layer == ALLY:
            return ENEMY | NEUTRAL | EXPLOSIVE

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
