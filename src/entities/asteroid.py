import random
import pygame
from src.entities.entity import Entity
from src.entities.entity_directions import DIRECTION_DOWN
from src.data.settings import ASTEROIDS
from src.data.assets import IMAGES


class Asteroid(Entity):

    def __init__(self, x, y, game_play, asteroid_size="medium"):
        self.data = ASTEROIDS[asteroid_size]
        self.img_path = IMAGES[f"asteroid_{asteroid_size}"]
        super().__init__(x, y, game_play)
        self.speed = self.data["speed"]
        self.hp = self.data["hp"]
        self.score_value = self.hp
        self.rotation_speed = random.uniform(*ASTEROIDS["rotation_speed_range"])
        self.velocity = DIRECTION_DOWN * self.speed
        splits_into_name = self.data.get("splits_into")
        if splits_into_name:
            self.SPLITS_INTO = None
        else:
            self.SPLITS_INTO = None

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.game_play.score.handle_score(self.score_value)
            self.game_play.score.handle_streak_meter_inc(self.score_value)
            self.split()

    def split(self):
        self.kill()

        if not self.SPLITS_INTO:
            return

        split_into_classname = self.SPLITS_INTO.__name__

        # Create split events (right and left)
        for angle in [ASTEROIDS["split_angle"], -ASTEROIDS["split_angle"]]:
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
                                "velocity_factor": ASTEROIDS["split_velocity_factor"],
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
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        screen.blit(rotated_image, rotated_rect)


class AsteroidSmall(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "small")
        self.SPLITS_INTO = None


class AsteroidMedium(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "medium")
        self.SPLITS_INTO = AsteroidSmall


class AsteroidLarge(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "large")
        self.SPLITS_INTO = AsteroidMedium


class AsteroidExtraLarge(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "xl")
        self.SPLITS_INTO = AsteroidLarge
