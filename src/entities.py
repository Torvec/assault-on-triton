import random
import pygame


# === Player Constants ===
PLAYER_RADIUS = 48
PLAYER_ACCELERATION = 600
PLAYER_SPEED = 350
PLAYER_LIVES = 3
PLAYER_SHIELD = 100
PLAYER_INVINCIBLE_TIME = 2
PLAYER_SHOOT_TIMER = 0.2
PLAYER_BOMB_AMMO = 3
PLAYER_BOMB_TIMER = 2.0
PLAYER_POWER_LEVEL = 1
PLAYER_BLAST_RADIUS = 128
PLAYER_IMG_PATH = "assets/player_spaceship.png"

# === Asteroid Constants ===
ASTEROID_SM_RADIUS = 16
ASTEROID_SM_SPEED = 120
ASTEROID_SM_HP = 2
ASTEROID_SM_IMG = "assets/asteroid_sm.png"

ASTEROID_MD_RADIUS = 32
ASTEROID_MD_SPEED = 100
ASTEROID_MD_HP = 4
ASTEROID_MD_IMG = "assets/asteroid_md.png"

ASTEROID_LG_RADIUS = 64
ASTEROID_LG_SPEED = 80
ASTEROID_LG_HP = 8
ASTEROID_LG_IMG = "assets/asteroid_lg.png"

ASTEROID_SPEED_RANGE = (80, 120)
ASTEROID_ROTATION_SPEED_RANGE = (-90, 90)

# === EnemyDrone Constants ===
ENEMY_DRONE_RADIUS = 16
ENEMY_DRONE_SPEED = 300
ENEMY_DRONE_HP = 5
ENEMY_DRONE_BLAST_RADIUS = 32
ENEMY_DRONE_IMG_PATH = "assets/enemy_drone.png"

# === EnemyShip Constants ===
ENEMY_SHIP_RADIUS = 32
ENEMY_SHIP_SPEED = 200
ENEMY_SHIP_HP = 10
ENEMY_SHIP_BLAST_RADIUS = 48
ENEMY_SHIP_IMG_PATH = "assets/enemy_ship.png"

# === Missile Constants ===
MISSILE_RADIUS = 10
MISSILE_SPEED = 200
MISSILE_HP = 1
MISSILE_BLAST_RADIUS = 64
MISSILE_IMG_PATH = "assets/missile.png"

# === Shot Constants ===
SHOT_RADIUS = 4
SHOT_RANGE = 512
SHOT_SPEED = 500
SHOT_IMG_PATH = "assets/blaster_shot.png"
SHOT_SFX_PATH = "assets/720118__baggonotes__player_shoot1.wav"

# === Bomb Constants ===
BOMB_RADIUS = 8
BOMB_SPEED = 200
BOMB_BLAST_RADIUS = 256
BOMB_TRIGGER_DISTANCE = 256
BOMB_IMG_PATH = "assets/e_bomb.png"

# === Explosion Constants ===
EXPLOSION_INITIAL_RADIUS = 2
EXPLOSION_EXPANSION_RATE = 192


class Entity(pygame.sprite.Sprite):

    _image_cache = {}

    @classmethod
    def load_image(cls, img_path):
        if img_path not in cls._image_cache:
            cls._image_cache[img_path] = pygame.image.load(img_path).convert_alpha()
        return cls._image_cache[img_path]

    def __init__(self, x, y, game_play):
        # Used to auto add sprites to groups upon creation if a .container attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        #
        if hasattr(self, "img_path") and self.img_path:
            self.image = self.load_image(self.img_path)
        self.position = pygame.Vector2(x, y)
        self.game_play = game_play
        self.play_area = game_play.play_area_rect
        self.radius = 0
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.is_hit = False
        self.hit_timer = 0.1
        self.blast_radius = 0

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def handle_boundaries(self, action=None):
        edges = {
            "top": self.play_area.top + self.radius,
            "right": self.play_area.right - self.radius * 0.25,
            "bottom": self.play_area.bottom - self.radius,
            "left": self.play_area.left + self.radius * 0.25,
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
        self.handle_hit_timer(dt)

    def draw(self, screen):
        pass


class Player(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = PLAYER_IMG_PATH
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
        self.blast_radius = PLAYER_BLAST_RADIUS

    def move_up(self, dt):
        self.velocity.y -= self.acceleration * dt

    def move_down(self, dt):
        self.velocity.y += self.acceleration * dt

    def move_left(self, dt):
        self.velocity.x -= self.acceleration * dt

    def move_right(self, dt):
        self.velocity.x += self.acceleration * dt

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

        if keys[pygame.K_a]:
            self.move_left(dt)
        if keys[pygame.K_d]:
            self.move_right(dt)
        if keys[pygame.K_w]:
            self.move_up(dt)
        if keys[pygame.K_s]:
            self.move_down(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_e]:
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
        ship_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, ship_rect)
        self.flash_when_hit(screen, self.image, ship_rect)


class Asteroid(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.rotation_speed = random.uniform(*ASTEROID_ROTATION_SPEED_RANGE)

    def split(self):
        self.remove_active_targets()

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt
        self.rotation += self.rotation_speed * dt

    def draw(self, screen):
        super().draw(screen)
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, rect)


class AsteroidSmall(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_SM_SPEED
        self.hp = ASTEROID_SM_HP
        self.img_path = ASTEROID_SM_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_SM_RADIUS
        self.score_value = self.hp


class AsteroidMedium(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_MD_SPEED
        self.hp = ASTEROID_MD_HP
        self.img_path = ASTEROID_MD_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_MD_RADIUS
        self.score_value = self.hp

    def split(self):
        self.remove_active_targets()
        new_angle = 30

        asteroid_a = AsteroidSmall(
            self.position.x - ASTEROID_SM_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_a)
        asteroid_a.velocity = self.velocity.rotate(new_angle) * 1.2

        asteroid_b = AsteroidSmall(
            self.position.x + ASTEROID_SM_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_b)
        asteroid_b.velocity = self.velocity.rotate(-new_angle) * 1.2


class AsteroidLarge(Asteroid):

    def __init__(self, x, y, game_play):
        self.speed = ASTEROID_LG_SPEED
        self.hp = ASTEROID_LG_HP
        self.img_path = ASTEROID_LG_IMG
        super().__init__(x, y, game_play)
        self.radius = ASTEROID_LG_RADIUS
        self.score_value = self.hp

    def split(self):
        self.remove_active_targets()
        new_angle = 30

        asteroid_a = AsteroidMedium(
            self.position.x - ASTEROID_MD_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_a)
        asteroid_a.velocity = self.velocity.rotate(new_angle) * 1.2

        asteroid_b = AsteroidMedium(
            self.position.x + ASTEROID_MD_RADIUS, self.position.y, self.game_play
        )
        self.game_play.active_targets.add(asteroid_b)
        asteroid_b.velocity = self.velocity.rotate(-new_angle) * 1.2


class EnemyDrone(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = ENEMY_DRONE_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = ENEMY_DRONE_RADIUS
        self.speed = ENEMY_DRONE_SPEED
        self.hp = ENEMY_DRONE_HP
        self.blast_radius = ENEMY_DRONE_BLAST_RADIUS
        self.score_value = self.hp

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)
        forward = pygame.Vector2(0, 1)
        self.position += forward * self.speed * dt

    def draw(self, screen):
        super().draw(screen)
        drone_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, drone_rect)
        self.flash_when_hit(screen, self.image, drone_rect)


class EnemyShip(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = ENEMY_SHIP_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = ENEMY_SHIP_RADIUS
        self.speed = ENEMY_SHIP_SPEED
        self.hp = ENEMY_SHIP_HP
        self.blast_radius = ENEMY_SHIP_BLAST_RADIUS
        self.score_value = self.hp

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)
        forward = pygame.Vector2(0, 1)
        self.position += forward * self.speed * dt

    def draw(self, screen):
        super().draw(screen)
        ship_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, ship_rect)
        self.flash_when_hit(screen, self.image, ship_rect)


class Missile(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = MISSILE_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = MISSILE_RADIUS
        self.speed = MISSILE_SPEED
        self.hp = MISSILE_HP
        self.blast_radius = MISSILE_BLAST_RADIUS
        self.score_value = self.hp

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

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
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        missile_rect = rotated_image.get_rect(center=self.position)
        screen.blit(rotated_image, missile_rect)


class Shot(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = SHOT_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = SHOT_RADIUS
        self.distance_traveled = 0
        self.max_range = SHOT_RANGE
        self.speed = SHOT_SPEED
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
        shot_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, shot_rect)


class Bomb(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = BOMB_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = BOMB_RADIUS
        self.speed = BOMB_SPEED
        self.blast_radius = BOMB_BLAST_RADIUS
        self.distance_traveled = 0
        self.trigger_distance = BOMB_TRIGGER_DISTANCE

    def sound(self):
        pass  # The launch sound not explosion sound

    def trigger_explosion(self, dt):
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
        bomb_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, bomb_rect)


class Explosion(Entity):

    def __init__(self, x, y, blast_radius, game_play):
        super().__init__(x, y, game_play)
        self.radius = EXPLOSION_INITIAL_RADIUS
        self.exp_rate = EXPLOSION_EXPANSION_RATE
        self.blast_radius = blast_radius

    def sound(self):
        pass

    def update(self, dt):
        super().update(dt)
        if self.radius < self.blast_radius:
            self.radius += self.exp_rate * dt
            if self.radius >= self.blast_radius:
                self.kill()

    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius
        )
