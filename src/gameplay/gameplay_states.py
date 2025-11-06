from enum import Enum, auto
from abc import ABC, abstractmethod
import pygame


class GameplayState(Enum):
    CUTSCENE = auto()
    PLAY = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    MISSION_COMPLETE = auto()


class State(ABC):
    def __init__(self, gameplay):
        self.gameplay = gameplay

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def handle_event(self, events):
        pass

    @abstractmethod
    def update(self, dt):
        pass

    @abstractmethod
    def draw(self, surface):
        pass


class CutsceneState(State):

    def enter(self):
        self.gameplay.player.controls_enabled = False
        self.gameplay.event_manager.is_paused = True
        self.gameplay.cutscene_manager.is_active = True

    def exit(self):
        self.gameplay.event_manager.is_paused = False
        self.gameplay.cutscene_manager.is_active = False

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameplay.change_state(GameplayState.PAUSED)

    def update(self, dt):
        self.gameplay.cutscene_manager.update(dt)

    def draw(self, surface):
        pass


class PlayState(State):

    def __init__(self, gameplay):
        super().__init__(gameplay)
        self.is_battle = False

    def enter(self):
        self.gameplay.event_manager.is_paused = self.is_battle
        self.gameplay.player.controls_enabled = True

    def exit(self):
        pass

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameplay.change_state(GameplayState.PAUSED)

    def update(self, dt):
        if self.gameplay.player.lives < 1:
            self.gameplay.score.store_score(self.score.score)
            self.gameplay.change_state(GameplayState.GAME_OVER)
            return

        self.gameplay.game_timer += dt
        self.gameplay.collision_manager.update()
        if not self.is_battle:
            self.gameplay.event_manager.update(dt)
        self.gameplay.score.update_streak_meter_decay(dt)
        self.gameplay.gameplay_ui.update(dt)

    def draw(self, surface):
        pass


class PausedState(State):

    def enter(self):
        self.previous_timeline_paused = self.gameplay.event_manager.is_paused
        self.previous_player_controls_enabled = self.gameplay.player.controls_enabled
        self.gameplay.pause_modal.is_visible = True
        self.gameplay.event_manager.is_paused = True
        self.gameplay.player.controls_enabled = False

    def exit(self):
        self.gameplay.pause_modal.is_visible = False
        self.gameplay.event_manager.is_paused = self.previous_timeline_paused
        self.gameplay.player.controls_enabled = self.previous_player_controls_enabled

    def handle_event(self, events):
        self.gameplay.pause_modal.handle_event(events)

    def update(self, dt):
        pass

    def draw(self, surface):
        self.gameplay.pause_modal.draw(surface)


class GameOverState(State):

    def enter(self):
        self.gameplay.game_over_modal.is_visible = True
        self.gameplay.event_manager.is_paused = True
        self.gameplay.player.controls_enabled = False

    def exit(self):
        self.gameplay.game_over_modal.is_visible = False

    def handle_event(self, events):
        self.gameplay.game_over_modal.handle_event(events)

    def update(self, dt):
        pass

    def draw(self, surface):
        self.gameplay.game_over_modal.draw(surface)


class MissionCompleteState(State):
    def enter(self):
        self.gameplay.event_manager.is_paused = True
        self.gameplay.player.controls_enabled = False
        self.gameplay.end_level_modal.is_visible = True
        self.gameplay.score.store_score(self.gameplay.score.score)

    def exit(self):
        self.gameplay.end_level_modal.is_visible = False

    def handle_event(self, events):
        self.gameplay.end_level_modal.handle_event(events)
        # EndLevelModal will handle the transition to next cutscene/credits

    def update(self, dt):
        pass

    def draw(self, surface):
        self.gameplay.end_level_modal.draw(surface)

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
