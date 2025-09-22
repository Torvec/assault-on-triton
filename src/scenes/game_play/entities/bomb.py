from src.scenes.game_play.entities.entity import Entity
from src.scenes.game_play.entities.explosion import Explosion
from src.scenes.game_play.entities.entity_data import *

class Bomb(Entity):

    def __init__(self, x, y, game_play):
        self.img_path = BOMB_IMG_PATH
        super().__init__(x, y, game_play)
        self.radius = BOMB_RADIUS
        self.speed = BOMB_SPEED
        self.blast_radius = BOMB_BLAST_RADIUS
        self.distance_traveled = 0
        self.trigger_distance = BOMB_TRIGGER_DISTANCE

    def sound(self):
        pass  # The launch sound not explosion sound

    def trigger_explosion(self, dt):
        distance_this_frame = self.velocity.length() * dt
        self.distance_traveled += distance_this_frame
        if self.distance_traveled >= self.trigger_distance:
            Explosion(
                self.position.x, self.position.y, self.blast_radius, self.game_play
            )
            self.kill()

    def update(self, dt):
        super().update(dt)
        self.trigger_explosion(dt)
        self.position += self.velocity * dt

    def draw(self, screen):
        super().draw(screen)
        bomb_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, bomb_rect)
