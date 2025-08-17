import pygame

class Scene():
    def __init__(self, game, screen, dt):
        self.game = game
        self.screen = screen
        self.dt = dt
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()

    def update(self, dt):
        self.updateable.update(dt)

    def draw(self, screen):
        screen.fill("black")
        for obj in self.drawable:
                obj.draw(screen)