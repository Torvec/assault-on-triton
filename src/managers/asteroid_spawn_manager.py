import pygame
import random
from src.entities import Asteroid
from src.data.global_consts import (
    ASTEROID_MAX_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_MIN_RADIUS,
)


class AsteroidSpawnManager(pygame.sprite.Sprite):
    def __init__(self, game, target, play_area_rect):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game = game
        self.play_area_rect = play_area_rect
        self.spawn_rate = 0.8
        self.spawn_timer = 0.0
        self.spawned = 0
        self.target_amount = target
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(
                    self.play_area_rect.left - ASTEROID_MAX_RADIUS,
                    self.play_area_rect.top + y * self.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.play_area_rect.right + ASTEROID_MAX_RADIUS,
                    self.play_area_rect.top + y * self.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(
                    self.play_area_rect.left + x * self.play_area_rect.width,
                    self.play_area_rect.top - ASTEROID_MAX_RADIUS,
                ),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    self.play_area_rect.left + x * self.play_area_rect.width,
                    self.play_area_rect.bottom + ASTEROID_MAX_RADIUS,
                ),
            ],
        ]

    def show_target_amount(self):
        return self.target_amount

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(
            self.game, position.x, position.y, radius, self.play_area_rect
        )
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_rate and self.spawned < self.target_amount:
            self.spawn_timer = 0
            self.spawned += 1

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
