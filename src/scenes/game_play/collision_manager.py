from src.entities.explosion import Explosion

"""
Factions:
    - Player
    - Enemy
    - Ally/Civilian
    - Environment (asteroids/space debris/other obstacles)

Collision Relationships:
- Player can not damage Player (player blasters, player bomb explosions, etc)
- Player can damage Enemy, Ally/Civilian, Environment entities via collision, blasters, bombs (reduced damage for ally/civilian entities?)
- 

All Collision Scenarios:
- Player receives damage by:
    - Colliding with another entity (enemy ship, asteroid, ally ship, debris, etc)
    - Getting hit by enemy/ally projectiles (blasters, missile, bombs, giant ass lasers, etc.)
- Player can damage:
    - Enemy/ally entities by colliding
    - Enemy/ally entities by shooting projectiles/bombs/special weapons
- Enemy entities don't damage other enemies via collisions (going to have to prevent them from ever touching if possible)
- Enemy entities don't damage other enemies via projectiles either
- Enemy entites can damage ally/civilian ships via projectiles
- Explosions:
    - Triggered by a player's bomb will damage only enemy entities (also might need to setup a DPS system as they currently do damage per frame)
    - Triggered by a player destroying an enemy ship type entity will damage other enemy ship types
    - Triggered by an enemy's bomb will damage the player and any ally/civilian entities

"""

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

    def handle_all_collisions(self):
        for handler in self.collision_handlers:
            for entity in handler["group"]:
                # Player collision
                if (
                    entity.collides_with(self.game_play.player)
                    and self.game_play.player.invincibleTime == 0
                ):
                    self.game_play.player.invincibleTime = 2
                    self.game_play.player.shield -= 5
                    self.game_play.player.is_hit = True
                    entity.hp -= 1
                    self.game_play.score.handle_streak_meter_dec()
                    # Check if entity should be destroyed after hitting player
                    if entity.hp <= 0:
                        handler["destroy_method"](entity)
                        self.game_play.score.handle_score(entity.score_value)
                    if self.game_play.player.shield <= 0:
                        self.game_play.player.lives -= 1
                        Explosion(
                            self.game_play.player.position.x,
                            self.game_play.player.position.y,
                            self.game_play.player.blast_radius,
                            self,
                        )
                        self.game_play.player.respawn()
                    if self.game_play.player.lives <= 0:
                        self.game_play.score.store_score(self.game_play.score.score)
                        self.game_play.game.set_scene("GameOver")

                # Shot collision
                for shot in self.game_play.shots:
                    if shot.collides_with(entity) and entity is not shot.owner:
                        entity.is_hit = True
                        shot.kill()
                        entity.hp -= 1
                        if entity.hp <= 0:
                            handler["destroy_method"](entity)
                            self.game_play.score.handle_score(entity.score_value)
                            self.game_play.score.handle_streak_meter_inc(
                                entity.score_value
                            )

                # Bomb collision
                for bomb in self.game_play.bombs:
                    if bomb.collides_with(entity):
                        Explosion(
                            bomb.position.x, bomb.position.y, bomb.blast_radius, self
                        )
                        bomb.kill()

                # Explosion Collision
                for explosion in self.game_play.explosions:
                    if explosion.collides_with(entity):
                        entity.is_hit = True
                        entity.hp -= 5
                        if entity.hp <= 0:
                            handler["destroy_method"](entity)
                            self.game_play.score.handle_score(entity.score_value)
                            self.game_play.score.handle_streak_meter_inc(
                                entity.score_value
                            )
