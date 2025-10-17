from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.data.settings import ENEMIES
from src.data.assets import IMAGES


class EnemyShip(Entity):

    def __init__(self, x, y, game_play):
        self.data = ENEMIES["ship"]
        self.img_path = IMAGES["enemy_ship"]
        super().__init__(x, y, game_play)
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
        screen.blit(self.image, self.rect)
        self.flash_when_hit(screen, self.image, self.rect)
