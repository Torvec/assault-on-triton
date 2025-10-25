import random
import pygame
from src.entities.collidable_entity import CollidableEntity
from src.entities.explosion import Explosion
from src.data.settings import ENEMIES
from src.data.assets import IMAGES
from src.entities.entity_directions import DIRECTION_DOWN


class Asteroid(CollidableEntity):

    def __init__(self, x, y, game_play, asteroid_size="md"):
        self.img_path = IMAGES[f"asteroid_{asteroid_size}"]
        super().__init__(x, y, game_play)
        self.speed = ENEMIES["asteroid"][asteroid_size]["speed"]
        self.hp = ENEMIES["asteroid"][asteroid_size]["hp"]
        self.score_value = self.hp
        self.rotation_speed = random.uniform(
            *ENEMIES["asteroid"]["rotation_speed_range"]
        )
        self.velocity = DIRECTION_DOWN * self.speed
        self.splits_into_name = (
            f"asteroid_{ENEMIES['asteroid'][asteroid_size]['splits_into']}"
            if ENEMIES["asteroid"][asteroid_size]["splits_into"] is not None
            else None
)

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.game_play.score.handle_score(self.score_value)
            self.game_play.score.handle_streak_meter_inc(self.score_value)
            self.split()

    def split(self):
        self.kill()

        if self.splits_into_name is None:
            return

        # Create split events (right and left)
        for angle in [
            ENEMIES["asteroid"]["split_angle"],
            -ENEMIES["asteroid"]["split_angle"],
        ]:
            split_event = {
                "event": "spawn_entities",
                "params": {
                    "type": self.splits_into_name,
                    "count": 1,
                    "location": self.position,
                    "formation": "single",
                    "behaviors": [
                        {
                            "action": "move_angled",
                            "params": {
                                "angle": angle,
                                "velocity_factor": ENEMIES["asteroid"][
                                    "split_velocity_factor"
                                ],
                            },
                        },
                        {"action": "rotate_constantly", "params": {}},
                    ],
                },
            }
            self.game_play.event_manager.handle_event(split_event)

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)


class AsteroidSM(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "sm")
        self.splits_into = None


class AsteroidMD(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "md")
        self.splits_into = "asteroid_sm"


class AsteroidLG(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "lg")
        self.splits_into = "asteroid_md"


class AsteroidXL(Asteroid):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "xl")
        self.splits_into = "asteroid_lg"


class Ship(CollidableEntity):
    def __init__(self, x, y, game_play, ship_type):
        self.img_path = IMAGES[ship_type]
        super().__init__(x, y, game_play)
        self.speed = ENEMIES[ship_type]["speed"]
        self.hp = ENEMIES[ship_type]["hp"]
        self.blast_radius = ENEMIES[ship_type]["blast_radius"]
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = ENEMIES[ship_type]["shot_cooldown"]
        self.shot_offset_pos = ENEMIES[ship_type]["shot_offset"]

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.game_play.score.handle_score(self.score_value)
            self.game_play.score.handle_streak_meter_inc(self.score_value)
            self.explode()
        self.is_hit = True

    def explode(self):
        Explosion(
            self.position.x, self.position.y, self.game_play, self.blast_radius, self
        )
        self.kill()

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class EnemyDrone(Ship):
    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "enemy_drone")


class EnemyShip(Ship):
    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play, "enemy_ship")
