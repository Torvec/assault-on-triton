from enum import Enum, auto
import pygame


class GameplayState(Enum):
    INIT = auto()
    CUTSCENE = auto()
    PLAY = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    MISSION_COMPLETE = auto()


class State:
    def __init__(self):
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass


class InitState(State):

    def __init__(self, event_manager):
        self.event_manager = event_manager

    def enter(self):
        print("Entering InitState")
        self.event_manager.start()

    def exit(self):
        print("Exiting InitState")


class CutsceneState(State):

    def __init__(self, gameplay, entity_manager, collision_manager):
        self.gameplay = gameplay
        self.entity_manager = entity_manager
        self.collision_manager = collision_manager

    def enter(self):
        print("Entering CutsceneState")
        self.entity_manager.player_group.sprite.controls_enabled = False
        self.collision_manager.boundary_handling_enabled = False

    def exit(self):
        print("Exiting CutsceneState")

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameplay.state_manager.change_state(GameplayState.PAUSED)


class PlayState(State):

    def __init__(
        self,
        gameplay,
        entity_manager,
        collision_manager,
        wave_manager,
        battle_manager,
        score_manager,
        gameplay_ui,
    ):
        self.gameplay = gameplay
        self.entity_manager = entity_manager
        self.collision_manager = collision_manager
        self.wave_manager = wave_manager
        self.battle_manager = battle_manager
        self.score_manager = score_manager
        self.gameplay_ui = gameplay_ui

    def enter(self):
        print("Entering PlayState")
        self.entity_manager.player_group.sprite.controls_enabled = True
        self.collision_manager.boundary_handling_enabled = True

    def exit(self):
        print("Exiting PlayState")
        pass

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameplay.state_manager.change_state(GameplayState.PAUSED)

    def update(self, dt):
        if not self.entity_manager.player_group.sprite:
            self.score_manager.store_score()
            self.gameplay.state_manager.change_state(GameplayState.GAME_OVER)
            return
        self.gameplay.game_timer += dt
        self.collision_manager.update()
        self.wave_manager.update(dt)
        self.battle_manager.update(dt)
        self.score_manager.update_streak_meter_decay(dt)
        self.gameplay_ui.update(dt)


class PausedState(State):

    def __init__(self, gameplay, entity_manager, pause_modal):
        self.gameplay = gameplay
        self.entity_manager = entity_manager
        self.pause_modal = pause_modal

    def enter(self):
        print("Entering PausedState")
        self.entity_manager.player_group.sprite.controls_enabled = False
        self.pause_modal.is_visible = True

    def exit(self):
        print("Exiting PausedState")
        self.pause_modal.is_visible = False

    def handle_event(self, events):
        self.pause_modal.handle_event(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.gameplay.state_manager.change_state(
                        self.gameplay.state_manager.previous_state
                    )

    def draw(self, surface):
        self.pause_modal.draw(surface)


class GameOverState(State):

    def __init__(self, gameplay):
        self.gameplay = gameplay

    def enter(self):
        print("Entering GameOverState")
        self.gameplay.create_game_over_modal()
        self.gameplay.game_over_modal.is_visible = True

    def exit(self):
        print("Exiting GameOverState")
        self.gameplay.game_over_modal.is_visible = False

    def handle_event(self, events):
        self.gameplay.game_over_modal.handle_event(events)

    def draw(self, surface):
        self.gameplay.game_over_modal.draw(surface)


class MissionCompleteState(State):

    def __init__(self, gameplay, entity_manager, score_manager):
        self.gameplay = gameplay
        self.entity_manager = entity_manager
        self.score_manager = score_manager

    def enter(self):
        print("Entering MissionCompleteState")
        self.entity_manager.player_group.sprite.controls_enabled = False
        self.score_manager.store_score()
        self.gameplay.create_end_level_modal()
        self.gameplay.end_level_modal.is_visible = True

    def exit(self):
        print("Exiting MissionCompleteState")
        self.gameplay.end_level_modal.is_visible = False

    def handle_event(self, events):
        self.gameplay.end_level_modal.handle_event(events)

    def draw(self, surface):
        self.gameplay.end_level_modal.draw(surface)
