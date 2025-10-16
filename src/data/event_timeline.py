"""
EVENT OUTLINE, SUMMARY

1) Intro Sequence -> Cutscene -> Mission Start Message =>
2) Enemy Wave Sequence 1 -> Asteroids -> Power Level Pickup -> Drones -> Ships -> Bomb ammo pickup -> Drones, Ships -> Power Level Up + Bomb ammo pickups =>
3) Mid-boss sequence -> Cutscene -> mid-boss fight -> Cutscene -> Checkpoint Reached -> Power Level Up, bomb ammo pickup =>
4) Enemy Wave Sequence 2 -> Destroyers, Drones -> Destroyers, Ships -> Gunships -> Overdrive pickup -> Destroyers, Drones, ships, gunships, asteroids =>
5) Level boss Sequence -> Cutscene -> Level boss fight -> Cutscene =>
6) Outro Sequence -> Cutscene -> Mission Complete message -> Score and Time Message -> To Be Continued Message =>
Back to main menu
"""

"""
EVENT OUTLINE, DETAILS

1) Intro Sequence

    # Cutscene Level Intro:Start
        - Player ship sprite is flying through the atmosphere
        - Background consists of clouds moving by fast
        - Hero and Commander dialogue:
        - Player ship breaks through clouds and the edge of the planet can be seen and is slowly scrolling downward
        - Can also see a debris ring around the planet
    # Cutscene Level Intro:End

    - Mission Start Message displays (3 seconds)

2) Enemy Wave Sequence 1

    - Asteroids Wave
    - Power Level Up pickup *** Pwr Lvl 2 ***
    - Drones Wave
    - Bomb ammo pickup
    - Ships Wave
    - Bomb ammo pickup
    - Drone + Ships wave
    - Power Level Up + Bomb Ammo pickups *** Pwr Lvl 3 ***

3) Mid-Boss Sequence

    # Cutscene Mid-Boss Intro:Start
        - Hero and Commander dialogue
        - Hero and Enemy Captain dialogue
        - Enemy Battlecruiser enters screen
    # Cutscene Mid-Boss Intro:End

    - Player has to destroy turrets and other weakpoints before destroying the main cannon/core
    - Player also has to deal with enemy drones and ships attacking as well

    # Cutscene Mid-Boss Defeat:Start
        - Hero and Enemy Captain dialogue
        - Battle cruiser blows up
    # Cutscene Mid-Boss Defeat:End

    - Power Level Up and bomb ammo pickups *** Pwr Lvl 4 ***

### CHECKPOINT ###

4) Enemy Wave Sequence 2

    - Destroyers + Drones wave
    - Destroyers + Ships wave
    - Bomb ammo pickup
    - Gunships wave
    - Overdrive pickup
    - Destroyers + Gunships + Ships + Drones + Asteroids wave

5) Level Boss Sequence

    # Cutscene Boss Intro:Start
        - Hero and Commander dialogue
        - Space base/battle station disguised as planetoid enters screen
        - 
    # Cutscene Boss Intro:End

    - Player has to destroy the outer shell of the station which is covered in asteroids as well as destroy the turrets
    - Player will be attacked by drones, ships, and gunships also
    - When the outer layers are destroyed the boss' health bar appears and the main cannon will be used along with more turrets

    # Cutscene Boss Defeat:Start
        - Battle station explodes
    # Cutscene Boss Defeat:End

6) Outro Sequence

    # Cutscene Start
        - Hero and Commander Dialogue
    # Cutscene End

    - Mission Complete message
    - Score and Time display
    - To be continued message
    - Press ENTER to go to main menu

- Back to Main Menu

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
