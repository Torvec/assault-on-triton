import pygame
import random
from src.menus import *
from src.wave_manager import WaveManager
from src.spawner import AsteroidSpawner, EnemyShipSpawner
from src.entities import Player, Asteroid, EnemyShip, Shot
from src.game_play_hud import GamePlayHUD
from src.render_text import render_text


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


class Start(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.start_menu = StartMenu(game)

    def update(self, dt, events):
        super().update(dt, events)
        self.start_menu.update(events)

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="ASTEROIDS",
            font_size=128,
            pos=(self.game.screen_w // 2, self.game.screen_h // 2 - 128),
        )

        self.start_menu.draw(screen)


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

    def handle_collisions(self):
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

    def update(self, dt, events):

        self.pause_menu.update(events)

        if not self.isPaused:
            super().update(dt)
            self.handle_collisions()

        if self.wave_manager.remaining_targets == 0:
            self.wave_manager.set_current_wave()
            AsteroidSpawner(
                self,
                self.wave_manager.waves[self.wave_manager.current_wave - 1][
                    "asteroids"
                ],
            )
            EnemyShipSpawner(
                self,
                self.wave_manager.waves[self.wave_manager.current_wave - 1][
                    "enemy_ships"
                ],
            )

    def draw(self, screen):
        super().draw(screen)
        self.game_play_hud.draw(screen)
        self.pause_menu.draw(screen)


class GameOver(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.score = game.score_manager
        self.game_over_menu = GameOverMenu(game)

    def update(self, dt, events):
        super().update(dt, events)

        self.game_over_menu.update(events)

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="GAME OVER",
            font_size=128,
            pos=(self.game.screen_w // 2, self.game.screen_h // 2 - 256),
        )

        self.game_over_menu.draw(screen)


class Options(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(Start(self.game))

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="OPTIONS",
            font_size=64,
            pos=(self.game.screen_w // 2, 64),
        )
        render_text(
            screen=self.game.screen,
            text="scores go here",
            color="grey",
            pos=(self.game.screen_w // 2, 128),
        )


class Scoreboard(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(Start(self.game))

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="HIGH SCORES",
            font_size=64,
            pos=(self.game.screen_w // 2, 64),
        )
        render_text(
            screen=self.game.screen,
            text="scores go here",
            color="grey",
            pos=(self.game.screen_w // 2, 128),
        )


class Credits(Scene):
    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(Start(self.game))

    def draw(self, screen):
        super().draw(screen)

        render_text(
            screen=self.game.screen,
            text="CREDITS",
            font_size=64,
            pos=(self.game.screen_w // 2, 64),
        )
        render_text(
            screen=self.game.screen,
            text="Credits go here",
            color="grey",
            pos=(self.game.screen_w // 2, 128),
        )
