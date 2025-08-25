import pygame
from scenes.scene import Scene
from managers.asteroid_spawn_manager import AsteroidSpawnManager
from entities.player import Player
from entities.asteroid import Asteroid
from entities.shot import Shot
from ui.pause_menu import PauseMenu
from ui.game_play_hud import GamePlayHUD


class GamePlay(Scene):
    def __init__(self, game):
        super().__init__(game)

        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        # Set containers attributes so the sprites automatically get added to the appropriate groups
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        AsteroidSpawnManager.containers = self.updateable
        Player.containers = (self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)

        self.play_area_rect = pygame.Rect(
            0, 0, self.game.screen_w, self.game.screen_h - 128
        )
        self.game_HUD_rect = pygame.Rect(
            0, self.game.screen_h - 128, self.game.screen_w, 128
        )

        self.asteroid_spawner = AsteroidSpawnManager(self.game, 10)
        self.player = Player(
            self.game, self.game.screen_w // 2, self.game.screen_h // 2
        )
        self.score = self.game.score_manager
        self.score.score = 0
        self.game_play_hud = GamePlayHUD(self.game, self)
        self.isPaused = False
        self.pause_menu = PauseMenu(self.game, self)

    def update(self, dt, events):

        self.pause_menu.update(events)

        if not self.isPaused:
            super().update(dt)

            for asteroid in self.asteroids:
                if (
                    asteroid.collides_with(self.player)
                    and self.player.invincibleTime == 0
                ):
                    self.player.lives -= 1
                    asteroid.split()
                    if self.player.lives <= 0:
                        from scenes.game_over import GameOver

                        self.game.scene_manager.set_scene(GameOver(self.game))
                    self.player.respawn()

                for shot in self.shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        self.asteroid_spawner.target_amount -= 1
                        self.score.inc_score(1)

    def draw(self, screen):
        super().draw(screen)
        self.game_play_hud.draw()
        self.pause_menu.draw(screen)
