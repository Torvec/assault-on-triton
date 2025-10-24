import pygame
from src.utils.render_text import render_text
from src.data.settings import UI
from src.data.dialogue import SCRIPTED
from src.data.messages import MESSAGES


class GamePlayHUD:

    def __init__(self, game, game_play):
        self.game = game
        self.game_play = game_play
        self.current_speaker = None
        self.current_dialogue = None
        self.dialogue_timer = 0
        self.dialogue_location = None
        self.current_message = None
        self.message_timer = 0

    def display_dialogue(self, dialogue_id):
        dialogue = SCRIPTED[dialogue_id]
        self.current_speaker = dialogue["speaker"]
        self.current_portrait = dialogue["portrait"]
        self.current_dialogue = dialogue["text"]
        self.dialogue_timer = dialogue["timer"]
        self.dialogue_location = dialogue["location"]

    def handle_dialogue_timer(self, dt):
        if self.dialogue_timer > 0:
            self.dialogue_timer -= dt
            if self.dialogue_timer <= 0:
                self.current_speaker = None
                self.current_text = None
                self.dialogue_location = None

    def display_message(self, message_id):
        self.current_message = MESSAGES[message_id]["text"]
        self.message_timer = MESSAGES[message_id]["timer"]

    def handle_message_timer(self, dt):
        if self.message_timer > 0:
            self.message_timer -= dt
            if self.message_timer <= 0:
                self.current_message = None
                self.message_timer = 0

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
        return f"TIME: {mins:02}:{secs:02}:{ms:03}"

    def draw_top_left(self, surface):
        """Score, multiplier, high score, time."""
        top_left_rect = pygame.Rect(
            0,
            0,
            surface.get_width() * 0.5,
            UI["hud_top_section_height"],
        )
        top_left_rect.topleft = surface.get_rect().midtop
        top_left_rect.x -= UI["hud_inner_padding"]
        top_left_rect.y += UI["hud_inner_padding"]
        pygame.draw.rect(surface, UI["colors"]["background"], top_left_rect)
        content_rect = pygame.Rect(
            top_left_rect.x + UI["hud_inner_padding"],
            top_left_rect.y + UI["hud_inner_padding"],
            top_left_rect.width - UI["hud_inner_padding"] * 2,
            top_left_rect.height - UI["hud_inner_padding"] * 2,
        )
        render_text(
            screen=surface,
            text=f"SCORE: {self.game_play.score.score:,}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"x{self.game_play.score.multiplier}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topright,
            align="topright",
        )
        self.draw_streak_meter(surface, content_rect)
        render_text(
            screen=surface,
            text=f"HI SCORE: {self.game.score_store.high_score:,}",
            font_name="zendots",
            font_size=UI["font_sizes"]["small"],
            color=UI["colors"]["primary"],
            pos=content_rect.bottomleft,
            align="bottomleft",
        )

    def draw_top_center(self, surface):
        """Enemy dialogue box."""
        if self.dialogue_location == "top":
            rect = pygame.Rect(
                UI["hud_inner_padding"],
                UI["hud_inner_padding"],
                surface.get_width() - UI["hud_inner_padding"] * 2,
                192,
            )
            pygame.draw.rect(surface, UI["colors"]["background"], rect)
            content_rect = pygame.Rect(
                rect.x + UI["hud_inner_padding"],
                rect.y + UI["hud_inner_padding"],
                rect.width - UI["hud_inner_padding"] * 2,
                rect.height - UI["hud_inner_padding"] * 2,
            )
            portrait = pygame.image.load(self.current_portrait)
            portrait_rect = portrait.get_rect()
            portrait_rect.topleft = content_rect.topleft
            surface.blit(portrait, portrait_rect)
            render_text(
                screen=surface,
                text=self.current_speaker,
                font_name="zendots",
                font_size=UI["font_sizes"]["large"],
                color=UI["colors"]["secondary"],
                pos=(
                    content_rect.topleft[0] + portrait.get_width() + 16,
                    content_rect.topleft[1],
                ),
                align="topleft",
            )
            render_text(
                screen=surface,
                text=self.current_dialogue,
                font_size=UI["font_sizes"]["large"],
                color=UI["colors"]["secondary"],
                pos=(
                    content_rect.midleft[0] + portrait.get_width() + 16,
                    content_rect.midleft[1],
                ),
                align="bottomleft",
            )

    def draw_mid_center(self, surface):
        if self.current_message:
            render_text(
                screen=surface,
                text=self.current_message,
                font_name="zendots",
                font_size=48,
                color="yellow",
                pos=surface.get_rect().center,
                align="center",
            )

    def draw_btm_center(self, surface):
        """Hero/Ally Dialogue Box"""
        if self.dialogue_location == "bottom":
            rect = pygame.Rect(
                0,
                0,
                surface.get_width() - UI["hud_inner_padding"] * 2,
                192,
            )
            rect.bottomleft = surface.get_rect().bottomleft
            rect.x += UI["hud_inner_padding"]
            rect.y -= UI["hud_inner_padding"]
            pygame.draw.rect(surface, UI["colors"]["background"], rect)
            content_rect = pygame.Rect(
                rect.x + UI["hud_inner_padding"],
                rect.y + UI["hud_inner_padding"],
                rect.width - UI["hud_inner_padding"] * 2,
                rect.height - UI["hud_inner_padding"] * 2,
            )
            portrait = pygame.image.load(self.current_portrait)
            portrait_rect = portrait.get_rect()
            portrait_rect.topleft = content_rect.topleft
            surface.blit(portrait, portrait_rect)
            render_text(
                screen=surface,
                text=self.current_speaker,
                font_name="zendots",
                font_size=UI["font_sizes"]["large"],
                color=UI["colors"]["secondary"],
                pos=(
                    content_rect.topleft[0] + portrait.get_width() + 16,
                    content_rect.topleft[1],
                ),
                align="topleft",
            )
            render_text(
                screen=surface,
                text=self.current_dialogue,
                font_size=UI["font_sizes"]["large"],
                color=UI["colors"]["secondary"],
                pos=(
                    content_rect.midleft[0] + portrait.get_width() + 16,
                    content_rect.midleft[1],
                ),
                align="midleft",
            )

    def draw_top_right(self, surface):
        """Player stats: HP, lives, bombs, power level."""
        rect = pygame.Rect(
            UI["hud_inner_padding"],
            UI["hud_inner_padding"],
            surface.get_width() * 0.5,
            UI["hud_top_section_height"],
        )
        pygame.draw.rect(surface, UI["colors"]["background"], rect)
        content_rect = pygame.Rect(
            rect.x + UI["hud_inner_padding"],
            rect.y + UI["hud_inner_padding"],
            rect.width - UI["hud_inner_padding"] * 2,
            rect.height - UI["hud_inner_padding"] * 2,
        )
        render_text(
            screen=surface,
            text=f"HP x {self.game_play.player.hp}%",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"LIVES x {self.game_play.player.lives}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.midleft,
            align="midleft",
        )
        render_text(
            screen=surface,
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
            screen=surface,
            text=f"PWR LVL {power_display}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.bottomleft,
            align="bottomleft",
        )

    def update(self, dt):
        self.handle_dialogue_timer(dt)
        self.handle_message_timer(dt)

    def draw(self, sidebar_l_surface, game_surface, sidebar_r_surface):
        self.draw_top_left(sidebar_l_surface)

        self.draw_top_center(game_surface)
        self.draw_mid_center(game_surface)
        self.draw_btm_center(game_surface)

        self.draw_top_right(sidebar_r_surface)
