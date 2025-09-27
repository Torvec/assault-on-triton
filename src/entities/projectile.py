from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.entities.entity_layer_flags import (
    PLAYER,
    ENEMY,
    ALLY,
    NEUTRAL,
    PROJECTILE,
    EXPLOSIVE,
)


class Projectile(Entity):
    layer = PROJECTILE

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner

    @property
    def mask(self):
        if self.owner.layer == PLAYER:
            return ENEMY | EXPLOSIVE | NEUTRAL
        elif self.owner.layer == ENEMY:
            return PLAYER | ALLY | NEUTRAL
        elif self.owner.layer == ALLY:
            return ENEMY | NEUTRAL

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExplosiveProjectile(Entity):
    layer = EXPLOSIVE

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner
        self.blast_radius = 0

    @property
    def mask(self):
        if self.owner.layer == PLAYER:
            return ENEMY | NEUTRAL
        elif self.owner.layer == ENEMY:
            return PLAYER | ALLY | NEUTRAL
        elif self.owner.layer == ALLY:
            return ENEMY | NEUTRAL

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
