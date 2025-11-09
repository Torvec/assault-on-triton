import sys
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
        self.ui_area_rect = pygame.Rect(
            0,
            0,
            1248,
            self.game.display_surface.get_height(),
        )
        self.ui_area_rect.center = self.game.display_surface.get_rect().center
        self.current_speaker = None
        self.current_dialogue = None
        self.dialogue_duration = 0
        self.dialogue_location = None
        self.current_message = None
        self.message_duration = 0

    def display_dialogue(self, dialogue_id):
        dialogue = SCRIPTED[dialogue_id]
        self.current_speaker = dialogue["speaker"]
        self.current_portrait = IMAGES[dialogue["portrait"]]
        self.current_dialogue = dialogue["text"]
        self.dialogue_duration = dialogue["duration"]
        self.dialogue_location = dialogue["location"]

    def handle_dialogue_duration(self, dt):
        if self.dialogue_duration > 0:
            self.dialogue_duration -= dt
            if self.dialogue_duration <= 0:
                self.current_speaker = None
                self.current_text = None
                self.dialogue_location = None

    def display_message(self, message_id):
        message = MESSAGES[message_id]
        self.current_message = message["text"]
        self.message_duration = message["duration"]

    def handle_message_duration(self, dt):
        if self.message_duration > 0:
            self.message_duration -= dt
            if self.message_duration <= 0:
                self.current_message = None
                self.message_duration = 0

    def draw_streak_meter(self, surface, rect):
        meter_border_rect = pygame.Rect(0, 0, rect.width, 16)
        meter_border_rect.midleft = rect.midleft
        pygame.draw.rect(surface, "white", meter_border_rect, 2, 4)
        fill_percent = (
            self.gameplay.score.streak_meter
            / self.gameplay.score.streak_meter_threshold
        )
        fill_width = int((rect.width - 4) * fill_percent)
        meter_fill_rect = pygame.Rect(0, 0, fill_width, 12)
        meter_fill_rect.midleft = meter_border_rect.midleft
        meter_fill_rect.x += 2
        pygame.draw.rect(surface, "grey50", meter_fill_rect)

    def draw_top_left(self, surface):
        """Score, multiplier, high score"""
        rect = pygame.Rect(
            0,
            0,
            self.ui_area_rect.width * 0.25,
            128,
        )
        rect.topleft = self.ui_area_rect.topleft
        rect.y += 16
        rect.x -= 16
        pygame.draw.rect(surface, UI["colors"]["background"], rect)
        content_rect = pygame.Rect(
            rect.x + 16,
            rect.y + 16,
            rect.width - 32,
            rect.height - 32,
        )
        render_text(
            screen=surface,
            text=f"SCORE: {self.gameplay.score.score:09}",
            font_name="zendots",
            font_size=UI["font_sizes"]["small"],
            color=UI["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"x{self.gameplay.score.multiplier}",
            font_name="zendots",
            font_size=UI["font_sizes"]["small"],
            color=UI["colors"]["primary"],
            pos=content_rect.topright,
            align="topright",
        )
        self.draw_streak_meter(surface, content_rect)
        render_text(
            screen=surface,
            text=f"HI SCORE: {self.game.score_store.high_score:09}",
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
                16,
                16,
                surface.get_width() - 4,
                192,
            )
            pygame.draw.rect(surface, UI["colors"]["background"], rect)
            content_rect = pygame.Rect(
                rect.x + 16,
                rect.y + 16,
                rect.width - 32,
                rect.height - 32,
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
        """For message overlays"""
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
                surface.get_width() - 32,
                192,
            )
            rect.bottomleft = surface.get_rect().bottomleft
            rect.x += 16
            rect.y -= 16
            pygame.draw.rect(surface, UI["colors"]["background"], rect)
            content_rect = pygame.Rect(
                rect.x + 16,
                rect.y + 16,
                rect.width - 16,
                rect.height - 16,
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
        if not self.gameplay.player_group.sprite:
            return

        rect = pygame.Rect(
            0,
            0,
            self.ui_area_rect.width * 0.25,
            128,
        )
        rect.topright = self.ui_area_rect.topright
        rect.y += 16
        rect.x += 16
        pygame.draw.rect(surface, UI["colors"]["background"], rect)
        content_rect = pygame.Rect(
            rect.x + 16,
            rect.y + 16,
            rect.width - 32,
            rect.height - 32,
        )
        render_text(
            screen=surface,
            text=f"HP x {self.gameplay.player_group.sprite.hp}%",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.topleft,
            align="topleft",
        )
        render_text(
            screen=surface,
            text=f"LIVES x {self.gameplay.player_group.sprite.lives}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.midleft,
            align="midleft",
        )
        render_text(
            screen=surface,
            text=f"BOMBS x {self.gameplay.player_group.sprite.bomb_ammo}",
            font_size=UI["font_sizes"]["large"],
            color=UI["colors"]["primary"],
            pos=content_rect.center,
            align="center",
        )
        power_display = UI["power_levels"].get(
            self.gameplay.player_group.sprite.power_level, "( ? )"
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
        self.handle_dialogue_duration(dt)
        self.handle_message_duration(dt)

    def draw(self, display_surface, game_surface):
        self.draw_top_left(display_surface)

        self.draw_top_center(game_surface)
        self.draw_mid_center(game_surface)
        self.draw_btm_center(game_surface)

        self.draw_top_right(display_surface)


class Modal:
    def __init__(self, gameplay, title, menu_items):
        self.gameplay = gameplay
        self.title = title
        self.menu_items = menu_items
        self.is_visible = False

    def handle_event(self, events):
        pass

    def draw(self, surface):
        if not self.is_visible:
            return

        rect = pygame.Rect(
            0,
            0,
            surface.get_width() * 0.75,
            surface.get_height() * 0.3,
        )
        rect.center = surface.get_rect().center
        pygame.draw.rect(surface, "grey4", rect, border_radius=24)
        pygame.draw.rect(surface, "grey70", rect, width=4, border_radius=24)

        render_text(
            screen=surface,
            text=self.title,
            font_name="zendots",
            font_size=48,
            pos=(rect.midtop[0], rect.midtop[1] + 8),
            align="midtop",
        )

        for i, item in enumerate(self.menu_items):
            render_text(
                screen=surface,
                text=item,
                font_name="spacegrotesk_semibold",
                font_size=32,
                color="grey",
                pos=(rect.midtop[0], rect.midtop[1] + 64 + (i * 48)),
                align="midtop",
            )


class PauseModal(Modal):
    def __init__(self, gameplay):
        super().__init__(
            gameplay,
            title="Game Paused",
            menu_items=[
                "[ESC] Resume",
                "[1] Restart",
                "[2] Start Menu",
                "[Q] Quit",
            ],
        )

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_1:
                        self.gameplay.game.change_screen("GamePlay")
                    case pygame.K_2:
                        self.gameplay.game.change_screen("Start")
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()


class EndLevelModal(Modal):
    def __init__(self, gameplay):
        super().__init__(
            gameplay,
            title="Mission Complete!",
            menu_items=[
                f"Score: {gameplay.game.score_store.current_score}",
                f"Time: {gameplay.game_timer}",
                "[ENTER] Credits",
            ],
        )
        # self.start_outro = False

    def handle_event(self, events):
        if not self.is_visible:
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.is_visible = False
                    outro_cutscene = {
                        "event": "trigger_cutscene",
                        "params": {"cutscene_id": "outro_2"},
                    }
                    self.gameplay.event_manager.handle_event(outro_cutscene)
        # for event in events:
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_RETURN:
        #             self.is_visible = False
        #             if not self.start_outro:
        #                 self.start_outro = True
        #                 move_player_to_top = {
        #                     "event": "move_player_to",
        #                     "params": {"x": 304, "y": -96, "speed": 300},
        #                 }
        #                 self.gameplay.event_manager.handle_event(move_player_to_top)

        # if self.start_outro:
        #     if self.gameplay.player_group.scripted_movement_active:
        #         return
        #     self.gameplay.game.change_screen("Credits")


class GameOverModal(Modal):
    def __init__(self, gameplay):
        super().__init__(
            gameplay,
            title="Game Over",
            menu_items=[
                "[Enter] Replay",
                "[1] Main Menu",
                "[2] Scoreboard",
                "[3] Credits",
                "[Q] Quit Game",
            ],
        )

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RETURN:
                        self.gameplay.game.change_screen("GamePlay")
                    case pygame.K_1:
                        self.gameplay.game.change_screen("Start")
                    case pygame.K_2:
                        self.gameplay.game.change_screen("Scoreboard")
                    case pygame.K_3:
                        self.gameplay.game.change_screen("Credits")
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()
