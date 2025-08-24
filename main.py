import pygame
from game import Game
from global_consts import TITLE_GAME


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(TITLE_GAME)
    display_info = pygame.display.Info()
    height = display_info.current_h
    width = height
    screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
    game = Game(screen)
    game.run()


if __name__ == "__main__":
    main()
