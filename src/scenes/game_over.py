import sys
import pygame
from src.scenes.scene import Scene
from src.render_text import render_text


class GameOver(Scene):

    def __init__(self, game):
        super().__init__(game)

    def controls(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.game.set_scene("GamePlay")
                if event.key == pygame.K_ESCAPE:
                    self.game.set_scene("Start")
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
            text="GAME OVER",
            font_size=128,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 256),
        )

    def draw_menu(self, game_surface):
        game_over_menu_rect = pygame.Rect(
            0, 0, self.game.gs_w * 0.75, self.game.gs_h * 0.3
        )
        game_over_menu_rect.center = (self.game.gs_w // 2, self.game.gs_h // 2)
        pygame.draw.rect(game_surface, "grey4", game_over_menu_rect)
        pygame.draw.rect(
            game_surface, "grey70", game_over_menu_rect, width=4, border_radius=24
        )

        render_text(
            screen=game_surface,
            text=f"Score: {self.game.score_store.current_score}",
            font_size=64,
            color="white",
            pos=(game_over_menu_rect.midtop[0], game_over_menu_rect.midtop[1] + 36),
            align="midtop",
        )
        render_text(
            screen=game_surface,
            text="[Enter] Replay",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] - 60),
        )
        render_text(
            screen=game_surface,
            text="[ESC] Main Menu",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] - 24),
        )
        render_text(
            screen=game_surface,
            text="[S] Scoreboard",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 12),
        )
        render_text(
            screen=game_surface,
            text="[C] Credits",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 48),
        )
        render_text(
            screen=game_surface,
            text="[Q] Quit Game",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 84),
        )

    def update(self, dt, events):
        super().update(dt, events)
        self.controls(events)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        self.draw_title(game_surface)
        self.draw_menu(game_surface)
