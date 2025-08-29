import random
import pygame

from src.global_consts import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_ACCELERATION,
    SHOT_COOLDOWN,
    SHOT_SPEED,
    ASTEROID_MIN_RADIUS,
    SHOT_RADIUS,
    SHOT_MAX_RANGE,
    SHOT_SFX,
)


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, radius, game_play):
        # Used to auto add sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        self.game_play = game_play

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def update(self, dt):
        lt = self.game_play.play_area_rect.left
        rt = self.game_play.play_area_rect.right
        tp = self.game_play.play_area_rect.top
        bm = self.game_play.play_area_rect.bottom

        if self.position[0] > rt + self.radius:
            self.position[0] = lt - self.radius
        if self.position[0] < lt - self.radius:
            self.position[0] = rt + self.radius
        if self.position[1] > bm + self.radius:
            self.position[1] = tp - self.radius
        if self.position[1] < tp - self.radius:
            self.position[1] = bm + self.radius

    def draw(self, screen):
        pass


class Player(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, PLAYER_RADIUS, game_play)
        self.rotation = 0
        self.lives = 3
        self.invincibleTime = 0
        self.shoot_timer = 0

    def shape(self):
        tp = self.position + pygame.Vector2(0, self.radius * 0.75).rotate(self.rotation)
        rt = self.position + pygame.Vector2(self.radius, 0).rotate(self.rotation)
        bm = self.position + pygame.Vector2(0, -self.radius * 2).rotate(self.rotation)
        lt = self.position + pygame.Vector2(-self.radius, 0).rotate(self.rotation)
        return [tp, rt, bm, lt]

    def update_direction(self):
        direction = pygame.mouse.get_pos() - self.position
        angle = pygame.Vector2(0, -1).angle_to(direction)
        self.rotation = angle

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.velocity += forward * PLAYER_ACCELERATION * dt

    def strafe(self, dt):
        right = pygame.Vector2(1, 0).rotate(self.rotation)
        self.velocity += right * PLAYER_ACCELERATION * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = SHOT_COOLDOWN
        shot_offset = pygame.Vector2(0, -self.radius).rotate(self.rotation)
        shot_pos = self.position + shot_offset
        shot = Shot(shot_pos.x, shot_pos.y, self.game_play)
        shot.velocity = (
            pygame.Vector2(0, -1).rotate(self.rotation) * SHOT_SPEED + self.velocity
        )
        shot.sound()

    def respawn(self):
        self.invincibleTime = 3
        self.position = (
            self.game_play.play_area_rect.width // 2,
            self.game_play.play_area_rect.height // 2,
        )

    def handle_invincibility(self, dt):
        if self.invincibleTime > 0:
            self.invincibleTime -= dt
        if self.invincibleTime < 0:
            self.invincibleTime = 0

    def controls(self, dt):
        keys = pygame.key.get_pressed()
        mouse_btn = pygame.mouse.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.strafe(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.strafe(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE] or mouse_btn[0]:
            self.shoot()

    def apply_acceleration(self, dt):
        self.velocity *= 0.99

        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

        self.position += self.velocity * dt

    def update(self, dt):
        super().update(dt)
        self.controls(dt)
        self.apply_acceleration(dt)
        self.update_direction()
        self.handle_invincibility(dt)
        self.shoot_timer -= dt

    def draw(self, screen):
        pygame.draw.polygon(screen, "slategray3", self.shape(), 0)
        pygame.draw.circle(screen, "red", self.position, self.radius, 1)


class Asteroid(Entity):

    def __init__(self, x, y, radius, game_play):
        super().__init__(x, y, radius, game_play)

    def split(self):
        self.kill()
        self.game_play.wave_manager.dec_target_count()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        a_velocity = self.velocity.rotate(random_angle)
        b_velocity = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid_a = Asteroid(
            self.position.x, self.position.y, new_radius, self.game_play
        )
        self.game_play.wave_manager.inc_target_count()
        asteroid_a.velocity = a_velocity * 1.2
        asteroid_b = Asteroid(
            self.position.x, self.position.y, new_radius, self.game_play
        )
        self.game_play.wave_manager.inc_target_count()
        asteroid_b.velocity = b_velocity * 1.2

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "wheat4", self.position, self.radius, 2)


class EnemyShip(Entity):

    def __init__(self, x, y, radius, game_play):
        super().__init__(x, y, radius, game_play)
        self.hp = 3
        self.rotation = 0
        self.game_play = game_play

    def shape(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def explode(self):
        self.kill()
        self.game_play.wave_manager.dec_target_count()
        # TODO: Debris flys off in random directions and then disappears after a few seconds

    def track_player(self):
        direction = self.game_play.player.position - self.position
        angle = pygame.Vector2(0, -1).angle_to(direction)
        self.rotation = angle

    def update(self, dt):
        super().update(dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * 250 * dt
        self.track_player()

    def draw(self, screen):
        pygame.draw.polygon(screen, "red", self.shape())


class Shot(Entity):
    def __init__(self, x, y, game_play):
        super().__init__(x, y, SHOT_RADIUS, game_play)
        self.start_position = pygame.Vector2(x, y)
        self.distance_traveled = 0

    def sound(self):
        self.shoot_sound = pygame.mixer.Sound(SHOT_SFX)
        self.shoot_sound.set_volume(0.5)
        self.shoot_sound.play()

    def handle_max_range(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame

        if self.distance_traveled >= SHOT_MAX_RANGE:
            self.kill()

    def update(self, dt):
        super().update(dt)
        self.handle_max_range(dt)

        self.position += self.velocity * dt

    def draw(self, screen):
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 0)
