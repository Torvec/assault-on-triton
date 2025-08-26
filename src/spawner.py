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
    def __init__(self, game, game_play, entities):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game = game
        self.game_play = game_play
        self.entities = entities
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.left - self.entity.radius,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.right + self.entity.radius,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.top - self.entity.radius,
                ),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.bottom + self.entity.radius,
                ),
            ],
        ]

    def spawn(self, radius, position, velocity):
        for entity, count in self.entities:
            if count > 0:
                if entity == "asteroid":
                    asteroid = Asteroid(
                        self.game,
                        position.x,
                        position.y,
                        radius,
                        self.game_play.play_area_rect,
                    )
                    asteroid.velocity = velocity
                if entity == "enemy_ship":
                    enemy_ship = EnemyShip(
                        self.game,
                        position.x,
                        position.y,
                        radius,
                        self.game_play.play_area_rect,
                        self.game_play.player,
                    )
                enemy_ship.velocity = velocity
                if entity == "boss":
                    pass

    def update(self, dt):
        self.spawn()


class EnemyShipSpawnManager(pygame.sprite.Sprite):
    def __init__(self, game, game_play, target):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game = game
        self.game_play = game_play
        self.spawn_rate = 1.2
        self.spawn_timer = 0.0
        self.spawned = 0
        self.target_amount = target
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.left - ENEMY_SHIP_RADIUS,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.right + ENEMY_SHIP_RADIUS,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.top - ENEMY_SHIP_RADIUS,
                ),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.bottom + ENEMY_SHIP_RADIUS,
                ),
            ],
        ]

    def show_target_amount(self):
        return self.target_amount

    def spawn(self, radius, position, velocity):
        enemy_ship = EnemyShip(
            self.game,
            position.x,
            position.y,
            radius,
            self.game_play.play_area_rect,
            self.game_play.player,
        )
        enemy_ship.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > self.spawn_rate and self.spawned < self.target_amount:
            self.spawn_timer = 0
            self.spawned += 1

            # spawn a new enemy ship at a random edge
            edge = random.choice(self.edges)
            speed = 200
            velocity = edge[0] * speed
            position = edge[1](random.uniform(0, 1))
            self.spawn(ENEMY_SHIP_RADIUS, position, velocity)


class AsteroidSpawnManager(pygame.sprite.Sprite):
    def __init__(self, game, game_play, target):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game = game
        self.game_play = game_play
        self.spawn_rate = 0.8
        self.spawn_timer = 0.0
        self.spawned = 0
        self.target_amount = target
        self.edges = [
            [
                pygame.Vector2(1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.left - ASTEROID_MAX_RADIUS,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(-1, 0),
                lambda y: pygame.Vector2(
                    self.game_play.play_area_rect.right + ASTEROID_MAX_RADIUS,
                    self.game_play.play_area_rect.top
                    + y * self.game_play.play_area_rect.height,
                ),
            ],
            [
                pygame.Vector2(0, 1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.top - ASTEROID_MAX_RADIUS,
                ),
            ],
            [
                pygame.Vector2(0, -1),
                lambda x: pygame.Vector2(
                    self.game_play.play_area_rect.left
                    + x * self.game_play.play_area_rect.width,
                    self.game_play.play_area_rect.bottom + ASTEROID_MAX_RADIUS,
                ),
            ],
        ]

    def show_target_amount(self):
        return self.target_amount

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(
            self.game, position.x, position.y, radius, self.game_play.play_area_rect
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
