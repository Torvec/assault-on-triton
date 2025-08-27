import random
import pygame

from src.entities import Asteroid, EnemyShip
from src.global_consts import (
    ENEMY_SHIP_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MIN_RADIUS,
)


class Spawner(pygame.sprite.Sprite):
    def __init__(self, game_play, target_count):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game_play = game_play
        self.target_count = target_count
        self.spawn_timer = 0.0
        self.spawned = 0
        self.entity_class = None
        self.entity_radius = None
        self.spawn_rate = None
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.left - self.entity_radius,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.right + self.entity_radius,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.top - self.entity_radius,
                ),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.bottom + self.entity_radius,
                ),
            ],
        ]

    def spawn_entity(self):
        pass

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_rate and self.spawned < self.target_count:
            self.spawn_timer = 0
            self.spawned += 1
            self.spawn_entity()


class AsteroidSpawner(Spawner):

    def __init__(self, game_play, target_count):
        super().__init__(game_play, target_count)
        self.entity_class = Asteroid
        self.entity_radius = ASTEROID_MAX_RADIUS
        self.spawn_rate = 0.8

    def spawn_entity(self):
        edge = random.choice(self.edges)
        speed = random.randint(40, 100)
        velocity = edge[0] * speed
        velocity = velocity.rotate(random.randint(-30, 30))
        position = edge[1](random.uniform(0, 1))
        kind = random.randint(1, ASTEROID_KINDS)
        actual_radius = ASTEROID_MIN_RADIUS * kind

        asteroid = self.entity_class(
            position.x, position.y, actual_radius, self.game_play
        )
        asteroid.velocity = velocity


class EnemyShipSpawner(Spawner):
    def __init__(self, game_play, target_count):
        super().__init__(game_play, target_count)
        self.entity_class = EnemyShip
        self.entity_radius = ENEMY_SHIP_RADIUS
        self.spawn_rate = 1.2

    def spawn_entity(self):
        edge = random.choice(self.edges)
        speed = 200
        velocity = edge[0] * speed
        position = edge[1](random.uniform(0, 1))

        enemy_ship = self.entity_class(
            position.x,
            position.y,
            self.entity_radius,
            self.game_play,
        )
        enemy_ship.velocity = velocity
