from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.explosion import Explosion
from src.scenes.game_play.entities.entity_data import *

class EnemyShip(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = ENEMY_SHIP_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = ENEMY_SHIP_RADIUS
        self.speed = ENEMY_SHIP_SPEED
        self.hp = ENEMY_SHIP_HP
        self.blast_radius = ENEMY_SHIP_BLAST_RADIUS
        self.score_value = self.hp

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)
        self.position += DIRECTION_DOWN * self.speed * dt

    def draw(self, screen):
        super().draw(screen)
        ship_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, ship_rect)
        self.flash_when_hit(screen, self.image, ship_rect)
