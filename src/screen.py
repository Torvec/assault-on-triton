import pygame
from src.backgrounds.background import Background


class Screen:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        # ! Really need to come up with a better way to handle background layers
        self.background = Background(0, 0, self.game.game_surface)
        self.background_2 = Background(0, 0, self.game.game_surface)
        self.background_3 = Background(0, 0, self.game.game_surface)

    def update(self, dt, events=None):
        self.background.update(dt)
        self.background_2.update(dt)
        self.background_3.update(dt)
        self.updateable.update(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        game_surface.fill("grey4")
        # ! Really need to come up with a better way to handle background layers
        self.background.draw(game_surface)
        self.background_2.draw(game_surface)
        self.background_3.draw(game_surface)
        sidebar_l_surface.fill("black")
        sidebar_r_surface.fill("black")

        for obj in self.drawable:
            obj.draw(game_surface)
