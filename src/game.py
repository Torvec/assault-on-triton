import pygame
from src.screens import Start, GamePlay, Options, Scoreboard, Credits
from src.score_store import ScoreStore
from data.settings import DISPLAY


class Game:

    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.game_surface = pygame.Surface(
            (DISPLAY["game_surface_width"], self.display_surface.get_height())
        )
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_store = ScoreStore()
        self.running = True
        self.scenes = {
            "Start": Start,
            "GamePlay": GamePlay,
            "Options": Options,
            "Scoreboard": Scoreboard,
            "Credits": Credits,
        }

        self.set_scene("Start")

    def set_scene(self, scene_name):
        if scene_name not in self.scenes:
            raise ValueError(f"Unknown scene: {scene_name}")
        self.current_scene = self.scenes[scene_name](self)

    def run(self):
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            self.current_scene.handle_event(events)
            self.current_scene.update(self.dt)
            self.current_scene.draw(self.display_surface, self.game_surface)
            self.display_surface.blit(
                self.game_surface, (DISPLAY["game_surface_offset"], 0)
            )
            pygame.display.flip()
            self.dt = self.clock.tick(DISPLAY["target_fps"]) / 1000
        pygame.quit()
