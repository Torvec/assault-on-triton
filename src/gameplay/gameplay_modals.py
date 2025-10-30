import sys
import pygame
from src.utils.render_text import render_text


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
                if event.key == pygame.K_ESCAPE:
                    self.gameplay.is_paused = not self.gameplay.is_paused
                    self.is_visible = self.gameplay.is_paused
                elif self.gameplay.is_paused:
                    match event.key:
                        case pygame.K_1:
                            self.gameplay.game.set_scene("GamePlay")
                        case pygame.K_2:
                            self.gameplay.game.set_scene("Start")
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
        self.start_outro = False

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.is_visible = False
                    if not self.start_outro:
                        self.start_outro = True
                        move_player_to_top = {
                            "event": "move_player_to",
                            "params": {"x": 304, "y": -96, "speed": 300},
                        }
                        self.gameplay.event_manager.handle_event(move_player_to_top)

        if self.start_outro:
            if self.gameplay.player.scripted_movement_active:
                return
            self.gameplay.game.set_scene("Credits")


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
                        self.gameplay.game.set_scene("GamePlay")
                    case pygame.K_1:
                        self.gameplay.game.set_scene("Start")
                    case pygame.K_2:
                        self.gameplay.game.set_scene("Scoreboard")
                    case pygame.K_3:
                        self.gameplay.game.set_scene("Credits")
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()
