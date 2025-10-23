import pygame
from src.utils.render_text import render_text
from src.data.settings import UI
from src.data.dialogue import SCRIPTED, DYNAMIC

"""

6 rects total
3 rects on either side of the game_surface
All the same width (game_surface width / 2)
Height is variable
Position derived from hud surface using get rect()
- 2 top rects = topleft and topright
- 2 middle rects = midleft and midright
- 2 bottom rects = bottomleft and bottomright

"""


class GamePlayHUD:

    def __init__(self, game, game_play):
        self.game = game
        self.game_play = game_play

    def display_dialogue(self, dialogue_id):
        dialogue = SCRIPTED[dialogue_id]
        self.current_speaker = dialogue["speaker"]
        self.current_text = dialogue["text"]
        self.dialogue_timer = dialogue["timer"]
        self.location = dialogue["location"]
        # self.portrait = dialogue["portrait"]

    def display_objective(self, objective_id):
        pass

    def display_hint(self, hint_id):
        pass

    def draw_streak_meter(self, surface, rect):
        meter_y = rect.top + UI["hud_meter_y_offset"]
        meter_rect = pygame.Rect(rect.left, meter_y, rect.width, UI["hud_meter_height"])
        pygame.draw.rect(
            surface,
            UI["colors"]["meter_border"],
            meter_rect,
            UI["hud_meter_border_width"],
        )
        percent = min(
            1.0,
            max(
                0.0,
                self.game_play.score.streak_meter
                / self.game_play.score.streak_meter_threshold,
            ),
        )
        if percent > 0:
            padding = UI["hud_meter_inner_padding"]
            fill_width = int((rect.width - padding * 2) * percent)
            fill_rect = pygame.Rect(
                rect.left + padding,
                meter_y + padding,
                fill_width,
                UI["hud_meter_inner_height"],
            )
            pygame.draw.rect(surface, UI["colors"]["meter_fill"], fill_rect)

    def format_time(self, game_timer):
        mins = int(game_timer // 60)
        secs = int(game_timer % 60)
        ms = int((game_timer % 1) * 1000)
        return f"T-{mins:02}:{secs:02}:{ms:03}"

    def draw_top_left(self, sidebar):
        """Score, multiplier, high score, time."""
        top_left_rect = pygame.Rect(
            0,
            0,
            self.game.sidebar_l_surface.get_width() * 0.5,
            UI["hud_top_section_height"],
        )
        top_left_rect.topleft = sidebar.get_rect().midtop
        top_left_rect.x -= UI["hud_inner_padding"]
        top_left_rect.y += UI["hud_inner_padding"]
        pygame.draw.rect(sidebar, UI["colors"]["background"], top_left_rect)
        content_rect = pygame.Rect(
            top_left_rect.x + UI["hud_inner_padding"],
            top_left_rect.y + UI["hud_inner_padding"],
            top_left_rect.width - UI["hud_inner_padding"] * 2,
            top_left_rect.height - UI["hud_inner_padding"] * 2,
        )
        render_text(
            screen=sidebar,
            text=f"SCORE: {self.game_play.score.score:,}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=sidebar,
            text=f"x{self.game_play.score.multiplier}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topright,
            align="topright",
        )
        self.draw_streak_meter(sidebar, content_rect)
        render_text(
            screen=sidebar,
            text=f"HI SCORE: {self.game.score_store.high_score:,}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.bottomleft,
            align="bottomleft",
        )
        # render_text(
        #     screen=sidebar,
        #     text=self.format_time(self.game_play.game_timer),
        #     font_size=self.FONTS["lg"],
        #     color=self.COLORS["primary"],
        #     pos=content_rect.bottomleft,
        #     align="bottomleft",
        # )

    def draw_mid_left(self, sidebar):
        """Hero (aka the player) dialogue box."""
        mid_left_rect = pygame.Rect(
            0,
            0,
            self.game.sidebar_l_surface.get_width() * 0.5,
            UI["hud_mid_section_height"],
        )
        mid_left_rect.midleft = sidebar.get_rect().center
        mid_left_rect.x -= UI["hud_inner_padding"]
        pygame.draw.rect(sidebar, UI["colors"]["background"], mid_left_rect)
        content_rect = pygame.Rect(
            mid_left_rect.x + UI["hud_inner_padding"],
            mid_left_rect.y + UI["hud_inner_padding"],
            mid_left_rect.width - UI["hud_inner_padding"] * 2,
            mid_left_rect.height - UI["hud_inner_padding"] * 2,
        )
        # render_text(
        #     screen=sidebar,
        #     text="[ Hero Profile Pic ]",
        #     font_size=UI["font_sizes"]["medium"],
        #     color=UI["colors"]["secondary"],
        #     pos=content_rect.midtop,
        #     align="center",
        # )
        render_text(
            screen=sidebar,
            text="[ Hero Dialogue ]",
            font_size=UI["font_sizes"]["medium"],
            color=UI["colors"]["secondary"],
            pos=content_rect.center,
            align="center",
        )

    def draw_btm_left(self, sidebar):
        """Objective display."""
        btm_left_rect = pygame.Rect(
            0,
            0,
            self.game.sidebar_l_surface.get_width() * 0.5,
            UI["hud_bottom_section_height"],
        )
        btm_left_rect.bottomleft = sidebar.get_rect().midbottom
        btm_left_rect.x -= UI["hud_inner_padding"]
        btm_left_rect.y -= UI["hud_inner_padding"]
        pygame.draw.rect(sidebar, UI["colors"]["background"], btm_left_rect)
        content_rect = pygame.Rect(
            btm_left_rect.x + UI["hud_inner_padding"],
            btm_left_rect.y + UI["hud_inner_padding"],
            btm_left_rect.width - UI["hud_inner_padding"] * 2,
            btm_left_rect.height - UI["hud_inner_padding"] * 2,
        )
        render_text(
            screen=sidebar,
            text="Objective: Defeat Enemy Waves (PLACEHOLDER)",
            font_size=UI["font_sizes"]["small"],
            color=UI["colors"]["secondary"],
            pos=content_rect.midleft,
            align="midleft",
        )

    def draw_top_right(self, sidebar):
        """Player stats: HP, lives, bombs, power level."""
        top_right_rect = pygame.Rect(
            0,
            0,
            self.game.sidebar_r_surface.get_width() * 0.5,
            UI["hud_top_section_height"],
        )
        top_right_rect.topleft = sidebar.get_rect().topleft
        top_right_rect.x += UI["hud_inner_padding"]
        top_right_rect.y += UI["hud_inner_padding"]
        pygame.draw.rect(sidebar, UI["colors"]["background"], top_right_rect)
        content_rect = pygame.Rect(
            top_right_rect.x + UI["hud_inner_padding"],
            top_right_rect.y + UI["hud_inner_padding"],
            top_right_rect.width - UI["hud_inner_padding"] * 2,
            top_right_rect.height - UI["hud_inner_padding"] * 2,
        )
        render_text(
            screen=sidebar,
            text=f"HP x {self.game_play.player.hp}%",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=sidebar,
            text=f"LIVES x {self.game_play.player.lives}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.midleft,
            align="midleft",
        )
        render_text(
            screen=sidebar,
            text=f"BOMBS x {self.game_play.player.bomb_ammo}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.center,
            align="center",
        )
        power_display = UI["power_levels"].get(
            self.game_play.player.power_level, "( ? )"
        )
        render_text(
            screen=sidebar,
            text=f"PWR LVL {power_display}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.bottomleft,
            align="bottomleft",
        )

    def draw_mid_right(self, sidebar):
        """Enemy/Ally Dialogue Box"""
        mid_right_rect = pygame.Rect(
            0,
            0,
            self.game.sidebar_r_surface.get_width() * 0.5,
            UI["hud_mid_section_height"],
        )
        mid_right_rect.midleft = sidebar.get_rect().midleft
        mid_right_rect.x += UI["hud_inner_padding"]
        pygame.draw.rect(sidebar, UI["colors"]["background"], mid_right_rect)
        content_rect = pygame.Rect(
            mid_right_rect.x + UI["hud_inner_padding"],
            mid_right_rect.y + UI["hud_inner_padding"],
            mid_right_rect.width - UI["hud_inner_padding"] * 2,
            mid_right_rect.height - UI["hud_inner_padding"] * 2,
        )
        # render_text(
        #     screen=sidebar,
        #     text="[ Enemy/Ally Profile Pic ]",
        #     font_size=UI["font_sizes"]["medium"],
        #     color=UI["colors"]["secondary"],
        #     pos=content_rect.midtop,
        #     align="center",
        # )
        render_text(
            screen=sidebar,
            text="[ Enemy/Ally Dialogue ]",
            font_size=UI["font_sizes"]["medium"],
            color=UI["colors"]["secondary"],
            pos=content_rect.center,
            align="center",
        )

    def draw_btm_right(self, sidebar):
        """Hints"""
        btm_right_rect = pygame.Rect(
            0,
            0,
            self.game.sidebar_r_surface.get_width() * 0.5,
            UI["hud_bottom_section_height"],
        )
        btm_right_rect.bottomleft = sidebar.get_rect().bottomleft
        btm_right_rect.x += UI["hud_inner_padding"]
        btm_right_rect.y -= UI["hud_inner_padding"]
        pygame.draw.rect(sidebar, UI["colors"]["background"], btm_right_rect)
        content_rect = pygame.Rect(
            btm_right_rect.x + UI["hud_inner_padding"],
            btm_right_rect.y + UI["hud_inner_padding"],
            btm_right_rect.width - UI["hud_inner_padding"] * 2,
            btm_right_rect.height - UI["hud_inner_padding"] * 2,
        )
        render_text(
            screen=sidebar,
            text="[Esc] to Pause Game",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["secondary"],
            pos=content_rect.midleft,
            align="midleft",
        )

    def update(self, dt):
        if self.dialogue_timer > 0:
            self.dialogue_timer -= dt
        else:
            self.current_speaker = None
            self.current_text = None

    def draw(self, sidebar_l_surface, sidebar_r_surface):
        self.draw_top_left(sidebar_l_surface)
        self.draw_mid_left(sidebar_l_surface)
        self.draw_btm_left(sidebar_l_surface)

        self.draw_top_right(sidebar_r_surface)
        self.draw_mid_right(sidebar_r_surface)
        self.draw_btm_right(sidebar_r_surface)
