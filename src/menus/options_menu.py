import pygame
from src.screen import Screen
from src.utils.render_text import render_text


class Options(Screen):

    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene("Start")

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)

        render_text(
            screen=game_surface,
            text="Options",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )

        render_text(
            screen=game_surface,
            text="scores go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
        )
