import pygame
from src.screens import Start, Options, Scoreboard, Credits, Thanks
from src.gameplay_screen import GamePlay
from src.score_store import ScoreStore
from data.settings import DISPLAY


class Game:

    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.game_surface = pygame.Surface(
            (DISPLAY["game_surface_width"], DISPLAY["screen_height"])
        )
        self.scaled_surface = self.scale_surface(self.game_surface)
        self.game_surface_offset = {
            "x": (self.display_surface.get_width() - self.scaled_surface.get_width())
            // 2,
            "y": (self.display_surface.get_height() - self.scaled_surface.get_height())
            // 2,
        }
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_store = ScoreStore()
        self.running = True
        self.screens = {
            "Start": Start,
            "GamePlay": GamePlay,
            "Options": Options,
            "Scoreboard": Scoreboard,
            "Credits": Credits,
            "Thanks": Thanks,
        }
        self.change_screen("Start")

    def change_screen(self, screen_name):
        if screen_name not in self.screens:
            raise ValueError(f"Unknown scene: {screen_name}")
        self.current_screen = self.screens[screen_name](self)

    def scale_surface(self, game_surface):
        return pygame.transform.scale(
            game_surface,
            (
                self.display_surface.get_height() * 9 / 16,
                self.display_surface.get_height(),
            ),
        )

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            self.current_screen.handle_event(events)
            self.current_screen.update(self.dt)
            self.current_screen.draw(self.display_surface, self.scaled_surface)
            self.display_surface.blit(
                self.scaled_surface,
                (self.game_surface_offset["x"], 0),
            )
            pygame.display.flip()
            self.dt = self.clock.tick(DISPLAY["target_fps"]) / 1000
        pygame.quit()
