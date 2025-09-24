import pygame
from src.scenes.scene import Scene
from src.render_text import render_text


class Scoreboard(Scene):

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
            text="HIGH SCORES",
            font_size=64,
            pos=(game_surface.get_width() // 2, 64),
        )

        render_text(
            screen=game_surface,
            text="scores go here",
            color="grey",
            pos=(game_surface.get_width() // 2, 128),
        )
