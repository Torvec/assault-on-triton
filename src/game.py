import pygame
from src.scenes import GamePlay
from src.score_manager import ScoreManager


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.screen_w = self.screen.get_width()
        self.screen_h = self.screen.get_height()
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_manager = ScoreManager()
        #! self.set_scene(Start(self))
        self.set_scene(GamePlay(self))
        self.running = True

    def set_scene(self, new_scene):
        self.current_scene = new_scene

    def run(self):
        while self.running:
            events = pygame.event.get()

            self.current_scene.update(self.dt, events)
            self.current_scene.draw(self.screen)

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()  # * Note: Doesn't need sys.exit() after this because it is the end of the file and nothing is running
