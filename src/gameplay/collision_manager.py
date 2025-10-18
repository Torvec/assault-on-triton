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


    def update(self):
        player = self.sprite_groups["player"].sprite
        if not player:
            return

        player.collides_with(self.sprite_groups["asteroids"])
        player.collides_with(self.sprite_groups["enemy_drones"])
        player.collides_with(self.sprite_groups["enemy_ships"])
        player.collides_with(self.sprite_groups["pickups"])
 