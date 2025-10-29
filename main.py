import traceback
import pygame
from src.game import Game
from src.data.settings import DISPLAY
from src.data.assets import IMAGES


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Assault On Triton")
    pygame.display.set_icon(pygame.image.load(IMAGES["icon"]))
    display_surface = pygame.display.set_mode(
        (DISPLAY["screen_width"], DISPLAY["screen_height"])
    )
    try:
        game = Game(display_surface)
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
