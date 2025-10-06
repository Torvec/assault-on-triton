from src.entities.entity import Entity
from src.entities.entity_layer_flags import PICKUP, PLAYER
from src.config.settings import PICKUPS, PLAYER as PLAYER_CONFIG
from src.config.assets import IMAGES


class Pickup(Entity):

    layer = PICKUP
    mask = PLAYER

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
        # Default pickup values - subclasses will override pickup_type
        pickup_type = getattr(self, "pickup_type", "health")
        config = PICKUPS.get(pickup_type, PICKUPS["health"])
        self.radius = config["radius"]
        self.speed = config["speed"]

    def apply(self, player):
        self.remove_active_targets()

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
        pickup_rect = self.image.get_rect(center=self.position)
        screen.blit(self.image, pickup_rect)


class HealthPickup(Pickup):

    pickup_type = "health"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["health_pickup"]
        self.player_config = PLAYER_CONFIG
        super().__init__(x, y, game_play)
        self.heal_amount = PICKUPS["health"]["heal_amount"]

    def apply(self, player):
        if player.hp >= 75:
            player.hp = self.player_config["base_hp"]
        else:
            player.hp += self.heal_amount
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class ExtraLifePickup(Pickup):

    pickup_type = "life"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["life_pickup"]
        self.player_config = PLAYER_CONFIG
        super().__init__(x, y, game_play)
        self.fallback_score = PICKUPS["life"]["fallback_score"]

    def apply(self, player):
        if player.lives < self.player_config["max_lives"]:
            player.lives += 1
        else:
            self.game_play.score.score += self.fallback_score
            self.game_play.score.handle_streak_meter_inc(self.fallback_score)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class PowerLevelPickup(Pickup):

    pickup_type = "power"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["power_pickup"]
        self.player_config = PLAYER_CONFIG
        super().__init__(x, y, game_play)
        self.fallback_score = PICKUPS["power"]["fallback_score"]

    def apply(self, player):
        if player.power_level < self.player_config["max_power_level"]:
            player.power_level += 1
        else:
            self.game_play.score.score += self.fallback_score
            self.game_play.score.handle_streak_meter_inc(self.fallback_score)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class OverdrivePickup(Pickup):

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["overdrive_pickup"]
        self.player_config = PLAYER_CONFIG
        super().__init__(x, y, game_play)

    def apply(self, player):
        player.power_level = 4
        player.overdriveTime = self.player_config["overdrive_duration"]
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class BombAmmoPickup(Pickup):

    pickup_type = "bomb"

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["bomb_pickup"]
        self.player_config = PLAYER_CONFIG
        super().__init__(x, y, game_play)
        self.fallback_score = PICKUPS["bomb"]["fallback_score"]

    def apply(self, player):
        if player.bomb_ammo < self.player_config["max_bomb_ammo"]:
            player.bomb_ammo += 1
        else:
            self.game_play.score.score += self.fallback_score
            self.game_play.score.handle_streak_meter_inc(self.fallback_score)
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)


class InvulnerabilityPickup(Pickup):

    def __init__(self, x, y, game_play):
        self.img_path = IMAGES["invulnerable_pickup"]
        self.player_config = PLAYER_CONFIG
        super().__init__(x, y, game_play)

    def apply(self, player):
        player.invincibleTime = self.player_config["invulnerable_duration"]
        super().apply(player)

    def update(self, dt):
        super().update(dt)

    def draw(self, screen):
        super().draw(screen)
