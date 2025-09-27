# Bit shift layer flags for collision detection (split bits in half for visual clarity in comments)
PLAYER = 1 << 0  # 0000 0001
ENEMY = 1 << 1  # 0000 0010
ALLY = 1 << 2  # 0000 0100
NEUTRAL = 1 << 3  # 0000 1000
PROJECTILE = 1 << 4  # 0001 0000
EXPLOSIVE = 1 << 5  # 0010 0000
EXPLOSION = 1 << 6  # 0100 0000
PICKUP = 1 << 7  # 1000 0000
