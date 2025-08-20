import pygame
from scenes.scene import Scene
from utils.render_text import render_text
from global_consts import SCREEN_WIDTH, CREDITS_TITLE

class Credits(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)

    def update(self, dt):
        super().update(dt)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            from scenes.main_menu import MainMenu
            self.game.set_scene(MainMenu(self.game, self.screen, self.dt))

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            CREDITS_TITLE.upper(),
            64,
            "white",
            (SCREEN_WIDTH // 2, 64)
        )
        render_text(
            self.screen,
            "Credits go here",
            36,
            "grey",
            (SCREEN_WIDTH // 2, 100)
        )