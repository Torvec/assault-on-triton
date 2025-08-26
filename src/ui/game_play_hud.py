import pygame
from src.ui.render_text import render_text


class GamePlayHUD:
    def __init__(self, game, game_play):
        self.game = game
        self.game_play = game_play
        self.game_play_hud_rect = pygame.Rect(
            0, self.game.screen_h - 128, self.game.screen_w, 128
        )

    def draw(self, screen):
        pygame.draw.rect(screen, "grey10", self.game_play_hud_rect)
        render_text(
            screen=screen,
            text=f"Lives: {self.game_play.player.lives}",
            color="grey90",
            pos=(
                self.game_play_hud_rect.midleft[0] + 36,
                self.game_play_hud_rect.midleft[1],
            ),
            align="midleft",
        )
        render_text(
            screen=screen,
            text=f"Score: {self.game_play.score.show_score()}",
            color="grey90",
            pos=self.game_play_hud_rect.center,
        )
        render_text(
            screen=screen,
            text=f"Targets: {self.game_play.asteroid_spawner.show_target_amount()} {self.game_play.enemy_ship_spawner.show_target_amount()}",
            color="grey90",
            pos=(
                self.game_play_hud_rect.midright[0] - 36,
                self.game_play_hud_rect.midright[1],
            ),
            align="midright",
        )
