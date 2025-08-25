from ui.render_text import render_text


class GamePlayHUD:
    def __init__(self, game, game_play):
        self.game = game
        self.game_play = game_play

    def draw(self):
        render_text(
            screen=self.game.screen,
            text=f"Lives: {self.game_play.player.lives}",
            color="grey90",
            pos=(self.game.screen_w // 4, self.game.screen_h - 64),
        )
        render_text(
            screen=self.game.screen,
            text=f"Score: {self.game_play.score.show_score()}",
            color="grey90",
            pos=(self.game.screen_w // 2, self.game.screen_h - 64),
        )
        render_text(
            screen=self.game.screen,
            text=f"Targets: {self.game_play.asteroid_spawner.show_target_amount()}",
            color="grey90",
            pos=(self.game.screen_w // 3, self.game.screen_h - 64),
        )
