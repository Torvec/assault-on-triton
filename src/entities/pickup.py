from src.entities.entity import Entity
from src.entities.entity_layer_flags import PICKUP, PLAYER


class Pickup(Entity):

    layer = PICKUP
    mask = PLAYER

    RADIUS = 12
    SPEED = 150

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.radius = self.RADIUS
        self.speed = self.SPEED

    def apply(self, player):
        self.remove_active_targets()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
        pickup_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, pickup_rect)


class HealthPickup(Pickup):

    IMG_PATH = "assets/health_pickup.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        if player.hp >= 75:
            player.hp = 100
        else:
            player.hp += 25
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExtraLifePickup(Pickup):

    IMG_PATH = "assets/life_pickup.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        score_amount = 100
        if player.lives < 3:
            player.lives += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class PowerLevelPickup(Pickup):

    IMG_PATH = "assets/power_pickup.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        score_amount = 100
        if player.power_level < 3:
            player.power_level += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class OverdrivePickup(Pickup):

    IMG_PATH = "assets/overdrive_pickup.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        player.power_level = 4
        super().apply(player)

    # TODO: Needs to be on a timer (30 secs?) and when that timer is up the power level will return to whatever it was before the pickup was activated

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class BombAmmoPickup(Pickup):

    IMG_PATH = "assets/bomb_pickup.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        score_amount = 100
        if player.bomb_ammo < 5:
            player.bomb_ammo += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
