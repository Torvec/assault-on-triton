import pygame
from scenes.scene import Scene
from utils.render_text import render_text
from global_consts import (
    TITLE_GAME_OVER,
    TITLE_SCORE,
    MENU_ITEM_REPLAY,
    MENU_ITEM_MAIN_MENU,
    MENU_ITEM_SCOREBOARD,
    MENU_ITEM_CREDITS,
)


class GameOver(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)
        self.score = game.score_manager

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from scenes.game_play import GamePlay

                self.game.scene_manager.set_scene(
                    GamePlay(self.game, self.screen, self.dt)
                )
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                from scenes.main_menu import MainMenu

                self.game.scene_manager.set_scene(
                    MainMenu(self.game, self.screen, self.dt)
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
            TITLE_GAME_OVER,
            128,
            "white",
            (self.game.screen_w // 2, self.game.screen_h // 2 - 40),
        )
        render_text(
            self.screen,
            TITLE_SCORE + str(self.score.show_score()),
            64,
            "white",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 36),
        )
        render_text(
            self.screen,
            MENU_ITEM_REPLAY,
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 72),
        )
        render_text(
            self.screen,
            MENU_ITEM_MAIN_MENU,
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 108),
        )
        render_text(
            self.screen,
            MENU_ITEM_SCOREBOARD,
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 144),
        )
        render_text(
            self.screen,
            MENU_ITEM_CREDITS,
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 180),
        )
