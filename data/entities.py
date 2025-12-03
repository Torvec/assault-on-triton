PLAYER = {
    "base_acceleration": 600,
    "base_speed": 350,
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
        1: {"x": 0, "y": -20},
        2: {"x": -7, "y": -56},
        3: {"x": 7, "y": -56},
        4: {"x": -20, "y": -55},
        5: {"x": 20, "y": -55},
        6: {"x": -25, "y": -20},
        7: {"x": 25, "y": -20},
    },
    "shots": {
        1: {"rate": 0.16, "active_pos": [1]},
        2: {"rate": 0.16, "active_pos": [2, 3]},
        3: {"rate": 0.16, "active_pos": [1, 2, 3]},
        4: {"rate": 0.16, "active_pos": [1, 2, 3, 4, 5]},
        5: {"rate": 0.16, "active_pos": [1, 2, 3, 4, 5, 6, 7]},
    },
}

ASTEROID = {
    "sm": {
        "speed": 100,
        "hp": 2,
        "splits_into": None,
    },
    "md": {
        "speed": 100,
        "hp": 4,
        "splits_into": "sm",
    },
    "lg": {
        "speed": 100,
        "hp": 6,
        "splits_into": "md",
    },
    "xl": {
        "speed": 100,
        "hp": 10,
        "splits_into": "lg",
    },
    "rotation_speed_range": (-90, 90),
    "split_angle": 30,
    "split_velocity_factor": 1.2,
}

ENEMY_DRONE = {
    "speed": 150,
    "hp": 4,
    "blast_radius": 32,
    "shot_origin": {
        1: {"x": 10, "y": 0},
        2: {"x": -10, "y": 0},
    },
}

ENEMY_SHIP = {
    "speed": 175,
    "hp": 8,
    "blast_radius": 48,
    "shot_origin": {
        1: {"x": 16, "y": 0},
        2: {"x": -16, "y": 0},
    },
}

SUB_BOSS = {
    "speed": 200,
    "hp": 256,
    "blast_radius": 256,
    "shot_origin": {
        1: {"x": 0, "y": 0},
        2: {"x": 0, "y": 0},
    },
}

LEVEL_BOSS = {
    "speed": 200,
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
            "range": 768,
            "speed": 700,
            "damage": 2,
        },
        2: {
            "range": 768,
            "speed": 700,
            "damage": 2,
        },
        3: {
            "range": 1024,
            "speed": 700,
            "damage": 3,
        },
        4: {
            "range": 1024,
            "speed": 700,
            "damage": 4,
        },
        5: {
            "range": 1024,
            "speed": 700,
            "damage": 6,
        },
    },
    "enemy_shot": {
        "range": 768,
        "speed": 400,
        "damage": 5,
    },
    "player_bomb": {
        "speed": 250,
        "trigger_distance": 256,
        "blast_radius": {
            1: 192,
            2: 256,
            3: 384,
            4: 512,
            5: 512,
        },
    },
    "enemy_bomb": {
        "speed": 250,
        "trigger_distance": 256,
        "blast_radius": 384,
    },
    "enemy_missile": {
        "speed": 200,
        "trigger_distance": 256,
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
    "expansion_rate": 256,
    "damage": 5,
}
