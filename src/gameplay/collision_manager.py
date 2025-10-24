class CollisionManager:
    def __init__(self, game_play):
        self.game_play = game_play
        self.sprite_groups = {
            "asteroids": self.game_play.asteroids,
            "enemy_drones": self.game_play.enemy_drones,
            "enemy_ships": self.game_play.enemy_ships,
            "missiles": self.game_play.missiles,
            "shots": self.game_play.shots,
            "bombs": self.game_play.bombs,
            "explosions": self.game_play.explosions,
            "pickups": self.game_play.pickups,
        }
        self.player = self.game_play.player_group.sprite

    def handle_shots(self, shot_type, colliders):
        for shot in shot_type:
            shot_v_colliders = shot.collides_with(colliders)
            if shot_v_colliders:
                for collider in shot_v_colliders:
                    collider.take_damage(shot.damage)
                    shot.kill()

    def handle_explosives(self, explosive_type, colliders):
        for explosive in explosive_type:
            if explosive.collides_with(colliders):
                explosive.explode()

    def handle_explosions(self, explosion_type, colliders):
        for explosion in explosion_type:
            explosion_v_colliders = explosion.collides_with(colliders)
            if explosion_v_colliders:
                for collider in explosion_v_colliders:
                    collider.take_damage(explosion.damage)

    def filter_by_owner(self, group, is_player=True):
        if is_player:
            return [e for e in self.sprite_groups[group] if e.owner == self.player]
        return [e for e in self.sprite_groups[group] if e.owner != self.player]

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
        player_shots = self.filter_by_owner("shots", is_player=True)
        enemy_shots = self.filter_by_owner("shots", is_player=False)
        player_bombs = self.filter_by_owner("bombs", is_player=True)
        enemy_bombs = self.filter_by_owner("bombs", is_player=False)
        player_missiles = self.filter_by_owner("missiles", is_player=True)
        enemy_missiles = self.filter_by_owner("missiles", is_player=False)
        player_explosions = self.filter_by_owner("explosions", is_player=True)
        enemy_explosions = self.filter_by_owner("explosions", is_player=False)
        player_bomb_colliders = [
            *self.hostiles,
            *enemy_shots,
            *enemy_bombs,
            *enemy_missiles,
            *enemy_explosions,
        ]
        enemy_bomb_colliders = [
            self.player,
            *player_shots,
            *player_bombs,
            *player_missiles,
            *player_explosions,
        ]
        enemy_missile_colliders = [self.player, *player_bombs, *player_explosions]
        self.handle_shots(player_shots, self.hostiles)
        self.handle_shots(enemy_shots, [self.player])
        self.handle_explosives(player_bombs, player_bomb_colliders)
        self.handle_explosives(enemy_bombs, enemy_bomb_colliders)
        self.handle_explosives(enemy_missiles, enemy_missile_colliders)
        self.handle_explosions(player_explosions, self.hostiles)
        self.handle_explosions(enemy_explosions, [self.player])
