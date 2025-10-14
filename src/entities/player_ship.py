import pygame
from src.entities.entity import Entity
from src.entities.shot import PlayerShot
from src.entities.bomb import PlayerBomb
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
from src.data.settings import PLAYER as PLAYER_DATA
from src.data.assets import IMAGES


class Player(Entity):

    layer = PLAYER
    mask = ENEMY | PROJECTILE | EXPLOSIVE | EXPLOSION | NEUTRAL | PICKUP

    def __init__(self, x, y, game_play):
        self.data = PLAYER_DATA
        self.img_path = IMAGES["player_ship"]
        super().__init__(x, y, game_play)

        self.radius = self.data["radius"]
        self.acceleration = self.data["base_acceleration"]
        self.speed = self.data["base_speed"]
        self.lives = self.data["base_lives"]
        self.hp = self.data["base_hp"]
        self.blast_radius = self.data["death_blast_radius"]

        self.invincibleTime = 0
        self.overdriveTime = 0
        self.shoot_timer = 0
        self.bomb_ammo = self.data["base_bomb_ammo"]
        self.bomb_timer = 0
        self.power_level = self.data["base_power_level"]

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
        self.shoot_timer = self.data["fire_rates"][self.power_level]
        shot_pos = self.position + DIRECTION_UP * self.radius
        shot_l1 = PlayerShot(
            shot_pos.x - self.data["primary_shot_offset"],
            shot_pos.y,
            self.game_play,
            self,
            self.power_level,
        )
        shot_r1 = PlayerShot(
            shot_pos.x + self.data["primary_shot_offset"],
            shot_pos.y,
            self.game_play,
            self,
            self.power_level,
        )
        shot_l1.velocity = DIRECTION_UP * shot_l1.speed
        shot_r1.velocity = DIRECTION_UP * shot_r1.speed
        if self.power_level > 2:
            shot_l2 = PlayerShot(
                shot_pos.x - self.data["secondary_shot_offset"],
                shot_pos.y,
                self.game_play,
                self,
                self.power_level,
            )
            shot_r2 = PlayerShot(
                shot_pos.x + self.data["secondary_shot_offset"],
                shot_pos.y,
                self.game_play,
                self,
                self.power_level,
            )
            shot_l2.velocity = DIRECTION_UP * shot_l1.speed
            shot_r2.velocity = DIRECTION_UP * shot_r1.speed
        if self.power_level > 3:
            shot_l3 = PlayerShot(
                shot_pos.x - self.data["tertiary_shot_offset"],
                shot_pos.y + 32,
                self.game_play,
                self,
                self.power_level,
            )
            shot_r3 = PlayerShot(
                shot_pos.x + self.data["tertiary_shot_offset"],
                shot_pos.y + 32,
                self.game_play,
                self,
                self.power_level,
            )
            shot_l3.velocity = DIRECTION_UP * shot_l1.speed
            shot_r3.velocity = DIRECTION_UP * shot_r1.speed
        shot_l1.sound()

    def release_bomb(self):
        if self.bomb_ammo <= 0 or self.bomb_timer > 0:
            return
        self.bomb_timer = self.data["bomb_cooldown"]
        self.bomb_ammo -= 1
        bomb = PlayerBomb(self.position.x, self.position.y, self.game_play, self)
        player_forward_speed = self.velocity.dot(DIRECTION_UP)
        forward_only_speed = max(0, player_forward_speed)
        bomb.velocity = DIRECTION_UP * (forward_only_speed + bomb.speed)
        bomb.sound()

    def respawn(self):
        self.invincibleTime = self.data["invincible_duration"]
        self.position.x = self.game_play.play_area_rect.width // 2
        self.position.y = self.game_play.play_area_rect.height - 100
        self.hp = self.data["base_hp"]

    def handle_hit(self, damage_amount):
        self.hp -= damage_amount
        self.invincibleTime = self.data["invincible_duration"]
        self.is_hit = True

    def handle_invincibility(self, dt):
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
        self.velocity *= self.data["velocity_decay"]
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
