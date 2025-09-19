import random
import pygame
from src.entities import (
    AsteroidLarge,
    AsteroidMedium,
    AsteroidSmall,
    EnemyDrone,
    EnemyShip,
    Missile,
)


ENTITY_REGISTRY = {
    "AsteroidLarge": AsteroidLarge,
    "AsteroidMedium": AsteroidMedium,
    "AsteroidSmall": AsteroidSmall,
    "EnemyDrone": EnemyDrone,
    "EnemyShip": EnemyShip,
    "Missile": Missile,
}


class SpawnManager(pygame.sprite.Sprite):

    def __init__(self, game_play, entity_name, target_count, spawn_rate):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game_play = game_play
        self.play_area = game_play.play_area_rect
        self.entity_class = ENTITY_REGISTRY[entity_name]
        self.target_count = target_count
        self.spawn_rate = spawn_rate
        self.spawn_timer = 0.0
        self.spawn_count = 0
        self.spawn_location = lambda x: pygame.Vector2(
            self.play_area.left + x * self.play_area.width,
            self.play_area.top - 64,
        )
        self.game_play.active_spawners.add(self)

    def spawn_entity(self):
        position = self.spawn_location(random.uniform(0, 1))
        entity = self.entity_class(position.x, position.y, self.game_play)
        entity.velocity = pygame.Vector2(0, 1) * entity.speed
        self.game_play.active_targets.add(entity)

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_count == self.target_count:
            if self in self.game_play.active_spawners:
                self.game_play.active_spawners.remove(self)
            return
        elif self.spawn_timer > self.spawn_rate:
            self.spawn_entity()
            self.spawn_timer = 0
            self.spawn_count += 1
