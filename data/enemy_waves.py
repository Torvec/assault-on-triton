WAVE = {
    "wave_sequence_1": [
        {
            "time": 1,
            "type": "asteroid_sm",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 2,
            "type": "asteroid_md",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 3,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 4,
            "type": "asteroid_md",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        # * Continues...
        # * ...
        # * ...
        # * ...
        # * ...
    ],
    "wave_sequence_2": [
        {
            "time": 1,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 2,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 3,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        # * Continues...
        # * ...
        # * ...
        # * ...
        # * ...
    ],
}
