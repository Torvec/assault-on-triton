from src.entities.entity import Entity
from src.entities.explosion import Explosion


class EnemyDrone(Entity):

    RADIUS = 16
    SPEED = 300
    HP = 3
    SHOT_COOLDOWN = 0.6
    SHOT_OFFSET_POS = 4
    DEATH_BLAST_RADIUS = 32
    IMG_PATH = "assets/enemy_drone.png"

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
        Explosion(self.position.x, self.position.y, self.blast_radius, self.game_play)

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        drone_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, drone_rect)
        self.flash_when_hit(screen, self.image, drone_rect)
