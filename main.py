import pygame
from src.game import Game


def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Asteroids")
    #! display_info = pygame.display.Info()
    #! height = display_info.current_h
    #! width = height
    #! screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    height = 1520 # * Note: My display is 1600px tall but the taskbar and window title bar are about 40px each
    width = height
    screen = pygame.display.set_mode((width, height))
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()
