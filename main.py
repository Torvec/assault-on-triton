import pygame
from global_consts import GAME_TITLE, SCREEN_WIDTH, SCREEN_HEIGHT
from game import Game

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption(GAME_TITLE)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
