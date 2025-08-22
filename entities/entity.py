import pygame


class Entity(pygame.sprite.Sprite):
    def __init__(self, game, x, y, radius):
        # Used to auto add sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.game = game
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        if self.position[0] > self.game.screen_w + self.radius:
            self.position[0] = -self.radius
        if self.position[0] < -self.radius:
            self.position[0] = self.game.screen_w + self.radius
        if self.position[1] > self.game.screen_h + self.radius:
            self.position[1] = -self.radius
        if self.position[1] < -self.radius:
            self.position[1] = self.game.screen_h + self.radius

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
