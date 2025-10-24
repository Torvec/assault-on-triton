TIMELINE = [
    {
        "time": 3,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_1"},
    },
    {
        "time": 6,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_2"},
    },
    {
        "time": 9,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_3"},
    },
    {
        "time": 12,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_4"},
    },
    {
        "time": 15,
        "event": "show_dialogue",
        "params": {"dialogue_id": "enemy_test"},
    },
    {"time": 15, "event": "show_message", "params": {"message_id": "mission_start"}},
    {
        "time": 16.3,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_lg",
            "count": 1,
            "location": "left_edge",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 16.7,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_md",
            "count": 1,
            "location": "right",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 16.9,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_sm",
            "count": 1,
            "location": "left",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 17.2,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_sm",
            "count": 1,
            "location": "center_left",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 18.5,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_md",
            "count": 1,
            "location": "right_edge",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 19.8,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_lg",
            "count": 1,
            "location": "far_right",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 20.1,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_md",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 21.4,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_sm",
            "count": 1,
            "location": "far_left",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 22.6,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_lg",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 23.9,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_lg",
            "count": 1,
            "location": "center_right",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 24.5,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_xl",
            "count": 1,
            "location": "right",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 24.6,
        "event": "spawn_entities",
        "params": {
            "type": "asteroid_xl",
            "count": 1,
            "location": "left",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 25.0,
        "event": "spawn_entities",
        "params": {
            "type": "power_level_pickup",
            "count": 1,
            "location": "right",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 27.5,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_drone",
            "count": 5,
            "location": "center",
            "formation": "column",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 33.6,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_drone",
            "count": 5,
            "location": "center",
            "formation": "wall",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 38.1,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 5,
            "location": "center",
            "formation": "column",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 43.3,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 5,
            "location": "center",
            "formation": "wall",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 48.6,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 6,
            "location": "center",
            "formation": "forward_v",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 54.3,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 6,
            "location": "center",
            "formation": "reverse_v",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 60.4,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 6,
            "location": "left",
            "formation": "echelon_l",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 65.4,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 6,
            "location": "right",
            "formation": "echelon_r",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 69.8,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 4,
            "location": "center",
            "formation": "diamond",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 71.0,
        "event": "spawn_entities",
        "params": {
            "type": "power_level_pickup",
            "count": 1,
            "location": "left",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 75.7,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_drone",
            "count": 4,
            "location": "left",
            "formation": "diamond",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 79.4,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_drone",
            "count": 4,
            "location": "right",
            "formation": "diamond",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 84.8,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 8,
            "location": "center",
            "formation": "circle",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 89.5,
        "event": "spawn_entities",
        "params": {
            "type": "enemy_ship",
            "count": 5,
            "location": "center",
            "formation": "x",
            "behaviors": [
                {"action": "move_straight", "params": {}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
]


# {
#     "time": 14.0,
#     "event": "spawn_entities",
#     "params": {
#         "type": "extra_life_pickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
# {
#     "time": 11.0,
#     "event": "spawn_entities",
#     "params": {
#         "type": "health_pickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
#     {
#     "time": 49.0,
#     "event": "spawn_entities",
#     "params": {
#         "type": "bomb_ammo_pickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
# {
#     "time": 19.0,
#     "event": "spawn_entities",
#     "params": {
#         "type": "power_level_pickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
# {
#     "time": 30.0,
#     "event": "spawn_entities",
#     "params": {
#         "type": "invulnerability_pickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
# {
#     "time": 25.0,
#     "event": "spawn_entities",
#     "params": {
#         "type": "overdrive_pickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
