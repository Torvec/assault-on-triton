from src.entities.entity import Entity
from src.entities.entity_layer_flags import PICKUP, PLAYER


class Pickup(Entity):

    layer = PICKUP
    mask = PLAYER

    RADIUS = 16
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
    HP_AMOUNT = 25

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        if player.hp >= 75:
            player.hp = player.BASE_HP
        else:
            player.hp += self.HP_AMOUNT
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
        if player.lives < player.MAX_LIVES:
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
        if player.power_level < player.MAX_POWER_LEVEL:
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
        player.overdriveTime = player.OVERDRIVE_DURATION
        super().apply(player)

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
        if player.bomb_ammo < player.MAX_BOMB_AMMO:
            player.bomb_ammo += 1
        else:
            self.game_play.score.score += score_amount
            self.game_play.score.handle_streak_meter_inc(score_amount)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class InvulnerabilityPickup(Pickup):

    IMG_PATH = "assets/invulnerable_pickup.png"

    def __init__(self, x, y, game_play):
        self.img_path = self.IMG_PATH
        super().__init__(x, y, game_play)

    def apply(self, player):
        player.invincibleTime = player.INVULNERABLE_DURATION
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
