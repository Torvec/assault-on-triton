from src.entities.entity import Entity
from src.data.settings import PICKUPS, PLAYER
from src.data.assets import IMAGES


class Pickup(Entity):

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        self.player = self.game_play.player
        pickup_type = getattr(self, "pickup_type", "health")
        data = PICKUPS.get(pickup_type, PICKUPS["health"])
        self.speed = data["speed"]

    def apply(self):
        pass

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.image, self.rect)


class HealthPickup(Pickup):

    pickup_type = "health"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["health_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, game_play)
        self.heal_amount = PICKUPS["health"]["heal_amount"]

    def apply(self):
        if self.player.hp >= 75:
            self.player.hp = self.player_data["base_hp"]
        else:
            self.player.hp += self.heal_amount
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExtraLifePickup(Pickup):

    pickup_type = "life"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["life_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, game_play)
        self.fallback_score = PICKUPS["life"]["fallback_score"]

    def apply(self):
        if self.player.lives < self.player_data["max_lives"]:
            self.player.lives += 1
        else:
            self.game_play.score.handle_score(self.fallback_score)
            self.game_play.score.handle_streak_meter_inc(self.fallback_score)
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class PowerLevelPickup(Pickup):

    pickup_type = "power"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["power_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, game_play)
        self.fallback_score = PICKUPS["power"]["fallback_score"]

    def apply(self):
        if self.player.power_level < self.player_data["max_power_level"]:
            self.player.power_level += 1
        else:
            self.game_play.score.handle_score(self.fallback_score)
            self.game_play.score.handle_streak_meter_inc(self.fallback_score)
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class OverdrivePickup(Pickup):

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["overdrive_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, game_play)

    def apply(self):
        self.player.power_level = 5
        self.player.overdriveTime = self.player_data["overdrive_duration"]
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class BombAmmoPickup(Pickup):

    pickup_type = "bomb"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["bomb_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, game_play)
        self.fallback_score = PICKUPS["bomb"]["fallback_score"]

    def apply(self):
        if self.player.bomb_ammo < self.player_data["max_bomb_ammo"]:
            self.player.bomb_ammo += 1
        else:
            self.game_play.score.handle_score(self.fallback_score)
            self.game_play.score.handle_streak_meter_inc(self.fallback_score)
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class InvulnerabilityPickup(Pickup):

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["invulnerable_pickup"]
        self.player_data = PLAYER
        super().__init__(x, y, game_play)

    def apply(self):
        self.player.invincibleTime = self.player_data["invulnerable_duration"]
        self.kill()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
