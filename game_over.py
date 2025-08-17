import pygame
from scene import Scene

class GameOver(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)
        print("Game Over Test")

    def update(self, dt):
        super().update(dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            from game_play import GamePlay
            self.game.set_scene(GamePlay(self.game, self.screen, self.dt))
        if keys[pygame.K_ESCAPE]:
            from main_menu import MainMenu
            self.game.set_scene(MainMenu(self.game, self.screen, self.dt))

    def draw(self, screen):
        super().draw(screen)