import sys
import pygame
from src.render_text import render_text


class StartMenu:
    def __init__(self, game):
        self.game = game

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from src.scenes import GamePlay

                self.game.set_scene(GamePlay(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_o:
                from src.scenes import Options

                self.game.set_scene(Options(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                from src.scenes import Scoreboard

                self.game.set_scene(Scoreboard(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                from src.scenes import Credits

                self.game.set_scene(Credits(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    def draw(self, screen):
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
                    from src.scenes import GamePlay

                    self.game.set_scene(GamePlay(self.game))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    from src.scenes import Start

                    self.game.set_scene(Start(self.game))
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
            pygame.draw.rect(
                screen, "grey70", pause_menu_rect, width=4, border_radius=24
            )

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


class GameOverMenu:
    def __init__(self, game):
        self.game = game

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                from src.scenes import GamePlay

                self.game.set_scene(GamePlay(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                from src.scenes import Start

                self.game.set_scene(Start(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                from src.scenes import Scoreboard

                self.game.set_scene(Scoreboard(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                from src.scenes import Credits

                self.game.set_scene(Credits(self.game))
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    def draw(self, screen):
        game_over_menu_rect = pygame.Rect(
            0, 0, self.game.screen_w // 2, self.game.screen_h // 4
        )
        game_over_menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2)
        pygame.draw.rect(screen, "grey4", game_over_menu_rect)
        pygame.draw.rect(
            screen, "grey70", game_over_menu_rect, width=4, border_radius=24
        )

        render_text(
            screen=self.game.screen,
            text=f"Score: {self.game.score_manager.show_score()}",
            font_size=64,
            color="white",
            pos=(game_over_menu_rect.midtop[0], game_over_menu_rect.midtop[1] + 36),
            align="midtop",
        )
        render_text(
            screen=self.game.screen,
            text="[Enter] Replay",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] - 72),
        )
        render_text(
            screen=self.game.screen,
            text="[ESC] Main Menu",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] - 36),
        )
        render_text(
            screen=self.game.screen,
            text="[S] Scoreboard",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1]),
        )
        render_text(
            screen=self.game.screen,
            text="[C] Credits",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 36),
        )
        render_text(
            screen=self.game.screen,
            text="[Q] Quit Game",
            color="grey",
            pos=(game_over_menu_rect.center[0], game_over_menu_rect.center[1] + 72),
        )
