import pygame
from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.shot import Shot
from src.scenes.game_play.entities.bomb import Bomb
from src.scenes.game_play.entities.entity_data import *


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
        self.shoot_timer = PLAYER_SHOOT_TIMER
        shot_pos = self.position + DIRECTION_UP * self.radius
        shot_l = Shot(shot_pos.x - PLAYER_SHOT_POS_OFFSET, shot_pos.y, self.game_play, self)
        shot_r = Shot(shot_pos.x + PLAYER_SHOT_POS_OFFSET, shot_pos.y, self.game_play, self)
        shot_l.velocity = DIRECTION_UP * shot_l.speed
        shot_r.velocity = DIRECTION_UP * shot_r.speed
        shot_l.sound()

    def release_bomb(self):
        if self.bomb_ammo <= 0 or self.bomb_timer > 0:
            return
        self.bomb_timer = 2.0
        self.bomb_ammo -= 1
        bomb = Bomb(self.position.x, self.position.y, self.game_play)
        player_forward_speed = self.velocity.dot(DIRECTION_UP)
        forward_only_speed = max(0, player_forward_speed)
        bomb.velocity = DIRECTION_UP * (forward_only_speed + bomb.speed)
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
