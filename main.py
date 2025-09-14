import pygame
from src.game import Game


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Assault On Triton")
    # screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((1920, 1080))
    try:
        game = Game(screen)
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
