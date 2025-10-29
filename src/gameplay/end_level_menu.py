import pygame
from src.utils.render_text import render_text


class EndLevelMenu:

    def __init__(self, game_play):
        self.game_play = game_play
        self.menu_title = "Mission Complete!"
        self.menu_items = [
            f"Score: {self.game_play.game.score_store.current_score}",
            f"Time: {self.game_play.game_timer}",
            "[ENTER] Credits",
        ]
        self.show_menu = False
        self.start_outro = False

    def handle_event(self, events):
        if not self.show_menu:
            return

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.show_menu = False
                    if not self.start_outro:
                        self.start_outro = True
                        move_player_to_top = {
                            "event": "move_player_to",
                            "params": {"x": 304, "y": -96, "speed": 300},
                        }
                        self.game_play.event_manager.handle_event(move_player_to_top)

        if self.start_outro:
            if self.game_play.player.scripted_movement_active:
                return
            self.game_play.game.set_scene("Credits")

    def draw(self, game_surface):
        if not self.show_menu:
            return

        rect = pygame.Rect(
            0,
            0,
            game_surface.get_width() * 0.75,
            game_surface.get_height() * 0.3,
        )
        rect.center = game_surface.get_rect().center
        pygame.draw.rect(game_surface, "grey4", rect, border_radius=24)
        pygame.draw.rect(game_surface, "grey70", rect, width=4, border_radius=24)
        render_text(
            screen=game_surface,
            text=self.menu_title,
            font_name="zendots",
            font_size=32,
            pos=(rect.midtop[0], rect.midtop[1] + 8),
            align="midtop",
        )
        for i, item in enumerate(self.menu_items):
            render_text(
                screen=game_surface,
                text=item,
                font_name="spacegrotesk_semibold",
                font_size=32,
                color="grey",
                pos=(
                    rect.midtop[0],
                    rect.midtop[1] + 64 + (i * 48),
                ),
                align="midtop",
            )
