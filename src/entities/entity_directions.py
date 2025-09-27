import pygame

DIRECTION_UP = pygame.Vector2(0, -1)
DIRECTION_DOWN = pygame.Vector2(0, 1)
DIRECTION_LEFT = pygame.Vector2(-1, 0)
DIRECTION_RIGHT = pygame.Vector2(1, 0)
DIRECTION_UP_LEFT = pygame.Vector2(-1, -1).normalize()
DIRECTION_UP_RIGHT = pygame.Vector2(1, -1).normalize()
DIRECTION_DOWN_LEFT = pygame.Vector2(-1, 1).normalize()
DIRECTION_DOWN_RIGHT = pygame.Vector2(1, 1).normalize()
