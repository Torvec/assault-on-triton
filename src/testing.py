import pygame
from src.screens import Screen
from src.entities import Player
from src.managers import CollisionManager, SpawnManager
from src.gameplay_ui import GamePlayUI


class Testing(Screen):
    def __init__(self, game):
        super().__init__(game)
        self.play_area_rect = pygame.Rect(
            0,
            0,
            self.game.game_surface.get_width(),
            self.game.game_surface.get_height(),
        )
        self.player_group = pygame.sprite.GroupSingle()
        Player.containers = (self.player_group, self.updateable, self.drawable)
        self.spawner = SpawnManager()
        self.collision = CollisionManager()
        self.gameplay_ui = GamePlayUI(self.game, self)

    def handle_event(self, events):
        super().handle_event(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)
        self.collision.update(dt)
        self.gameplay_ui.update(dt)

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        self.gameplay_ui.draw(display_surface, game_surface)
        