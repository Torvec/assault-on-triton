import pygame
from src.screens import Start, Options, Scoreboard, Credits, Thanks
from src.gameplay_screen import GamePlay
from src.score_store import ScoreStore
from data.settings import DISPLAY


class Game:

    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.game_surface = pygame.Surface((DISPLAY["base_gs_w"], DISPLAY["base_gs_h"]))
        self.scaled_gs = self.scale_surface(self.game_surface)
        self.scaled_gs_center = self.display_surface.get_rect().center
        self.scaled_gs_rect = self.scaled_gs.get_rect(center=self.scaled_gs_center)
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
        scale_w = self.display_surface.get_width() // DISPLAY["base_gs_w"]
        scale_h = self.display_surface.get_height() // DISPLAY["base_gs_h"]
        scale = max(1, min(scale_w, scale_h))
        return pygame.transform.scale(
            game_surface,
            (
                self.game_surface.get_width() * scale,
                self.game_surface.get_height() * scale,
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
            self.current_screen.draw(self.display_surface, self.scaled_gs)
            self.display_surface.blit(self.scaled_gs, (self.scaled_gs_rect))
            pygame.display.flip()
            self.dt = self.clock.tick(DISPLAY["target_fps"]) / 1000
        pygame.quit()
