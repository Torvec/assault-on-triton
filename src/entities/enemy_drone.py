from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.entities.entity_data import *


class EnemyDrone(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = ENEMY_DRONE_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = ENEMY_DRONE_RADIUS
        self.speed = ENEMY_DRONE_SPEED
        self.hp = ENEMY_DRONE_HP
        self.blast_radius = ENEMY_DRONE_BLAST_RADIUS
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = ENEMY_DRONE_SHOT_COOLDOWN
        self.shot_offset_pos = ENEMY_DRONE_SHOT_OFFSET_POS

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        drone_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, drone_rect)
        self.flash_when_hit(screen, self.image, drone_rect)
