from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.explosion import Explosion
from src.scenes.game_play.entities.entity_data import *


class EnemyDrone(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = ENEMY_DRONE_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = ENEMY_DRONE_RADIUS
        self.speed = ENEMY_DRONE_SPEED
        self.hp = ENEMY_DRONE_HP
        self.blast_radius = ENEMY_DRONE_BLAST_RADIUS
        self.score_value = self.hp
        self.shoot_timer = 0.4
        self.shot_offset_pos = 4

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)
        self.position += DIRECTION_DOWN * self.speed * dt
        self.shoot_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        drone_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, drone_rect)
        self.flash_when_hit(screen, self.image, drone_rect)
