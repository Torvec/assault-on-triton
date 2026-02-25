# Display
BASE_GS_WIDTH = 216
BASE_GS_HEIGHT = 360
TARGET_FPS = 60

# Audio
MASTER_VOL = 1.0
SFX_VOL = 0.5
MUSIC_VOL = 0.7

# Scoring
STREAK_THESHOLD_BASE = 10
STREAK_DECAY_BASE = 1
STREAK_DELAY_BASE = 3
STREAK_MULTIPLIER_INIT = 1
STREAK_METER_INIT = 0

UI = {
    "colors": {
        "primary": "#E6D819",
        "secondary": "gray80",
        "background": "grey10",
        "meter_border": "grey70",
        "meter_fill": "grey50",
    },
    "power_levels": {
        1: "1",
        2: "2",
        3: "3",
        4: "4",
        5: "OV",
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
