import random
import pygame

from src.data.global_consts import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_ACCELERATION,
    SHOT_COOLDOWN,
    SHOT_SPEED,
    ASTEROID_MIN_RADIUS,
    SHOT_RADIUS,
    SHOT_MAX_RANGE,
    SHOT_SFX,
)


class Entity(pygame.sprite.Sprite):
    def __init__(self, game, x, y, radius, play_area_rect):
        # Used to auto add sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.game = game
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.play_area_rect = play_area_rect

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def update(self, dt):
        left = self.play_area_rect.left
        right = self.play_area_rect.right
        top = self.play_area_rect.top
        bottom = self.play_area_rect.bottom

        if self.position[0] > right + self.radius:
            self.position[0] = left - self.radius
        if self.position[0] < left - self.radius:
            self.position[0] = right + self.radius
        if self.position[1] > bottom + self.radius:
            self.position[1] = top - self.radius
        if self.position[1] < top - self.radius:
            self.position[1] = bottom + self.radius

    def draw(self, screen):
        pass


class Player(Entity):
    def __init__(self, game, x, y, play_area_rect):
        super().__init__(game, x, y, PLAYER_RADIUS, play_area_rect)
        self.rotation = 0
        self.lives = 3
        self.invincibleTime = 0
        self.shoot_timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHOT_COOLDOWN
        shot = Shot(self.game, self.position.x, self.position.y, self.play_area_rect)
        shot.velocity = (
            pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED + self.velocity
        )
        shot.sound()

    def respawn(self):
        self.invincibleTime = 3
        self.position = (
            self.play_area_rect.width // 2,
            self.play_area_rect.height // 2,
        )

    def update(self, dt):
        super().update(dt)
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

        self.velocity *= 0.99

        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

        self.position += self.velocity * dt

        if self.invincibleTime > 0:
            self.invincibleTime -= dt
            if self.invincibleTime < 0:
                self.invincibleTime = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "slategray3", self.triangle(), 0)


class Asteroid(Entity):
    def __init__(self, game, x, y, radius, play_area_rect):
        super().__init__(game, x, y, radius, play_area_rect)

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a_velocity = self.velocity.rotate(random_angle)
        b_velocity = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(
            self.game, self.position.x, self.position.y, new_radius, self.play_area_rect
        )
        asteroid_a.velocity = a_velocity * 1.2
        asteroid_b = Asteroid(
            self.game, self.position.x, self.position.y, new_radius, self.play_area_rect
        )
        asteroid_b.velocity = b_velocity * 1.2

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "wheat4", self.position, self.radius, 2)


class Shot(Entity):
    def __init__(self, game, x, y, play_area_rect):
        super().__init__(game, x, y, SHOT_RADIUS, play_area_rect)
        self.start_position = pygame.Vector2(x, y)
        self.distance_traveled = 0

    def sound(self):
        self.shoot_sound = pygame.mixer.Sound(SHOT_SFX)
        self.shoot_sound.set_volume(0.5)
        self.shoot_sound.play()

    def update(self, dt):
        super().update(dt)
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame

        if self.distance_traveled >= SHOT_MAX_RANGE:
            self.kill()

        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 0)
