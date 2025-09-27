from src.entities.entity import Entity
from src.entities.entity_layer_flags import PICKUP, PLAYER


class Pickup(Entity):

    layer = PICKUP
    mask = PLAYER

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
