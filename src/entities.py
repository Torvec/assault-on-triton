import random
import pygame
from data.assets import IMAGES, SOUNDS
from data.entities import (
    EXPLOSIONS,
    PICKUPS,
    PROJECTILES,
    PLAYER,
    ASTEROID,
    ENEMY_DRONE,
    ENEMY_SHIP,
    ENEMY_DESTROYER,
    ENEMY_TURRET,
    SUB_BOSS,
    LEVEL_BOSS,
)

DIRECTION_UP = pygame.Vector2(0, -1)
DIRECTION_DOWN = pygame.Vector2(0, 1)
DIRECTION_LEFT = pygame.Vector2(-1, 0)
DIRECTION_RIGHT = pygame.Vector2(1, 0)
DIRECTION_UP_LEFT = pygame.Vector2(-1, -1).normalize()
DIRECTION_UP_RIGHT = pygame.Vector2(1, -1).normalize()
DIRECTION_DOWN_LEFT = pygame.Vector2(-1, 1).normalize()
DIRECTION_DOWN_RIGHT = pygame.Vector2(1, 1).normalize()


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
        self._debug_print_timer = 0

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
            center = (flash.get_width() * 0.5, flash.get_height() * 0.5)
            pygame.draw.circle(
                flash,
                (255, 255, 255, 180),
                center,
                self.rect.width * 0.5,
            )
            screen.blit(flash, entity_rect)

    def handle_hit_timer(self, dt):
        if self.is_hit:
            self.hit_timer -= dt
            if self.hit_timer <= 0:
                self.is_hit = False
                self.hit_timer = self.HIT_TIMER

    def handle_behaviors(self, dt):
        from src import entity_behaviors

        for behavior_data in self.behaviors:
            behavior_fn_name = behavior_data["action"]

            behavior_fn = getattr(entity_behaviors, behavior_fn_name, None)
            if not behavior_fn:
                raise ValueError(
                    f"Behavior function '{behavior_fn_name}' not found in entity_behaviors."
                )

            params = behavior_data.get("params", {})
            params["dt"] = dt
            behavior_fn(self, **params)

    def update(self, dt):
        self.rect.center = (self.position.x, self.position.y)
        self.handle_behaviors(dt)
        self.handle_hit_timer(dt)
        self.gameplay.collision_manager.handle_boundaries(self)
        self._debug_print_timer += dt
        if self._debug_print_timer >= 1.0 and len(self.behaviors) > 0:
            print(self.behaviors)
            self._debug_print_timer = 0

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
        self.speed = ASTEROID[asteroid_size]["speed"]
        self.hp = ASTEROID[asteroid_size]["hp"]
        self.score_value = self.hp
        self.rotation_speed = random.uniform(*ASTEROID["rotation_speed_range"])
        self.velocity = DIRECTION_DOWN * self.speed
        self.splits_into_name = (
            f"asteroid_{ASTEROID[asteroid_size]['splits_into']}"
            if ASTEROID[asteroid_size]["splits_into"] is not None
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
            ASTEROID["split_angle"],
            -ASTEROID["split_angle"],
        ]:
            split_event = {
                "type": self.splits_into_name,
                "location": self.position,
                "behaviors": [
                    {
                        "action": "move_straight",
                        "params": {
                            "speed": 100,
                            "angle": angle,
                            "velocity_factor": ASTEROID["split_velocity_factor"],
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


class EnemyDrone(Entity):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["enemy_drone"]
        super().__init__(x, y, gameplay)
        self.hp = ENEMY_DRONE["hp"]
        self.blast_radius = ENEMY_DRONE["blast_radius"]
        self.score_value = self.hp
        self.shot_origin = ENEMY_DRONE["shot_origin"]

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

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class EnemyShip(Entity):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["enemy_ship"]
        super().__init__(x, y, gameplay)
        self.hp = ENEMY_SHIP["hp"]
        self.blast_radius = ENEMY_SHIP["blast_radius"]
        self.score_value = self.hp
        self.shot_origin = ENEMY_SHIP["shot_origin"]

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

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class EnemyDestroyer(Entity):
    """
    Need to define the area where the destroyer itself can be damaged which is the bridge only, turrets have their own separate hit detection.
    Destroying the bridge is the only thing that destroyes the destroyer.
    The destroyer sprite will have the bridge on it rather than it being a separate sprite like the turrets and missile launchers are
    """

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["enemy_destroyer"]
        super().__init__(x, y, gameplay)
        self.hp = ENEMY_DESTROYER["hp"]
        self.blast_radius = ENEMY_DESTROYER["blast_radius"]
        self.score_value = self.hp
        self.turret_positions = ENEMY_DESTROYER["turret_positions"]
        self.turrets = []
        self.create_turrets()

    def create_turrets(self):
        for _, (turret_x, turret_y) in enumerate(self.turret_positions):
            rel_x = self.position.x + turret_x
            rel_y = self.position.y + turret_y

            self.gameplay.spawn_manager.spawn_entity(
                "enemy_turret",
                pygame.Vector2(rel_x, rel_y),
                [
                    {
                        "action": "track_player",
                        "params": {},
                    },
                    {
                        "action": "follow_parent",
                        "params": {
                            "parent": self,
                            "offset_x": turret_x,
                            "offset_y": turret_y,
                        },
                    },
                    {
                        "action": "shoot",
                        "params": {
                            "shoot_rate": 0.3,
                            "ammo_count": 6,
                            "reload_time": 2.0,
                            "projectile_type": "enemy_shot",
                        },
                    },
                ],
            )

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

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class EnemyTurret(Entity):
    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["enemy_turret"]
        super().__init__(x, y, gameplay)
        self.hp = ENEMY_TURRET["hp"]
        self.blast_radius = ENEMY_TURRET["blast_radius"]
        self.score_value = self.hp
        self.shot_origin = ENEMY_TURRET["shot_origin"]

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.gameplay.score_manager.handle_score(self.score_value)
            self.explode()
        self.is_hit = True

    def explode(self):
        Explosion(
            self.position.x, self.position.y, self.gameplay, self.blast_radius, None
        )
        self.kill()

    def draw(self, surface):
        super().draw(surface)
        rotated_image = pygame.transform.rotate(self.image, -self.rotation)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, rotated_rect)
        self.flash_when_hit(surface, rotated_image, rotated_rect)


class SubBoss(Entity):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["sub_boss"]
        super().__init__(x, y, gameplay)
        self.speed = SUB_BOSS["speed"]
        self.hp = SUB_BOSS["hp"]
        self.blast_radius = SUB_BOSS["blast_radius"]
        self.score_value = self.hp
        self.shot_origin = SUB_BOSS["shot_origin"]

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

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class LevelBoss(Entity):

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["level_boss"]
        super().__init__(x, y, gameplay)
        self.speed = LEVEL_BOSS["speed"]
        self.hp = LEVEL_BOSS["hp"]
        self.blast_radius = LEVEL_BOSS["blast_radius"]
        self.score_value = self.hp
        self.shot_origin = LEVEL_BOSS["shot_origin"]

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

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)


class Pickup(Entity):

    def __init__(self, x, y, gameplay):
        super().__init__(x, y, gameplay)
        self.player = self.gameplay.entity_manager.get_entity_instance("player")
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
        super().__init__(x, y, gameplay)
        self.heal_amount = PICKUPS["health"]["heal_amount"]

    def apply(self):
        if self.player.hp >= 75:
            self.player.hp = PLAYER["base_hp"]
        else:
            self.player.hp += self.heal_amount
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class PowerLevelPickup(Pickup):

    pickup_type = "power"

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["power_pickup"]
        super().__init__(x, y, gameplay)
        self.fallback_score = PICKUPS["power"]["fallback_score"]

    def apply(self):
        if self.player.power_level < PLAYER["max_power_level"]:
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
        super().__init__(x, y, gameplay)

    def apply(self):
        self.player.power_level = 5
        self.player.overdriveTime = PLAYER["overdrive_duration"]
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, surface):
        super().draw(surface)


class BombAmmoPickup(Pickup):

    pickup_type = "bomb"

    def __init__(self, x, y, gameplay):
        self.img_path = IMAGES["bomb_pickup"]
        super().__init__(x, y, gameplay)
        self.fallback_score = PICKUPS["bomb"]["fallback_score"]

    def apply(self):
        if self.player.bomb_ammo < PLAYER["max_bomb_ammo"]:
            self.player.bomb_ammo += 1
        else:
            self.gameplay.score_manager.handle_score(self.fallback_score)
            self.gameplay.score_manager.handle_streak_meter_inc(self.fallback_score)
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
            offset = PLAYER["shot_origin"][pos]
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
            self.explode()
            return
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

    def controls(self, dt):
        if not self.controls_enabled:
            return

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.position += DIRECTION_LEFT * self.speed * dt
        if keys[pygame.K_d]:
            self.position += DIRECTION_RIGHT * self.speed * dt
        if keys[pygame.K_w]:
            self.position += DIRECTION_UP * self.speed * dt
        if keys[pygame.K_s]:
            self.position += DIRECTION_DOWN * self.speed * dt
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_e]:
            self.release_bomb()

    def update(self, dt):
        super().update(dt)
        self.controls(dt)
        self.gameplay.collision_manager.handle_boundaries(self, action="block")
        self.handle_invincibility(dt)
        self.handle_overdrive(dt)
        self.shoot_timer -= dt
        self.bomb_timer -= dt

    def draw(self, surface):
        super().draw(surface)
        surface.blit(self.image, self.rect)
        self.flash_when_hit(surface, self.image, self.rect)
