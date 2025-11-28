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
