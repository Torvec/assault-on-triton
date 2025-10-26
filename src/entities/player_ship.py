import pygame
from src.entities.entity import Entity
from src.entities.projectile import PlayerShot, PlayerBomb
from src.entities.explosion import Explosion
from src.entities.entity_directions import DIRECTION_UP
from src.data.settings import PLAYER
from src.data.assets import IMAGES


class Player(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["player_ship"]
        super().__init__(x, y, game_play)
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
        self.scripted_movement_active = False
        self.target_position = pygame.Vector2(0, 0)
        self.movement_speed = 0

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
                self.game_play,
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
        bomb = PlayerBomb(self.position.x, self.position.y, self.game_play, self)
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
        self.game_play.score.handle_streak_meter_dec()
        self.hp -= amount
        if self.hp <= 0:
            self.lives -= 1
            self.explode()
            if self.lives <= 0:
                return
            else:
                self.respawn()
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
            self.game_play,
            self.blast_radius,
            self,
        )
        self.kill()

    def respawn(self):
        self.invincibleTime = PLAYER["invincible_duration"]
        self.position.x = self.game_play.play_area_rect.width // 2
        self.position.y = self.game_play.play_area_rect.height - 100
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

    def move_player_to(self, x, y, speed):
        self.controls_enabled = False
        self.scripted_movement_active = True
        self.target_position = pygame.Vector2(x, y)
        self.movement_speed = speed

    def handle_scripted_movement(self, dt):
        if not self.scripted_movement_active:
            return

        # Calculate direction to target
        direction = self.target_position - self.position
        distance = direction.length()

        # Check if we've reached the target
        if distance < 5:  # Threshold to prevent jittering
            self.position = self.target_position.copy()
            self.scripted_movement_active = False
            self.velocity = pygame.Vector2(0, 0)
            return

        # Move towards target at specified speed
        if distance > 0:
            direction.normalize_ip()
            self.velocity = direction * self.movement_speed
            self.position += self.velocity * dt

    def update(self, dt):
        super().update(dt)
        self.controls(dt)
        if not self.scripted_movement_active:
            self.apply_acceleration(dt)
            self.handle_boundaries("block")
        else:
            self.handle_scripted_movement(dt)
        self.handle_invincibility(dt)
        self.handle_overdrive(dt)
        self.shoot_timer -= dt
        self.bomb_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)
        self.flash_when_hit(screen, self.image, self.rect)
