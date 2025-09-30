from src.entities.entity import Entity
from src.entities.entity_layer_flags import PICKUP, PLAYER


class Pickup(Entity):

    layer = PICKUP
    mask = PLAYER

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)

    def apply(self):
        pass

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class HealthPickup(Pickup):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)

    def apply(self):
        self.game_play.player.hp += 25

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExtraLifePickup(Pickup):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)

    def apply(self):
        score_amount = 100
        if self.game_play.player.lives < 3:
            self.game_play.player.live += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class PowerLevelPickup(Pickup):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)

    def apply(self):
        score_amount = 100
        if self.game_play.player.power_level < 3:
            self.game_play.player.power_level += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class OverdrivePickup(Pickup):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)

    def apply(self):
        self.game_play.player.power_level = 4

    # TODO: Needs to be on a timer (30 secs?) and when that timer is up the power level will return to whatever it was before the pickup was activated

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class BombAmmoPickup(Pickup):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)

    def apply(self):
        score_amount = 100
        if self.game_play.player.bomb_ammo < 5:
            self.game_play.player.bomb_ammo += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)
