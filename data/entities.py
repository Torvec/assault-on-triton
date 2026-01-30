PLAYER = {
    "base_acceleration": 600,
    "base_speed": 200,
    "base_lives": 1,
    "max_lives": 3,
    "base_hp": 100,
    "invincible_duration": 2,
    "invulnerable_duration": 30,
    "overdrive_duration": 20,
    "base_bomb_ammo": 3,
    "max_bomb_ammo": 6,
    "bomb_cooldown": 2.0,
    "base_power_level": 1,
    "max_power_level": 4,
    "death_blast_radius": 128,
    "velocity_decay": 0.99,
    "shot_origin": {
        1: {"x": 0, "y": -24},
        2: {"x": -6, "y": -20},
        3: {"x": 6, "y": -20},
        4: {"x": -12, "y": -12},
        5: {"x": 12, "y": -12},
        6: {"x": -18, "y": -8},
        7: {"x": 18, "y": -8},
    },
    "shots": {
        1: {"rate": 0.28, "active_pos": [1]},
        2: {"rate": 0.24, "active_pos": [2, 3]},
        3: {"rate": 0.20, "active_pos": [2, 3, 4, 5]},
        4: {"rate": 0.16, "active_pos": [2, 3, 4, 5, 6, 7]},
        5: {"rate": 0.12, "active_pos": [1, 2, 3, 4, 5, 6, 7]},
    },
}

ASTEROID = {
    "sm": {
        "speed": 80,
        "hp": 2,
        "splits_into": None,
    },
    "md": {
        "speed": 80,
        "hp": 4,
        "splits_into": "sm",
    },
    "lg": {
        "speed": 80,
        "hp": 6,
        "splits_into": "md",
    },
    "xl": {
        "speed": 80,
        "hp": 10,
        "splits_into": "lg",
    },
    "rotation_speed_range": (-90, 90),
    "split_angle": 30,
    "split_velocity_factor": 1.2,
}

ENEMY_DRONE = {
    "hp": 4,
    "blast_radius": 48,
    "shot_origin": {
        1: {"x": 11, "y": 11},
        2: {"x": -11, "y": 11},
    },
}

ENEMY_FIGHTER = {
    "hp": 8,
    "blast_radius": 64,
    "shot_origin": {
        1: {"x": 13, "y": 6},
        2: {"x": -13, "y": 6},
    },
}

ENEMY_DESTROYER = {
    "hp": 16,
    "blast_radius": 216,
    "turret_positions": [
        (0, 120),
        (0, 60),
        (36, -30),
        (-36, -30),
    ],
}

ENEMY_TURRET = {
    "hp": 4,
    "blast_radius": 64,
    "shot_origin": {1: {"x": 0, "y": 24}},
}

SUB_BOSS = {
    "hp": 256,
    "blast_radius": 256,
    "shot_origin": {
        1: {"x": 0, "y": 0},
        2: {"x": 0, "y": 0},
    },
}

LEVEL_BOSS = {
    "hp": 512,
    "blast_radius": 512,
    "shot_origin": {
        1: {"x": 0, "y": 0},
        2: {"x": 0, "y": 0},
    },
}

PROJECTILES = {
    "player_shot": {
        1: {
            "range": 180,
            "speed": 500,
            "damage": 2,
        },
        2: {
            "range": 220,
            "speed": 500,
            "damage": 2,
        },
        3: {
            "range": 260,
            "speed": 500,
            "damage": 3,
        },
        4: {
            "range": 300,
            "speed": 500,
            "damage": 4,
        },
        5: {
            "range": 360,
            "speed": 500,
            "damage": 6,
        },
    },
    "enemy_shot": {
        "range": 200,
        "speed": 300,
        "damage": 5,
    },
    "player_bomb": {
        "speed": 200,
        "trigger_distance": 128,
        "blast_radius": {
            1: 64,
            2: 128,
            3: 192,
            4: 256,
            5: 360,
        },
    },
    "enemy_bomb": {
        "speed": 200,
        "trigger_distance": 128,
        "blast_radius": 128,
    },
    "enemy_missile": {
        "speed": 200,
        "trigger_distance": 128,
        "blast_radius": 64,
    },
}

PICKUPS = {
    "health": {
        "radius": 16,
        "speed": 120,
        "heal_amount": 25,
    },
    "power": {
        "radius": 16,
        "speed": 120,
        "fallback_score": 100,
    },
    "bomb": {
        "radius": 16,
        "speed": 120,
        "fallback_score": 100,
    },
    "life": {
        "radius": 16,
        "speed": 120,
        "fallback_score": 100,
    },
}

EXPLOSIONS = {
    "initial_radius": 4,
    "expansion_rate": 128,
    "damage": 5,
}
