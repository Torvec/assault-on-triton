import pygame
from src.screen import Screen
from src.utils.render_text import render_text


class Options(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
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
