import pygame
from global_consts import SCREEN_WIDTH, SCREEN_HEIGHT
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
        AsteroidSpawnManager()
        Player.containers = (self.updateable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        Shot.containers = (self.shots, self.updateable, self.drawable)
        self.score = game.score_manager

    def update(self, dt):
        super().update(dt)
        for asteroid in self.asteroids:
                if asteroid.collides_with(self.player):
                    self.game.set_scene(GameOver(self.game, self.screen, self.dt))
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
            (SCREEN_WIDTH // 2, 16)
        )