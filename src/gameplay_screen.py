import pygame
from src.screens import Screen
from src.backgrounds import Planet, PlanetTwo, StarField
from src.entities import (
    Asteroid,
    EnemyDrone,
    EnemyShip,
    SubBoss,
    LevelBoss,
    Missile,
    Shot,
    Bomb,
    Explosion,
    Pickup,
    Player,
)
from src.managers import (
    CollisionManager,
    EventManager,
    CutsceneManager,
    ScoreManager,
    BattleManager,
    WaveManager,
)
from src.gameplay_ui import GamePlayUI, PauseModal, EndLevelModal, GameOverModal
from src.gameplay_states import (
    GameplayState,
    InitState,
    PlayState,
    CutsceneState,
    PausedState,
    GameOverState,
    MissionCompleteState,
)
from data.event_queue import EVENT_QUEUE

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

        self.player_group = pygame.sprite.GroupSingle()
        self.asteroids = pygame.sprite.Group()
        self.enemy_drones = pygame.sprite.Group()
        self.enemy_ships = pygame.sprite.Group()
        self.sub_boss_group = pygame.sprite.GroupSingle()
        self.level_boss_group = pygame.sprite.GroupSingle()
        self.missiles = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.pickups = pygame.sprite.Group()

        Player.containers = (self.player_group, self.updateable, self.drawable)
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        EnemyDrone.containers = (self.enemy_drones, self.updateable, self.drawable)
        EnemyShip.containers = (self.enemy_ships, self.updateable, self.drawable)
        SubBoss.containers = (self.sub_boss_group, self.updateable, self.drawable)
        LevelBoss.containers = (self.level_boss_group, self.updateable, self.drawable)
        Missile.containers = (self.missiles, self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)
        Bomb.containers = (self.bombs, self.updateable, self.drawable)
        Explosion.containers = (self.explosions, self.updateable, self.drawable)
        Pickup.containers = (self.pickups, self.updateable, self.drawable)

        self.event_manager = EventManager(self, EVENT_QUEUE)
        self.wave_manager = WaveManager(self)
        self.battle_manager = BattleManager(self)
        self.cutscene_manager = CutsceneManager(self)
        self.collision_manager = CollisionManager(self)
        self.score_manager = ScoreManager(self.game.score_store)

        self.gameplay_ui = GamePlayUI(self.game, self)
        self.pause_modal = PauseModal(self)

        self.current_state = None
        self.previous_state = None
        self.states = {
            GameplayState.INIT: InitState(self),
            GameplayState.CUTSCENE: CutsceneState(self),
            GameplayState.PLAY: PlayState(self),
            GameplayState.PAUSED: PausedState(self),
            GameplayState.GAME_OVER: GameOverState(self),
            GameplayState.MISSION_COMPLETE: MissionCompleteState(self),
        }
        self.change_state(GameplayState.INIT)

    def create_game_over_modal(self):
        self.game_over_modal = GameOverModal(self)

    def create_end_level_modal(self):
        self.end_level_modal = EndLevelModal(self)

    def change_state(self, new_state):
        if self.current_state:
            self.states[self.current_state].exit()
            self.previous_state = self.current_state
        self.current_state = new_state
        self.states[self.current_state].enter()

    def handle_event(self, events):
        self.states[self.current_state].handle_event(events)

    def update(self, dt):
        if self.current_state != GameplayState.PAUSED:
            super().update(dt)
            self.gameplay_ui.update(dt)
        self.states[self.current_state].update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        self.gameplay_ui.draw(display_surface, game_surface)
        self.states[self.current_state].draw(game_surface)
