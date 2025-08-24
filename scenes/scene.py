import pygame
import random


class Scene:
    def __init__(self, game, screen, dt):
        self.game = game
        self.screen = screen
        self.dt = dt
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.stars = [
            (
                random.randint(0, screen.get_width()),
                random.randint(0, screen.get_height()),
            )
            for _ in range(150)
        ]

    def update(self, dt, events=None):
        self.updateable.update(dt)

    def draw(self, screen):
        screen.fill("grey2")
        # Draw star field
        for x, y in self.stars:
            pygame.draw.circle(screen, "grey80", (x, y), 1)
        for obj in self.drawable:
            obj.draw(screen)
