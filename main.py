import pygame
from game import Game
from global_consts import TITLE_GAME, SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(TITLE_GAME)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Game(screen)
    game.run()


if __name__ == "__main__":
    main()
