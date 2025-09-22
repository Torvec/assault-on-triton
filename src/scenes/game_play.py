import pygame
from src.scenes.scene import Scene
from src.entities import *
from src.event_manager import EventManager
from src.spawn_manager import SpawnManager
from src.event_timeline import TIMELINE
from src.pause_menu import PauseMenu
from src.game_play_hud import GamePlayHUD


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
        self.event_manager = EventManager(self, TIMELINE)
        self.active_targets = set()

        # Level completion tracking
        self.level_complete = False
        self.level_end_timer = 0
        self.level_end_delay = 5.0  # 5 seconds delay

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
                    # Check if entity should be destroyed after hitting player
                    if entity.hp <= 0:
                        handler["destroy_method"](entity)
                        self.score.handle_score(entity.score_value)
                    if self.player.shield <= 0:
                        self.player.lives -= 1
                        Explosion(
                            self.player.position.x,
                            self.player.position.y,
                            self.player.blast_radius,
                            self,
                        )
                        self.player.respawn()
                    if self.player.lives <= 0:
                        self.game.set_scene("GameOver")

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

    def handle_level_complete(self, dt):
        if (
            len(self.active_targets) == 0
            and self.event_manager.current_index >= len(self.event_manager.timeline)
            and not self.level_complete
        ):
            self.level_complete = True
            self.level_end_timer = self.level_end_delay

        if self.level_complete:
            self.level_end_timer -= dt
            if self.level_end_timer <= 0:
                self.game.set_scene("GameOver")

    def update(self, dt, events):
        self.pause_menu.update(events)
        if not self.isPaused:
            super().update(dt)
            self.elapsed_time += dt
            self.handle_collisions()
            self.event_manager.update(dt)
            self.score.update_streak_meter_decay(dt)
            self.handle_level_complete(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        self.pause_menu.draw(game_surface)
        self.game_play_hud.draw(sidebar_l_surface, sidebar_r_surface)
