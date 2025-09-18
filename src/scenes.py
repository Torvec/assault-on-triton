import random
import pygame
from src.menus import *
from src.game_play_hud import GamePlayHUD
from src.sequence_manager import SequenceManager
from src.spawn_manager import SpawnManager
from src.entities import *
from src.render_text import render_text


class Scene:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.stars = [
            (
                random.randint(0, self.game.gs_w),
                random.randint(0, self.game.gs_h),
            )
            for _ in range(150)
        ]

    def update(self, dt, events=None):
        self.updateable.update(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        game_surface.fill("grey4")
        sidebar_l_surface.fill("black")
        sidebar_r_surface.fill("black")
        # Draw star field
        for x, y in self.stars:
            pygame.draw.circle(game_surface, "grey70", (x, y), 1)
        for obj in self.drawable:
            obj.draw(game_surface)


class Start(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.start_menu = StartMenu(game)

    def update(self, dt, events):
        super().update(dt, events)
        self.start_menu.update(events)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)

        render_text(
            screen=game_surface,
            text="ASSAULT",
            font_size=128,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 304),
        )

        render_text(
            screen=game_surface,
            text="ON",
            font_size=96,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 224),
        )

        render_text(
            screen=game_surface,
            text="TRITON",
            font_size=128,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 128),
        )

        self.start_menu.draw(game_surface)


class GamePlay(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.elapsed_time = 0
        self.play_area_rect = pygame.Rect(
            0,
            0,
            self.game.gs_w,
            self.game.gs_h,
        )
        self.game_play_hud = GamePlayHUD(self.game, self)
        self.score = self.game.score_manager
        self.score.init_score_manager()
        self.isPaused = False
        self.pause_menu = PauseMenu(self)
        self.sequence_manager = SequenceManager(self)
        self.active_spawners = set()
        self.active_targets = set()

        # Sprite Groups
        self.asteroids = pygame.sprite.Group()
        self.enemy_drones = pygame.sprite.Group()
        self.enemy_ships = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        # Set containers attributes so the sprites automatically get added to the appropriate groups
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        EnemyDrone.containers = (self.enemy_drones, self.updateable, self.drawable)
        EnemyShip.containers = (self.enemy_ships, self.updateable, self.drawable)
        Missile.containers = (self.missiles, self.updateable, self.drawable)
        SpawnManager.containers = self.updateable
        Player.containers = (self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)
        Bomb.containers = (self.bombs, self.updateable, self.drawable)
        Explosion.containers = (self.explosions, self.updateable, self.drawable)

        self.player = Player(
            self.play_area_rect.width // 2,
            self.play_area_rect.height - 100,
            self,
        )

    def handle_collisions(self):
        collision_handlers = [
            {
                "group": self.asteroids,
                "destroy_method": lambda entity: entity.split(),
            },
            {
                "group": self.enemy_drones,
                "destroy_method": lambda entity: entity.explode(),
            },
            {
                "group": self.enemy_ships,
                "destroy_method": lambda entity: entity.explode(),
            },
            {
                "group": self.missiles,
                "destroy_method": lambda entity: entity.explode(),
            },
        ]

        # ! TODO: This needs to be refactored before it gets WAY out of hand
        for handler in collision_handlers:
            for entity in handler["group"]:
                # Player collision
                if (
                    entity.collides_with(self.player)
                    and self.player.invincibleTime == 0
                ):
                    self.player.invincibleTime = 2
                    self.player.shield -= 5
                    self.player.is_hit = True
                    entity.hp -= 1
                    self.score.handle_streak_meter_dec()
                    if self.player.shield <= 0:
                        self.player.lives -= 1
                        Explosion(
                            self.player.position.x, self.player.position.y, 128, self
                        )
                        self.player.respawn()
                    if self.player.lives <= 0:
                        self.game.set_scene(GameOver(self.game))
                        # self.game.set_scene(GamePlay(self.game))

                # Shot collision
                for shot in self.shots:
                    if shot.collides_with(entity):
                        entity.is_hit = True
                        shot.kill()
                        entity.hp -= 1
                        if entity.hp <= 0:
                            handler["destroy_method"](entity)
                            self.score.handle_score(entity.score_value)
                            self.score.handle_streak_meter_inc(entity.score_value)

                # Bomb collision
                for bomb in self.bombs:
                    if bomb.collides_with(entity):
                        Explosion(
                            bomb.position.x, bomb.position.y, bomb.blast_radius, self
                        )
                        bomb.kill()

                # Explosion Collision
                for explosion in self.explosions:
                    if explosion.collides_with(entity):
                        entity.is_hit = True
                        entity.hp -= 5
                        if entity.hp <= 0:
                            handler["destroy_method"](entity)
                            self.score.handle_score(entity.score_value)
                            self.score.handle_streak_meter_inc(entity.score_value)

    def handle_event_sequence(self):
        if not self.active_targets and not self.active_spawners:
            if self.sequence_manager.event_active:
                self.sequence_manager.set_current_event()
            self.sequence_manager.run_sequence()

    def update(self, dt, events):
        self.pause_menu.update(events)
        if not self.isPaused:
            super().update(dt)
            self.elapsed_time += dt
            self.handle_collisions()
            self.handle_event_sequence()
            self.score.update_streak_meter_decay(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        self.pause_menu.draw(game_surface)
        self.game_play_hud.draw(sidebar_l_surface, sidebar_r_surface)


class GameOver(Scene):

    def __init__(self, game):
        super().__init__(game)
        self.score = game.score_manager
        self.game_over_menu = GameOverMenu(game)

    def update(self, dt, events):
        super().update(dt, events)

        self.game_over_menu.update(events)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)

        render_text(
            screen=game_surface,
            text="GAME OVER",
            font_size=128,
            pos=(game_surface.get_width() // 2, game_surface.get_height() // 2 - 256),
        )

        self.game_over_menu.draw(game_surface)


class Options(Scene):

    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(Start(self.game))

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)

        render_text(
            screen=game_surface,
            text="OPTIONS",
            font_size=64,
            pos=(game_surface.get_width() // 2, 64),
        )

        render_text(
            screen=game_surface,
            text="scores go here",
            color="grey",
            pos=(game_surface.get_width() // 2, 128),
        )


class Scoreboard(Scene):

    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(Start(self.game))

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)

        render_text(
            screen=game_surface,
            text="HIGH SCORES",
            font_size=64,
            pos=(game_surface.get_width() // 2, 64),
        )

        render_text(
            screen=self.game.game_surface,
            text="scores go here",
            color="grey",
            pos=(game_surface.get_width() // 2, 128),
        )


class Credits(Scene):

    def __init__(self, game):
        super().__init__(game)

    def update(self, dt, events):
        super().update(dt, events)

        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.set_scene(Start(self.game))

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)

        render_text(
            screen=game_surface,
            text="CREDITS",
            font_size=64,
            pos=(game_surface.get_width() // 2, 64),
        )

        render_text(
            screen=game_surface,
            text="Credits go here",
            color="grey",
            pos=(game_surface.get_width() // 2, 128),
        )
