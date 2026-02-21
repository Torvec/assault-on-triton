import pygame
from src.game import Game
from data.assets import ICON_IMG


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Assault On Triton")
    pygame.display.set_icon(pygame.image.load(ICON_IMG))
    display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    game = Game(display_surface)
    game.run()


if __name__ == "__main__":
    main()
