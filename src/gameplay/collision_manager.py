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
        self.hostiles = [
            *self.sprite_groups["asteroids"],
            *self.sprite_groups["enemy_drones"],
            *self.sprite_groups["enemy_ships"],
        ]

    def update(self):
        """
        Player v Neutral / Player v Enemy Drones / Player v Enemy Ships / Player v Pickups
        """
        if self.hostiles:
            player_v_hostiles = self.player.collides_with(self.hostiles)
            if player_v_hostiles:
                for hostile in player_v_hostiles:
                    #! player takes damage
                    #! hostile takes damage
                    pass
        if self.sprite_groups["pickups"]:
            player_v_pickups = self.player.collides_with(self.sprite_groups["pickups"])
            if player_v_pickups:
                for pickup in player_v_pickups:
                    #! Apply pickup function to player
                    pickup.kill()
        if not any(
            [
                self.sprite_groups["shots"],
                self.sprite_groups["bombs"],
                self.sprite_groups["missiles"],
                self.sprite_groups["explosions"],
            ]
        ):
            return
        """
        Entity groups based on owner attribute, for early filtering
        """
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
        """
        Player Shots v Neutral / Player Shots v Enemies / Player Shots v Enemy Bombs / Player Shots v Enemy Missiles
        """
        for shot in player_shots:
            colliders = [
                *self.hostiles,
                *enemy_bombs,
                *enemy_missiles,
            ]
            shot_v_colliders = shot.collides_with(colliders)
            if shot_v_colliders:
                for collider in shot_v_colliders:
                    #! collider takes damage
                    print("player shot collided")
                    shot.kill()
        """
        Enemy Shots v Player / Enemy Shots v Neutral / Enemy Shots v Player Bombs
        """
        for shot in enemy_shots:
            colliders = [
                self.player,
                *self.sprite_groups["asteroids"],
                *player_bombs,
                *player_missiles,
            ]
            shot_v_colliders = shot.collides_with(colliders)
            if shot_v_colliders:
                for collider in shot_v_colliders:
                    #! collider takes damage
                    shot.kill()
        """
        Player Bombs v Neutral / Player Bombs v Enemy Drones / Player Bombs v Enemy Ships
        """
        for bomb in player_bombs:
            if bomb.collides_with(self.hostiles):
                #! bomb takes damage -> explodes
                pass
        """
        Enemy Bombs v Player / Enemy Bombs v Neutral / Enemy Bombs v Player Bombs
        """
        for bomb in enemy_bombs:
            colliders = [self.player, *self.sprite_groups["asteroids"], *player_bombs]
            if bomb.collides_with(colliders):
                #! bomb takes damage -> explodes
                pass
        """
        Enemy Missiles v Player / Enemy Missiles v Asteroids / Enemy Missiles v Player Bombs
        """
        for missile in enemy_missiles:
            colliders = [
                self.player,
                *self.sprite_groups["asteroids"],
                *player_bombs,
            ]
            if missile.collides_with(colliders):
                #! missile takes damage -> explodes
                pass
        """
        Player Explosion v Neutral / Player Explosion v Enemy Drones / Player Explosion v Enemy Ship / Player Explosion v Enemy Missiles / Player Explosion v Enemy Bombs
        """
        for explosion in player_explosions:
            colliders = [
                *self.hostiles,
                *enemy_bombs,
                *enemy_missiles,
            ]
            explosion_v_colliders = explosion.collides_with(colliders)
            if explosion_v_colliders:
                for collider in explosion_v_colliders:
                    #! collider takes damage
                    pass
        """
        Enemy Explosion v Player / Enemy Explosion v Neutral / Enemy Explosion v Player Missiles / Enemy Explosion v Player Bombs
        """
        for explosion in enemy_explosions:
            colliders = [
                self.player,
                *self.sprite_groups["asteroids"],
                *player_missiles,
                *player_bombs,
            ]
            explosion_v_colliders = explosion.collides_with(colliders)
            if explosion_v_colliders:
                for collider in explosion_v_colliders:
                    #! collider takes damage
                    pass
