from src.entities.projectile import ExplosiveProjectile
from src.entities.explosion import Explosion
from src.config.settings import PROJECTILES
from src.config.assets import IMAGES


class Bomb(ExplosiveProjectile):

    def __init__(self, x, y, game_play, owner):
        super().__init__(x, y, game_play, owner)
        self.distance_traveled = 0
        self.radius = 0
        self.speed = 0
        self.blast_radius = 0
        self.trigger_distance = 0

    def sound(self):
        pass  # The launch sound not explosion sound

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
        bomb_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, bomb_rect)


class PlayerBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.config = PROJECTILES["player_bomb"]
        self.img_path = IMAGES["bomb"]
        super().__init__(x, y, game_play, owner)
        self.radius = self.config["radius"]
        self.speed = self.config["speed"]
        self.blast_radius = self.config["blast_radius"][owner.power_level]
        self.trigger_distance = self.config["trigger_distance"]


class EnemyBomb(Bomb):

    def __init__(self, x, y, game_play, owner):
        self.config = PROJECTILES["enemy_bomb"]
        self.img_path = IMAGES["bomb"]
        super().__init__(x, y, game_play, owner)
        self.radius = self.config["radius"]
        self.speed = self.config["speed"]
        self.blast_radius = self.config["blast_radius"]
        self.trigger_distance = self.config["trigger_distance"]
