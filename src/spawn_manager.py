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

SPAWN_LOCATIONS = {
    "left_edge": 0.1,
    "far_left": 0.2,
    "left": 0.3,
    "center_left": 0.4,
    "center": 0.5,
    "center_right": 0.6,
    "right": 0.7,
    "far_right": 0.8,
    "right_edge": 0.9,
}


class SpawnManager(pygame.sprite.Sprite):

    def __init__(self, game_play, entity_name, count, location, formation):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game_play = game_play
        self.play_area = game_play.play_area_rect
        self.entity_name = entity_name
        self.count = count
        self.location = location
        self.formation = formation

    def spawn_entity(self):
        if self.location not in SPAWN_LOCATIONS:
            print(
                f"Warning: Unknown spawn location '{self.location}'. Using 'center' instead."
            )
            self.location = "center"

        if self.entity_name not in ENTITY_REGISTRY:
            print(f"Error: Unknown entity type '{self.entity_name}'. Cannot spawn.")
            return

        x_multiplier = SPAWN_LOCATIONS[self.location]

        position = pygame.Vector2(
            self.play_area.left + x_multiplier * self.play_area.width,
            self.play_area.top - 64,
        )

        entity_class = ENTITY_REGISTRY[self.entity_name]
        entity = entity_class(position.x, position.y, self.game_play)

        self.game_play.active_targets.add(entity)

        entity.velocity = pygame.Vector2(0, 1) * entity.speed
