import pygame
from scenes.scene import Scene
from utils.render_text import render_text
from global_consts import (
    GAME_OVER_TEXT, 
    GAME_OVER_SCORE,
    GAME_OVER_REPLAY, 
    GAME_OVER_MAIN_MENU,
    GAME_OVER_SCOREBOARD,
    GAME_OVER_CREDITS,
    SCREEN_WIDTH, 
    SCREEN_HEIGHT
)

class GameOver(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)
        self.score = game.score_manager

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            from scenes.game_play import GamePlay
            self.game.set_scene(GamePlay(self.game, self.screen, self.dt))
            self.score.score = 0
        if keys[pygame.K_ESCAPE]:
            from scenes.main_menu import MainMenu
            self.game.set_scene(MainMenu(self.game, self.screen, self.dt))

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            GAME_OVER_TEXT,
            128,
            "white",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40)
        )
        render_text(
            self.screen,
            GAME_OVER_SCORE + str(self.score.show_score()),
            64,
            "white",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 36)
        )
        render_text(
            self.screen,
            GAME_OVER_REPLAY,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 72)
        )
        render_text(
            self.screen,
            GAME_OVER_MAIN_MENU,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 108)
        )
        render_text(
            self.screen,
            GAME_OVER_SCOREBOARD,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 144)
        )
        render_text(
            self.screen,
            GAME_OVER_CREDITS,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 180)
        )