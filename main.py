import pygame
from src.game import Game
from data.assets import IMAGES


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Assault On Triton")
    pygame.display.set_icon(pygame.image.load(IMAGES["icon"]))
    display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    game = Game(display_surface)
    game.run()


if __name__ == "__main__":
    main()
