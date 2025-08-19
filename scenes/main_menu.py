import pygame
from scenes.scene import Scene
from global_consts import (
    GAME_TITLE, 
    MAIN_MENU_MESSAGE, 
    SCREEN_WIDTH, 
    SCREEN_HEIGHT
)

class MainMenu(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            from scenes.game_play import GamePlay
            self.game.set_scene(GamePlay(self.game, self.screen, self.dt))
        if keys[pygame.K_o]:
            from scenes.options import Options
            self.game.set_scene(Options(self.game, self.screen, self.dt))
        if keys[pygame.K_c]:
            from scenes.credits import Credits
            self.game.set_scene(Credits(self.game, self.screen, self.dt))

    def draw(self, screen):
        super().draw(screen)

        title_font = pygame.font.Font(None, 128)
        title_upper = GAME_TITLE.upper()
        title = title_font.render(title_upper, False, "white")
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
        self.screen.blit(title, title_rect)
        
        message_font = pygame.font.Font(None, 36)
        message = message_font.render(MAIN_MENU_MESSAGE, False, "grey")
        message_rect = message.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 36))
        self.screen.blit(message, message_rect)

        options_font = pygame.font.Font(None, 36)
        options = options_font.render("[O] Options", False, "grey")
        options_rect = options.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 72))
        self.screen.blit(options, options_rect)

        credits_font = pygame.font.Font(None, 36)
        credits = credits_font.render("[C] Credits", False, "grey")
        credits_rect = credits.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 108))
        self.screen.blit(credits, credits_rect)