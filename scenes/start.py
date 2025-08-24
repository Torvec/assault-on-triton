import pygame
import sys
from scenes.scene import Scene
from ui.render_text import render_text


class Start(Scene):
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
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            "ASTEROIDS",
            128,
            "white",
            (self.game.screen_w // 2, self.game.screen_h // 2 - 128),
        )
        render_text(
            self.screen,
            "[Enter] Play",
            48,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2),
        )
        render_text(
            self.screen,
            "[O] Options",
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 36),
        )
        render_text(
            self.screen,
            "[S] Scoreboard",
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 72),
        )
        render_text(
            self.screen,
            "[C] Credits",
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 108),
        )
        render_text(
            self.screen,
            "[ESC] Quit Game",
            36,
            "grey",
            (self.game.screen_w // 2, self.game.screen_h // 2 + 144),
        )
