WAVE = {
    "wave_sequence_1": [
        #! Asteroids Wave
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
        {
            "time": 8,
            "type": "asteroid_xl",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 9,
            "type": "asteroid_xl",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Enemy Drones Wave
        {
            "time": 16,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 17,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 18,
            "type": "enemy_drone",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 19,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 20,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 20.75,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 20.75,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 25,
            "type": "power_level_pickup",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 27,
            "type": "bomb_ammo_pickup",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Enemy Ships Wave
        {
            "time": 33,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 34,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 35,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 36,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 37,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        #! Drones + Ships Wave
        {
            "time": 42,
            "type": "bomb_ammo_pickup",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    ],
    "wave_sequence_2": [
        {
            "time": 0,
            "type": "bomb_ammo_pickup",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 1,
            "type": "power_level_pickup",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Gunships Wave
        #! Gunships + Drones Wave
        #! Gunships + Ships Wave
        {
            "time": 5,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 6,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 7,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        #! Destroyers
        {
            "time": 12,
            "type": "bomb_ammo_pickup",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 14,
            "type": "overdrive_pickup",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Destroyers + Gunships + Ships + Drones + Asteroids Wave
    ],
}
