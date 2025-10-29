import pygame

from src.screen import Screen

from src.gameplay.background import StarField, Planet, PlanetTwo

# Entities
from src.entities.player_ship import Player
from src.entities.projectile import Shot, Bomb, Missile
from src.entities.explosion import Explosion
from src.entities.enemy import Asteroid, EnemyDrone, EnemyShip
from src.entities.pickup import Pickup

# Managers
from src.gameplay.event_manager import EventManager
from src.gameplay.score_manager import ScoreManager
from src.gameplay.collision_manager import CollisionManager

# Data
from src.data.event_timeline import TIMELINE

# UI
from src.gameplay.pause_menu import PauseMenu
from src.gameplay.gameplay_hud import GamePlayHUD
from src.gameplay.end_level_menu import EndLevelMenu


class GamePlay(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.game_timer = 0
        self.play_area_rect = pygame.Rect(
            0,
            0,
            self.game.game_surface.get_width(),
            self.game.game_surface.get_height(),
        )
        self.backgrounds = [
            StarField(0, 0, self.game),
            Planet(
                self.play_area_rect.midbottom[0],
                self.play_area_rect.midbottom[1],
                self.game,
            ),
            PlanetTwo(
                self.play_area_rect.midtop[0],
                self.play_area_rect.midtop[1] - 128,
                self.game,
            ),
        ]
        self.game_play_hud = GamePlayHUD(self.game, self)
        self.score = ScoreManager(self.game.score_store)
        self.is_paused = False
        self.pause_menu = PauseMenu(self)
        self.event_manager = EventManager(self, TIMELINE)
        self.end_level_menu = EndLevelMenu(self)
        self.level_complete = False

        # Sprite Groups
        self.player_group = pygame.sprite.GroupSingle()
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
        Player.containers = (self.player_group, self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)
        Bomb.containers = (self.bombs, self.updateable, self.drawable)
        Explosion.containers = (self.explosions, self.updateable, self.drawable)
        Pickup.containers = (self.pickups, self.updateable, self.drawable)

        self.player = Player(
            self.play_area_rect.midbottom[0],
            self.play_area_rect.midbottom[1],
            self,
        )

        self.collision_manager = CollisionManager(self)

    def handle_game_over(self):
        if self.player.lives < 1:
            self.score.store_score(self.score.score)
            self.game.set_scene("GameOver")

    def handle_level_complete(self, dt):
        timeline_index = self.event_manager.timeline_index
        timeline_length = len(self.event_manager.timeline)
        hostile_count = (
            len(self.asteroids) + len(self.enemy_drones) + len(self.enemy_ships)
        )

        if timeline_index >= timeline_length and hostile_count == 0:
            if not self.level_complete:
                self.level_complete = True
                self.level_end_timer = 5

            self.level_end_timer -= dt
            if self.level_end_timer <= 0 and not self.end_level_menu.show_menu:
                self.score.store_score(self.score.score)
                # fmt: off
                move_player_to_center = {
                        "event": "move_player_to",
                        "params": {"x": 304, "y": 540, "speed": 200},
                    }
                # fmt: on
                self.event_manager.handle_event(move_player_to_center)
                self.end_level_menu.show_menu = True

    def handle_event(self, events):
        self.pause_menu.handle_event(events)
        self.end_level_menu.handle_event(events)

    def update(self, dt):
        if not self.is_paused:
            super().update(dt)
            self.game_timer += dt
            self.event_manager.update(dt)
            self.collision_manager.update()
            self.score.update_streak_meter_decay(dt)
            self.game_play_hud.update(dt)
            self.handle_game_over()
            self.handle_level_complete(dt)

    def draw(self, game_surface, sidebar_l_surface, sidebar_r_surface):
        super().draw(game_surface, sidebar_l_surface, sidebar_r_surface)
        self.game_play_hud.draw(sidebar_l_surface, game_surface, sidebar_r_surface)
        self.pause_menu.draw(game_surface)
        self.end_level_menu.draw(game_surface)
