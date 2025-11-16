import random
import pygame
from data.assets import IMAGES, SOUNDS
from data.settings import EXPLOSIONS, PICKUPS, PROJECTILES, PLAYER, ENEMIES

DIRECTION_UP = pygame.Vector2(0, -1)
DIRECTION_DOWN = pygame.Vector2(0, 1)
DIRECTION_LEFT = pygame.Vector2(-1, 0)
DIRECTION_RIGHT = pygame.Vector2(1, 0)
DIRECTION_UP_LEFT = pygame.Vector2(-1, -1).normalize()
DIRECTION_UP_RIGHT = pygame.Vector2(1, -1).normalize()
DIRECTION_DOWN_LEFT = pygame.Vector2(-1, 1).normalize()
DIRECTION_DOWN_RIGHT = pygame.Vector2(1, 1).normalize()


def move_straight(entity, direction, dt):
    match direction:
        case "down":
            direction = DIRECTION_DOWN
        case _:
            pass
    entity.position += direction * entity.speed * dt


def move_to_location(entity, x, y, speed, dt):
    target = pygame.Vector2(x, y)
    direction = target - entity.position
    distance = direction.length()

    if distance < 5:  # Threshold to prevent jittering
        entity.position = target.copy()
        entity.velocity = pygame.Vector2(0, 0)
        entity.behaviors = [
            b for b in entity.behaviors if b.get("action") != "move_to_location"
        ]
        entity.gameplay.cutscene_manager.on_action_complete()
        return

    if distance > 0:
        direction.normalize_ip()
        entity.velocity = direction * speed
        entity.position += entity.velocity * dt


def move_angled(entity, dt, **kwargs):
    angle = kwargs.get("angle", 0)
    velocity_factor = kwargs.get("velocity_factor", 1.0)

    # Sets up a flag so that the changing of direction only happens once and not continuously
    if not hasattr(entity, "_angled_velocity_set"):

        base_velocity = DIRECTION_DOWN * entity.speed
        entity.velocity = base_velocity.rotate(angle) * velocity_factor
        entity._angled_velocity_set = True

    entity.position += entity.velocity * dt


def rotate_constantly(entity, dt):
    entity.rotation += entity.rotation_speed * dt


def shoot(entity, dt):
    if entity.shoot_timer > 0:
        return

    entity.shoot_timer = entity.shoot_cooldown

    shot_pos = entity.position + DIRECTION_DOWN * entity.rect.height // 2

    shot_l = EnemyShot(
        shot_pos.x - entity.shot_offset_pos, shot_pos.y, entity.gameplay, entity
    )
    shot_r = EnemyShot(
        shot_pos.x + entity.shot_offset_pos, shot_pos.y, entity.gameplay, entity
    )
    shot_l.velocity = DIRECTION_DOWN * shot_l.speed
    shot_r.velocity = DIRECTION_DOWN * shot_r.speed
    shot_l.sound()


class Entity(pygame.sprite.Sprite):

    HIT_TIMER = 0.1

    _image_cache = {}
    _sound_cache = {}

    @classmethod
    def load_image(cls, img_path):
        if img_path not in cls._image_cache:
            cls._image_cache[img_path] = pygame.image.load(img_path).convert_alpha()
        return cls._image_cache[img_path]

    @classmethod
    def load_sound(cls, sound_path):
        if sound_path not in cls._sound_cache:
            cls._sound_cache[sound_path] = pygame.mixer.Sound(sound_path)
        return cls._sound_cache[sound_path]

    def __init__(self, x, y, gameplay):
        # Auto adds sprites to groups upon creation if a containers attribute is present
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # Image cache check so images only get loaded once instead of every time an entity is spawned
        if getattr(self, "img_path", None):
            self.image = self.load_image(self.img_path)
        # Sfx cache check so sound files only get loaded once instead of every time its used
        if getattr(self, "sfx_path", None):
            self.sfx = self.load_sound(self.sfx_path)

        self.position = pygame.Vector2(x, y)
        self.gameplay = gameplay
        self.rect = self.image.get_rect()
        self.rect.center = (self.position.x, self.position.y)
        self.mask = pygame.mask.from_surface(self.image)
        self.mask_surface = self.mask.to_surface()
        self.is_hit = False
        self.hit_timer = self.HIT_TIMER
        self.blast_radius = 0
        self.play_area = gameplay.play_area_rect
        self.speed = 0
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.behaviors = []

    def collides_with(self, other_group):
        rect_collisions = pygame.sprite.spritecollide(self, other_group, False)
        if rect_collisions:
            mask_collisions = pygame.sprite.spritecollide(
                self, other_group, False, pygame.sprite.collide_mask
            )
            if mask_collisions:
                return mask_collisions
        return []

    def take_damage(self, amount):
        pass

    def flash_when_hit(self, screen, entity_surface, entity_rect):
        if self.is_hit:
            flash = pygame.Surface(entity_surface.get_size(), pygame.SRCALPHA)
            center = (flash.get_width() // 2, flash.get_height() // 2)
            pygame.draw.circle(
                flash, (255, 255, 255, 180), center, self.rect.width // 2
            )
            screen.blit(flash, entity_rect)

    def handle_hit_timer(self, dt):
        if self.is_hit:
            self.hit_timer -= dt
            if self.hit_timer <= 0:
                self.is_hit = False
                self.hit_timer = self.HIT_TIMER

    def handle_behaviors(self, dt):
        for behavior_data in self.behaviors:
            behavior_fn_name = behavior_data["action"]
            behavior_fn = globals().get(behavior_fn_name)
            if not behavior_fn:
                raise ValueError(f"Behavior function '{behavior_fn_name}' not found.")
            params = behavior_data.get("params", {})
            params["dt"] = dt
            behavior_fn(self, **params)

    def update(self, dt):
        self.rect.center = (self.position.x, self.position.y)
        self.handle_behaviors(dt)
        self.handle_hit_timer(dt)
        self.gameplay.collision_manager.handle_boundaries(self)

    def draw(self, surface):
        pass


class Explosion(Entity):

    def __init__(self, x, y, gameplay, blast_radius, owner):
        self.img_path = IMAGES["explosion"]
        super().__init__(x, y, gameplay)
        self.blast_radius = blast_radius
        self.owner = owner
        self.init_radius = EXPLOSIONS["initial_radius"]
        self.exp_rate = EXPLOSIONS["expansion_rate"]
        self.damage = EXPLOSIONS["damage"]

    def sound(self):
        #! TODO: Get sound effect for explosion
        pass

    def collides_with(self, other_group):
        """Use circular collision detection for explosions"""
        collisions = []
        current_radius = self.init_radius

        for sprite in other_group:
            distance = self.position.distance_to(sprite.position)
            sprite_radius = sprite.rect.width * 0.5

            if distance <= current_radius + sprite_radius:
                collisions.append(sprite)

        return collisions

    def handle_explosion_expansion(self, dt):
        if self.init_radius < self.blast_radius:
            self.init_radius += self.exp_rate * dt
            if self.init_radius >= self.blast_radius:
                self.kill()

    def handle_explosion_animation(self, screen):
        scaled_image = pygame.transform.scale(
            self.image, (self.init_radius * 2, self.init_radius * 2)
        )
        scaled_rect = scaled_image.get_rect(center=self.rect.center)
        screen.blit(scaled_image, scaled_rect)

    def update(self, dt):
        super().update(dt)
        self.handle_explosion_expansion(dt)

    def draw(self, screen):
        super().draw(screen)
        self.handle_explosion_animation(screen)


class Projectile(Entity):

    def __init__(self, x, y, gameplay, owner):
        super().__init__(x, y, gameplay)
        self.owner = owner
        self.distance_traveled = 0

    def sound(self):
        self.sfx.set_volume(0.5)
        self.sfx.play()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class Shot(Projectile):

    def __init__(self, x, y, gameplay, owner):
        super().__init__(x, y, gameplay, owner)

    def sound(self):
        super().sound()

    def handle_max_range(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if (
            self.distance_traveled >= self.max_range
            or self.rect.bottom < 0
            or self.rect.top > self.gameplay.play_area_rect.height
        ):
            self.kill()

    def update(self, dt):
        super().update(dt)
        self.handle_max_range(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)


class PlayerShot(Shot):

    def __init__(self, x, y, gameplay, owner, power_level):
        if power_level == 5:
            image_key = "player_shot_ov"
        else:
            image_key = f"player_shot_lv{power_level}"
        self.img_path = IMAGES[image_key]
        self.sfx_path = SOUNDS["player_shoot"]
        super().__init__(x, y, gameplay, owner)
        self.max_range = PROJECTILES["player_shot"][power_level]["range"]
        self.speed = PROJECTILES["player_shot"][power_level]["speed"]
        self.damage = PROJECTILES["player_shot"][power_level]["damage"]


class EnemyShot(Shot):

    def __init__(self, x, y, gameplay, owner):
        self.img_path = IMAGES["enemy_shot"]
        self.sfx_path = SOUNDS["player_shoot"]
        super().__init__(x, y, gameplay, owner)
        self.max_range = PROJECTILES["enemy_shot"]["range"]
        self.speed = PROJECTILES["enemy_shot"]["speed"]
        self.damage = PROJECTILES["enemy_shot"]["damage"]


class ExplosiveProjectile(Entity):

    def __init__(self, x, y, gameplay, owner):
        super().__init__(x, y, gameplay)
        self.owner = owner
        self.distance_traveled = 0
        self.trigger_distance = 0
        self.blast_radius = 0

    def sound(self):
        self.sfx.set_volume(0.5)
        self.sfx.play()

    def check_trigger_distance(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.trigger_distance:
            self.explode()

    def explode(self):
        Explosion(
            self.position.x,
            self.position.y,
            self.gameplay,
            self.blast_radius,
            self.owner,
        )
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class Bomb(ExplosiveProjectile):

    def __init__(self, x, y, gameplay, owner):
        super().__init__(x, y, gameplay, owner)

    def sound(self):
        super().sound()

    def update(self, dt):
        super().update(dt)
        self.check_trigger_distance(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)


class PlayerBomb(Bomb):

    def __init__(self, x, y, gameplay, owner):
        self.img_path = IMAGES["player_bomb"]
        #! Add sfx_path when sound is available
        super().__init__(x, y, gameplay, owner)
        self.speed = PROJECTILES["player_bomb"]["speed"]
        self.trigger_distance = PROJECTILES["player_bomb"]["trigger_distance"]
        self.blast_radius = PROJECTILES["player_bomb"]["blast_radius"][
            owner.power_level
        ]


class EnemyBomb(Bomb):

    def __init__(self, x, y, gameplay, owner):
        self.img_path = IMAGES["enemy_bomb"]
        #! Add sfx_path when sound is available
        super().__init__(x, y, gameplay, owner)
        self.speed = PROJECTILES["enemy_bomb"]["speed"]
        self.trigger_distance = PROJECTILES["enemy_bomb"]["trigger_distance"]
        self.blast_radius = PROJECTILES["enemy_bomb"]["blast_radius"]


class Missile(ExplosiveProjectile):

    def __init__(self, x, y, gameplay, owner):
        self.img_path = IMAGES["enemy_missile"]
        #! Add sfx_path when sound is available
        super().__init__(x, y, gameplay, owner)
        self.speed = PROJECTILES["enemy_missile"]["speed"]
        self.trigger_distance = PROJECTILES["enemy_missile"]["trigger_distance"]
        self.blast_radius = PROJECTILES["enemy_missile"]["blast_radius"]

    def track_player(self):
        direction = self.gameplay.player.position - self.position
        return DIRECTION_DOWN.angle_to(direction)

    def update(self, dt):
        super().update(dt)
        forward = DIRECTION_DOWN.rotate(self.rotation)
        self.position += forward * self.speed * dt
        self.rotation = self.track_player()

    def draw(self, screen):
        super().draw(screen)
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        screen.blit(rotated_image, self.rect)


class Asteroid(Entity):

    def __init__(self, x, y, gameplay, asteroid_size="md"):
        self.img_path = IMAGES[f"asteroid_{asteroid_size}"]
        super().__init__(x, y, gameplay)
        self.speed = ENEMIES["asteroid"][asteroid_size]["speed"]
        self.hp = ENEMIES["asteroid"][asteroid_size]["hp"]
        self.score_value = self.hp
        self.rotation_speed = random.uniform(
            *ENEMIES["asteroid"]["rotation_speed_range"]
        )
        self.velocity = DIRECTION_DOWN * self.speed
        self.splits_into_name = (
            f"asteroid_{ENEMIES['asteroid'][asteroid_size]['splits_into']}"
            if ENEMIES["asteroid"][asteroid_size]["splits_into"] is not None
            else None
        )

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.gameplay.score_manager.handle_score(self.score_value)
            self.gameplay.score_manager.handle_streak_meter_inc(self.score_value)
            self.split()

    def split(self):
        self.kill()

        if self.splits_into_name is None:
            return

        # Create split events (right and left)
        for angle in [
            ENEMIES["asteroid"]["split_angle"],
            -ENEMIES["asteroid"]["split_angle"],
        ]:
            split_event = {
                "type": self.splits_into_name,
                "location": self.position,
                "behaviors": [
                    {
                        "action": "move_angled",
                        "params": {
                            "angle": angle,
                            "velocity_factor": ENEMIES["asteroid"][
                                "split_velocity_factor"
                            ],
                        },
                    },
                    {"action": "rotate_constantly", "params": {}},
                ],
            }
            self.gameplay.wave_manager.spawn_enemy(split_event)

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)


class AsteroidSM(Asteroid):

    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "sm")
        self.splits_into = None


class AsteroidMD(Asteroid):

    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "md")
        self.splits_into = "asteroid_sm"


class AsteroidLG(Asteroid):

    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "lg")
        self.splits_into = "asteroid_md"


class AsteroidXL(Asteroid):

    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "xl")
        self.splits_into = "asteroid_lg"


class Ship(Entity):
    def __init__(self, x, y, gameplay, ship_type):
        self.img_path = IMAGES[ship_type]
        super().__init__(x, y, gameplay)
        self.speed = ENEMIES[ship_type]["speed"]
        self.hp = ENEMIES[ship_type]["hp"]
        self.blast_radius = ENEMIES[ship_type]["blast_radius"]
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = ENEMIES[ship_type]["shot_cooldown"]
        self.shot_offset_pos = ENEMIES[ship_type]["shot_offset"]

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.gameplay.score_manager.handle_score(self.score_value)
            self.gameplay.score_manager.handle_streak_meter_inc(self.score_value)
            self.explode()
        self.is_hit = True

    def explode(self):
        Explosion(
            self.position.x, self.position.y, self.gameplay, self.blast_radius, None
        )
        self.kill()

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class EnemyDrone(Ship):
    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "enemy_drone")


class EnemyShip(Ship):
    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "enemy_ship")


class Boss(Entity):
    def __init__(self, x, y, gameplay, boss_type):
        self.img_path = IMAGES[boss_type]
        super().__init__(x, y, gameplay)
        self.speed = ENEMIES[boss_type]["speed"]
        self.hp = ENEMIES[boss_type]["hp"]
        self.blast_radius = ENEMIES[boss_type]["blast_radius"]
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = ENEMIES[boss_type]["shot_cooldown"]
        self.shot_offset_pos = ENEMIES[boss_type]["shot_offset"]

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.gameplay.score_manager.handle_score(self.score_value)
            self.gameplay.score_manager.handle_streak_meter_inc(self.score_value)
            self.gameplay.battle_manager.end_battle()
        self.is_hit = True

    def explode(self):
        Explosion(
            self.position.x, self.position.y, self.gameplay, self.blast_radius, None
        )
        self.kill()

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class SubBoss(Boss):
    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "sub_boss")


class LevelBoss(Boss):
    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay, "level_boss")


class Pickup(Entity):

    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay)
        self.player = self.gameplay.player_group.sprite
        pickup_type = getattr(self, "pickup_type", "health")
        data = PICKUPS.get(pickup_type, PICKUPS["health"])
        self.speed = data["speed"]
        self.rotation_speed = 45

    def apply(self):
        pass

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)
        rotated_image = pygame.transform.rotate(self.image, self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)


class HealthPickup(Pickup):

    pickup_type = "health"

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["health_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, gameplay)
        self.heal_amount = PICKUPS["health"]["heal_amount"]

    def apply(self):
        if self.player.hp >= 75:
            self.player.hp = self.player_data["base_hp"]
        else:
            self.player.hp += self.heal_amount
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class ExtraLifePickup(Pickup):

    pickup_type = "life"

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["life_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, gameplay)
        self.fallback_score = PICKUPS["life"]["fallback_score"]

    def apply(self):
        if self.player.lives < self.player_data["max_lives"]:
            self.player.lives += 1
        else:
            self.gameplay.score_manager.handle_score(self.fallback_score)
            self.gameplay.score_manager.handle_streak_meter_inc(self.fallback_score)
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class PowerLevelPickup(Pickup):

    pickup_type = "power"

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["power_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, gameplay)
        self.fallback_score = PICKUPS["power"]["fallback_score"]

    def apply(self):
        if self.player.power_level < self.player_data["max_power_level"]:
            self.player.power_level += 1
        else:
            self.gameplay.score_manager.handle_score(self.fallback_score)
            self.gameplay.score_manager.handle_streak_meter_inc(self.fallback_score)
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class OverdrivePickup(Pickup):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["overdrive_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, gameplay)

    def apply(self):
        self.player.power_level = 5
        self.player.overdriveTime = self.player_data["overdrive_duration"]
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class BombAmmoPickup(Pickup):

    pickup_type = "bomb"

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["bomb_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, gameplay)
        self.fallback_score = PICKUPS["bomb"]["fallback_score"]

    def apply(self):
        if self.player.bomb_ammo < self.player_data["max_bomb_ammo"]:
            self.player.bomb_ammo += 1
        else:
            self.gameplay.score_manager.handle_score(self.fallback_score)
            self.gameplay.score_manager.handle_streak_meter_inc(self.fallback_score)
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class InvulnerabilityPickup(Pickup):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["invulnerable_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, gameplay)

    def apply(self):
        self.player.invincibleTime = self.player_data["invulnerable_duration"]
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class Player(Entity):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["player_ship"]
        super().__init__(x, y, gameplay)
        self.acceleration = PLAYER["base_acceleration"]
        self.speed = PLAYER["base_speed"]
        self.lives = PLAYER["base_lives"]
        self.hp = PLAYER["base_hp"]
        self.blast_radius = PLAYER["death_blast_radius"]
        self.invincibleTime = 0
        self.overdriveTime = 0
        self.shoot_timer = 0
        self.bomb_ammo = PLAYER["base_bomb_ammo"]
        self.bomb_timer = 0
        self.power_level = PLAYER["base_power_level"]
        self.controls_enabled = False

    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER["shots"][self.power_level]["rate"]
        positions_to_fire = PLAYER["shots"][self.power_level]["active_pos"]
        for pos in positions_to_fire:
            offset = PLAYER["shot_pos"][pos]
            shot = PlayerShot(
                self.position.x + offset["x"],
                self.position.y + offset["y"],
                self.gameplay,
                self,
                self.power_level,
            )
            shot.velocity = DIRECTION_UP * shot.speed
        shot.sound()

    def release_bomb(self):
        if self.bomb_ammo <= 0 or self.bomb_timer > 0:
            return
        self.bomb_timer = PLAYER["bomb_cooldown"]
        self.bomb_ammo -= 1
        bomb = PlayerBomb(self.position.x, self.position.y, self.gameplay, self)
        player_forward_speed = self.velocity.dot(DIRECTION_UP)
        forward_only_speed = max(0, player_forward_speed)
        bomb.velocity = DIRECTION_UP * (forward_only_speed + bomb.speed)
        #! bomb.sound() # No sound yet, so don't need to call it

    def handle_overdrive(self, dt):
        if self.overdriveTime > 0:
            self.overdriveTime -= dt
        if self.overdriveTime < 0:
            self.overdriveTime = 0
            self.power_level -= 1

    def take_damage(self, amount):
        if self.invincibleTime > 0:
            return
        self.gameplay.score_manager.handle_streak_meter_dec()
        self.hp -= amount
        if self.hp <= 0:
            self.lives -= 1
            if self.lives <= 0:
                self.explode()
                return
            # else:
            #     self.respawn()
        self.invincibleTime = PLAYER["invincible_duration"]
        self.is_hit = True

    def handle_invincibility(self, dt):
        if self.invincibleTime > 0:
            self.invincibleTime -= dt
        if self.invincibleTime < 0:
            self.invincibleTime = 0

    def explode(self):
        Explosion(
            self.position.x,
            self.position.y,
            self.gameplay,
            self.blast_radius,
            None,
        )
        self.kill()

    def respawn(self):
        self.invincibleTime = PLAYER["invincible_duration"]
        self.position.x = self.gameplay.play_area_rect.width // 2
        self.position.y = self.gameplay.play_area_rect.height - 100
        self.hp = PLAYER["base_hp"]

    def controls(self, dt):
        if not self.controls_enabled:
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.velocity.x -= self.acceleration * dt
        if keys[pygame.K_d]:
            self.velocity.x += self.acceleration * dt
        if keys[pygame.K_w]:
            self.velocity.y -= self.acceleration * dt
        if keys[pygame.K_s]:
            self.velocity.y += self.acceleration * dt
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_e]:
            self.release_bomb()

    def apply_acceleration(self, dt):
        self.velocity *= PLAYER["velocity_decay"]
        if self.velocity.length() > self.speed:
            self.velocity.scale_to_length(self.speed)
        self.position += self.velocity * dt

    def update(self, dt):
        super().update(dt)
        self.controls(dt)
        self.apply_acceleration(dt)
        self.gameplay.collision_manager.handle_boundaries(self, action="block")
        self.handle_invincibility(dt)
        self.handle_overdrive(dt)
        self.shoot_timer -= dt
        self.bomb_timer -= dt

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)
