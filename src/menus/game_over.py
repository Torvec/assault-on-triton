import sys
import pygame
from src.screen import Screen
from src.utils.render_text import render_text


class GameOver(Screen):

    menu_title = "Game Over"
    menu_items = [
        "[Enter] Replay",
        "[ESC] Main Menu",
        "[S] Scoreboard",
        "[C] Credits",
        "[Q] Quit Game",
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
                    case pygame.K_ESCAPE:
                        self.game.set_scene("Start")
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
            text=self.menu_title,
            font_size=128,
            pos=(game_surface.get_width() * 0.5, game_surface.get_height() * 0.5 - 256),
        )
        game_over_menu_rect = pygame.Rect(
            0, 0, game_surface.get_width() * 0.75, game_surface.get_height() * 0.3
        )
        game_over_menu_rect.center = game_surface.get_rect().center
        pygame.draw.rect(game_surface, "grey4", game_over_menu_rect, border_radius=24)
        pygame.draw.rect(
            game_surface, "grey70", game_over_menu_rect, width=4, border_radius=24
        )
        render_text(
            screen=game_surface,
            text=f"Score: {self.game.score_store.current_score}",
            font_size=64,
            color="white",
            pos=(game_over_menu_rect.midtop[0], game_over_menu_rect.midtop[1] + 8),
            align="midtop",
        )
        for i, item in enumerate(self.menu_items):
            render_text(
                screen=game_surface,
                text=item,
                font_name="spacegrotesk_semibold",
                color="grey",
                pos=(
                    game_over_menu_rect.midtop[0],
                    game_over_menu_rect.midtop[1] + i * 48,
                ),
                align="midtop",
            )
