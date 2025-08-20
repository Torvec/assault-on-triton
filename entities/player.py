import pygame
from entities.circleshape import CircleShape
from entities.shot import Shot
from global_consts import (
    PLAYER_RADIUS,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_ACCELERATION,
    SHOT_COOLDOWN,
    SHOT_SPEED,
    SHOT_SFX,
)


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0
        self.shoot_sound = pygame.mixer.Sound(SHOT_SFX)
        self.shoot_sound.set_volume(0.5)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "slategray3", self.triangle(), 0)
        # Shows collision circle
        # pygame.draw.circle( screen, "red", (int(self.position.x), int(self.position.y)), self.radius, 1)

    def update(self, dt):
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        if self.position[0] > SCREEN_WIDTH:
            self.position[0] = 0
        if self.position[0] < 0:
            self.position[0] = SCREEN_WIDTH
        if self.position[1] > SCREEN_HEIGHT:
            self.position[1] = 0
        if self.position[1] < 0:
            self.position[1] = SCREEN_HEIGHT

        self.velocity *= 0.99

        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

        self.position += self.velocity * dt

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
        self.shoot_sound.play()
