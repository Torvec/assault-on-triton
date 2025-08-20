import pygame
from scenes.main_menu import MainMenu
from utils.score_manager import ScoreManager

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.running = True
        self.score_manager = ScoreManager()
        self.set_scene(MainMenu(self, self.screen, self.dt))

    def set_scene(self, new_scene):
        self.current_scene = new_scene

    def run(self):
        while self.running:
            
            self.current_scene.update(self.dt)
            self.current_scene.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000
        
        pygame.quit()