TIMELINE = [
    {"time": 0, "event": "show_message", "params": {"text": "Mission Start!"}},
    # ASTEROID FIELD
    {
        "time": 0.3,
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
        "time": 0.7,
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
        "time": 0.9,
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
        "time": 1.2,
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
        "time": 1.5,
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
        "time": 1.8,
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
        "time": 2.1,
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
        "time": 2.4,
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
        "time": 2.6,
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
        "time": 2.9,
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
    # PICKUP
    {
        "time": 3.0,
        "event": "spawn_entities",
        "params": {
            "type": "HealthPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    # ENEMY SHIPS
    {
        "time": 4.0,
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
    # PICKUP
    {
        "time": 5.0,
        "event": "spawn_entities",
        "params": {
            "type": "ExtraLifePickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 6.0,
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
    # PICKUP
    {
        "time": 7.0,
        "event": "spawn_entities",
        "params": {
            "type": "PowerLevelPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    # PICKUP
    {
        "time": 9.0,
        "event": "spawn_entities",
        "params": {
            "type": "PowerLevelPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    # PICKUP
    {
        "time": 11.0,
        "event": "spawn_entities",
        "params": {
            "type": "PowerLevelPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    # PICKUP
    {
        "time": 13.0,
        "event": "spawn_entities",
        "params": {
            "type": "PowerLevelPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 14.0,
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
    # PICKUP
    {
        "time": 6.0,
        "event": "spawn_entities",
        "params": {
            "type": "OverdrivePickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 18.0,
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
    # PICKUP
    {
        "time": 20.0,
        "event": "spawn_entities",
        "params": {
            "type": "InvulnerabilityPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 22.0,
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
    # PICKUP
    {
        "time": 24.0,
        "event": "spawn_entities",
        "params": {
            "type": "BombAmmoPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 26.0,
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
    # PICKUP
    {
        "time": 28.0,
        "event": "spawn_entities",
        "params": {
            "type": "BombAmmoPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 30.0,
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
    # PICKUP
    {
        "time": 31.0,
        "event": "spawn_entities",
        "params": {
            "type": "BombAmmoPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 32.0,
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
        "time": 34.0,
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
    # PICKUP
    {
        "time": 36.0,
        "event": "spawn_entities",
        "params": {
            "type": "BombAmmoPickup",
            "count": 1,
            "location": "center",
            "formation": "single",
            "behaviors": [
                {"action": "move_straight", "params": {}},
            ],
        },
    },
    {
        "time": 38.0,
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
        "time": 42.0,
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
