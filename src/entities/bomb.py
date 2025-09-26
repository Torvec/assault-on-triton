from src.entities.projectile import ExplosiveProjectile
from src.entities.explosion import Explosion


class Bomb(ExplosiveProjectile):
    
    RADIUS = 8
    SPEED = 200
    BLAST_RADIUS = 384
    TRIGGER_DISTANCE = 256
    IMG_PATH = "assets/e_bomb.png"

    def __init__(self, x, y, game_play, owner):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play, owner)
        self.radius = self.RADIUS
        self.speed = self.SPEED
        self.blast_radius = self.BLAST_RADIUS
        self.distance_traveled = 0
        self.trigger_distance = self.TRIGGER_DISTANCE

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
