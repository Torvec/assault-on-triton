TIMELINE = [
    {"time": 0, "event": "show_message", "params": {"text": "Mission Start!"}},
    {
        "time": 1.3,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidLarge",
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
        "time": 2.7,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidMedium",
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
        "time": 3.9,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidSmall",
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
        "time": 4.2,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidSmall",
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
        "time": 5.5,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidMedium",
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
        "time": 6.8,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidLarge",
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
        "time": 7.1,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidMedium",
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
        "time": 8.4,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidSmall",
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
        "time": 9.6,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidLarge",
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
        "time": 10.9,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidLarge",
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
        "time": 11.5,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidXL",
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
        "time": 11.6,
        "event": "spawn_entities",
        "params": {
            "type": "AsteroidXL",
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
        "time": 12.0,
        "event": "spawn_entities",
        "params": {
            "type": "PowerLevelPickup",
            "count": 1,
            "location": "right",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 16.5,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyDrone",
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
        "time": 23.6,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyDrone",
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
        "time": 28.1,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 33.3,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 38.6,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 44.3,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 50.4,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 55.4,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 59.8,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 61.0,
        "event": "spawn_entities",
        "params": {
            "type": "PowerLevelPickup",
            "count": 1,
            "location": "left",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 65.7,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyDrone",
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
        "time": 69.4,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyDrone",
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
        "time": 74.8,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
        "time": 79.5,
        "event": "spawn_entities",
        "params": {
            "type": "EnemyShip",
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
#         "type": "ExtraLifePickup",
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
#         "type": "HealthPickup",
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
#         "type": "BombAmmoPickup",
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
#         "type": "PowerLevelPickup",
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
#         "type": "InvulnerabilityPickup",
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
#         "type": "OverdrivePickup",
#         "count": 1,
#         "location": "center",
#         "formation": "single",
#         "behaviors": [
#             {"action": "move_straight", "params": {}},
#         ],
#     },
# },
