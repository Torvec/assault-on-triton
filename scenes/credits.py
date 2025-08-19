import pygame
from scenes.scene import Scene
from global_consts import SCREEN_WIDTH, CREDITS_TITLE

class Credits(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)

        title_font = pygame.font.Font(None, 64)
        title_upper = CREDITS_TITLE.upper()
        title = title_font.render(title_upper, False, "white")
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, 64))
        self.screen.blit(title, title_rect)
        
        message_font = pygame.font.Font(None, 36)
        message = message_font.render("Credits go here", False, "grey")
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, 100))
        self.screen.blit(message, message_rect)