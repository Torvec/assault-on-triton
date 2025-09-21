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

    def _single_formation(self, center_pos, count, spacing):
        return [center_pos]

    def _wall_formation(self, center_pos, count, spacing):
        positions = []
        for i in range(count):
            offset_x = (i - count // 2) * spacing
            positions.append(center_pos + pygame.Vector2(offset_x, 0))
        return positions

    def _column_formation(self, center_pos, count, spacing):
        positions = []
        for i in range(count):
            offset_y = (i - count // 2) * spacing
            positions.append(center_pos + pygame.Vector2(0, offset_y))
        return positions

    def _echelon_l_formation(self, center_pos, count, spacing):
        positions = []
        for i in range(count):
            offset = (i - count // 2) * spacing * 0.7
            positions.append(center_pos + pygame.Vector2(-offset, offset))
        return positions

    def _echelon_r_formation(self, center_pos, count, spacing):
        positions = []
        for i in range(count):
            offset = (i - count // 2) * spacing * 0.7
            positions.append(center_pos + pygame.Vector2(offset, offset))
        return positions

    def _reverse_v_formation(self, center_pos, count, spacing):
        positions = []

        pairs = (count - 1) // 2
        max_offset = pairs * spacing * 0.5 
        adjusted_center = pygame.Vector2(center_pos.x, center_pos.y - max_offset)

        positions.append(adjusted_center)

        for i in range(1, pairs + 1):
            distance = i * spacing
            positions.append(
                adjusted_center + pygame.Vector2(-distance, distance * 0.5)
            )
            positions.append(adjusted_center + pygame.Vector2(distance, distance * 0.5))

        if count % 2 == 0:
            positions.append(adjusted_center + pygame.Vector2(0, spacing * 1.5))

        return positions

    def _forward_v_formation(self, center_pos, count, spacing):
        positions = []

        positions.append(center_pos)

        pairs = (count - 1) // 2
        for i in range(1, pairs + 1):
            distance = i * spacing
            positions.append(center_pos + pygame.Vector2(-distance, -distance * 0.5))
            positions.append(center_pos + pygame.Vector2(distance, -distance * 0.5))

        if count % 2 == 0:
            positions.append(center_pos + pygame.Vector2(0, -spacing * 1.5))

        return positions

    def _diamond_formation(self, center_pos, count, spacing):
        positions = []

        # Adjust center_pos so the bottom entity spawns at the given position
        # This ensures the whole formation is off-screen initially
        formation_center = pygame.Vector2(center_pos.x, center_pos.y - spacing)

        offsets = [
            pygame.Vector2(0, -spacing),  # Top
            pygame.Vector2(-spacing, 0),  # Left
            pygame.Vector2(spacing, 0),  # Right
            pygame.Vector2(0, spacing),  # Bottom (will be at center_pos)
        ]

        for offset in offsets:
            positions.append(formation_center + offset)

        return positions

    def _circle_formation(self, center_pos, count, spacing):
        positions = []
        radius = spacing * 1.5
        for i in range(count):
            angle = (i / count) * 360
            offset = pygame.Vector2(radius, 0).rotate(angle)
            positions.append(center_pos + offset)
        return positions

    def calculate_formation_positions(self, center_pos, formation, count):
        spacing = 96
        method_name = f"_{formation}_formation"
        formation_func = getattr(self, method_name)
        return formation_func(center_pos, count, spacing)

    def spawn_entity(self):
        if self.location not in SPAWN_LOCATIONS:
            print(f"Warning: Unknown spawn location '{self.location}'.")
            return

        if self.entity_name not in ENTITY_REGISTRY:
            print(f"Error: Unknown entity type '{self.entity_name}'. Cannot spawn.")
            return

        # Calculate the center position for the formation
        x_multiplier = SPAWN_LOCATIONS[self.location]
        center_pos = pygame.Vector2(
            self.play_area.left + x_multiplier * self.play_area.width,
            self.play_area.top - 64,
        )

        # Get all positions for the formation
        positions = self.calculate_formation_positions(
            center_pos, self.formation, self.count
        )

        # Spawn an entity at each position
        entity_class = ENTITY_REGISTRY[self.entity_name]
        for position in positions:
            entity = entity_class(position.x, position.y, self.game_play)
            self.game_play.active_targets.add(entity)
            entity.velocity = pygame.Vector2(0, 1) * entity.speed
