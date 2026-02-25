import platform
import pygame
from src.game import Game
from data.assets import ICON_IMG


def handle_windows_dpi():
    if platform.system() == "Windows":
        try:
            import ctypes

            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception as e:
            print(f"Could not set DPI awareness: {e}")


def main():

    handle_windows_dpi()
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Assault On Triton")
    pygame.display.set_icon(pygame.image.load(ICON_IMG))
    display_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    game = Game(display_surface)
    game.run()


if __name__ == "__main__":
    main()
