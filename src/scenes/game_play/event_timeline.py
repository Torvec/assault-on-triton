TIMELINE = [
    {"time": 0, "event": "show_message", "params": {"text": "Mission Start!"}},
    # ASTEROID FIELD
    {
        "time": 0.3,
        "event": "spawn_enemies",
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
        "time": 0.7,
        "event": "spawn_enemies",
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
        "time": 0.9,
        "event": "spawn_enemies",
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
        "time": 1.2,
        "event": "spawn_enemies",
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
        "time": 1.5,
        "event": "spawn_enemies",
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
        "time": 1.8,
        "event": "spawn_enemies",
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
        "time": 2.1,
        "event": "spawn_enemies",
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
        "time": 2.4,
        "event": "spawn_enemies",
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
        "time": 2.6,
        "event": "spawn_enemies",
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
        "time": 2.9,
        "event": "spawn_enemies",
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
    # Asteroid Field 2
    # {
    #     "time": 5.9,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidLarge",
    #         "count": 1,
    #         "location": "left_edge",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 6.6,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidMedium",
    #         "count": 1,
    #         "location": "right",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 6.8,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidSmall",
    #         "count": 1,
    #         "location": "left",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 7.3,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidSmall",
    #         "count": 1,
    #         "location": "center_left",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 7.5,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidMedium",
    #         "count": 1,
    #         "location": "right_edge",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 7.8,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidLarge",
    #         "count": 1,
    #         "location": "far_right",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 8.1,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidMedium",
    #         "count": 1,
    #         "location": "center",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 8.4,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidSmall",
    #         "count": 1,
    #         "location": "far_left",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 8.6,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidLarge",
    #         "count": 1,
    #         "location": "center",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # {
    #     "time": 8.9,
    #     "event": "spawn_enemies",
    #     "params": {
    #         "type": "AsteroidLarge",
    #         "count": 1,
    #         "location": "center_right",
    #         "formation": "single",
    #         "behaviors": [
    #             {"action": "move_straight", "params": {}},
    #             {"action": "rotate_constantly", "params": {}},
    #         ],
    #     },
    # },
    # # ENEMY SHIPS
    {
        "time": 4.0,
        "event": "spawn_enemies",
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
        "time": 6.0,
        "event": "spawn_enemies",
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
        "time": 14.0,
        "event": "spawn_enemies",
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
        "time": 18.0,
        "event": "spawn_enemies",
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
        "time": 22.0,
        "event": "spawn_enemies",
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
        "time": 26.0,
        "event": "spawn_enemies",
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
        "time": 30.0,
        "event": "spawn_enemies",
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
        "time": 32.0,
        "event": "spawn_enemies",
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
        "time": 34.0,
        "event": "spawn_enemies",
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
        "time": 38.0,
        "event": "spawn_enemies",
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
        "time": 42.0,
        "event": "spawn_enemies",
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
