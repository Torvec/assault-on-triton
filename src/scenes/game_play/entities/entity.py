import pygame
from src.scenes.game_play.entities.entity_data import *
import src.scenes.game_play.entities.entity_behaviors as entity_behaviors


class Entity(pygame.sprite.Sprite):

    _image_cache = {}

    @classmethod
    def load_image(cls, img_path):
        if img_path not in cls._image_cache:
            cls._image_cache[img_path] = pygame.image.load(img_path).convert_alpha()
        return cls._image_cache[img_path]

    def __init__(self, x, y, game_play):
        # Used to auto add sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        if hasattr(self, "img_path") and self.img_path:
            self.image = self.load_image(self.img_path)
        self.position = pygame.Vector2(x, y)
        self.game_play = game_play
        self.play_area = game_play.play_area_rect
        self.radius = 0
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.is_hit = False
        self.hit_timer = HIT_TIMER
        self.blast_radius = 0
        self.behaviors = []

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def handle_boundaries(self, action=None):
        edges = {
            "top": self.play_area.top + self.radius,
            "right": self.play_area.right - self.radius * 0.25,
            "bottom": self.play_area.bottom - self.radius,
            "left": self.play_area.left + self.radius * 0.25,
        }
        if action == "block":
            self.position.x = max(edges["left"], min(self.position.x, edges["right"]))
            self.position.y = max(edges["top"], min(self.position.y, edges["bottom"]))
        if action == None and (
            self.position.x + self.radius < self.play_area.left
            or self.position.x - self.radius > self.play_area.right
            or self.position.y - self.radius > self.play_area.bottom
        ):
            self.remove_active_targets()

    def remove_active_targets(self):
        if self in self.game_play.active_targets:
            self.kill()
            self.game_play.active_targets.remove(self)

    def flash_when_hit(self, screen, entity_surface, entity_rect):
        if self.is_hit:
            flash = pygame.Surface(entity_surface.get_size(), pygame.SRCALPHA)
            center = (flash.get_width() // 2, flash.get_height() // 2)
            pygame.draw.circle(flash, (255, 255, 255, 180), center, self.radius)
            screen.blit(flash, entity_rect)

    def handle_hit_timer(self, dt):
        if self.is_hit:
            self.hit_timer -= dt
            if self.hit_timer <= 0:
                self.is_hit = False
                self.hit_timer = HIT_TIMER

    def handle_behaviors(self, dt):
        for behavior_data in self.behaviors:
            behavior_fn_name = behavior_data["action"]
            behavior_fn = getattr(entity_behaviors, behavior_fn_name)
            params = behavior_data.get("params", {})
            params["dt"] = dt
            behavior_fn(self, **params)

    def update(self, dt):
        self.handle_boundaries()
        self.handle_hit_timer(dt)
        self.handle_behaviors(dt)

    def draw(self, screen):
        pass
