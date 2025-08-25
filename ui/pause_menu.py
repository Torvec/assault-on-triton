import pygame
import sys
from ui.render_text import render_text


class PauseMenu:

    def __init__(self, game, game_play):
        self.game = game
        self.game_play = game_play

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game_play.isPaused = not self.game_play.isPaused
            if self.game_play.isPaused:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    from scenes.game_play import GamePlay

                    self.game.scene_manager.set_scene(GamePlay(self.game))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    from scenes.start import Start

                    self.game.scene_manager.set_scene(Start(self.game))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def draw(self, screen):
        if self.game_play.isPaused:
            pause_menu_rect = pygame.Rect(
                0, 0, self.game.screen_w // 2, self.game.screen_h // 4
            )
            pause_menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2)
            pygame.draw.rect(screen, "grey4", pause_menu_rect)
            pygame.draw.rect(screen, "grey70", pause_menu_rect, width=4, border_radius=24)

            render_text(
                screen=self.game.screen,
                text="GAME PAUSED",
                font_size=64,
                pos=(pause_menu_rect.midtop[0], pause_menu_rect.midtop[1] + 64),
                align="midtop",
            )
            render_text(
                screen=self.game.screen,
                text="[ESC] Resume",
                color="grey",
                pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] - 36),
            )
            render_text(
                screen=self.game.screen,
                text="[1] Restart",
                color="grey",
                pos=(pause_menu_rect.center[0], pause_menu_rect.center[1]),
            )
            render_text(
                screen=self.game.screen,
                text="[2] Main Menu",
                color="grey",
                pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] + 36),
            )
            render_text(
                screen=self.game.screen,
                text="[Q] QUIT",
                color="grey",
                pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] + 72),
            )
