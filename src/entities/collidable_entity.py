import pygame
from src.entities.entity import Entity


class CollidableEntity(Entity):

    HIT_TIMER = 0.1

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_surface = self.mask.to_surface()
        self.is_hit = False
        self.hit_timer = self.HIT_TIMER
        self.blast_radius = 0

    def handle_boundaries(self, action="kill"):
        if action == "block":
            self.position.x = max(
                self.play_area.left + self.rect.width // 2,
                min(self.position.x, self.play_area.right - self.rect.width // 2),
            )
            self.position.y = max(
                self.play_area.top + self.rect.height // 2,
                min(self.position.y, self.play_area.bottom - self.rect.height // 2),
            )
        elif action == "kill" and (
            self.rect.right < self.play_area.left
            or self.rect.left > self.play_area.right
            or self.rect.top > self.play_area.bottom
        ):
            self.kill()

    def collides_with(self, other_group):
        rect_collisions = pygame.sprite.spritecollide(self, other_group, False)
        if rect_collisions:
            mask_collisions = pygame.sprite.spritecollide(
                self, other_group, False, pygame.sprite.collide_mask
            )
            if mask_collisions:
                return mask_collisions
        return []

    def take_damage(self, amount):
        pass

    def flash_when_hit(self, screen, entity_surface, entity_rect):
        if self.is_hit:
            #! screen.blit(self.mask_surface, (self.position.x, self.position.y))
            flash = pygame.Surface(entity_surface.get_size(), pygame.SRCALPHA)
            center = (flash.get_width() // 2, flash.get_height() // 2)
            pygame.draw.circle(
                flash, (255, 255, 255, 180), center, self.rect.width // 2
            )
            screen.blit(flash, entity_rect)

    def handle_hit_timer(self, dt):
        if self.is_hit:
            self.hit_timer -= dt
            if self.hit_timer <= 0:
                self.is_hit = False
                self.hit_timer = self.HIT_TIMER

    def update(self, dt):
        super().update(dt)
        self.handle_boundaries()
        self.handle_hit_timer(dt)

    def draw(self, screen):
        pass
