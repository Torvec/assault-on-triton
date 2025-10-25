import pygame
from src.entities.collidable_entity import CollidableEntity
from src.entities.explosion import Explosion
from src.data.settings import PROJECTILES
from src.data.assets import IMAGES, SOUNDS
from src.entities.entity_directions import DIRECTION_DOWN


class Projectile(CollidableEntity):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class Shot(Projectile):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play, owner)

        self.distance_traveled = 0
        self.max_range = 0
        self.speed = 0
        self.damage = 0
        self.sfx = None

    def sound(self):
        self.shoot_sound = pygame.mixer.Sound(self.sfx)
        self.shoot_sound.set_volume(0.5)
        self.shoot_sound.play()

    def handle_max_range(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if (
            self.distance_traveled >= self.max_range
            or self.rect.bottom < 0
            or self.rect.top > self.game_play.play_area_rect.height
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

    def __init__(self, x, y, game_play, owner, power_level):
        self.data = PROJECTILES["player_shot"][power_level]
        if power_level == 5:
            image_key = "player_shot_ov"
        else:
            image_key = f"player_shot_lv{power_level}"
        self.img_path = IMAGES[image_key]
        super().__init__(x, y, game_play, owner)
        self.max_range = self.data["range"]
        self.speed = self.data["speed"]
        self.damage = self.data["damage"]
        self.sfx = SOUNDS["player_shoot"]


class EnemyShot(Shot):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["enemy_shot"]
        self.img_path = IMAGES["enemy_shot"]
        super().__init__(x, y, game_play, owner)
        self.max_range = self.data["range"]
        self.speed = self.data["speed"]
        self.damage = self.data["damage"]
        self.sfx = SOUNDS["player_shoot"]


class ExplosiveProjectile(CollidableEntity):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner
        self.trigger_distance = 0
        self.blast_radius = 0

    def check_trigger_distance(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.trigger_distance:
            self.explode()

    def explode(self):
        Explosion(
            self.position.x,
            self.position.y,
            self.game_play,
            self.blast_radius,
            self.owner,
        )
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class Bomb(ExplosiveProjectile):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play, owner)
        self.distance_traveled = 0
        self.speed = 0
        self.blast_radius = 0

    def sound(self):
        #! TODO: get sound effect for releasing bomb
        pass

    def update(self, dt):
        super().update(dt)
        self.check_trigger_distance(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)


class PlayerBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["player_bomb"]
        self.img_path = IMAGES["player_bomb"]
        super().__init__(x, y, game_play, owner)
        self.speed = self.data["speed"]
        self.trigger_distance = self.data["trigger_distance"]
        self.blast_radius = self.data["blast_radius"][owner.power_level]


class EnemyBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["enemy_bomb"]
        self.img_path = IMAGES["enemy_bomb"]
        super().__init__(x, y, game_play, owner)
        self.speed = self.data["speed"]
        self.trigger_distance = self.data["trigger_distance"]
        self.blast_radius = self.data["blast_radius"]


class Missile(ExplosiveProjectile):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["enemy_missile"]
        self.img_path = IMAGES["enemy_missile"]
        super().__init__(x, y, game_play, owner)
        self.speed = self.data["speed"]
        self.trigger_distance = self.data["trigger_distance"]
        self.blast_radius = self.data["blast_radius"]

    def track_player(self):
        direction = self.game_play.player.position - self.position
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
