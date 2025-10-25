import pygame
import src.entities.entity_behaviors as entity_behaviors


class Entity(pygame.sprite.Sprite):

    _image_cache = {}

    @classmethod
    def load_image(cls, img_path):
        if img_path not in cls._image_cache:
            cls._image_cache[img_path] = pygame.image.load(img_path).convert_alpha()
        return cls._image_cache[img_path]

    def __init__(self, x, y, game_play):
        # Auto adds sprites to groups upon creation if a container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Image cache check so images only get loaded once instead of every time an entity is spawned
        if getattr(self, "img_path", None):
            self.image = self.load_image(self.img_path)

        self.position = pygame.Vector2(x, y)
        self.game_play = game_play
        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)

        # Instance Attributes for all entities
        self.play_area = game_play.play_area_rect
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        
        self.behaviors = []

    def handle_behaviors(self, dt):
        for behavior_data in self.behaviors:
            behavior_fn_name = behavior_data["action"]
            behavior_fn = getattr(entity_behaviors, behavior_fn_name)
            params = behavior_data.get("params", {})
            params["dt"] = dt
            behavior_fn(self, **params)

    def update(self, dt):
        self.rect.center = (self.position.x, self.position.y)
        self.handle_behaviors(dt)

    def draw(self, surface):
        pass
