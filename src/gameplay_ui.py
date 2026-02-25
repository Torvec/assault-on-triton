import pygame
import data.settings as ui
import data.assets as a
from src.render_text import render_text
from data.dialogue import SCRIPTED
from data.messages import MESSAGES


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

        # hud icons
        self.hp_hud_icon = pygame.image.load(a.HP_HUD_ICON).convert_alpha()
        self.bomb_ammo_hud_icon = pygame.image.load(
            a.BOMB_AMMO_HUD_ICON
        ).convert_alpha()
        self.pwr_lvl_hud_icon = pygame.image.load(a.PWR_LVL_HUD_ICON).convert_alpha()

    def display_dialogue(self, dialogue_id):
        dialogue = SCRIPTED[dialogue_id]
        self.current_speaker = dialogue["speaker"]
        self.current_portrait = dialogue["portrait"]
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

        height = 16 * scale_factor
        width = gs_rect.width - 8 * scale_factor

        rect = pygame.Rect(0, 0, width, height)
        rect.x = 4 * scale_factor
        rect.y = 4 * scale_factor

        render_text(
            screen=surface,
            text="SCORE:",
            font_path=a.ZENDOTS_FONT,
            font_size=8,
            scale_factor=scale_factor,
            color="#E6D819",
            pos=rect.topleft,
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"{self.gameplay.score_manager.score:09}",
            font_path=a.ZENDOTS_FONT,
            font_size=8,
            scale_factor=scale_factor,
            color="white",
            pos=(rect.topleft[0] + 42 * scale_factor, rect.topleft[1]),
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"x{self.gameplay.score_manager.multiplier}",
            font_path=a.ZENDOTS_FONT,
            font_size=8,
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
                font_path=a.ZENDOTS_FONT,
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
            surface.get_width() - 8 * scale_factor,
            48 * scale_factor,
        )
        rect.bottomleft = surface.get_rect().bottomleft
        rect.x += 4 * scale_factor
        rect.y -= 24 * scale_factor

        pygame.draw.rect(surface, "grey10", rect)

        content_rect = pygame.Rect(
            rect.x + 4 * scale_factor,
            rect.y + 4 * scale_factor,
            rect.width - 4 * scale_factor,
            rect.height - 4 * scale_factor,
        )

        portrait = pygame.image.load(self.current_portrait)
        portrait_rect = portrait.get_rect()
        portrait_rect.topleft = content_rect.topleft
        surface.blit(portrait, portrait_rect)

        render_text(
            screen=surface,
            text=self.current_speaker,
            font_path=a.ZENDOTS_FONT,
            font_size=10,
            scale_factor=scale_factor,
            color="gray80",
            pos=(
                content_rect.topleft[0] + portrait.get_width() + 4 * scale_factor,
                content_rect.topleft[1],
            ),
            align="topleft",
        )
        render_text(
            screen=surface,
            text=self.current_dialogue,
            font_size=8,
            scale_factor=scale_factor,
            color="gray80",
            pos=(
                content_rect.midleft[0] + portrait.get_width() + 4 * scale_factor,
                content_rect.midleft[1],
            ),
            align="midleft",
        )

    def scale_icon(self, icon, scale_factor):
        w = int(icon.get_width() * scale_factor)
        h = int(icon.get_height() * scale_factor)
        return pygame.transform.scale(icon, (w, h))

    def draw_player_status_hud(self, surface, scale_factor):
        if not self.gameplay.entity_manager.player_group.sprite:
            return

        player = self.gameplay.entity_manager.player_group.sprite
        gs_rect = surface.get_rect()

        hud_height = 16 * scale_factor
        hud_width = gs_rect.width - 8 * scale_factor
        hud_rect = pygame.Rect(0, 0, hud_width, hud_height)
        hud_rect.midbottom = (gs_rect.centerx, gs_rect.bottom - 4 * scale_factor)

        power_display = ui.UI["power_levels"].get(player.power_level, "?")
        sections = [
            (self.scale_icon(self.hp_hud_icon, scale_factor), f"{player.hp}%"),
            (
                self.scale_icon(self.bomb_ammo_hud_icon, scale_factor),
                f"x {player.bomb_ammo}",
            ),
            (
                self.scale_icon(self.pwr_lvl_hud_icon, scale_factor),
                f"Lv. {power_display}",
            ),
        ]

        section_width = hud_rect.width // len(sections)
        gap = 2 * scale_factor

        for i, (icon, text) in enumerate(sections):
            section_rect = pygame.Rect(
                hud_rect.x + i * section_width,
                hud_rect.y,
                section_width,
                hud_rect.height,
            )
            text_surf = pygame.font.Font(a.ZENDOTS_FONT, int(8 * scale_factor)).render(
                text, False, "#E6D819"
            )
            total_width = icon.get_width() + gap + text_surf.get_width()
            start_x = section_rect.centerx - total_width // 2

            icon_rect = icon.get_rect(midleft=(start_x, section_rect.centery))
            surface.blit(icon, icon_rect)

            text_rect = text_surf.get_rect(
                midleft=(icon_rect.right + gap, section_rect.centery)
            )
            surface.blit(text_surf, text_rect)

    def update(self, dt):
        self.handle_dialogue_duration(dt)
        self.handle_message_duration(dt)

    def draw_ui(self, ui_surface, scale_factor):
        self.draw_score(ui_surface, scale_factor)
        self.draw_message_overlay(ui_surface, scale_factor)
        self.draw_dialogue_box(ui_surface, scale_factor)
        self.draw_player_status_hud(ui_surface, scale_factor)
