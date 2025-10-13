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
from src.data.settings import ENEMIES
from src.data.assets import IMAGES


class EnemyDrone(Entity):

    layer = ENEMY
    mask = PLAYER | ALLY | PROJECTILE | EXPLOSIVE | EXPLOSION | NEUTRAL

    def __init__(self, x, y, game_play):
        self.data = ENEMIES["drone"]
        self.img_path = IMAGES["enemy_drone"]
        super().__init__(x, y, game_play)
        self.radius = self.data["radius"]
        self.speed = self.data["speed"]
        self.hp = self.data["hp"]
        self.blast_radius = self.data["blast_radius"]
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = self.data["shot_cooldown"]
        self.shot_offset_pos = self.data["shot_offset"]

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
        drone_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, drone_rect)
        self.flash_when_hit(screen, self.image, drone_rect)
