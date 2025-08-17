import pygame
from game_play import GamePlay

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.current_scene = GamePlay(self.screen, self.dt)
        self.running = True

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