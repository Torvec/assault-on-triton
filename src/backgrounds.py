import pygame
from data.assets import IMAGES


class Background:

    def __init__(self, x, y, game):
        self.position = pygame.Vector2(x, y)
        self.game = game
        self.velocity = pygame.Vector2(0, 0)
        self.scroll_speed = 0

        if hasattr(self, "img_path"):
            self.image = pygame.image.load(self.img_path).convert_alpha()
            self.rect = self.image.get_rect(center=self.position)

    def scroll_vertically(self, dt, direction):
        self.position.y += direction * self.scroll_speed * dt
        self.rect.center = self.position

    def transform_scale(self, dt, target_width, target_height, rate):
        if not hasattr(self, "current_width"):
            self.current_width = self.image.get_width()
            self.current_height = self.image.get_height()

        if self.current_width < target_width:
            self.current_width = min(self.current_width + rate * dt, target_width)
        elif self.current_width > target_width:
            self.current_width = max(self.current_width - rate * dt, target_width)

        if self.current_height < target_height:
            self.current_height = min(self.current_height + rate * dt, target_height)
        elif self.current_height > target_height:
            self.current_height = max(self.current_height - rate * dt, target_height)

    def update(self, dt):
        pass

    def draw(self, surface):
        pass


class StarField(Background):

    def __init__(self, x, y, game):
        self.img_path = IMAGES["starfield"]
        super().__init__(x, y, game)
        self.scroll_speed = 4
        self.image_height = self.image.get_height()
        self.offset_y = 0

    def update(self, dt):
        self.scroll_vertically(dt, direction=1)
        self.offset_y = (self.offset_y + self.scroll_speed * dt) % self.image_height

    def draw(self, surface):
        surface.blit(self.image, (self.position.x, self.offset_y))
        surface.blit(self.image, (self.position.x, self.offset_y - self.image_height))


class Planet(Background):

    def __init__(self, x, y, game):
        self.img_path = IMAGES["planet"]
        super().__init__(x, y, game)
        self.scroll_speed = 8
        self.current_width = self.image.get_width() * 4
        self.current_height = self.image.get_height() * 4
        self.target_size = 16
        self.change_rate = 10

    def update(self, dt):
        self.scroll_vertically(dt, direction=1)
        self.transform_scale(dt, self.target_size, self.target_size, self.change_rate)

    def draw(self, surface):
        scaled_image = pygame.transform.scale(
            self.image, (int(self.current_width), int(self.current_height))
        )
        planet_rect = scaled_image.get_rect(center=self.position)
        surface.blit(scaled_image, planet_rect)


class PlanetTwo(Background):

    def __init__(self, x, y, game):
        self.img_path = IMAGES["planet_two"]
        super().__init__(x, y, game)
        self.scroll_speed = 2
        self.current_width = 2
        self.current_height = 2
        self.target_size = 1024
        self.change_rate = 4

    def update(self, dt):
        self.scroll_vertically(dt, direction=1)
        self.transform_scale(dt, self.target_size, self.target_size, self.change_rate)

    def draw(self, surface):
        scaled_image = pygame.transform.scale(
            self.image, (int(self.current_width), int(self.current_height))
        )
        planet_rect = scaled_image.get_rect(center=self.position)
        surface.blit(scaled_image, planet_rect)
