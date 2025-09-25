class CollisionManager:
    def __init__(self, game_play):
        self.game_play = game_play
        self.collision_handlers = [
            {
                "group": self.game_play.asteroids,
                "destroy_method": lambda entity: entity.split(),
            },
            {
                "group": self.game_play.enemy_drones,
                "destroy_method": lambda entity: entity.explode(),
            },
            {
                "group": self.game_play.enemy_ships,
                "destroy_method": lambda entity: entity.explode(),
            },
            {
                "group": self.game_play.missiles,
                "destroy_method": lambda entity: entity.explode(),
            },
        ]

    def handle_entity_hit(self, entity, damage_amount):
        entity.hp -= damage_amount
        entity.is_hit = True

    def handle_entity_destroyed(self, entity, handler, add_to_score):
        if entity.hp <= 0:
            handler["destroy_method"](entity)
        if add_to_score:
            self.game_play.score.handle_score(entity.score_value)
            self.game_play.score.handle_streak_meter_inc(entity.score_value)
        else:
            return

    def handle_all_collisions(self):
        for handler in self.collision_handlers:
            for entity in handler["group"]:
                # Player collision
                if (
                    entity.collides_with(self.game_play.player)
                    and self.game_play.player.invincibleTime == 0
                ):
                    self.game_play.player.handle_hit(1)
                    self.handle_entity_hit(entity, 1)
                    self.game_play.score.handle_streak_meter_dec()
                    self.handle_entity_destroyed(entity, handler, add_to_score=False)
                    if self.game_play.player.hp <= 0:
                        self.game_play.player.handle_death()
                    if self.game_play.player.lives <= 0:
                        self.game_play.score.store_score(self.game_play.score.score)
                        self.game_play.game.set_scene("GameOver")

                # Shot collision
                for shot in self.game_play.shots:
                    if shot.collides_with(entity) and entity is not shot.owner:
                        shot.kill()
                        self.handle_entity_hit(entity, 1)
                        self.handle_entity_destroyed(entity, handler, add_to_score=True)

                # Bomb collision
                for bomb in self.game_play.bombs:
                    if bomb.collides_with(entity):
                        bomb.explode()

                # Explosion Collision
                for explosion in self.game_play.explosions:
                    if explosion.collides_with(entity):
                        self.handle_entity_hit(entity, 5)
                        self.handle_entity_destroyed(entity, handler, add_to_score=True)
