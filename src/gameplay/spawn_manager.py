import pygame
from src.entities.enemy import (
    AsteroidXL,
    AsteroidLG,
    AsteroidMD,
    AsteroidSM,
    EnemyDrone,
    EnemyShip,
)
from src.entities.pickup import (
    HealthPickup,
    ExtraLifePickup,
    PowerLevelPickup,
    OverdrivePickup,
    BombAmmoPickup,
    InvulnerabilityPickup,
)


class SpawnManager:

    spawn_locations = {
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

    entities = {
        "asteroid_xl": AsteroidXL,
        "asteroid_lg": AsteroidLG,
        "asteroid_md": AsteroidMD,
        "asteroid_sm": AsteroidSM,
        "enemy_drone": EnemyDrone,
        "enemy_ship": EnemyShip,
        "health_pickup": HealthPickup,
        "extra_life_pickup": ExtraLifePickup,
        "power_level_pickup": PowerLevelPickup,
        "overdrive_pickup": OverdrivePickup,
        "bomb_ammo_pickup": BombAmmoPickup,
        "invulnerability_pickup": InvulnerabilityPickup,
    }

    def __init__(self, game_play, entity_name, location, behaviors):
        self.game_play = game_play
        self.entity_name = entity_name
        self.location = location
        self.behaviors = behaviors

    def spawn_entity(self):
        position = self.calc_position()
        entity_class = self.entities[self.entity_name]
        entity = entity_class(position.x, position.y, self.game_play)
        for behavior in self.behaviors:
            entity.behaviors.append(behavior)

    def calc_position(self):
        play_area = self.game_play.play_area_rect

        if isinstance(self.location, pygame.Vector2):
            return self.location.copy()  # Copy to avoid reference issues

        elif isinstance(self.location, dict):
            x = self.location.get("x", play_area.centerx)
            y = self.location.get("y", play_area.top - 128)
            return pygame.Vector2(x, y)

        elif isinstance(self.location, str):
            offset_x = self.spawn_locations[self.location]
            return pygame.Vector2(
                play_area.left + (offset_x * play_area.width),
                play_area.top - 128,
            )

        return pygame.Vector2(play_area.centerx, play_area.top - 128)
