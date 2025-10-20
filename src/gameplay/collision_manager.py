class CollisionManager:
    def __init__(self, game_play):
        self.game_play = game_play
        self.sprite_groups = {
            "player": self.game_play.player_group,
            "asteroids": self.game_play.asteroids,
            "enemy_drones": self.game_play.enemy_drones,
            "enemy_ships": self.game_play.enemy_ships,
            "missiles": self.game_play.missiles,
            "shots": self.game_play.shots,
            "bombs": self.game_play.bombs,
            "explosions": self.game_play.explosions,
            "pickups": self.game_play.pickups,
        }
        self.player = self.sprite_groups["player"].sprite

    def update(self):
        self.hostiles = [
            *self.sprite_groups["asteroids"],
            *self.sprite_groups["enemy_drones"],
            *self.sprite_groups["enemy_ships"],
        ]
        if self.hostiles:
            player_v_hostiles = self.player.collides_with(self.hostiles)
            if player_v_hostiles:
                for hostile in player_v_hostiles:
                    self.player.take_damage(1)
                    hostile.take_damage(1)
        if self.sprite_groups["pickups"]:
            player_v_pickups = self.player.collides_with(self.sprite_groups["pickups"])
            if player_v_pickups:
                for pickup in player_v_pickups:
                    pickup.apply()
        if not any(
            [
                self.sprite_groups["shots"],
                self.sprite_groups["bombs"],
                self.sprite_groups["missiles"],
                self.sprite_groups["explosions"],
            ]
        ):
            return
        player_shots = [
            e for e in self.sprite_groups["shots"] if e.owner == self.player
        ]
        enemy_shots = [e for e in self.sprite_groups["shots"] if e.owner != self.player]
        player_bombs = [
            e for e in self.sprite_groups["bombs"] if e.owner == self.player
        ]
        enemy_bombs = [e for e in self.sprite_groups["bombs"] if e.owner != self.player]
        player_missiles = [
            e for e in self.sprite_groups["missiles"] if e.owner == self.player
        ]
        enemy_missiles = [
            e for e in self.sprite_groups["missiles"] if e.owner != self.player
        ]
        player_explosions = [
            e for e in self.sprite_groups["explosions"] if e.owner == self.player
        ]
        enemy_explosions = [
            e for e in self.sprite_groups["explosions"] if e.owner != self.player
        ]
        for shot in player_shots:
            shot_v_hostiles = shot.collides_with(self.hostiles)
            if shot_v_hostiles:
                for hostile in shot_v_hostiles:
                    hostile.take_damage(shot.damage)
                    shot.kill()
        for shot in enemy_shots:
            shot_v_player = shot.collides_with([self.player])
            if shot_v_player:
                for collider in shot_v_player:
                    collider.take_damage(shot.damage)
                    shot.kill()
        for bomb in player_bombs:
            colliders = [
                *self.hostiles,
                *enemy_shots,
                *enemy_bombs,
                *enemy_missiles,
                *enemy_explosions,
            ]
            if bomb.collides_with(colliders):
                bomb.explode()
        for bomb in enemy_bombs:
            colliders = [
                self.player,
                *player_shots,
                *player_bombs,
                *player_missiles,
                *player_explosions,
            ]
            if bomb.collides_with(colliders):
                bomb.explode()
        for missile in enemy_missiles:
            colliders = [self.player, *player_bombs, *player_explosions]
            if missile.collides_with(colliders):
                missile.explode()
        for explosion in player_explosions:
            explosion_v_hostiles = explosion.collides_with(self.hostiles)
            if explosion_v_hostiles:
                for hostile in explosion_v_hostiles:
                    hostile.take_damage(explosion.damage)
        for explosion in enemy_explosions:
            explosion_v_player = explosion.collides_with([self.player])
            if explosion_v_player:
                for collider in explosion_v_player:
                    collider.take_damage(explosion.damage)
