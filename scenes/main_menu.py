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