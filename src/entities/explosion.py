import pygame
from src.entities.collidable_entity import CollidableEntity
from src.data.settings import EXPLOSIONS
from src.data.assets import IMAGES


class Explosion(CollidableEntity):

    def __init__(self, x, y, game_play, blast_radius, owner):
        self.data = EXPLOSIONS
        self.img_path = IMAGES["explosion"]
        super().__init__(x, y, game_play)
        self.blast_radius = blast_radius
        self.owner = owner
        self.init_radius = self.data["initial_radius"]
        self.exp_rate = self.data["expansion_rate"]
        self.damage = self.data["damage"]

    def sound(self):
        #! TODO: Get sound effect for explosion
        pass

    def collides_with(self, other_group):
        """Use circular collision detection for explosions"""
        collisions = []
        current_radius = self.init_radius

        for sprite in other_group:
            distance = self.position.distance_to(sprite.position)
            sprite_radius = sprite.rect.width // 2

            if distance <= current_radius + sprite_radius:
                collisions.append(sprite)

        return collisions

    def update(self, dt):
        super().update(dt)
        if self.init_radius < self.blast_radius:
            self.init_radius += self.exp_rate * dt
            if self.init_radius >= self.blast_radius:
                self.kill()

    def draw(self, screen):
        super().draw(screen)
        scaled_image = pygame.transform.scale(
            self.image, (self.init_radius * 2, self.init_radius * 2)
        )
        scaled_rect = scaled_image.get_rect(center=self.rect.center)
        screen.blit(scaled_image, scaled_rect)
