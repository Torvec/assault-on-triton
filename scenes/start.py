import pygame
import sys
from scenes.scene import Scene
from ui.render_text import render_text


class Start(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from scenes.game_play import GamePlay

                self.game.scene_manager.set_scene(GamePlay(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                from scenes.options import Options

                self.game.scene_manager.set_scene(Options(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                from scenes.scoreboard import Scoreboard

                self.game.scene_manager.set_scene(Scoreboard(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                from scenes.credits import Credits

                self.game.scene_manager.set_scene(Credits(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="ASTEROIDS",
            font_size=128,
            pos=(self.game.screen_w // 2, self.game.screen_h // 2 - 128),
        )

        menu_rect = pygame.Rect(0, 0, self.game.screen_w // 2, self.game.screen_h // 4)
        menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2 + 128)
        pygame.draw.rect(screen, "grey4", menu_rect)
        pygame.draw.rect(screen, "grey70", menu_rect, width=4, border_radius=24)

        render_text(
            screen=self.game.screen,
            text="[Enter] PLAY",
            font_size=48,
            color="grey",
            pos=(menu_rect.midtop[0], menu_rect.midtop[1] + 48),
            align="midtop",
        )
        render_text(
            screen=self.game.screen,
            text="[O] OPTIONS",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1] - 36),
        )
        render_text(
            screen=self.game.screen,
            text="[S] SCORES",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1]),
        )
        render_text(
            screen=self.game.screen,
            text="[C] CREDITS",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1] + 36),
        )
        render_text(
            screen=self.game.screen,
            text="[Q] QUIT",
            color="grey",
            pos=(menu_rect.center[0], menu_rect.center[1] + 72),
        )
