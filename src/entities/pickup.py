from src.entities.entity import Entity
from src.entities.entity_layer_flags import LAYER_PICKUP, LAYER_PLAYER

class Pickup(Entity):
    
    layer = LAYER_PICKUP
    mask = LAYER_PLAYER

    def __init__(self, x, y, game_play):
        super().__init__(x, y, game_play)
