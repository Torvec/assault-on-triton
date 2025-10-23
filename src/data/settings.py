DISPLAY = {
    "game_surface_width": 608,
    "sidebar_width": 608,
    "sidebar_left_offset": 48,
    "game_surface_offset": 48 + 608,
    "sidebar_right_offset": 1264,
    "target_fps": 60,
}

PLAYER = {
    "radius": 48,
    "base_acceleration": 600,
    "base_speed": 350,
    "base_lives": 1,
    "max_lives": 3,
    "base_hp": 100,
    "invincible_duration": 2,
    "invulnerable_duration": 30,
    "overdrive_duration": 20,
    "primary_shot_offset": 8,
    "secondary_shot_offset": 20,
    "tertiary_shot_offset": 24,
    "base_bomb_ammo": 3,
    "max_bomb_ammo": 6,
    "bomb_cooldown": 2.0,
    "base_power_level": 1,
    "max_power_level": 4,
    "death_blast_radius": 128,
    "velocity_decay": 0.99,
    "fire_rates": {
        1: 0.2,
        2: 0.18,
        3: 0.16,
        4: 0.14,
        5: 0.12,  # overdrive
    },
}

ENEMIES = {
    "asteroid": {
        "sm": {"speed": 120, "hp": 2, "splits_into": None},
        "md": {"speed": 100, "hp": 4, "splits_into": "sm"},
        "lg": {"speed": 80, "hp": 6, "splits_into": "md"},
        "xl": {"speed": 60, "hp": 12, "splits_into": "lg"},
        "rotation_speed_range": (-90, 90),
        "split_angle": 30,
        "split_velocity_factor": 1.2,
    },
    "enemy_drone": {
        "radius": 16,
        "speed": 300,
        "hp": 4,
        "shot_cooldown": 0.6,
        "shot_offset": 4,
        "blast_radius": 32,
    },
    "enemy_ship": {
        "radius": 32,
        "speed": 200,
        "hp": 8,
        "shot_cooldown": 0.4,
        "shot_offset": 4,
        "blast_radius": 48,
    },
}

PROJECTILES = {
    "player_shot": {
        1: {"range": 512, "speed": 500, "damage": 1},
        2: {"range": 768, "speed": 600, "damage": 2},
        3: {"range": 1024, "speed": 700, "damage": 4},
        4: {"range": 1024, "speed": 800, "damage": 6},
        5: {"range": 1024, "speed": 1000, "damage": 8},
    },
    "enemy_shot": {"range": 512, "speed": 500, "damage": 2},
    "player_bomb": {
        "radius": 8,
        "speed": 200,
        "trigger_distance": 256,
        "blast_radius": {1: 192, 2: 256, 3: 384, 4: 512},
    },
    "enemy_bomb": {
        "radius": 8,
        "speed": 200,
        "trigger_distance": 256,
        "blast_radius": 384,
    },
    "enemy_missile": {
        "radius": 10,
        "speed": 200,
        "trigger_distance": 256,
        "blast_radius": 64,
    },
}


PICKUPS = {
    "health": {"radius": 16, "speed": 150, "heal_amount": 25},
    "power": {"radius": 16, "speed": 150, "fallback_score": 100},
    "bomb": {"radius": 16, "speed": 150, "fallback_score": 100},
    "life": {"radius": 16, "speed": 150, "fallback_score": 100},
}

EXPLOSIONS = {"initial_radius": 4, "expansion_rate": 256, "damage": 5}

AUDIO = {"master_volume": 1.0, "sfx_volume": 0.5, "music_volume": 0.7}

SCORING = {
    "streak_threshold_base": 10,
    "streak_decay_base": 1,
    "streak_delay": 3,  # seconds before decay starts
    "initial_multiplier": 1,
    "initial_streak_meter": 0,
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
    "power_levels": {1: "( I )", 2: "( II )", 3: "( III )", 4: "( IV )", 5: "( OV )"},
}
