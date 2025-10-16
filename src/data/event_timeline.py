"""

INTRO CUTSCENE

Player sprite flying through atmosphere
Hero and Commander have dialogue about incoming asteroids/meteors
Player ship sprite enters space (can see the edge of the planet) -> End cutscene

"""
# Mission Start text shows up for 3 seconds then disappears
# Various individual asteroids of different sizes come from different spawn points
# Player gets a power level up pickup
# Enemy drones attack for multiple waves
# Player gets a bomb ammo pickup
# Enemy ships attack for multiple waves
# Player gets another power level up pickup
# Multiple mixed waves of enemy ships and drones attack
# Player gets another bomb ammo pickup

"""

MID-BOSS SEQUENCE

Starts with a cutscene with dialogue between the hero and commander about an incoming vessel
The battle cruiser enters the screen and the enemy commander has dialogue with the hero -> End cutscene

Player has to destroy all turrets on battle cruiser and then the main cannon to destroy it for good
There will also be enemy drones and ships attacking as well

"""


# Once destroyed the player will get another power level pickup and bomb ammo pickups
# Various waves of enemy ships and drones along with destroyer class and gunships attack
# Just before the boss encounter an overdrive pickup will be dropped and the player will face off against many more enemies and asteroids back to back until the boss appears

"""

BOSS SEQUENCE

Starts with a cutscene of the hero and commander having dialogue about a massive object incoming and then it appears on screen -> end cutscene

A massive space base/battleship disguised as a planetoid, uses asteroids to protect itself and various turrets to attack
Need to destroy all turrets and destroy the rock layer covering the battleship in order to expose weakpoints
Enemy drones and ships will attack as well during the fight
Boss health bar doesn't appear until core exposed

"""

"""

OUTRO CUTSCENE

The hero and commander will have dialogue about the mission success and that they have detected more enemies incoming
Mission Complete shows on screen
Score and Time shows on screen 
To be continued shows on screen
Back to main menu

"""

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
