WAVE = {
    "wave_sequence_1": [
        #! Asteroids Wave
        {
            "time": 0,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 0.5,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 0.75,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 1,
            "type": "asteroid_sm",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 1.25,
            "type": "asteroid_sm",
            "location": "top_far_right",
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
            "time": 4,
            "type": "asteroid_sm",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 6,
            "type": "asteroid_lg",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 8,
            "type": "asteroid_lg",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 10,
            "type": "asteroid_lg",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 14,
            "type": "asteroid_xl",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 16,
            "type": "asteroid_xl",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Enemy Drones Wave
        {
            "time": 22,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 24,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 26,
            "type": "enemy_drone",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 28,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 30,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 31,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 31,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 35,
            "type": "power_level_pickup",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 37,
            "type": "bomb_ammo_pickup",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Enemy Ships Wave
        {
            "time": 43,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 44,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 45,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 46,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 47,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 48,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 49,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 51,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 52,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 53,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 54,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 55,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 56,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 57,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        #! Drones + Ships Wave
        {
            "time": 62,
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
