import pygame
from global_consts import SCREEN_WIDTH, SCREEN_HEIGHT
from scene import Scene
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from game_over import GameOver

class GamePlay(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        AsteroidField.containers = self.updateable
        AsteroidField()
        Player.containers = (self.updateable, self.drawable)
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        Shot.containers = (self.shots, self.updateable, self.drawable)

    def update(self, dt):
        super().update(dt)
        for asteroid in self.asteroids:
                if asteroid.collides_with(self.player):
                    self.game.set_scene(GameOver(self.game, self.screen, self.dt))
                for shot in self.shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
    
    def draw(self, screen):
        super().draw(screen)
