import pygame
from scenes.start import Start
from managers.score_manager import ScoreManager
from managers.scene_manager import SceneManager


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_w = self.screen.get_width()
        self.screen_h = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_manager = ScoreManager()
        self.scene_manager = SceneManager(Start(self))
        self.running = True

    def run(self):
        while self.running:
            events = pygame.event.get()

            self.scene_manager.update(self.dt, events)
            self.scene_manager.draw(self.screen)

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()  # Doesn't need sys.exit() after this because it is the end of the file and nothing is running
