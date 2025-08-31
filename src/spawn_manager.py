import random
import pygame


class SpawnManager(pygame.sprite.Sprite):
    def __init__(self, game_play, entity_class, target_count, spawn_rate):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.game_play = game_play
        self.entity_class = entity_class
        self.target_count = target_count
        self.spawn_rate = spawn_rate
        self.play_area = game_play.play_area_rect
        self.spawn_timer = 0.0
        self.spawn_count = 0
        self.spawn_location = [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(
                self.play_area.left + x * self.play_area.width,
                self.play_area.top - 50,
            ),
        ]
        self.game_play.active_spawners.add(self)

    def spawn_entity(self):
        position = self.spawn_location[1](random.uniform(0, 1))
        entity = self.entity_class(position.x, position.y, self.game_play)
        entity.velocity = self.spawn_location[0] * entity.speed
        self.game_play.active_targets.add(entity)
        print(
            f"{entity} added to Active Targets. Length: {len(self.game_play.active_targets)}"
        )

    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_count == self.target_count:
            if self in self.game_play.active_spawners:
                self.game_play.active_spawners.remove(self)
            return
        elif self.spawn_timer > self.spawn_rate:
            self.spawn_entity()
            self.spawn_timer = 0
            self.spawn_count += 1
