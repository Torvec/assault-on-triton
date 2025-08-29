import pygame
from src.game import Game


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Asteroids")
    display_info = pygame.display.Info()
    height = display_info.current_h
    width = height
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
