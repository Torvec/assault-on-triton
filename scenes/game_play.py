import pygame
from global_consts import SCREEN_WIDTH, SCREEN_HEIGHT
from scenes.scene import Scene
from entities.player import Player
from entities.asteroid import Asteroid
from utils.asteroid_spawn_manager import AsteroidSpawnManager
from entities.shot import Shot
from scenes.game_over import GameOver

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
        self.score = 0

    def update(self, dt):
        super().update(dt)
        for asteroid in self.asteroids:
                if asteroid.collides_with(self.player):
                    self.game.set_scene(GameOver(self.game, self.screen, self.dt))
                for shot in self.shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        self.score += 1
    
    def draw(self, screen):
        super().draw(screen)

        score_font = pygame.font.Font(None, 32)
        score = score_font.render(f"Score: {self.score}", True, "grey90")
        score_rect = score.get_rect(center=(SCREEN_WIDTH // 2, 16))
        self.screen.blit(score, score_rect)