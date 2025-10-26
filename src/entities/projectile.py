import pygame
from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.data.settings import PROJECTILES
from src.data.assets import IMAGES, SOUNDS
from src.entities.entity_directions import DIRECTION_DOWN


class Projectile(Entity):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
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

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play, owner)

    def sound(self):
        super().sound()

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
        if power_level == 5:
            image_key = "player_shot_ov"
        else:
            image_key = f"player_shot_lv{power_level}"
        self.img_path = IMAGES[image_key]
        self.sfx_path = SOUNDS["player_shoot"]
        super().__init__(x, y, game_play, owner)
        self.max_range = PROJECTILES["player_shot"][power_level]["range"]
        self.speed = PROJECTILES["player_shot"][power_level]["speed"]
        self.damage = PROJECTILES["player_shot"][power_level]["damage"]


class EnemyShot(Shot):

    def __init__(self, x, y, game_play, owner):
        self.img_path = IMAGES["enemy_shot"]
        self.sfx_path = SOUNDS["player_shoot"]
        super().__init__(x, y, game_play, owner)
        self.max_range = PROJECTILES["enemy_shot"]["range"]
        self.speed = PROJECTILES["enemy_shot"]["speed"]
        self.damage = PROJECTILES["enemy_shot"]["damage"]


class ExplosiveProjectile(Entity):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
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

    def __init__(self, x, y, game_play, owner):
        self.img_path = IMAGES["player_bomb"]
        #! Add sfx_path when sound is available
        super().__init__(x, y, game_play, owner)
        self.speed = PROJECTILES["player_bomb"]["speed"]
        self.trigger_distance = PROJECTILES["player_bomb"]["trigger_distance"]
        self.blast_radius = PROJECTILES["player_bomb"]["blast_radius"][
            owner.power_level
        ]


class EnemyBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.img_path = IMAGES["enemy_bomb"]
        #! Add sfx_path when sound is available
        super().__init__(x, y, game_play, owner)
        self.speed = PROJECTILES["enemy_bomb"]["speed"]
        self.trigger_distance = PROJECTILES["enemy_bomb"]["trigger_distance"]
        self.blast_radius = PROJECTILES["enemy_bomb"]["blast_radius"]


class Missile(ExplosiveProjectile):

    def __init__(self, x, y, game_play, owner):
        self.img_path = IMAGES["enemy_missile"]
        #! Add sfx_path when sound is available
        super().__init__(x, y, game_play, owner)
        self.speed = PROJECTILES["enemy_missile"]["speed"]
        self.trigger_distance = PROJECTILES["enemy_missile"]["trigger_distance"]
        self.blast_radius = PROJECTILES["enemy_missile"]["blast_radius"]

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
