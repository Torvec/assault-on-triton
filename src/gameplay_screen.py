from src.screens import Screen
from src.backgrounds import Planet, PlanetTwo, StarField
from src.gameplay_managers import (
    EntityManager,
    CollisionManager,
    SpawnManager,
    EventManager,
    CutsceneManager,
    ScoreManager,
    BattleManager,
    WaveManager,
    StateManager,
)
from src.gameplay_ui import GamePlayUI
from src.gameplay_modals import PauseModal, EndLevelModal, GameOverModal
from src.gameplay_states import GameplayState
from data.event_queue import EVENT_QUEUE


class GamePlay(Screen):

    def __init__(self, game):
        super().__init__(game)

        self.game_timer = 0

        self.play_area_rect = self.game.game_surface.get_rect()

        self.backgrounds = [
            StarField(0, 0),
            Planet(self.play_area_rect.midbottom[0], self.play_area_rect.midbottom[1]),
            PlanetTwo(
                self.play_area_rect.midtop[0], self.play_area_rect.midtop[1] - 128
            ),
        ]

        self.gameplay_ui = GamePlayUI(self.game, self)

        self.pause_modal = PauseModal(self)

        self.entity_manager = EntityManager()
        self.event_manager = EventManager(
            self,
            EVENT_QUEUE,
        )
        self.spawn_manager = SpawnManager(
            self,
            self.play_area_rect,
            self.entity_manager,
        )
        self.wave_manager = WaveManager(
            self.entity_manager,
            self.spawn_manager,
            self.event_manager,
        )
        self.battle_manager = BattleManager(
            self.entity_manager,
            self.event_manager,
        )
        self.cutscene_manager = CutsceneManager(
            self.entity_manager,
            self.event_manager,
            self.gameplay_ui,
        )
        self.collision_manager = CollisionManager(
            self.entity_manager,
            self.play_area_rect,
        )
        self.score_manager = ScoreManager(
            self.game.score_store,
        )
        self.state_manager = StateManager(
            self,
            self.event_manager,
            self.entity_manager,
            self.collision_manager,
            self.wave_manager,
            self.battle_manager,
            self.gameplay_ui,
            self.pause_modal,
            self.score_manager,
        )

        self.state_manager.change_state(GameplayState.INIT)

    def create_game_over_modal(self):
        self.game_over_modal = GameOverModal(self)

    def create_end_level_modal(self):
        self.end_level_modal = EndLevelModal(self)

    def handle_bg_update(self, dt):
        for bg in self.backgrounds:
            bg.update(dt)

    def handle_bg_draw(self, surface):
        for bg in self.backgrounds:
            bg.draw(surface)

    def handle_event(self, events):
        self.state_manager.handle_event(events)

    def update(self, dt):
        if self.state_manager.current_state != GameplayState.PAUSED:
            self.handle_bg_update(dt)
            self.entity_manager.updateable.update(dt)
            self.gameplay_ui.update(dt)
            self.event_manager.update(dt)
        self.state_manager.update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        self.handle_bg_draw(game_surface)
        self.entity_manager.draw(game_surface)
        self.gameplay_ui.draw(display_surface, game_surface)
        self.state_manager.draw(game_surface)
