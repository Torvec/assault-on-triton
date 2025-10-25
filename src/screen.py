import pygame


class Screen:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()

    def update(self, dt, events=None):
        self.updateable.update(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        game_surface.fill("grey4")
        sidebar_l_surface.fill("black")
        sidebar_r_surface.fill("black")

        for obj in self.drawable:
            obj.draw(game_surface)
