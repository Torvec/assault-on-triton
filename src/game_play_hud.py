import pygame
from src.render_text import render_text


class GamePlayHUD:

    def __init__(self, game_play):
        self.game_play = game_play
        self.width = self.game_play.game.gs_w
        self.height = 96
        self.game_play_hud_rect = pygame.Rect(
            0, 0, self.width, self.height
        )

    def draw(self, screen):
        pygame.draw.rect(screen, "grey5", self.game_play_hud_rect)

        # SCORE x MULTIPLIER
        render_text(
            screen=screen,
            text=f"Score: {self.game_play.score.score}",
            font_size=24,
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] - 256,
                self.game_play_hud_rect.center[1] - 24,
            ),
            align="midleft"
        )
        render_text(
            screen=screen,
            text=f"Score x{self.game_play.score.multiplier} T-{self.game_play.score.streak_timer:.2f}",
            font_size=24,
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] - 256,
                self.game_play_hud_rect.center[1] + 24,
            ),
            align="midleft",
        )

        # LIVES x SHIELD
        render_text(
            screen=screen,
            text=f"Shield x {self.game_play.player.shield}%",
            font_size=24,
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 256,
                self.game_play_hud_rect.center[1] - 24,
            ),
            align="midright",
        )
        render_text(
            screen=screen,
            text=f"Bombs x {self.game_play.player.bomb_ammo}",
            font_size=24,
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 256,
                self.game_play_hud_rect.center[1],
            ),
            align="midright",
        )
        render_text(
            screen=screen,
            text=f"Life x {self.game_play.player.lives}",
            font_size=24,
            color="grey90",
            pos=(
                self.game_play_hud_rect.center[0] + 256,
                self.game_play_hud_rect.center[1] + 24,
            ),
            align="midright"
        )
