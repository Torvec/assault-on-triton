import pygame
from src.score_store import ScoreStore
from src.render_text import render_text


class GamePlayHUD:

    def __init__(self, game, game_play):
        self.game = game
        self.game_play = game_play
        self.score_store = ScoreStore()
        self.top_left_rect = pygame.Rect(
            312, 16, self.game.sidebar_l_surface.get_width() // 2, 128
        )
        self.mid_left_rect = pygame.Rect(
            312,
            self.game.sidebar_l_surface.get_height() // 2,
            self.game.sidebar_l_surface.get_width() // 2,
            192,
        )
        self.btm_left_rect = pygame.Rect(
            312,
            self.game.sidebar_l_surface.get_height() - 48,
            self.game.sidebar_l_surface.get_width() // 2,
            32,
        )
        self.top_right_rect = pygame.Rect(
            16, 16, self.game.sidebar_r_surface.get_width() // 2, 128
        )
        self.mid_right_rect = pygame.Rect(
            16,
            self.game.sidebar_r_surface.get_height() // 2,
            self.game.sidebar_r_surface.get_width() // 2,
            192,
        )
        self.btm_right_rect = pygame.Rect(
            16,
            self.game.sidebar_r_surface.get_height() - 48,
            self.game.sidebar_r_surface.get_width() // 2,
            32,
        )

    def draw_streak_meter(self, surface):
        streak_meter_bar_x = self.top_left_rect.left
        streak_meter_bar_y = self.top_left_rect.top + 24
        streak_meter_bar_rect = pygame.Rect(
            streak_meter_bar_x,
            streak_meter_bar_y,
            surface.get_width() // 2,
            16,
        )
        pygame.draw.rect(surface, "grey70", streak_meter_bar_rect, 2)

        percent_filled = (
            self.game_play.score.streak_meter
            / self.game_play.score.streak_meter_threshold
        )
        percent_filled = max(0.0, min(1.0, percent_filled))
        streak_meter_x = streak_meter_bar_rect.left + 2
        streak_meter_y = streak_meter_bar_rect.top + 2
        streak_meter_width = int((surface.get_width() // 2 - 4) * percent_filled)
        streak_meter_height = 12
        streak_meter_rect = pygame.Rect(
            streak_meter_x, streak_meter_y, streak_meter_width, streak_meter_height
        )
        pygame.draw.rect(surface, "grey50", streak_meter_rect)

    def draw(self, sidebar_l_surface, sidebar_r_surface):
        pygame.draw.rect(sidebar_l_surface, "grey10", self.top_left_rect)

        render_text(
            screen=sidebar_l_surface,
            text=f"SCORE: {self.game_play.score.score}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_left_rect.topleft),
            align="topleft",
        )

        render_text(
            screen=sidebar_l_surface,
            text=f"x{self.game_play.score.multiplier}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_left_rect.topright),
            align="topright",
        )

        self.draw_streak_meter(sidebar_l_surface)

        render_text(
            screen=sidebar_l_surface,
            text=f"HI SCORE: {self.score_store.high_score}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_left_rect.midleft),
            align="midleft",
        )

        mins = int(self.game_play.elapsed_time // 60)
        secs = int(self.game_play.elapsed_time % 60)
        ms = int((self.game_play.elapsed_time % 1) * 1000)
        render_text(
            screen=sidebar_l_surface,
            text=f"TIME: {mins:02}:{secs:02}:{ms:03}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_left_rect.bottomleft),
            align="bottomleft",
        )

        pygame.draw.rect(sidebar_l_surface, "grey10", self.mid_left_rect)

        pygame.draw.rect(sidebar_l_surface, "grey10", self.btm_left_rect)
        render_text(
            screen=sidebar_l_surface,
            text="Objective: Defeat Enemy Waves (PLACEHOLDER)",
            font_size=16,
            color="gray80",
            pos=(self.btm_left_rect.midleft),
            align="midleft",
        )

        pygame.draw.rect(sidebar_r_surface, "grey10", self.top_right_rect)
        render_text(
            screen=sidebar_r_surface,
            text=f"Shield x {self.game_play.player.shield}%",
            font_size=24,
            color="#E6D819",
            pos=(self.top_right_rect.topleft),
            align="topleft",
        )

        render_text(
            screen=sidebar_r_surface,
            text=f"LIVES x {self.game_play.player.lives}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_right_rect.midleft),
            align="midleft",
        )

        render_text(
            screen=sidebar_r_surface,
            text=f"BOMBS x {self.game_play.player.bomb_ammo}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_right_rect.center),
            align="center",
        )

        power_levels = {
            1: "( I )",
            2: "( II )",
            3: "( III )",
            4: "( OV )",
        }
        render_text(
            screen=sidebar_r_surface,
            text=f"PWR LVL {power_levels[self.game_play.player.power_level]}",
            font_size=24,
            color="#E6D819",
            pos=(self.top_right_rect.bottomleft),
            align="bottomleft",
        )

        pygame.draw.rect(sidebar_r_surface, "grey10", self.mid_right_rect)

        pygame.draw.rect(sidebar_r_surface, "grey10", self.btm_right_rect)
        render_text(
            screen=sidebar_r_surface,
            text="[Esc] to Pause Game",
            font_size=24,
            color="gray80",
            pos=(self.btm_right_rect.midleft),
            align="midleft",
        )
