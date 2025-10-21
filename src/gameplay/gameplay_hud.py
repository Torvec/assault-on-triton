import pygame
from src.utils.render_text import render_text
from src.data.settings import UI


class GamePlayHUD:

    def __init__(self, game, game_play):
        self.data = UI
        self.game = game
        self.game_play = game_play
        self._create_rects()

    def _create_section_rect(self, x, y, width, height):
        return pygame.Rect(x, y, width, height)

    def _get_padded_rect(self, rect):
        """Return a rect with inner padding applied for content positioning."""
        return pygame.Rect(
            rect.x + self.data["hud_inner_padding"],
            rect.y + self.data["hud_inner_padding"],
            rect.width - self.data["hud_inner_padding"] * 2,
            rect.height - self.data["hud_inner_padding"] * 2,
        )

    def _create_rects(self):
        # Left sidebar
        left_width = self.game.sidebar_l_surface.get_width()
        left_height = self.game.sidebar_l_surface.get_height()
        section_width = left_width // 2
        section_x = left_width // 2 - self.data["hud_padding"]

        self.top_left_rect = self._create_section_rect(
            section_x,
            self.data["hud_padding"],
            section_width,
            self.data["hud_top_section_height"],
        )
        self.mid_left_rect = self._create_section_rect(
            section_x,
            left_height // 2,
            section_width,
            self.data["hud_mid_section_height"],
        )
        self.btm_left_rect = self._create_section_rect(
            section_x,
            left_height - self.data["hud_bottom_section_height"],
            section_width,
            self.data["hud_bottom_section_height"] - self.data["hud_padding"],
        )

        # Right sidebar
        right_width = self.game.sidebar_r_surface.get_width()
        right_height = self.game.sidebar_r_surface.get_height()

        self.top_right_rect = self._create_section_rect(
            self.data["hud_padding"],
            self.data["hud_padding"],
            right_width // 2,
            self.data["hud_top_section_height"],
        )
        self.mid_right_rect = self._create_section_rect(
            self.data["hud_padding"],
            right_height // 2,
            right_width // 2,
            self.data["hud_mid_section_height"],
        )
        self.btm_right_rect = self._create_section_rect(
            self.data["hud_padding"],
            right_height - self.data["hud_bottom_section_height"],
            right_width // 2,
            self.data["hud_bottom_section_height"] - self.data["hud_padding"],
        )

    def _draw_section_bg(self, surface, rect):
        pygame.draw.rect(surface, self.data["colors"]["background"], rect)

    def _draw_streak_meter(self, surface, rect):
        meter_y = rect.top + self.data["hud_meter_y_offset"]
        meter_rect = pygame.Rect(
            rect.left, meter_y, rect.width, self.data["hud_meter_height"]
        )

        # Border
        pygame.draw.rect(
            surface,
            self.data["colors"]["meter_border"],
            meter_rect,
            self.data["hud_meter_border_width"],
        )

        # Fill
        percent = min(
            1.0,
            max(
                0.0,
                self.game_play.score.streak_meter
                / self.game_play.score.streak_meter_threshold,
            ),
        )

        if percent > 0:
            padding = self.data["hud_meter_inner_padding"]
            fill_width = int((rect.width - padding * 2) * percent)
            fill_rect = pygame.Rect(
                rect.left + padding,
                meter_y + padding,
                fill_width,
                self.data["hud_meter_inner_height"],
            )
            pygame.draw.rect(surface, self.data["colors"]["meter_fill"], fill_rect)

    def _format_time(self, game_timer):
        mins = int(game_timer // 60)
        secs = int(game_timer % 60)
        ms = int((game_timer % 1) * 1000)
        return f"T-{mins:02}:{secs:02}:{ms:03}"

    def draw_top_left(self, sidebar, rect):
        """Score, multiplier, high score, time."""
        self._draw_section_bg(sidebar, rect)

        content_rect = self._get_padded_rect(rect)

        # Score and multiplier
        render_text(
            screen=sidebar,
            text=f"SCORE: {self.game_play.score.score:,}",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=sidebar,
            text=f"x{self.game_play.score.multiplier}",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.topright,
            align="topright",
        )

        # Streak meter
        self._draw_streak_meter(sidebar, content_rect)

        # High score
        render_text(
            screen=sidebar,
            text=f"HI SCORE: {self.game.score_store.high_score:,}",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.bottomleft,
            align="bottomleft",
        )

        #! Time
        #! render_text(
        #!     screen=sidebar,
        #!     text=self._format_time(self.game_play.game_timer),
        #!     font_size=self.FONTS["lg"],
        #!     color=self.COLORS["primary"],
        #!     pos=content_rect.bottomleft,
        #!     align="bottomleft",
        #! )

    def draw_mid_left(self, sidebar, rect):
        """Hero (aka the player) dialogue box."""
        self._draw_section_bg(sidebar, rect)

        content_rect = self._get_padded_rect(rect)
        render_text(
            screen=sidebar,
            text="[ Hero Profile Pic ]",
            font_size=self.data["font_sizes"]["medium"],
            color=self.data["colors"]["secondary"],
            pos=content_rect.midtop,
            align="center",
        )
        render_text(
            screen=sidebar,
            text="[ Hero Dialogue ]",
            font_size=self.data["font_sizes"]["medium"],
            color=self.data["colors"]["secondary"],
            pos=content_rect.center,
            align="center",
        )

    def draw_btm_left(self, sidebar, rect):
        """Objective display."""
        self._draw_section_bg(sidebar, rect)

        content_rect = self._get_padded_rect(rect)
        render_text(
            screen=sidebar,
            text="Objective: Defeat Enemy Waves (PLACEHOLDER)",
            font_size=self.data["font_sizes"]["small"],
            color=self.data["colors"]["secondary"],
            pos=content_rect.midleft,
            align="midleft",
        )

    def draw_top_right(self, sidebar, rect):
        """Player stats: HP, lives, bombs, power level."""
        self._draw_section_bg(sidebar, rect)

        content_rect = self._get_padded_rect(rect)
        player = self.game_play.player

        # HP
        render_text(
            screen=sidebar,
            text=f"HP x {player.hp}%",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )

        # Lives
        render_text(
            screen=sidebar,
            text=f"LIVES x {player.lives}",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.midleft,
            align="midleft",
        )

        # Bombs
        render_text(
            screen=sidebar,
            text=f"BOMBS x {player.bomb_ammo}",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.center,
            align="center",
        )

        # Power Level
        power_display = self.data["power_levels"].get(player.power_level, "( ? )")
        render_text(
            screen=sidebar,
            text=f"PWR LVL {power_display}",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["primary"],
            pos=content_rect.bottomleft,
            align="bottomleft",
        )

    def draw_mid_right(self, sidebar, rect):
        """Enemy/Ally Dialogue Box"""
        self._draw_section_bg(sidebar, rect)

        content_rect = self._get_padded_rect(rect)
        render_text(
            screen=sidebar,
            text="[ Enemy/Ally Profile Pic ]",
            font_size=self.data["font_sizes"]["medium"],
            color=self.data["colors"]["secondary"],
            pos=content_rect.midtop,
            align="center",
        )
        render_text(
            screen=sidebar,
            text="[ Enemy/Ally Dialogue ]",
            font_size=self.data["font_sizes"]["medium"],
            color=self.data["colors"]["secondary"],
            pos=content_rect.center,
            align="center",
        )

    def draw_btm_right(self, sidebar, rect):
        """Instructions."""
        self._draw_section_bg(sidebar, rect)

        content_rect = self._get_padded_rect(rect)
        render_text(
            screen=sidebar,
            text="[Esc] to Pause Game",
            font_size=self.data["font_sizes"]["large"],
            color=self.data["colors"]["secondary"],
            pos=content_rect.midleft,
            align="midleft",
        )

    def draw(self, sidebar_l_surface, sidebar_r_surface):
        self.draw_top_left(sidebar_l_surface, self.top_left_rect)
        self.draw_mid_left(sidebar_l_surface, self.mid_left_rect)
        self.draw_btm_left(sidebar_l_surface, self.btm_left_rect)

        self.draw_top_right(sidebar_r_surface, self.top_right_rect)
        self.draw_mid_right(sidebar_r_surface, self.mid_right_rect)
        self.draw_btm_right(sidebar_r_surface, self.btm_right_rect)
