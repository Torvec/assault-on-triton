import random
import pygame


class Scene:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.stars = [
            (
                random.randint(0, self.game.gs_w),
                random.randint(0, self.game.gs_h),
            )
            for _ in range(150)
        ]

    def update(self, dt, events=None):
        self.updateable.update(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        game_surface.fill("grey4")
        sidebar_l_surface.fill("black")
        sidebar_r_surface.fill("black")
        # Draw star field
        for x, y in self.stars:
            pygame.draw.circle(game_surface, "grey70", (x, y), 1)
        for obj in self.drawable:
            obj.draw(game_surface)
