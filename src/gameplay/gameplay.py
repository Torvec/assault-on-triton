import pygame

from src.screen import Screen

from src.gameplay.gameplay_states import (
    GameplayState,
    CutsceneState,
    PlayState,
    PausedState,
    GameOverState,
    MissionCompleteState,
)

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
from src.gameplay.gameplay_modals import PauseModal, GameOverModal, EndLevelModal
from src.gameplay.gameplay_ui import GamePlayUI


class GamePlay(Screen):

    def __init__(self, game):
        super().__init__(game)
        self.current_state = None
        self.previous_state = None
        self.states = {}
        self.game_timer = 0
        self.is_paused = False
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

        self.event_manager = EventManager(self, TIMELINE)
        self.collision_manager = CollisionManager(self)
        self.gameplay_ui = GamePlayUI(self.game, self)
        self.score = ScoreManager(self.game.score_store)
        self.pause_modal = PauseModal(self)
        self.end_level_modal = EndLevelModal(self)
        self.game_over_modal = GameOverModal(self)

        self.init_states()

    def init_states(self):
        self.states[GameplayState.CUTSCENE] = CutsceneState(self)
        self.states[GameplayState.PLAY] = PlayState(self)
        self.states[GameplayState.PAUSED] = PausedState(self)
        self.states[GameplayState.GAME_OVER] = GameOverState(self)
        self.states[GameplayState.MISSION_COMPLETE] = MissionCompleteState(self)

    def change_state(self, new_state):
        if self.current_state:
            self.states[self.current_state].exit()
            self.previous_state = self.current_state

        self.current_state = new_state
        self.states[self.current_state].enter()

    # def handle_level_complete(self, dt):
    #     timeline_index = self.event_manager.timeline_index
    #     timeline_length = len(self.event_manager.timeline)
    #     hostile_count = (
    #         len(self.asteroids) + len(self.enemy_drones) + len(self.enemy_ships)
    #     )

    #     if timeline_index >= timeline_length and hostile_count == 0:
    #         if not self.level_complete:
    #             self.level_complete = True
    #             self.level_end_timer = 5

    #         self.level_end_timer -= dt
    #         if self.level_end_timer <= 0 and not self.end_level_modal.is_visible:
    #             self.score.store_score(self.score.score)
    #             # fmt: off
    #             move_player_to_center = {
    #                     "event": "move_player_to",
    #                     "params": {"x": 304, "y": 540, "speed": 200},
    #                 }
    #             # fmt: on
    #             self.event_manager.handle_event(move_player_to_center)
    #             self.end_level_modal.is_visible = True

    def handle_event(self, events):
        if self.current_state:
            self.states[self.current_state].handle_event(events)

    def update(self, dt):
        super().update(dt)
        if self.current_state:
            self.states[self.current_state].update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        self.gameplay_ui.draw(display_surface, game_surface)
        if self.current_state:
            self.states[self.current_state].draw(game_surface)
