from src.entities.entity_layer_flags import *


class CollisionManager:
    def __init__(self, game_play):
        self.game_play = game_play
        self.sprite_groups = [
            self.game_play.asteroids,
            self.game_play.enemy_drones,
            self.game_play.enemy_ships,
            self.game_play.missiles,
            self.game_play.shots,
            self.game_play.bombs,
            self.game_play.explosions,
            self.game_play.pickups,
        ]
        self.destroy_methods = {
            NEUTRAL: lambda entity: (
                entity.split() if hasattr(entity, "split") else entity.kill()
            ),
            ENEMY: lambda entity: (
                entity.explode() if hasattr(entity, "explode") else entity.kill()
            ),
            EXPLOSIVE: lambda entity: (
                entity.explode() if hasattr(entity, "explode") else entity.kill()
            ),
        }

        # Use frozenset for collision layer pairs so that (A, B) and (B, A) map to the same handler.
        # This ensures symmetric collision handling regardless of entity order.
        # If a tuple or set were used, you'd need to add both (A, B) and (B, A) for every case.
        self.collision_handlers = {
            frozenset({PLAYER, ENEMY}): self._handle_player_vs_hostile,
            frozenset({PLAYER, NEUTRAL}): self._handle_player_vs_hostile,
            frozenset({PLAYER, PROJECTILE}): self._handle_projectile_vs_player,
            frozenset({PLAYER, EXPLOSIVE}): self._handle_explosive_projectile_vs_player,
            frozenset({PLAYER, EXPLOSION}): self._handle_explosion_vs_player,
            frozenset({PLAYER, PICKUP}): self._handle_player_vs_pickup,
            frozenset({PROJECTILE, ENEMY}): self._handle_projectile_vs_target,
            frozenset({PROJECTILE, NEUTRAL}): self._handle_projectile_vs_target,
            frozenset({PROJECTILE, EXPLOSIVE}): self._handle_projectile_vs_explosive,
            frozenset({EXPLOSIVE, ENEMY}): self._handle_explosive_projectile_vs_target,
            frozenset(
                {EXPLOSIVE, NEUTRAL}
            ): self._handle_explosive_projectile_vs_target,
            frozenset({EXPLOSIVE, ALLY}): self._handle_explosive_projectile_vs_target,
            frozenset({EXPLOSION, ENEMY}): self._handle_explosion_vs_entity,
            frozenset({EXPLOSION, NEUTRAL}): self._handle_explosion_vs_entity,
            frozenset({EXPLOSION, EXPLOSIVE}): self._handle_explosion_vs_explosive,
        }

    def can_collide(self, entity_a, entity_b):
        return (entity_a.mask & entity_b.layer) != 0 and (
            entity_b.mask & entity_a.layer
        ) != 0

    def handle_all_collisions(self):
        entities = [self.game_play.player]
        for group in self.sprite_groups:
            entities.extend(sprite for sprite in group.sprites() if sprite.alive())

        for i, entity_a in enumerate(entities):
            if not entity_a.alive():
                continue
            for entity_b in entities[i + 1 :]:
                if not entity_b.alive():
                    continue
                if self.can_collide(entity_a, entity_b) and entity_a.collides_with(
                    entity_b
                ):
                    self.handle_collision(entity_a, entity_b)

    def handle_collision(self, entity_a, entity_b):
        key = frozenset({entity_a.layer, entity_b.layer})
        handler_fn = self.collision_handlers.get(key)
        if handler_fn:
            handler_fn(entity_a, entity_b)

    # === HANDLER FUNCTIONS ===

    # _split_pair ensures that the entity with the specified layer is always returned first.
    # This makes handler code simpler and more predictable, so you can always refer to the first
    # return value as the 'main' entity (e.g., player, projectile, etc.) regardless of argument order.
    def _split_pair(self, entity_a, entity_b, layer):
        return (entity_a, entity_b) if entity_a.layer == layer else (entity_b, entity_a)

    def _apply_damage_to_player(self, player, damage):
        if player.invincibleTime > 0:
            return
        player.handle_hit(damage)
        self.game_play.score.handle_streak_meter_dec()
        if player.hp <= 0:
            player.handle_death()
        if player.lives <= 0:
            self.game_play.score.store_score(self.game_play.score.score)
            self.game_play.game.set_scene("GameOver")

    def _damage_entity(self, target, damage, source=None):
        if not hasattr(target, "hp"):
            return
        target.hp -= damage
        target.is_hit = True
        if target.hp <= 0:
            self._destroy_entity(target, source)

    def _destroy_entity(self, target, source=None):
        destroy = self.destroy_methods.get(target.layer)
        if destroy:
            destroy(target)
        else:
            target.kill()

        if source and source.layer == PLAYER and hasattr(target, "score_value"):
            self.game_play.score.handle_score(target.score_value)
            self.game_play.score.handle_streak_meter_inc(target.score_value)

    def _handle_player_vs_hostile(self, entity_a, entity_b):
        player, hostile = self._split_pair(entity_a, entity_b, PLAYER)
        self._apply_damage_to_player(player, 1)
        self._damage_entity(hostile, 1)

    def _handle_projectile_vs_player(self, entity_a, entity_b):
        projectile, player = self._split_pair(entity_a, entity_b, PROJECTILE)
        owner = getattr(projectile, "owner", None)
        if owner is player:
            return
        projectile.kill()
        self._apply_damage_to_player(player, projectile.damage)

    def _handle_projectile_vs_target(self, entity_a, entity_b):
        projectile, target = self._split_pair(entity_a, entity_b, PROJECTILE)
        owner = getattr(projectile, "owner", None)
        if owner is target:
            return
        projectile.kill()
        if target.layer == EXPLOSIVE:
            if hasattr(target, "hp"):
                self._damage_entity(target, projectile.damage, source=owner)
            else:
                target.explode()
                if owner and owner.layer == PLAYER and hasattr(target, "score_value"):
                    self.game_play.score.handle_score(target.score_value)
                    self.game_play.score.handle_streak_meter_inc(target.score_value)
            return
        self._damage_entity(target, projectile.damage, source=owner)

    def _handle_projectile_vs_explosive(self, entity_a, entity_b):
        projectile, explosive = self._split_pair(entity_a, entity_b, PROJECTILE)
        owner = getattr(projectile, "owner", None)
        if owner is explosive:
            return
        projectile.kill()
        if hasattr(explosive, "hp"):
            self._damage_entity(explosive, projectile.damage, source=owner)
        else:
            explosive.explode()
            if owner and owner.layer == PLAYER and hasattr(explosive, "score_value"):
                self.game_play.score.handle_score(explosive.score_value)
                self.game_play.score.handle_streak_meter_inc(explosive.score_value)

    def _handle_explosive_projectile_vs_player(self, entity_a, entity_b):
        explosive, player = self._split_pair(entity_a, entity_b, EXPLOSIVE)
        owner = getattr(explosive, "owner", None)
        explosive.explode()

    def _handle_explosive_projectile_vs_target(self, entity_a, entity_b):
        explosive, target = self._split_pair(entity_a, entity_b, EXPLOSIVE)
        owner = getattr(explosive, "owner", None)
        if owner is target:
            return
        explosive.explode()

    def _handle_explosion_vs_player(self, entity_a, entity_b):
        explosion, player = self._split_pair(entity_a, entity_b, EXPLOSION)
        owner = getattr(explosion, "owner", None)
        if owner is player:
            return
        self._apply_damage_to_player(player, explosion.damage)

    def _handle_explosion_vs_entity(self, entity_a, entity_b):
        explosion, target = self._split_pair(entity_a, entity_b, EXPLOSION)
        owner = getattr(explosion, "owner", None)
        self._damage_entity(target, explosion.damage, source=owner)

    def _handle_explosion_vs_explosive(self, entity_a, entity_b):
        explosion, explosive = self._split_pair(entity_a, entity_b, EXPLOSION)
        explosive.explode()

    def _handle_player_vs_pickup(self, entity_a, entity_b):
        player, pickup = self._split_pair(entity_a, entity_b, PLAYER)
        if hasattr(pickup, "apply"):
            pickup.apply(player)
        pickup.kill()
