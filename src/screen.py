import pygame


class Screen:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.backgrounds = []

    def handle_event(self, events):
        pass

    def update(self, dt):
        for bg in self.backgrounds:
            bg.update(dt)
        self.updateable.update(dt)

    def draw(self, display_surface, game_surface):
        display_surface.fill("black")
        game_surface.fill("#0c0c12")

        for bg in self.backgrounds:
            bg.draw(game_surface)

        for obj in self.drawable:
            obj.draw(game_surface)
