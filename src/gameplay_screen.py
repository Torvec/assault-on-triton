import pygame
from src.screens import Screen
from src.backgrounds import (
    Planet,
    PlanetTwo,
    StarField,
)
from src.managers import (
    EntityManager,
    CollisionManager,
    SpawnManager,
    EventManager,
    CutsceneManager,
    ScoreManager,
    BattleManager,
    WaveManager,
)
from src.gameplay_ui import (
    GamePlayUI,
    PauseModal,
    EndLevelModal,
    GameOverModal,
)
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

        self.gameplay_ui = GamePlayUI(self.game, self)
        self.pause_modal = PauseModal(self)

        self.entity_manager = EntityManager()
        self.event_manager = EventManager(self, EVENT_QUEUE)
        self.spawn_manager = SpawnManager(
            self, self.play_area_rect, self.entity_manager
        )
        self.wave_manager = WaveManager(
            self.entity_manager, self.spawn_manager, self.event_manager
        )
        self.battle_manager = BattleManager(self.entity_manager, self.event_manager)
        self.cutscene_manager = CutsceneManager(
            self.entity_manager, self.event_manager, self.gameplay_ui
        )
        self.collision_manager = CollisionManager(
            self.entity_manager, self.play_area_rect
        )
        self.score_manager = ScoreManager(self.game.score_store)

        self.current_state = None
        self.previous_state = None
        self.states = {
            GameplayState.INIT: InitState(self.event_manager),
            GameplayState.CUTSCENE: CutsceneState(
                self, self.entity_manager, self.collision_manager
            ),
            GameplayState.PLAY: PlayState(
                self,
                self.entity_manager,
                self.collision_manager,
                self.wave_manager,
                self.battle_manager,
                self.score_manager,
                self.gameplay_ui,
            ),
            GameplayState.PAUSED: PausedState(
                self, self.entity_manager, self.pause_modal
            ),
            GameplayState.GAME_OVER: GameOverState(self),
            GameplayState.MISSION_COMPLETE: MissionCompleteState(
                self, self.entity_manager, self.score_manager
            ),
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
            for bg in self.backgrounds:
                bg.update(dt)
            self.entity_manager.updateable.update(dt)
            self.gameplay_ui.update(dt)
            self.event_manager.update(dt)
        self.states[self.current_state].update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)

        for bg in self.backgrounds:
            bg.draw(game_surface)

        for obj in self.entity_manager.drawable:
            obj.draw(game_surface)

        self.gameplay_ui.draw(display_surface, game_surface)
        self.states[self.current_state].draw(game_surface)
