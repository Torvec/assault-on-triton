DISPLAY = {
    "screen_width": 1920,
    "screen_height": 1080,
    "game_surface_width": 608,
    "sidebar_width": 608,
    "sidebar_left_offset": 48,
    "game_surface_offset": 48 + 608,
    "sidebar_right_offset": 48 + 608 + 608,
    "target_fps": 60,
}

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
    "shot_pos": {
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
    "shot_cooldown": 0.8,
    "shot_offset": 4,
    "blast_radius": 32,
}

ENEMY_SHIP = {
    "speed": 175,
    "hp": 8,
    "shot_cooldown": 0.6,
    "shot_offset": 4,
    "blast_radius": 48,
}

SUB_BOSS = {
    "speed": 200,
    "hp": 256,
    "shot_cooldown": 0.4,
    "shot_offset": 4,
    "blast_radius": 256,
}

LEVEL_BOSS = {
    "speed": 200,
    "hp": 512,
    "shot_cooldown": 0.4,
    "shot_offset": 4,
    "blast_radius": 512,
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
        "range": 512,
        "speed": 300,
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

AUDIO = {
    "master_volume": 1.0,
    "sfx_volume": 0.5,
    "music_volume": 0.7,
}

SCORING = {
    "streak_threshold_base": 10,
    "streak_decay_base": 1,
    "streak_delay": 3,  # seconds before decay starts
    "init_multiplier": 1,
    "init_streak_meter": 0,
}

UI = {
    "hud_padding": 16,
    "hud_inner_padding": 16,
    "hud_top_section_height": 128,
    "hud_mid_section_height": 256,
    "hud_bottom_section_height": 48,
    "hud_meter_height": 16,
    "hud_meter_y_offset": 24,
    "hud_meter_border_width": 2,
    "hud_meter_inner_padding": 2,
    "hud_meter_inner_height": 12,
    "font_sizes": {
        "large": 24,
        "medium": 20,
        "small": 16,
    },
    "colors": {
        "primary": "#E6D819",
        "secondary": "gray80",
        "background": "grey10",
        "meter_border": "grey70",
        "meter_fill": "grey50",
    },
    "power_levels": {
        1: "( I )",
        2: "( II )",
        3: "( III )",
        4: "( IV )",
        5: "( OV )",
    },
}

SPAWN_LOCATIONS = {
    "top_left_edge": (0.1, "top"),  # 1
    "top_far_left": (0.2, "top"),  # 2
    "top_left": (0.3, "top"),  # 3
    "top_center_left": (0.4, "top"),  # 4
    "top_center": (0.5, "top"),  # 5
    "top_center_right": (0.6, "top"),  # 6
    "top_right": (0.7, "top"),  # 7
    "top_far_right": (0.8, "top"),  # 8
    "top_right_edge": (0.9, "top"),  # 9
    "player_spawn": (0.5, "btm"),
}
