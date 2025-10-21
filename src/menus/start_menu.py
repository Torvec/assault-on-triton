import sys
import pygame
from src.screen import Screen
from src.utils.render_text import render_text


class Start(Screen):

    menu_items = [
        "[Enter] PLAY",
        "[O] OPTIONS",
        "[S] SCORES",
        "[C] CREDITS",
        "[Q] QUIT",
    ]

    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RETURN:
                        self.game.set_scene("GamePlay")
                    case pygame.K_o:
                        self.game.set_scene("Options")
                    case pygame.K_s:
                        self.game.set_scene("Scoreboard")
                    case pygame.K_c:
                        self.game.set_scene("Credits")
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        render_text(
            screen=game_surface,
            text="ASSAULT",
            font_name="zendots",
            font_size=96,
            antialias=True,
            pos=(game_surface.get_width() * 0.5, game_surface.get_height() * 0.5 - 304),
        )

        render_text(
            screen=game_surface,
            text="ON",
            font_name="zendots",
            font_size=64,
            antialias=True,
            pos=(game_surface.get_width() * 0.5, game_surface.get_height() * 0.5 - 224),
        )

        render_text(
            screen=game_surface,
            text="TRITON",
            font_name="zendots",
            font_size=96,
            antialias=True,
            pos=(game_surface.get_width() * 0.5, game_surface.get_height() * 0.5 - 128),
        )
        menu_rect = pygame.Rect(
            0, 0, game_surface.get_width() * 0.75, game_surface.get_height() * 0.25
        )
        menu_rect.center = game_surface.get_rect().center
        menu_rect.y += 128
        pygame.draw.rect(game_surface, "grey4", menu_rect, border_radius=24)
        pygame.draw.rect(game_surface, "grey70", menu_rect, width=4, border_radius=24)

        for i, item in enumerate(self.menu_items):
            render_text(
                screen=game_surface,
                text=item,
                font_name="spacegrotesk_semibold",
                font_size=32,
                color="grey",
                pos=(menu_rect.midtop[0], menu_rect.midtop[1] + 8 + (i * 48)),
                align="midtop",
            )
