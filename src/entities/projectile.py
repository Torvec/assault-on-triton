from src.entities.entity import Entity
from src.entities.explosion import Explosion


class Projectile(Entity):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExplosiveProjectile(Entity):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play)
        self.owner = owner
        self.blast_radius = 0

    def explode(self):
        self.remove_active_targets()
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
