import sys
import pygame
from src.render_text import render_text
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


class Screen:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.backgrounds = []

    def handle_event(self, events):
        pass

    def update(self, dt):
        for bg in self.backgrounds:
            bg.update(dt)
        self.updateable.update(dt)

    def draw(self, display_surface, game_surface):
        display_surface.fill("black")
        game_surface.fill("#0c0c12")

        for bg in self.backgrounds:
            bg.draw(game_surface)

        for obj in self.drawable:
            obj.draw(game_surface)


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
        self.end_level_modal = EndLevelModal(self)
        self.game_over_modal = GameOverModal(self)

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


class Credits(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="Credits",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )
        render_text(
            screen=game_surface,
            text="Credits go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
        )


class Options(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="Options",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )
        render_text(
            screen=game_surface,
            text="scores go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
        )


class Scoreboard(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="High Scores",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )
        render_text(
            screen=game_surface,
            text="scores go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
        )


class Start(Screen):

    menu_items = [
        "[Enter] PLAY",
        "[O] OPTIONS",
        "[S] SCORES",
        "[C] CREDITS",
        "[Q] QUIT",
    ]

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RETURN:
                        self.game.change_screen("GamePlay")
                    case pygame.K_o:
                        self.game.change_screen("Options")
                    case pygame.K_s:
                        self.game.change_screen("Scoreboard")
                    case pygame.K_c:
                        self.game.change_screen("Credits")
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def update(self, dt):
        super().update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="ASSAULT",
            font_name="zendots",
            font_size=84,
            antialias=True,
            pos=(
                game_surface.get_rect().center[0],
                game_surface.get_rect().center[1] - 188,
            ),
            align="midbottom",
        )
        render_text(
            screen=game_surface,
            text="ON",
            font_name="zendots",
            font_size=72,
            antialias=True,
            pos=(
                game_surface.get_rect().center[0],
                game_surface.get_rect().center[1] - 84 - 32,
            ),
            align="midbottom",
        )
        render_text(
            screen=game_surface,
            text="TRITON",
            font_name="zendots",
            font_size=84,
            antialias=True,
            pos=(
                game_surface.get_rect().center[0],
                game_surface.get_rect().center[1] - 32,
            ),
            align="midbottom",
        )
        menu_rect = pygame.Rect(
            0, 0, game_surface.get_width() * 0.75, game_surface.get_height() * 0.25
        )
        menu_rect.midtop = game_surface.get_rect().center
        pygame.draw.rect(game_surface, "grey4", menu_rect, border_radius=24)
        pygame.draw.rect(game_surface, "grey70", menu_rect, width=4, border_radius=24)
        for i, item in enumerate(self.menu_items):
            render_text(
                screen=game_surface,
                text=item,
                font_name="spacegrotesk_semibold",
                font_size=32,
                color="grey",
                pos=(menu_rect.midtop[0], menu_rect.midtop[1] + 8 + (i * 48)),
                align="midtop",
            )
