import sys
import pygame
from src.scenes.scene import Scene
from src.render_text import render_text


class Start(Scene):

    def __init__(self, game):
        super().__init__(game)

    def controls(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.set_scene("GamePlay")
                if event.key == pygame.K_o:
                    self.game.set_scene("Options")
                if event.key == pygame.K_s:
                    self.game.set_scene("Scoreboard")
                if event.key == pygame.K_c:
                    self.game.set_scene("Credits")
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def draw_title(self, game_surface):
        render_text(
            screen=game_surface,
            text="ASSAULT",
            font_name="zendots",
            font_size=96,
            antialias=True,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 304),
        )

        render_text(
            screen=game_surface,
            text="ON",
            font_name="zendots",
            font_size=64,
            antialias=True,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 224),
        )

        render_text(
            screen=game_surface,
            text="TRITON",
            font_name="zendots",
            font_size=96,
            antialias=True,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 128),
        )

    def draw_menu(self, game_surface):
        menu_rect = pygame.Rect(0, 0, self.game.gs_w * 0.75, self.game.gs_h // 4)
        menu_rect.center = (self.game.gs_w // 2, self.game.gs_h // 2 + 128)
        pygame.draw.rect(game_surface, "grey4", menu_rect)
        pygame.draw.rect(game_surface, "grey70", menu_rect, width=4, border_radius=24)

        render_text(
            screen=game_surface,
            text="[Enter] PLAY",
            font_name="spacegrotesk_semibold",
            color="grey",
            pos=(menu_rect.midtop[0], menu_rect.midtop[1] + 24),
            align="midtop",
        )
        render_text(
            screen=game_surface,
            text="[O] OPTIONS",
            font_name="spacegrotesk_semibold",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1] - 36),
        )
        render_text(
            screen=game_surface,
            text="[S] SCORES",
            font_name="spacegrotesk_semibold",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1]),
        )
        render_text(
            screen=game_surface,
            text="[C] CREDITS",
            font_name="spacegrotesk_semibold",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1] + 36),
        )
        render_text(
            screen=game_surface,
            text="[Q] QUIT",
            font_name="spacegrotesk_semibold",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1] + 72),
        )

    def update(self, dt, events):
        super().update(dt, events)
        self.controls(events)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        self.draw_title(game_surface)
        self.draw_menu(game_surface)
