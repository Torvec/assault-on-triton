import pygame

class Menu():
    def __init__(self, game, screen, dt, width, height, x, y):
        self.game = game
        self.screen = screen
        self.dt = dt
        self.width = width
        self.height = height
        self.pos_x = x
        self.pos_y = y

    def update(self, dt=None, events=None):
        pass

    def draw(self, screen):
        menu_surface = pygame.Surface((self.width, self.height))
        menu_rect = menu_surface.get_rect()
        pygame.draw.rect(menu_surface, "grey", menu_rect)
        menu_rect.topleft = (self.pos_x, self.pos_y)
        screen.blit(menu_surface, menu_rect)