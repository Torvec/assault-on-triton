import pygame
import sys
from scenes.scene import Scene
from ui.render_text import render_text


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
                from scenes.start import Start

                self.game.scene_manager.set_scene(
                    Start(self.game, self.screen, self.dt)
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            "GAME OVER",
            128,
            "white",
            (self.game.screen_w // 2, self.game.screen_h // 2 - 256),
        )

        game_over_menu_rect = pygame.Rect(
            0, 0, self.game.screen_w // 2, self.game.screen_h // 4
        )
        game_over_menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2)
        pygame.draw.rect(screen, "grey4", game_over_menu_rect)
        pygame.draw.rect(
            screen, "grey70", game_over_menu_rect, width=4, border_radius=24
        )

        render_text(
            self.screen,
            f"Score: {self.score.show_score()}",
            64,
            "white",
            (game_over_menu_rect.midtop[0], game_over_menu_rect.midtop[1] + 36),
            align="midtop"
        )
        render_text(
            self.screen,
            "[Enter] Replay",
            36,
            "grey",
            (game_over_menu_rect.center[0], game_over_menu_rect.center[1] - 72),
        )
        render_text(
            self.screen,
            "[ESC] Main Menu",
            36,
            "grey",
            (game_over_menu_rect.center[0], game_over_menu_rect.center[1] - 36),
        )
        render_text(
            self.screen,
            "[S] Scoreboard",
            36,
            "grey",
            (game_over_menu_rect.center[0], game_over_menu_rect.center[1]),
        )
        render_text(
            self.screen,
            "[C] Credits",
            36,
            "grey",
            (game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 36),
        )
        render_text(
            self.screen,
            "[Q] Quit Game",
            36,
            "grey",
            (game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 72),
        )
