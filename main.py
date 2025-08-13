import pygame
from global_consts import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        updateable.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
            
        pygame.display.flip()

        dt = clock.tick(60) / 1000
    
    pygame.quit()

if __name__ == "__main__":
    main()
