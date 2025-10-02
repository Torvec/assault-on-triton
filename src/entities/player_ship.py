import pygame
from src.entities.entity import Entity
from src.entities.shot import PlayerShot
from src.entities.bomb import Bomb
from src.entities.explosion import Explosion
from src.entities.entity_layer_flags import (
    PLAYER,
    ENEMY,
    PROJECTILE,
    EXPLOSIVE,
    EXPLOSION,
    NEUTRAL,
    PICKUP,
)
from src.entities.entity_directions import DIRECTION_UP


class Player(Entity):

    layer = PLAYER
    mask = ENEMY | PROJECTILE | EXPLOSIVE | EXPLOSION | NEUTRAL | PICKUP

    RADIUS = 48
    BASE_ACCELERATION = 600
    BASE_SPEED = 350
    BASE_LIVES = 1
    MAX_LIVES = 3
    BASE_HP = 100
    INVINCIBLE_DURATION = 2
    INVULNERABLE_DURATION = 30
    OVERDRIVE_DURATION = 30
    OVERDRIVE_SHOT_POS_OFFSET = 20
    OVERDRIVE_SHOOT_COOLDOWN = 0.1
    LVL1_SHOOT_COOLDOWN = 0.2
    LVL2_SHOOT_COOLDOWN = 0.1625
    LVL3_SHOOT_COOLDOWN = 0.125
    SHOT_POS_OFFSET = 8
    BASE_BOMB_AMMO = 3
    MAX_BOMB_AMMO = 6
    BOMB_RELEASE_COOLDOWN = 2.0
    BASE_POWER_LEVEL = 1
    MAX_POWER_LEVEL = 3
    DEATH_BLAST_RADIUS = 128
    VELOCITY_DECAY = 0.99
    IMG_PATH = "assets/player_spaceship.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = self.RADIUS
        self.acceleration = self.BASE_ACCELERATION
        self.speed = self.BASE_SPEED
        self.lives = self.BASE_LIVES
        self.hp = self.BASE_HP
        self.invincibleTime = 0
        self.overdriveTime = 0
        self.shoot_timer = 0
        self.bomb_ammo = self.BASE_BOMB_AMMO
        self.bomb_timer = 0
        self.power_level = self.BASE_POWER_LEVEL
        self.blast_radius = self.DEATH_BLAST_RADIUS

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
        fire_rate = {
            1: self.LVL1_SHOOT_COOLDOWN,
            2: self.LVL2_SHOOT_COOLDOWN,
            3: self.LVL3_SHOOT_COOLDOWN,
            4: self.OVERDRIVE_SHOOT_COOLDOWN,
        }
        self.shoot_timer = fire_rate[self.power_level]
        shot_pos = self.position + DIRECTION_UP * self.radius
        shot_l = PlayerShot(
            shot_pos.x - self.SHOT_POS_OFFSET,
            shot_pos.y,
            self.game_play,
            self,
            self.power_level,
        )
        shot_r = PlayerShot(
            shot_pos.x + self.SHOT_POS_OFFSET,
            shot_pos.y,
            self.game_play,
            self,
            self.power_level,
        )
        if self.overdriveTime > 0:
            shot_l2 = PlayerShot(
                shot_pos.x - self.OVERDRIVE_SHOT_POS_OFFSET,
                shot_pos.y,
                self.game_play,
                self,
                self.power_level,
            )
            shot_r2 = PlayerShot(
                shot_pos.x + self.OVERDRIVE_SHOT_POS_OFFSET,
                shot_pos.y,
                self.game_play,
                self,
                self.power_level,
            )
            shot_l2.velocity = DIRECTION_UP * shot_l.speed
            shot_r2.velocity = DIRECTION_UP * shot_r.speed
        shot_l.velocity = DIRECTION_UP * shot_l.speed
        shot_r.velocity = DIRECTION_UP * shot_r.speed
        shot_l.sound()

    def release_bomb(self):
        if self.bomb_ammo <= 0 or self.bomb_timer > 0:
            return
        self.bomb_timer = self.BOMB_RELEASE_COOLDOWN
        self.bomb_ammo -= 1
        bomb = Bomb(self.position.x, self.position.y, self.game_play, self)
        player_forward_speed = self.velocity.dot(DIRECTION_UP)
        forward_only_speed = max(0, player_forward_speed)
        bomb.velocity = DIRECTION_UP * (forward_only_speed + bomb.speed)
        bomb.sound()

    def respawn(self):
        self.invincibleTime = self.INVINCIBLE_DURATION
        self.position.x = self.game_play.play_area_rect.width // 2
        self.position.y = self.game_play.play_area_rect.height - 100
        self.hp = self.BASE_HP

    def handle_hit(self, damage_amount):
        self.hp -= damage_amount
        self.invincibleTime = self.INVINCIBLE_DURATION
        self.is_hit = True

    def handle_invincibility(self, dt):
        """Handles invincibility frames when hit and invulnerability powerup timer"""
        if self.invincibleTime > 0:
            self.invincibleTime -= dt
        if self.invincibleTime < 0:
            self.invincibleTime = 0

    def handle_overdrive(self, dt):
        if self.overdriveTime > 0:
            self.overdriveTime -= dt
        if self.overdriveTime < 0:
            self.overdriveTime = 0
            self.power_level -= 1

    def handle_death(self):
        self.lives -= 1
        Explosion(
            self.position.x,
            self.position.y,
            self.blast_radius,
            self,
        )
        self.respawn()

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
        self.velocity *= self.VELOCITY_DECAY
        if self.velocity.length() > self.speed:
            self.velocity.scale_to_length(self.speed)
        self.position += self.velocity * dt

    def update(self, dt):
        super().update(dt)
        self.controls(dt)
        self.apply_acceleration(dt)
        self.handle_boundaries("block")
        self.handle_invincibility(dt)
        self.handle_overdrive(dt)
        self.shoot_timer -= dt
        self.bomb_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        ship_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, ship_rect)
        self.flash_when_hit(screen, self.image, ship_rect)
