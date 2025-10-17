from src.entities.projectile import ExplosiveProjectile
from src.entities.explosion import Explosion
from src.data.settings import PROJECTILES
from src.data.assets import IMAGES


class Bomb(ExplosiveProjectile):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play, owner)
        self.distance_traveled = 0
        self.speed = 0
        self.blast_radius = 0
        self.trigger_distance = 0

    def sound(self):
        #! TODO: get sound effect for releasing bomb
        pass

    def check_trigger_distance(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.trigger_distance:
            self.explode()

    def explode(self):
        Explosion(
            self.position.x,
            self.position.y,
            self.game_play,
            self.blast_radius,
            self.owner,
        )
        self.kill()

    def update(self, dt):
        super().update(dt)
        self.check_trigger_distance(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)


class PlayerBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["player_bomb"]
        self.img_path = IMAGES["bomb"]
        super().__init__(x, y, game_play, owner)
        self.speed = self.data["speed"]
        self.blast_radius = self.data["blast_radius"][owner.power_level]
        self.trigger_distance = self.data["trigger_distance"]


class EnemyBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.data = PROJECTILES["enemy_bomb"]
        self.img_path = IMAGES["bomb"]
        super().__init__(x, y, game_play, owner)
        self.speed = self.data["speed"]
        self.blast_radius = self.data["blast_radius"]
        self.trigger_distance = self.data["trigger_distance"]
