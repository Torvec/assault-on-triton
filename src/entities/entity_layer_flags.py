# Bit shift layer flags for collision detection (split bits in half for visual clarity in comments)
LAYER_PLAYER = 1 << 0  # 0000 0001
LAYER_ENEMY = 1 << 1  # 0000 0010
LAYER_ALLY = 1 << 2  # 0000 0100
LAYER_NEUTRAL = 1 << 3  # 0000 1000
LAYER_PROJECTILE = 1 << 4  # 0001 0000
LAYER_EXPLOSIVE_PROJECTILE = 1 << 5  # 0010 0000
LAYER_EXPLOSION = 1 << 6 # 0100 0000
LAYER_PICKUP = 1 << 7  # 1000 0000
