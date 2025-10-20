from src.entities.entity import Entity
from src.entities.explosion import Explosion
from src.data.settings import ENEMIES
from src.data.assets import IMAGES


class EnemyDrone(Entity):

    def __init__(self, x, y, game_play):
        self.data = ENEMIES["drone"]
        self.img_path = IMAGES["enemy_drone"]
        super().__init__(x, y, game_play)
        self.speed = self.data["speed"]
        self.hp = self.data["hp"]
        self.blast_radius = self.data["blast_radius"]
        self.score_value = self.hp
        self.shoot_timer = 0
        self.shoot_cooldown = self.data["shot_cooldown"]
        self.shot_offset_pos = self.data["shot_offset"]

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.game_play.score.handle_score(self.score_value)
            self.game_play.score.handle_streak_meter_inc(self.score_value)
            self.explode()
        self.is_hit = True

    def explode(self):
        Explosion(
            self.position.x, self.position.y, self.game_play, self.blast_radius, self
        )
        self.kill()

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)
        self.flash_when_hit(screen, self.image, self.rect)


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

    def take_damage(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            self.game_play.score.handle_score(self.score_value)
            self.game_play.score.handle_streak_meter_inc(self.score_value)
            self.explode()
        self.is_hit = True

    def explode(self):
        Explosion(
            self.position.x, self.position.y, self.game_play, self.blast_radius, self
        )
        self.kill()

    def update(self, dt):
        super().update(dt)
        self.shoot_timer -= dt

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)
        self.flash_when_hit(screen, self.image, self.rect)
