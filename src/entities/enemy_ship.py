from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.entities.entity_layer_flags import (
    LAYER_PLAYER,
    LAYER_ENEMY,
    LAYER_ALLY,
    LAYER_NEUTRAL,
    LAYER_PROJECTILE,
    LAYER_EXPLOSIVE_PROJECTILE,
    LAYER_EXPLOSION,
)


class EnemyShip(Entity):

    layer = LAYER_ENEMY
    mask = (
        LAYER_PLAYER
        | LAYER_ALLY
        | LAYER_PROJECTILE
        | LAYER_EXPLOSIVE_PROJECTILE
        | LAYER_EXPLOSION
        | LAYER_NEUTRAL
    )

    RADIUS = 32
    SPEED = 200
    HP = 6
    SHOT_COOLDOWN = 0.4
    SHOT_OFFSET_POS = 4
    DEATH_BLAST_RADIUS = 48
    IMG_PATH = "assets/enemy_ship.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = self.RADIUS
        self.speed = self.SPEED
        self.hp = self.HP
        self.blast_radius = self.DEATH_BLAST_RADIUS
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = self.SHOT_COOLDOWN
        self.shot_offset_pos = self.SHOT_OFFSET_POS

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
