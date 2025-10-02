import random
import pygame
from src.entities.entity import Entity
from src.entities.entity_layer_flags import (
    PLAYER,
    ENEMY,
    ALLY,
    NEUTRAL,
    PROJECTILE,
    EXPLOSIVE,
    EXPLOSION,
)
from src.entities.entity_directions import DIRECTION_DOWN


class Asteroid(Entity):

    layer = NEUTRAL
    mask = PLAYER | ENEMY | ALLY | PROJECTILE | EXPLOSIVE | EXPLOSION | NEUTRAL

    ROTATION_SPEED_RANGE = (-90, 90)
    SPLIT_ANGLE = 30
    SPLIT_VELOCITY_FACTOR = 1.2

    RADIUS = 32
    SPEED = 100
    HP = 4
    IMG_PATH = "assets/asteroid_md.png"
    SPLITS_INTO = None

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = self.RADIUS
        self.speed = self.SPEED
        self.hp = self.HP
        self.score_value = self.hp
        self.rotation_speed = random.uniform(*self.ROTATION_SPEED_RANGE)
        self.velocity = DIRECTION_DOWN * self.speed

    def split(self):
        self.remove_active_targets()

        if not self.SPLITS_INTO:
            return

        split_into_classname = self.SPLITS_INTO.__name__

        # Create split events (right and left)
        for angle in [self.SPLIT_ANGLE, -self.SPLIT_ANGLE]:
            split_event = {
                "event": "spawn_entities",
                "params": {
                    "type": split_into_classname,
                    "count": 1,
                    "location": self.position,
                    "formation": "single",
                    "behaviors": [
                        {
                            "action": "move_angled",
                            "params": {
                                "angle": angle,
                                "velocity_factor": self.SPLIT_VELOCITY_FACTOR,
                            },
                        },
                        {"action": "rotate_constantly", "params": {}},
                    ],
                },
            }
            self.game_play.event_manager.handle_event(split_event)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)


class AsteroidSmall(Asteroid):

    RADIUS = 16
    SPEED = 120
    HP = 2
    IMG_PATH = "assets/asteroid_sm.png"
    SPLITS_INTO = None


class AsteroidMedium(Asteroid):

    RADIUS = 32
    SPEED = 100
    HP = 4
    IMG_PATH = "assets/asteroid_md.png"
    SPLITS_INTO = AsteroidSmall


class AsteroidLarge(Asteroid):

    RADIUS = 64
    SPEED = 80
    HP = 6
    IMG_PATH = "assets/asteroid_lg.png"
    SPLITS_INTO = AsteroidMedium
