WAVE = {
    "wave_sequence_1": [
        {
            "time": 0,
            "event": "spawn_entity",
            "params": {
                "type": "asteroid_lg",
                "location": "top_left_edge",
                "behaviors": [
                    {"action": "move_straight", "params": {"direction": "down"}},
                    {"action": "rotate_constantly", "params": {}},
                ],
            },
        },
        # * Continues...
        # * ...
        # * ...
        # * ...
        # * ...
    ],
    "wave_sequence_2": [
        {
            "time": 0,
            "event": "spawn_entity",
            "params": {
                "type": "enemy_ship",
                "location": "top_center",
                "behaviors": [
                    {"action": "move_straight", "params": {"direction": "down"}},
                    {"action": "shoot", "params": {}},
                ],
            },
        },
        # * Continues...
        # * ...
        # * ...
        # * ...
        # * ...
    ],
}
