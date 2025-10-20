import pygame
from src.entities.asteroid import (
    AsteroidExtraLarge,
    AsteroidLarge,
    AsteroidMedium,
    AsteroidSmall,
)
from src.entities.enemy import EnemyDrone, EnemyShip
from src.entities.pickup import (
    HealthPickup,
    ExtraLifePickup,
    PowerLevelPickup,
    OverdrivePickup,
    BombAmmoPickup,
    InvulnerabilityPickup,
)
from src.entities import entity_formations


class SpawnManager:

    def __init__(self, game_play, entity_name, count, location, formation, behaviors):
        self.game_play = game_play
        self.play_area = game_play.play_area_rect
        self.entity_name = entity_name
        self.count = count
        self.location = location
        self.spawn_locations = {
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
        self.entity_dict = {
            "AsteroidXL": AsteroidExtraLarge,
            "AsteroidLarge": AsteroidLarge,
            "AsteroidMedium": AsteroidMedium,
            "AsteroidSmall": AsteroidSmall,
            "EnemyDrone": EnemyDrone,
            "EnemyShip": EnemyShip,
            "HealthPickup": HealthPickup,
            "ExtraLifePickup": ExtraLifePickup,
            "PowerLevelPickup": PowerLevelPickup,
            "OverdrivePickup": OverdrivePickup,
            "BombAmmoPickup": BombAmmoPickup,
            "InvulnerabilityPickup": InvulnerabilityPickup,
        }
        self.formation = formation
        self.behaviors = behaviors

    def calculate_formation_positions(self, fwd_pos, formation, count):
        spacing = 96
        formation_fn_name = f"{formation}_formation"
        formation_fn = getattr(entity_formations, formation_fn_name)
        return formation_fn(fwd_pos, count, spacing)

    def spawn_entity(self):
        # Support both string location and direct Vector2 position
        if isinstance(self.location, pygame.Vector2):
            fwd_pos = self.location
        else:
            # Calculate the forward position for the formation
            x_multiplier = self.spawn_locations[self.location]
            fwd_pos = pygame.Vector2(
                self.play_area.left + x_multiplier * self.play_area.width,
                self.play_area.top - 128,
            )

        # Get all positions for the formation
        positions = self.calculate_formation_positions(
            fwd_pos, self.formation, self.count
        )

        # Spawn an entity at each position
        entity_class = self.entity_dict[self.entity_name]

        for position in positions:
            entity = entity_class(position.x, position.y, self.game_play)
            for behavior in self.behaviors:
                entity.behaviors.append(behavior)
