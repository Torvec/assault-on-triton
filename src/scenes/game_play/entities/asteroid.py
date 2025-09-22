import random
import pygame
from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.entity_data import *

class Asteroid(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.rotation_speed = random.uniform(*ASTEROID_ROTATION_SPEED_RANGE)

    def split(self):
        self.remove_active_targets()

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt

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
        self.remove_active_targets()
        new_angle = ASTEROID_SPLIT_ANGLE

        asteroid_a = AsteroidSmall(
            self.position.x - ASTEROID_SM_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_a)
        asteroid_a.velocity = (
            self.velocity.rotate(new_angle) * ASTEROID_SPLIT_VELOCITY_FACTOR
        )

        asteroid_b = AsteroidSmall(
            self.position.x + ASTEROID_SM_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_b)
        asteroid_b.velocity = (
            self.velocity.rotate(-new_angle) * ASTEROID_SPLIT_VELOCITY_FACTOR
        )


class AsteroidLarge(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_LG_SPEED
        self.hp = ASTEROID_LG_HP
        self.img_path = ASTEROID_LG_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_LG_RADIUS
        self.score_value = self.hp

    def split(self):
        self.remove_active_targets()
        new_angle = ASTEROID_SPLIT_ANGLE

        asteroid_a = AsteroidMedium(
            self.position.x - ASTEROID_MD_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_a)
        asteroid_a.velocity = (
            self.velocity.rotate(new_angle) * ASTEROID_SPLIT_VELOCITY_FACTOR
        )

        asteroid_b = AsteroidMedium(
            self.position.x + ASTEROID_MD_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_b)
        asteroid_b.velocity = (
            self.velocity.rotate(-new_angle) * ASTEROID_SPLIT_VELOCITY_FACTOR
        )
