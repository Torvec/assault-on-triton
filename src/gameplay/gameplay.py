import pygame

from src.screen import Screen

# Entities
from src.entities.player_ship import Player
from src.entities.shot import Shot
from src.entities.bomb import Bomb
from src.entities.explosion import Explosion
from src.entities.asteroid import Asteroid
from src.entities.enemy_drone import EnemyDrone
from src.entities.enemy_ship import EnemyShip
from src.entities.missile import Missile
from src.entities.pickup import Pickup

# Managers
from src.gameplay.event_manager import EventManager
from src.gameplay.spawn_manager import SpawnManager
from src.gameplay.score_manager import ScoreManager
from src.gameplay.collision_manager import CollisionManager
from src.data.event_timeline import TIMELINE

# UI
from src.gameplay.pause_menu import PauseMenu
from src.gameplay.gameplay_hud import GamePlayHUD

# Backgrounds
from src.backgrounds.background import StarField, Planet, PlanetTwo


class GamePlay(Screen):

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
        self.score = ScoreManager(self.game.score_store)
        self.isPaused = False
        self.pause_menu = PauseMenu(self)
        self.event_manager = EventManager(self, TIMELINE)
        self.active_targets = set()
        # ! Need a better way to handle background layers, this is kind of shit
        self.background = StarField(0, 0, self.game)
        self.background_2 = Planet(256, self.game.gs_h - 196, self.game)
        self.background_3 = PlanetTwo(self.game.gs_w // 2, -128, self.game)

        # Level completion tracking
        self.level_complete = False
        self.level_end_timer = 0
        self.level_end_delay = 10.0

        # Sprite Groups
        self.asteroids = pygame.sprite.Group()
        self.enemy_drones = pygame.sprite.Group()
        self.enemy_ships = pygame.sprite.Group()
        self.missiles = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.pickups = pygame.sprite.Group()

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
        Pickup.containers = (self.pickups, self.updateable, self.drawable)

        self.player = Player(
            self.play_area_rect.width // 2,
            self.play_area_rect.height - 100,
            self,
        )

        # Has to go after every sprite is loaded so they can be accessed
        self.collision_manager = CollisionManager(self)

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
                self.score.store_score(self.score.score)
                self.game.set_scene("GameOver")

    def update(self, dt, events):
        self.pause_menu.update(events)
        if not self.isPaused:
            super().update(dt)
            self.elapsed_time += dt
            self.collision_manager.handle_all_collisions()
            self.event_manager.update(dt)
            self.score.update_streak_meter_decay(dt)
            self.handle_level_complete(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        self.pause_menu.draw(game_surface)
        self.game_play_hud.draw(sidebar_l_surface, sidebar_r_surface)
