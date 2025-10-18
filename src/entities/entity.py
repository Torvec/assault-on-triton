import pygame
import src.entities.entity_behaviors as entity_behaviors


class Entity(pygame.sprite.Sprite):

    HIT_TIMER = 0.1

    _image_cache = {}

    @classmethod
    def load_image(cls, img_path):
        if img_path not in cls._image_cache:
            cls._image_cache[img_path] = pygame.image.load(img_path).convert_alpha()
        return cls._image_cache[img_path]

    def __init__(self, x, y, game_play):
        # Auto adds sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Image cache check so images only get loaded once instead of every time an entity is spawned
        if getattr(self, "img_path", None):
            self.image = self.load_image(self.img_path)
        # else:
        #     self.image = pygame.Surface((1, 1), pygame.SRCALPHA)

        # Init Parameters
        self.position = pygame.Vector2(x, y)
        self.game_play = game_play

        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_surface = self.mask.to_surface()

        # Instance Attributes for all entities
        self.play_area = game_play.play_area_rect
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.is_hit = False
        self.hit_timer = self.HIT_TIMER
        self.blast_radius = 0
        self.behaviors = []

    def collides_with(self, other_group):
        """
        Checks for rect collision first, then mask collision for per pixel detection
        """
        if pygame.sprite.spritecollide(self, other_group, False):
            if pygame.sprite.spritecollide(
                self, other_group, False, pygame.sprite.collide_mask
            ):
                return True
        return False

    def handle_boundaries(self, action=None):
        edges = {
            "top": self.play_area.top + self.rect.height // 2,
            "right": self.play_area.right - self.rect.width // 2,
            "bottom": self.play_area.bottom - self.rect.height // 2,
            "left": self.play_area.left + self.rect.width // 2,
        }
        if action == "block":
            self.position.x = max(edges["left"], min(self.position.x, edges["right"]))
            self.position.y = max(edges["top"], min(self.position.y, edges["bottom"]))
        elif action is None and (
            self.position.x + self.rect.width // 2 < self.play_area.left
            or self.position.x - self.rect.width // 2 > self.play_area.right
            or self.position.y - self.rect.height // 2 > self.play_area.bottom
        ):
            self.remove_active_targets()

    def remove_active_targets(self):
        if self in self.game_play.active_targets:
            self.kill()
            self.game_play.active_targets.remove(self)

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

    def handle_behaviors(self, dt):
        for behavior_data in self.behaviors:
            behavior_fn_name = behavior_data["action"]
            behavior_fn = getattr(entity_behaviors, behavior_fn_name)
            params = behavior_data.get("params", {})
            params["dt"] = dt
            behavior_fn(self, **params)

    def update(self, dt):
        self.rect.center = (self.position.x, self.position.y)
        self.handle_boundaries()
        self.handle_hit_timer(dt)
        self.handle_behaviors(dt)

    def draw(self, screen):
        pygame.draw.rect(screen, "white", self.rect, 1)
