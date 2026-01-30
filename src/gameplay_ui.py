import pygame
from src.render_text import render_text
from data.settings import UI
from data.dialogue import SCRIPTED
from data.messages import MESSAGES
from data.assets import IMAGES


class GamePlayUI:

    def __init__(self, game, gameplay):
        self.game = game
        self.gameplay = gameplay
        self.game_surface_rect = self.game.game_surface.get_rect()

        # dialogue state
        self.current_speaker = None
        self.current_dialogue = None
        self.current_portrait = None
        self.dialogue_duration = 0

        # message state
        self.current_message = None
        self.message_duration = 0
        self.message_is_blocking = False

    def display_dialogue(self, dialogue_id):
        dialogue = SCRIPTED[dialogue_id]
        self.current_speaker = dialogue["speaker"]
        self.current_portrait = IMAGES[dialogue["portrait"]]
        self.current_dialogue = dialogue["text"]
        self.dialogue_duration = dialogue["duration"]

    def handle_dialogue_duration(self, dt):
        if self.dialogue_duration > 0:
            self.dialogue_duration -= dt
            if self.dialogue_duration <= 0:
                self.current_speaker = None
                self.current_text = None
                self.current_portrait = None
                self.dialogue_duration = 0
                self.gameplay.cutscene_manager.on_action_complete()

    def display_message(self, message_id):
        message = MESSAGES[message_id]
        self.current_message = message["text"]
        self.message_duration = message["duration"]
        self.message_is_blocking = message["blocking"]

        if not self.message_is_blocking:
            self.gameplay.event_manager.on_event_complete()

    def handle_message_duration(self, dt):
        if self.message_duration > 0:
            self.message_duration -= dt

            if self.message_duration <= 0:
                self.current_message = None
                self.message_duration = 0

                if self.message_is_blocking:
                    self.gameplay.event_manager.on_event_complete()

    def draw_score(self, surface, scale_factor):
        gs_rect = surface.get_rect()

        height = 16
        width = gs_rect.width - 8

        rect = pygame.Rect(0, 0, width, height)
        rect.topleft = (gs_rect.left + 4, gs_rect.top + 4)

        render_text(
            screen=surface,
            text=f"SCORE: {self.gameplay.score_manager.score:09}",
            font_name="zendots",
            font_size=10,
            scale_factor=scale_factor,
            color="#E6D819",
            pos=rect.topleft,
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"x{self.gameplay.score_manager.multiplier}",
            font_name="zendots",
            font_size=10,
            scale_factor=scale_factor,
            color="#E6D819",
            pos=rect.topright,
            align="topright",
        )

    def draw_message_overlay(self, surface, scale_factor):
        if self.current_message:
            render_text(
                screen=surface,
                text=self.current_message,
                font_name="zendots",
                font_size=18,
                scale_factor=scale_factor,
                color="#E6D819",
                pos=surface.get_rect().center,
                align="center",
            )

    def draw_dialogue_box(self, surface, scale_factor):
        if not (
            self.current_speaker and self.current_dialogue and self.current_portrait
        ):
            return

        rect = pygame.Rect(
            0,
            0,
            surface.get_width() - 8,
            48 * scale_factor,
        )
        rect.bottomleft = surface.get_rect().bottomleft
        rect.x += 4 * scale_factor
        rect.y -= 16 * scale_factor

        pygame.draw.rect(surface, "grey10", rect)

        content_rect = pygame.Rect(
            rect.x + 4,
            rect.y + 4,
            rect.width - 4,
            rect.height - 4,
        )

        portrait = pygame.image.load(self.current_portrait)
        portrait_rect = portrait.get_rect()
        portrait_rect.topleft = content_rect.topleft
        surface.blit(portrait, portrait_rect)

        render_text(
            screen=surface,
            text=self.current_speaker,
            font_name="zendots",
            font_size=16,
            scale_factor=scale_factor,
            color="gray80",
            pos=(
                content_rect.topleft[0] + portrait.get_width() + 4,
                content_rect.topleft[1],
            ),
            align="topleft",
        )
        render_text(
            screen=surface,
            text=self.current_dialogue,
            font_size=16,
            scale_factor=scale_factor,
            color="gray80",
            pos=(
                content_rect.midleft[0] + portrait.get_width() + 4,
                content_rect.midleft[1],
            ),
            align="midleft",
        )

    def draw_player_status_hud(self, surface, scale_factor):
        if not self.gameplay.entity_manager.player_group.sprite:
            return

        gs_rect = surface.get_rect()

        hud_height = 16
        hud_width = gs_rect.width - 8

        rect = pygame.Rect(0, 0, hud_width, hud_height)
        rect.midbottom = (gs_rect.centerx, gs_rect.bottom - 4)

        player = self.gameplay.entity_manager.player_group.sprite

        render_text(
            screen=surface,
            text=f"HP x {player.hp}%",
            font_size=12,
            scale_factor=scale_factor,
            color="#E6D819",
            pos=rect.bottomleft,
            align="bottomleft",
        )
        render_text(
            screen=surface,
            text=f"BOMBS x {player.bomb_ammo}",
            font_size=12,
            scale_factor=scale_factor,
            color="#E6D819",
            pos=rect.midbottom,
            align="midbottom",
        )
        power_display = UI["power_levels"].get(player.power_level, "( ? )")
        render_text(
            screen=surface,
            text=f"PWR LVL {power_display}",
            font_size=12,
            scale_factor=scale_factor,
            color="#E6D819",
            pos=rect.bottomright,
            align="bottomright",
        )

    def update(self, dt):
        self.handle_dialogue_duration(dt)
        self.handle_message_duration(dt)

    def draw_ui(self, ui_surface, scale_factor):
        self.draw_score(ui_surface, scale_factor)
        self.draw_message_overlay(ui_surface, scale_factor)
        self.draw_dialogue_box(ui_surface, scale_factor)
        self.draw_player_status_hud(ui_surface, scale_factor)
