import random
import pygame


class Background:
    def __init__(self, x, y, game):
        self.position = pygame.Vector2(x, y)
        self.game = game
        self.velocity = pygame.Vector2(0, 0)
        self.scroll_speed = 0

    def update(self, dt):
        pass

    def draw(self, game_surface):
        pass


class StarField(Background):

    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.scroll_speed = 4
        self.stars = [
            (
                random.randint(0, self.game.gs_w),
                random.randint(-self.game.gs_h, self.game.gs_h),
                random.randint(1, 3),
            )
            for _ in range(200)
        ]

    def update(self, dt):
        super().update(dt)
        direction = pygame.Vector2(0, 1)
        self.position += direction * self.scroll_speed * dt

    def draw(self, game_surface):
        super().draw(game_surface)
        offset = self.position.y
        star_size = random.randint(1, 4)
        for x, y, star_size in self.stars:
            pygame.draw.circle(game_surface, "grey70", (x, y + offset), star_size)


class Planet(Background):

    def __init__(self, x, y, game):
        super().__init__(x, y, game)
        self.image = pygame.image.load("assets/backgrounds/planet.png")
        self.scroll_speed = 8
        self.current_width = self.image.get_width()
        self.current_height = self.image.get_height()
        self.scale_to_size = 16
        self.shrink_rate = 5

    def update(self, dt):
        super().update(dt)
        if (
            self.current_width > self.scale_to_size
            and self.current_height > self.scale_to_size
        ):
            self.current_width -= self.shrink_rate * dt
            self.current_height -= self.shrink_rate * dt
            self.current_width = max(self.current_width, self.scale_to_size)
            self.current_height = max(self.current_height, self.scale_to_size)
        direction = pygame.Vector2(0, 1)
        self.position += direction * self.scroll_speed * dt

    def draw(self, game_surface):
        super().draw(game_surface)
        scaled_image = pygame.transform.scale(
            self.image, (self.current_width, self.current_height)
        )
        planet_rect = scaled_image.get_rect(center=self.position)
        game_surface.blit(scaled_image, planet_rect)
