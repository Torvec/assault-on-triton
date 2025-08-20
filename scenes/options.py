import pygame
from scenes.scene import Scene
from utils.render_text import render_text
from global_consts import SCREEN_WIDTH, TITLE_OPTIONS


class Options(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                from scenes.main_menu import MainMenu

                self.game.scene_manager.set_scene(
                    MainMenu(self.game, self.screen, self.dt)
                )

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen, TITLE_OPTIONS.upper(), 64, "white", (SCREEN_WIDTH // 2, 64)
        )
        render_text(self.screen, "scores go here", 36, "grey", (SCREEN_WIDTH // 2, 100))
