import pygame
from scenes.scene import Scene
from utils.render_text import render_text
from global_consts import (
    TITLE_GAME,
    MENU_ITEM_PLAY,
    MENU_ITEM_OPTIONS,
    MENU_ITEM_SCOREBOARD,
    MENU_ITEM_CREDITS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)


class MainMenu(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from scenes.game_play import GamePlay

                self.game.scene_manager.set_scene(
                    GamePlay(self.game, self.screen, self.dt)
                )
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                from scenes.options import Options

                self.game.scene_manager.set_scene(
                    Options(self.game, self.screen, self.dt)
                )
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                from scenes.scoreboard import Scoreboard

                self.game.scene_manager.set_scene(
                    Scoreboard(self.game, self.screen, self.dt)
                )
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                from scenes.credits import Credits

                self.game.scene_manager.set_scene(
                    Credits(self.game, self.screen, self.dt)
                )

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            TITLE_GAME.upper(),
            128,
            "white",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 40),
        )
        render_text(
            self.screen,
            MENU_ITEM_PLAY,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 36),
        )
        render_text(
            self.screen,
            MENU_ITEM_OPTIONS,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 72),
        )
        render_text(
            self.screen,
            MENU_ITEM_SCOREBOARD,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 108),
        )
        render_text(
            self.screen,
            MENU_ITEM_CREDITS,
            36,
            "grey",
            (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 144),
        )
