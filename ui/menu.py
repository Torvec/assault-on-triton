import pygame

class Menu():
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

    def update(self):
        pass

    def draw(self, screen):
        menu_width = self.game.screen_w // 2
        menu_height = self.game.screen_h // 2
        menu_surface = pygame.Surface((menu_width, menu_height), pygame.SRCALPHA)
        pygame.draw.rect(menu_surface, (255, 255, 255, 128), menu_surface.get_rect())

        menu_rect = menu_surface.get_rect()
        menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2 + 128)

        screen.blit(menu_surface, menu_rect)