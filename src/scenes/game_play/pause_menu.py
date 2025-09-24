import sys
import pygame
from src.render_text import render_text


class PauseMenu:

    def __init__(self, game_play):
        self.game_play = game_play
        self.screen_w = game_play.game.gs_w
        self.screen_h = game_play.game.gs_h

    def controls(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_play.isPaused = not self.game_play.isPaused
                if self.game_play.isPaused:
                    if event.key == pygame.K_1:
                        self.game_play.game.set_scene("GamePlay")
                    if event.key == pygame.K_2:
                        self.game_play.game.set_scene("Start")
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def draw_menu(self, screen):
        pause_menu_rect = pygame.Rect(
            0,
            0,
            self.screen_w * 0.75,
            self.screen_h * 0.3,
        )
        pause_menu_rect.center = (
            self.screen_w // 2,
            self.screen_h // 2,
        )
        pygame.draw.rect(screen, "grey4", pause_menu_rect)
        pygame.draw.rect(screen, "grey70", pause_menu_rect, width=4, border_radius=24)

        render_text(
            screen=screen,
            text="GAME PAUSED",
            font_size=64,
            pos=(pause_menu_rect.midtop[0], pause_menu_rect.midtop[1] + 64),
            align="midtop",
        )
        render_text(
            screen=screen,
            text="[ESC] Resume",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] - 36),
        )
        render_text(
            screen=screen,
            text="[1] Restart",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1]),
        )
        render_text(
            screen=screen,
            text="[2] Main Menu",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] + 36),
        )
        render_text(
            screen=screen,
            text="[Q] QUIT",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] + 72),
        )

    def update(self, events):
        self.controls(events)

    def draw(self, screen):
        if self.game_play.isPaused:
            self.draw_menu(screen)
