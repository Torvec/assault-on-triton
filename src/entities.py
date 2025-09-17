import random
import pygame


# === Player Constants ===
PLAYER_RADIUS = 48
PLAYER_ACCELERATION = 600
PLAYER_SPEED = 300
PLAYER_LIVES = 3
PLAYER_SHIELD = 100
PLAYER_INVINCIBLE_TIME = 2
PLAYER_SHOOT_TIMER = 0.2
PLAYER_BOMB_AMMO = 3
PLAYER_BOMB_TIMER = 2.0
PLAYER_POWER_LEVEL = 1
PLAYER_IMG_PATH = "assets/player_spaceship.png"

# === Asteroid Constants ===
ASTEROID_RADII = [16, 32, 64]
ASTEROID_MIN_RADIUS = 16
ASTEROID_MID_RADIUS = 32
ASTEROID_MAX_RADIUS = 64
ASTEROID_SPEED_RANGE = (80, 120)
ASTEROID_ROTATION_SPEED_RANGE = (-90, 90)
ASTEROID_HP = 4
ASTEROID_IMG_LG = "assets/asteroid_lg.png"
ASTEROID_IMG_MD = "assets/asteroid_md.png"
ASTEROID_IMG_SM = "assets/asteroid_sm.png"

# === EnemyDrone Constants ===
ENEMY_DRONE_RADIUS = 16
ENEMY_DRONE_SPEED = 300
ENEMY_DRONE_HP = 5
ENEMY_DRONE_IMG_PATH = "assets/enemy_drone.png"

# === EnemyShip Constants ===
ENEMY_SHIP_RADIUS = 32
ENEMY_SHIP_SPEED = 200
ENEMY_SHIP_HP = 10
ENEMY_SHIP_IMG_PATH = "assets/enemy_ship.png"

# === Missile Constants ===
MISSILE_RADIUS = 10
MISSILE_SPEED = 200
MISSILE_HP = 1

# === Shot Constants ===
SHOT_RADIUS = 4
SHOT_MAX_RANGE_FACTOR = 1  # Uses play_area_rect.height
SHOT_SPEED = 500
SHOT_IMG_PATH = "assets/blaster_shot.png"
SHOT_SFX_PATH = "assets/720118__baggonotes__player_shoot1.wav"

# === Bomb Constants ===
BOMB_RADIUS = 8
BOMB_IMG_PATH = "assets/e_bomb.png"
BOMB_SPEED = 200
BOMB_BLAST_RADIUS = 256
BOMB_TRIGGER_DISTANCE_FACTOR = 0.25  # Uses play_area_rect.height

# === Explosion Constants ===
EXPLOSION_INITIAL_RADIUS = 2
EXPLOSION_EXPANSION_RATE = 192


class Entity(pygame.sprite.Sprite):

    def __init__(self, x, y, game_play):
        # Used to auto add sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.game_play = game_play
        self.play_area = game_play.play_area_rect
        self.radius = 0
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.is_hit = False
        self.hit_timer = 0.1

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def handle_boundaries(self, action=None):
        edges = {
            "top": self.play_area.top + self.radius,
            "right": self.play_area.right - self.radius,
            "bottom": self.play_area.bottom - self.radius,
            "left": self.play_area.left + self.radius,
        }
        if action == "block":
            self.position.x = max(edges["left"], min(self.position.x, edges["right"]))
            self.position.y = max(edges["top"], min(self.position.y, edges["bottom"]))
        if action == None and (
            self.position.x + self.radius < self.play_area.left
            or self.position.x - self.radius > self.play_area.right
            or self.position.y - self.radius > self.play_area.bottom
        ):
            self.remove_active_targets()

    def remove_active_targets(self):
        if self in self.game_play.active_targets:
            self.kill()
            self.game_play.active_targets.remove(self)

    def show_collision(self):
        keys = pygame.key.get_pressed()
        toggle = False
        if keys[pygame.K_BACKQUOTE]:
            return not toggle

    def flash_when_hit(self, screen, entity_surface, entity_rect):
        if self.is_hit:
            flash = pygame.Surface(entity_surface.get_size(), pygame.SRCALPHA)
            center = (flash.get_width() // 2, flash.get_height() // 2)
            pygame.draw.circle(flash, (255, 255, 255, 180), center, self.radius)
            screen.blit(flash, entity_rect)

    def handle_hit_timer(self, dt):
        if self.is_hit:
            self.hit_timer -= dt
            if self.hit_timer <= 0:
                self.is_hit = False
                self.hit_timer = 0.1

    def update(self, dt):
        self.handle_boundaries()
        self.show_collision()
        self.handle_hit_timer(dt)

    def draw(self, screen):
        if self.show_collision():
            pygame.draw.circle(
                screen, "red", self.position, self.radius, 1
            )  # Collision circle


class Player(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = PLAYER_RADIUS
        self.acceleration = PLAYER_ACCELERATION
        self.speed = PLAYER_SPEED
        self.lives = PLAYER_LIVES
        self.shield = PLAYER_SHIELD
        self.invincibleTime = 0
        self.shoot_timer = 0
        self.bomb_ammo = PLAYER_BOMB_AMMO
        self.bomb_timer = 0
        self.power_level = PLAYER_POWER_LEVEL
        self.ship_image = pygame.image.load(PLAYER_IMG_PATH).convert_alpha()

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.velocity += forward * self.acceleration * dt

    def strafe(self, dt):
        right = pygame.Vector2(1, 0).rotate(self.rotation)
        self.velocity += right * self.acceleration * dt

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = 0.2
        shot_pos = self.position + pygame.Vector2(0, -self.radius)
        shot_l = Shot(shot_pos.x - 8, shot_pos.y, self.game_play)
        shot_r = Shot(shot_pos.x + 8, shot_pos.y, self.game_play)
        shot_l.velocity = pygame.Vector2(0, -1) * shot_l.speed
        shot_r.velocity = pygame.Vector2(0, -1) * shot_r.speed
        shot_l.sound()

    def release_bomb(self):
        if self.bomb_ammo <= 0 or self.bomb_timer > 0:
            return
        self.bomb_timer = 2.0
        self.bomb_ammo -= 1
        bomb = Bomb(self.position.x, self.position.y, self.game_play)
        forward = pygame.Vector2(0, -1)
        player_forward_speed = self.velocity.dot(forward)
        forward_only_speed = max(0, player_forward_speed)
        bomb.velocity = forward * (forward_only_speed + bomb.speed)
        bomb.sound()

    def respawn(self):
        self.invincibleTime = 2
        self.position.x = self.game_play.play_area_rect.width // 2
        self.position.y = self.game_play.play_area_rect.height - 100
        self.shield = 100

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
        if keys[pygame.K_e] or mouse_btn[1]:
            self.release_bomb()

    def apply_acceleration(self, dt):
        self.velocity *= 0.99
        if self.velocity.length() > self.speed:
            self.velocity.scale_to_length(self.speed)
        self.position += self.velocity * dt

    def update(self, dt):
        super().update(dt)
        self.controls(dt)
        self.apply_acceleration(dt)
        self.handle_boundaries("block")
        self.handle_invincibility(dt)
        self.shoot_timer -= dt
        self.bomb_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        ship_rect = self.ship_image.get_rect(center=self.position)
        screen.blit(self.ship_image, ship_rect)
        self.flash_when_hit(screen, self.ship_image, ship_rect)


class Asteroid(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = random.choice(ASTEROID_RADII)
        self.min_radius = ASTEROID_MIN_RADIUS
        self.mid_radius = ASTEROID_MID_RADIUS
        self.max_radius = ASTEROID_MAX_RADIUS
        self.speed = random.randint(*ASTEROID_SPEED_RANGE)
        self.rotation_speed = random.uniform(*ASTEROID_ROTATION_SPEED_RANGE)
        self.asteroid_lg = pygame.image.load(ASTEROID_IMG_LG).convert_alpha()
        self.asteroid_md = pygame.image.load(ASTEROID_IMG_MD).convert_alpha()
        self.asteroid_sm = pygame.image.load(ASTEROID_IMG_SM).convert_alpha()
        self.hp = ASTEROID_HP
        self.score_value = self.hp

    def split(self):
        self.remove_active_targets()
        if self.radius <= self.min_radius:
            return

        new_angle = 30
        new_radius = self.radius // 2

        asteroid_a = Asteroid(
            self.position.x - new_radius, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_a)
        asteroid_a.radius = new_radius
        asteroid_a.velocity = self.velocity.rotate(new_angle) * 1.2

        asteroid_b = Asteroid(
            self.position.x + new_radius, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_b)
        asteroid_b.radius = new_radius
        asteroid_b.velocity = self.velocity.rotate(-new_angle) * 1.2

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt

    def draw(self, screen):
        super().draw(screen)
        if self.radius == self.max_radius:
            image = self.asteroid_lg
        elif self.radius == self.mid_radius:
            image = self.asteroid_md
        else:
            image = self.asteroid_sm

        rotated_image = pygame.transform.rotate(image, self.rotation)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)


class EnemyDrone(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = ENEMY_DRONE_RADIUS
        self.speed = ENEMY_DRONE_SPEED
        self.hp = ENEMY_DRONE_HP
        self.score_value = self.hp
        self.enemy_drone_img = pygame.image.load(ENEMY_DRONE_IMG_PATH).convert_alpha()

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, 48, self.game_play)

    def update(self, dt):
        super().update(dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def draw(self, screen):
        super().draw(screen)
        drone_rect = self.enemy_drone_img.get_rect(center=self.position)
        screen.blit(self.enemy_drone_img, drone_rect)
        self.flash_when_hit(screen, self.enemy_drone_img, drone_rect)


class EnemyShip(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = ENEMY_SHIP_RADIUS
        self.speed = ENEMY_SHIP_SPEED
        self.hp = ENEMY_SHIP_HP
        self.score_value = self.hp
        self.enemy_ship_image = pygame.image.load(ENEMY_DRONE_IMG_PATH).convert_alpha()

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, 32, self.game_play)

    def update(self, dt):
        super().update(dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt

    def draw(self, screen):
        super().draw(screen)
        ship_rect = self.enemy_ship_image.get_rect(center=self.position)
        screen.blit(self.enemy_ship_image, ship_rect)
        self.flash_when_hit(screen, self.enemy_ship_image, ship_rect)


class Missile(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = MISSILE_RADIUS
        self.speed = MISSILE_SPEED
        self.hp = MISSILE_HP
        self.score_value = self.hp

    def shape(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius // 2
        points = {
            "top": self.position + forward * self.radius,
            "right": self.position - forward * self.radius + right,
            "left": self.position - forward * self.radius - right,
        }
        return list(points.values())

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, 64, self.game_play)

    def track_player(self):
        direction = self.game_play.player.position - self.position
        angle = pygame.Vector2(0, 1).angle_to(direction)
        return angle

    def update(self, dt):
        super().update(dt)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * self.speed * dt
        self.rotation = self.track_player()

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.polygon(screen, "white", self.shape())


class Shot(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = SHOT_RADIUS
        self.distance_traveled = 0
        self.max_range = game_play.play_area_rect.height
        self.speed = SHOT_SPEED
        self.shot_image = pygame.image.load(SHOT_IMG_PATH).convert_alpha()
        self.sfx = SHOT_SFX_PATH

    def sound(self):
        self.shoot_sound = pygame.mixer.Sound(self.sfx)
        self.shoot_sound.set_volume(0.5)
        self.shoot_sound.play()

    def handle_max_range(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.max_range:
            self.kill()

    def update(self, dt):
        super().update(dt)
        self.handle_max_range(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        shot_rect = self.shot_image.get_rect(center=self.position)
        screen.blit(self.shot_image, shot_rect)


class Bomb(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = BOMB_RADIUS
        self.bomb_image = pygame.image.load(BOMB_IMG_PATH)
        self.speed = BOMB_SPEED
        self.blast_radius = BOMB_BLAST_RADIUS
        self.distance_traveled = 0
        self.trigger_distance = (
            game_play.play_area_rect.height * BOMB_TRIGGER_DISTANCE_FACTOR
        )

    def sound(self):
        pass  # The launch sound not explosion sound

    def trigger_explosion(
        self,
        dt,
    ):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.trigger_distance:
            Explosion(
                self.position.x, self.position.y, self.blast_radius, self.game_play
            )
            self.kill()

    def update(self, dt):
        super().update(dt)
        self.trigger_explosion(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        super().draw(screen)
        bomb_rect = self.bomb_image.get_rect(center=self.position)
        screen.blit(self.bomb_image, bomb_rect)


class Explosion(Entity):

    def __init__(self, x, y, blast_radius, game_play):
        super().__init__(x, y, game_play)
        self.radius = EXPLOSION_INITIAL_RADIUS
        self.expansion_rate = EXPLOSION_EXPANSION_RATE
        self.blast_radius = blast_radius

    def sound(self):
        pass

    def update(self, dt):
        super().update(dt)
        if self.radius < self.blast_radius:
            self.radius += self.expansion_rate * dt
        if self.radius >= self.blast_radius:
            self.kill()

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius
        )
