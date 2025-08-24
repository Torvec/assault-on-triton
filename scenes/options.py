import pygame
from scenes.scene import Scene
from ui.render_text import render_text


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                from scenes.start import Start

                self.game.scene_manager.set_scene(Start(self.game))

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="OPTIONS",
            font_size=64,
            pos=(self.game.screen_w // 2, 64),
        )
        render_text(
            screen=self.game.screen,
            text="scores go here",
            color="grey",
            pos=(self.game.screen_w // 2, 128),
        )
