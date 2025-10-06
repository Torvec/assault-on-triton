"""
Game configuration constants and settings.
Centralizes all game parameters for easy tweaking and balancing.
"""

# Display Settings
DISPLAY = {
    "game_surface_width": 608,
    "sidebar_width": 608,
    "sidebar_left_offset": 48,
    "sidebar_right_offset": 1264,
    "target_fps": 60,
}

# Player Configuration
PLAYER = {
    "radius": 48,
    "base_acceleration": 600,
    "base_speed": 350,
    "base_lives": 1,
    "max_lives": 3,
    "base_hp": 100,
    "invincible_duration": 2,
    "invulnerable_duration": 30,
    "overdrive_duration": 30,
    "shot_offset": 8,
    "overdrive_shot_offset": 20,
    "base_bomb_ammo": 3,
    "max_bomb_ammo": 6,
    "bomb_cooldown": 2.0,
    "base_power_level": 1,
    "max_power_level": 3,
    "death_blast_radius": 128,
    "velocity_decay": 0.99,
    "fire_rates": {
        1: 0.2,
        2: 0.1625,
        3: 0.125,
        4: 0.1,  # overdrive
    },
}

# Enemy Configuration
ENEMIES = {
    "drone": {
        "radius": 16,
        "speed": 300,
        "hp": 3,
        "shot_cooldown": 0.6,
        "shot_offset": 4,
        "blast_radius": 32,
    },
    "ship": {
        "radius": 32,
        "speed": 200,
        "hp": 6,
        "shot_cooldown": 0.4,
        "shot_offset": 4,
        "blast_radius": 48,
    },
}

# Projectile Configuration
PROJECTILES = {
    "player_shots": {
        1: {"range": 512, "speed": 500, "damage": 1},
        2: {"range": 768, "speed": 600, "damage": 2},
        3: {"range": 1024, "speed": 700, "damage": 4},
        4: {"range": 1024, "speed": 1000, "damage": 8},
    },
    "enemy_shot": {
        "range": 512,
        "speed": 500,
        "damage": 2,
    },
    "bomb": {
        "radius": 8,
        "speed": 200,
        "blast_radius": 384,
        "trigger_distance": 256,
    },
    "missile": {
        "radius": 10,
        "speed": 200,
        "hp": 1,
        "blast_radius": 64,
    },
}

# Asteroid Configuration
ASTEROIDS = {
    "small": {
        "radius": 16,
        "speed": 120,
        "hp": 2,
        "splits_into": None,
    },
    "medium": {
        "radius": 32,
        "speed": 100,
        "hp": 4,
        "splits_into": "small",
    },
    "large": {
        "radius": 64,
        "speed": 80,
        "hp": 6,
        "splits_into": "medium",
    },
    "rotation_speed_range": (-90, 90),
    "split_angle": 30,
    "split_velocity_factor": 1.2,
}

# Pickup Configuration
PICKUPS = {
    "health": {
        "radius": 16,
        "speed": 150,
        "heal_amount": 25,
    },
    "power": {
        "radius": 16,
        "speed": 150,
        "fallback_score": 100,
    },
    "bomb": {
        "radius": 16,
        "speed": 150,
        "fallback_score": 100,
    },
    "life": {
        "radius": 16,
        "speed": 150,
        "fallback_score": 100,
    },
}

# Explosion Configuration
EXPLOSIONS = {
    "initial_radius": 2,
    "expansion_rate": 256,
    "damage": 5,
}

# Audio Configuration
AUDIO = {
    "master_volume": 1.0,
    "sfx_volume": 0.5,
    "music_volume": 0.7,
}

# Game Balance
SCORING = {
    "streak_threshold_base": 10,
    "streak_decay_base": 1,
    "streak_delay": 3,  # seconds before decay starts
    "initial_multiplier": 1,
    "initial_streak_meter": 0,
}

# UI Configuration
UI = {
    "hud_padding": 16,
    "hud_inner_padding": 16,
    "hud_top_section_height": 128,
    "hud_mid_section_height": 192,
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
}
