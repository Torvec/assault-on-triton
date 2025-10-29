import pygame
from src.score_store import ScoreStore
from src.data.settings import DISPLAY


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
            "Start": lambda: self._import_scene("src.menus.start_menu", "Start"),
            "GamePlay": lambda: self._import_scene("src.gameplay.gameplay", "GamePlay"),
            "GameOver": lambda: self._import_scene("src.menus.game_over", "GameOver"),
            "Options": lambda: self._import_scene("src.menus.options_menu", "Options"),
            "Scoreboard": lambda: self._import_scene(
                "src.menus.scoreboard", "Scoreboard"
            ),
            "Credits": lambda: self._import_scene("src.menus.credits", "Credits"),
        }

        self.set_scene("Start")

    def _import_scene(self, import_path, class_name):
        module = __import__(import_path, fromlist=[class_name])
        return getattr(module, class_name)(self)

    def set_scene(self, scene_name):
        if scene_name not in self.scenes:
            raise ValueError(f"Unknown scene: {scene_name}")
        self.current_scene = self.scenes[scene_name]()

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
