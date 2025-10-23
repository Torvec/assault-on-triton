import sys
import pygame
from src.utils.render_text import render_text


class PauseMenu:

    menu_title = "Paused"
    menu_items = [
        "[ESC] Resume",
        "[1] Restart",
        "[2] Main Menu",
        "[Q] QUIT",
    ]

    def __init__(self, game_play):
        self.game_play = game_play

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_play.is_paused = not self.game_play.is_paused
                if self.game_play.is_paused:
                    match event.key:
                        case pygame.K_1:
                            self.game_play.game.set_scene("GamePlay")
                        case pygame.K_2:
                            self.game_play.game.set_scene("Start")
                        case pygame.K_q:
                            pygame.quit()
                            sys.exit()

    def draw(self, game_surface):
        if self.game_play.is_paused:
            pause_menu_rect = pygame.Rect(
                0,
                0,
                game_surface.get_width() * 0.75,
                game_surface.get_height() * 0.3,
            )
            pause_menu_rect.center = game_surface.get_rect().center
            pygame.draw.rect(game_surface, "grey4", pause_menu_rect, border_radius=24)
            pygame.draw.rect(
                game_surface, "grey70", pause_menu_rect, width=4, border_radius=24
            )
            render_text(
                screen=game_surface,
                text=self.menu_title,
                font_name="zendots",
                font_size=48,
                pos=(pause_menu_rect.midtop[0], pause_menu_rect.midtop[1] + 8),
                align="midtop",
            )
            for i, item in enumerate(self.menu_items):
                render_text(
                    screen=game_surface,
                    text=item,
                    font_name="spacegrotesk_semibold",
                    font_size=32,
                    color="grey",
                    pos=(
                        pause_menu_rect.midtop[0],
                        pause_menu_rect.midtop[1] + 64 + (i * 48),
                    ),
                    align="midtop",
                )
