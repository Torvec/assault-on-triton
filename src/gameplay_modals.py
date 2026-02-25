import sys
import pygame
import data.assets as a
from src.render_text import render_text


class Modal:
    def __init__(self, gameplay, title, menu_items):
        self.gameplay = gameplay
        self.title = title
        self.menu_items = menu_items
        self.is_visible = False

    def handle_event(self, events):
        pass

    def draw_ui(self, surface, scale_factor):
        if not self.is_visible:
            return

        rect = pygame.Rect(
            0,
            0,
            surface.get_width() - 4,
            surface.get_height() * 0.55,
        )
        rect.center = surface.get_rect().center
        pygame.draw.rect(surface, "grey4", rect, border_radius=12)
        pygame.draw.rect(surface, "grey70", rect, width=2, border_radius=12)

        render_text(
            screen=surface,
            text=self.title,
            font_path=a.ZENDOTS_FONT,
            font_size=18,
            scale_factor=scale_factor,
            pos=(rect.midtop[0], rect.midtop[1] + 8 * scale_factor),
            align="midtop",
        )

        for i, item in enumerate(self.menu_items):
            render_text(
                screen=surface,
                text=item,
                font_path=a.SPACEGROTESK_SEMIBOLD_FONT,
                font_size=16,
                scale_factor=scale_factor,
                color="grey",
                pos=(
                    rect.midtop[0],
                    rect.midtop[1] + 40 * scale_factor + (i * 24 * scale_factor),
                ),
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
                f"Time: {gameplay.game_timer:.2f}".replace(".", ":"),
                "[ENTER] Continue",
            ],
        )

    def handle_event(self, events):
        if not self.is_visible:
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.gameplay.event_manager.on_event_complete()


class GameOverModal(Modal):
    def __init__(self, gameplay):
        super().__init__(
            gameplay,
            title="Game Over",
            menu_items=[
                f"Score: {gameplay.game.score_store.get_current_score()}",
                f"Time: {gameplay.game_timer:.2f}".replace(".", ":"),
                "[Enter] Replay",
                "[1] Main Menu",
                "[2] Scoreboard",
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
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()
