import random
import pygame
from src.menus import PauseMenu
from src.wave_manager import WaveManager
from src.spawner import EnemyShipSpawner, AsteroidSpawner
from src.entities import Player, Asteroid, EnemyShip, Shot
from src.game_play_hud import GamePlayHUD


class Scene:
    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.stars = [
            (
                random.randint(0, self.game.screen.get_width()),
                random.randint(0, self.game.screen.get_height()),
            )
            for _ in range(150)
        ]

    def update(self, dt, events=None):
        self.updateable.update(dt)

    def draw(self, screen):
        screen.fill("grey2")
        # Draw star field
        for x, y in self.stars:
            pygame.draw.circle(screen, "grey80", (x, y), 1)
        for obj in self.drawable:
            obj.draw(screen)


class GamePlay(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.game_play_hud = GamePlayHUD(self)
        self.play_area_rect = pygame.Rect(
            0, 0, self.game.screen_w, self.game.screen_h - self.game_play_hud.height
        )
        self.score = self.game.score_manager
        self.score.score = 0
        self.isPaused = False
        self.pause_menu = PauseMenu(self.game, self)
        self.wave_manager = WaveManager()

        # Sprite Groups
        self.asteroids = pygame.sprite.Group()
        self.enemy_ships = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()

        # Set containers attributes so the sprites automatically get added to the appropriate groups
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        EnemyShip.containers = (self.enemy_ships, self.updateable, self.drawable)
        AsteroidSpawner.containers = self.updateable
        EnemyShipSpawner.containers = self.updateable
        Player.containers = (self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)

        self.player = Player(
            self.play_area_rect.width // 2,
            self.play_area_rect.height // 2,
            self,
        )

        self.asteroid_spawner = AsteroidSpawner(
            self,
            self.wave_manager.waves[self.wave_manager.current_wave - 1]["asteroids"],
        )
        self.enemy_ship_spawner = EnemyShipSpawner(
            self,
            self.wave_manager.waves[self.wave_manager.current_wave - 1]["enemy_ships"],
        )

        self.collision_handlers = [
            {
                "group": self.asteroids,
                "destroy_method": lambda entity: entity.split(),
            },
            {
                "group": self.enemy_ships,
                "destroy_method": lambda entity: entity.explode(),
            },
        ]

    def update(self, dt, events):

        self.pause_menu.update(events)

        if not self.isPaused:
            super().update(dt)

            # Handle all entity types with a single loop
            for handler in self.collision_handlers:
                for entity in handler["group"]:
                    # Player collision
                    if (
                        entity.collides_with(self.player)
                        and self.player.invincibleTime == 0
                    ):
                        self.player.lives -= 1
                        handler["destroy_method"](entity)
                        if self.player.lives <= 0:
                            self.game.set_scene(GamePlay(self.game))
                        self.player.respawn()

                    # Shot collision
                    for shot in self.shots:
                        if shot.collides_with(entity):
                            shot.kill()
                            handler["destroy_method"](entity)
                            self.score.inc_score(1)

    def draw(self, screen):
        super().draw(screen)
        self.game_play_hud.draw(screen)
        self.pause_menu.draw(screen)
