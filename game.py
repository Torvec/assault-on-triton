import pygame
from scenes.main_menu import MainMenu
from utils.score_manager import ScoreManager
from utils.scene_manager import SceneManager


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True
        self.score_manager = ScoreManager()
        self.scene_manager = SceneManager(MainMenu(self, self.screen, self.dt))

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

        pygame.quit()
