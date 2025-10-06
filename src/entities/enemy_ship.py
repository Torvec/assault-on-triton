from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.entities.entity_layer_flags import (
    PLAYER,
    ENEMY,
    ALLY,
    NEUTRAL,
    PROJECTILE,
    EXPLOSIVE,
    EXPLOSION,
)
from src.config.settings import ENEMIES
from src.config.assets import IMAGES


class EnemyShip(Entity):

    layer = ENEMY
    mask = PLAYER | ALLY | PROJECTILE | EXPLOSIVE | EXPLOSION | NEUTRAL

    def __init__(self, x, y, game_play):
        self.config = ENEMIES["ship"]
        self.img_path = IMAGES["enemy_ship"]
        super().__init__(x, y, game_play)
        self.radius = self.config["radius"]
        self.speed = self.config["speed"]
        self.hp = self.config["hp"]
        self.blast_radius = self.config["blast_radius"]
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = self.config["shot_cooldown"]
        self.shot_offset_pos = self.config["shot_offset"]

    def explode(self):
        self.remove_active_targets()
        Explosion(
            self.position.x, self.position.y, self.game_play, self.blast_radius, self
        )

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        ship_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, ship_rect)
        self.flash_when_hit(screen, self.image, ship_rect)
