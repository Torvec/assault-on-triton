TIMELINE = [
    {
        "time": 0,
        "event": "move_player_to",
        "params": {"x": 304, "y": 540, "speed": 200},
    },
    {
        "time": 1.5,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_1"},
    },
    {
        "time": 4.5,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_2"},
    },
    {
        "time": 7.5,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_3"},
    },
    {
        "time": 10.5,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_4"},
    },
    {"time": 13.5, "event": "enable_player_controls", "params": {}},
    {"time": 13.5, "event": "show_message", "params": {"message_id": "mission_start"}},
    {
        "time": 16.3,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 16.7,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_md",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 16.9,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_sm",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 17.2,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_sm",
            "location": "center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 18.5,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_md",
            "location": "right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 19.8,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 20.1,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_md",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 21.4,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_sm",
            "location": "far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 22.6,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 23.9,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 24.5,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_xl",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 24.6,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_xl",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 25.0,
        "event": "spawn_entity",
        "params": {
            "type": "power_level_pickup",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
            ],
        },
    },
    {
        "time": 27.5,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 33.6,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 38.1,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 43.3,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 48.6,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 54.3,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 60.4,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 65.4,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 69.8,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 71.0,
        "event": "spawn_entity",
        "params": {
            "type": "power_level_pickup",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
            ],
        },
    },
    {
        "time": 75.7,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 79.4,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 84.8,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 89.5,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
]
