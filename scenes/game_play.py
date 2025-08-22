import pygame
from scenes.scene import Scene
from entities.player import Player
from entities.asteroid import Asteroid
from utils.asteroid_spawn_manager import AsteroidSpawnManager
from entities.shot import Shot
from scenes.game_over import GameOver
from utils.render_text import render_text


class GamePlay(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        AsteroidSpawnManager.containers = self.updateable
        AsteroidSpawnManager(self.game)
        Player.containers = (self.updateable, self.drawable)
        self.player = Player(
            self.game, self.game.screen_w // 2, self.game.screen_h // 2
        )
        Shot.containers = (self.shots, self.updateable, self.drawable)
        self.score = game.score_manager
        self.score.score = 0
        self.isPaused = False
        print(self.isPaused)

    def update(self, dt, events):

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.isPaused = not self.isPaused
            if self.isPaused:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.game.scene_manager.set_scene(
                        GamePlay(self.game, self.screen, self.dt)
                    )
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    from scenes.main_menu import MainMenu

                    self.game.scene_manager.set_scene(
                        MainMenu(self.game, self.screen, self.dt)
                    )

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
                        self.game.scene_manager.set_scene(
                            GameOver(self.game, self.screen, self.dt)
                        )
                    self.player.respawn()

                for shot in self.shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        self.score.inc_score(1)

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            f"Score: {self.score.show_score()}",
            32,
            "grey90",
            (self.game.screen_w // 2, self.game.screen_h - 64),
        )

        render_text(
            self.screen,
            f"Lives: {self.player.lives}",
            32,
            "grey90",
            (self.game.screen_w // 4, self.game.screen_h - 64),
        )

        if self.isPaused:
            render_text(
                self.screen,
                "Paused",
                64,
                "white",
                (self.game.screen_w // 2, self.game.screen_h // 2),
            )
            render_text(
                self.screen,
                "[ESC] Resume",
                36,
                "grey",
                (self.game.screen_w // 2, self.game.screen_h // 2 + 36),
            )
            render_text(
                self.screen,
                "[1] Restart",
                36,
                "grey",
                (self.game.screen_w // 2, self.game.screen_h // 2 + 72),
            )
            render_text(
                self.screen,
                "[2] Main Menu",
                36,
                "grey",
                (self.game.screen_w // 2, self.game.screen_h // 2 + 108),
            )
