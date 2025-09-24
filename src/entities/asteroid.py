import random
import pygame
from src.entities.entity import Entity
from src.entities.entity_data import *


class Asteroid(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.rotation_speed = random.uniform(*ASTEROID_ROTATION_SPEED_RANGE)
        self.velocity = DIRECTION_DOWN * self.speed

    def split(self, split_into=None):
        self.remove_active_targets()
        if split_into:
            split_event_r = {
                "event": "spawn_enemies",
                "params": {
                    "type": split_into,
                    "count": 1,
                    "location": self.position,
                    "formation": "single",
                    "behaviors": [
                        {
                            "action": "move_angled",
                            "params": {
                                "angle": ASTEROID_SPLIT_ANGLE,
                                "velocity_factor": ASTEROID_SPLIT_VELOCITY_FACTOR,
                            },
                        },
                        {"action": "rotate_constantly", "params": {}},
                    ],
                },
            }
            split_event_l = {
                "event": "spawn_enemies",
                "params": {
                    "type": split_into,
                    "count": 1,
                    "location": self.position,
                    "formation": "single",
                    "behaviors": [
                        {
                            "action": "move_angled",
                            "params": {
                                "angle": -ASTEROID_SPLIT_ANGLE,
                                "velocity_factor": ASTEROID_SPLIT_VELOCITY_FACTOR,
                            },
                        },
                        {"action": "rotate_constantly", "params": {}},
                    ],
                },
            }
            self.game_play.event_manager.handle_event(split_event_r)
            self.game_play.event_manager.handle_event(split_event_l)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)


class AsteroidSmall(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_SM_SPEED
        self.hp = ASTEROID_SM_HP
        self.img_path = ASTEROID_SM_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_SM_RADIUS
        self.score_value = self.hp


class AsteroidMedium(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_MD_SPEED
        self.hp = ASTEROID_MD_HP
        self.img_path = ASTEROID_MD_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_MD_RADIUS
        self.score_value = self.hp

    def split(self):
        super().split("AsteroidSmall")


class AsteroidLarge(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_LG_SPEED
        self.hp = ASTEROID_LG_HP
        self.img_path = ASTEROID_LG_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_LG_RADIUS
        self.score_value = self.hp

    def split(self):
        super().split("AsteroidMedium")
