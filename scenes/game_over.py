import pygame
from global_consts import (
    GAME_OVER_TEXT, 
    GAME_OVER_REPLAY, 
    GAME_OVER_MAIN_MENU, 
    SCREEN_WIDTH, 
    SCREEN_HEIGHT
)
from scenes.scene import Scene

class GameOver(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            from scenes.game_play import GamePlay
            self.game.set_scene(GamePlay(self.game, self.screen, self.dt))
        if keys[pygame.K_ESCAPE]:
            from scenes.main_menu import MainMenu
            self.game.set_scene(MainMenu(self.game, self.screen, self.dt))

    def draw(self, screen):
        super().draw(screen)

        title_font = pygame.font.Font(None, 128)
        title_upper = GAME_OVER_TEXT.upper()
        title = title_font.render(title_upper, False, "white")
        title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40))
        self.screen.blit(title, title_rect)
        
        replay_font = pygame.font.Font(None, 36)
        replay = replay_font.render(GAME_OVER_REPLAY, False, "grey")
        replay_rect = replay.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 36))
        self.screen.blit(replay, replay_rect)

        main_menu_font = pygame.font.Font(None, 36)
        main_menu = main_menu_font.render(GAME_OVER_MAIN_MENU, False, "grey")
        main_menu_rect = main_menu.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 64))
        self.screen.blit(main_menu, main_menu_rect)