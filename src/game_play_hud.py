import pygame
from src.render_text import render_text


class GamePlayHUD:
    def __init__(self, game_play):
        self.game_play = game_play
        self.width = self.game_play.game.screen_w
        self.height = 128
        self.game_play_hud_rect = pygame.Rect(
            0, self.game_play.game.screen_h - self.height, self.width, self.height
        )

    def draw(self, screen):
        pygame.draw.rect(screen, "grey5", self.game_play_hud_rect)
        # LIVES
        render_text(
            screen=screen,
            text="Lives",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] - 144,
                self.game_play_hud_rect.center[1],
            ),
        )
        render_text(
            screen=screen,
            text=f"{self.game_play.player.lives}",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] - 144,
                self.game_play_hud_rect.center[1] + 36,
            ),
        )
        # EVENT
        render_text(
            screen=screen,
            text="Event",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] - 48,
                self.game_play_hud_rect.center[1],
            ),
        )
        render_text(
            screen=screen,
            text=f"{self.game_play.sequence_manager.current_event}",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] - 48,
                self.game_play_hud_rect.center[1] + 36,
            ),
        )
        # TARGETS
        render_text(
            screen=screen,
            text="Targets",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 48,
                self.game_play_hud_rect.center[1],
            ),
        )
        render_text(
            screen=screen,
            text=f"{len(self.game_play.active_targets)}",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 48,
                self.game_play_hud_rect.center[1] + 36,
            ),
        )
        # SCORE
        render_text(
            screen=screen,
            text="Score",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 144,
                self.game_play_hud_rect.center[1],
            ),
        )
        render_text(
            screen=screen,
            text=f"{self.game_play.score.show_score()}",
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 144,
                self.game_play_hud_rect.center[1] + 36,
            ),
        )
