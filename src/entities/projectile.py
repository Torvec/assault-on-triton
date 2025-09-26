from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.entities.entity_layer_flags import (
    LAYER_PLAYER,
    LAYER_ENEMY,
    LAYER_ALLY,
    LAYER_NEUTRAL,
    LAYER_PROJECTILE,
    LAYER_EXPLOSIVE_PROJECTILE,
)


class Projectile(Entity):
    layer = LAYER_PROJECTILE

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner

    @property
    def mask(self):
        if self.owner.layer == LAYER_PLAYER:
            return LAYER_ENEMY | LAYER_EXPLOSIVE_PROJECTILE | LAYER_NEUTRAL
        elif self.owner.layer == LAYER_ENEMY:
            return LAYER_PLAYER | LAYER_ALLY | LAYER_NEUTRAL
        elif self.owner.layer == LAYER_ALLY:
            return LAYER_ENEMY | LAYER_NEUTRAL

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExplosiveProjectile(Entity):
    layer = LAYER_EXPLOSIVE_PROJECTILE

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner
        self.blast_radius = 0

    @property
    def mask(self):
        if self.owner.layer == LAYER_PLAYER:
            return LAYER_ENEMY | LAYER_NEUTRAL
        elif self.owner.layer == LAYER_ENEMY:
            return LAYER_PLAYER | LAYER_ALLY | LAYER_NEUTRAL
        elif self.owner.layer == LAYER_ALLY:
            return LAYER_ENEMY | LAYER_NEUTRAL

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
