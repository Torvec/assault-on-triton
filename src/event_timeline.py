TIMELINE = [
    {"time": 0, "event": "show_message", "params": {"text": "Mission Start!"}},
    {
        "time": 0.3,
        "event": "spawn_enemies",
        "params": {
            "type": "AsteroidLarge",
            "count": 1,
            "location": "left_edge",
            "formation": "single",
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
        },
    },
]
