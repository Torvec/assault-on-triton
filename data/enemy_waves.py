WAVE = {
    "test_wave": [
        # {
        #     "time": 0,
        #     "type": "enemy_drone",
        #     "location": "top_center_left",
        #     "behaviors": [
        #         {
        #             "action": "move_saw_wave",
        #             "params": {
        #                 "x_speed": 200,
        #                 "y_speed": 150,
        #                 "init_direction": "right",
        #             },
        #         },
        #         {
        #             "action": "shoot",
        #             "params": {
        #                 "shoot_rate": 0.1,
        #                 "ammo_count": 18,
        #                 "reload_time": 1.5,
        #                 "projectile_type": "enemy_shot",
        #             },
        #         },
        #     ],
        # },
        # {
        #     "time": 2,
        #     "type": "enemy_drone",
        #     "location": "top_center_right",
        #     "behaviors": [
        #         {
        #             "action": "move_saw_wave",
        #             "params": {
        #                 "x_speed": 200,
        #                 "y_speed": 150,
        #                 "init_direction": "left",
        #             },
        #         },
        #         {
        #             "action": "shoot",
        #             "params": {
        #                 "shoot_rate": 0.1,
        #                 "ammo_count": 18,
        #                 "reload_time": 1.5,
        #                 "projectile_type": "enemy_shot",
        #             },
        #         },
        #     ],
        # },
        # {
        #     "time": 6,
        #     "type": "enemy_ship",
        #     "location": "top_center",
        #     "behaviors": [
        #         {
        #             "action": "move_sine_wave",
        #             "params": {
        #                 "frequency": 4,
        #                 "amplitude": 600,
        #                 "speed": 200,
        #             },
        #         },
        #         {
        #             "action": "shoot",
        #             "params": {
        #                 "shoot_rate": 0.2,
        #                 "ammo_count": 18,
        #                 "reload_time": 1.5,
        #                 "projectile_type": "enemy_shot",
        #             },
        #         },
        #     ],
        # },
        # {
        #     "time": 8,
        #     "type": "enemy_ship",
        #     "location": "top_center",
        #     "behaviors": [
        #         {
        #             "action": "move_sine_wave",
        #             "params": {
        #                 "frequency": -4,
        #                 "amplitude": 600,
        #                 "speed": 200,
        #             },
        #         },
        #         {
        #             "action": "shoot",
        #             "params": {
        #                 "shoot_rate": 0.2,
        #                 "ammo_count": 18,
        #                 "reload_time": 1.5,
        #                 "projectile_type": "enemy_shot",
        #             },
        #         },
        #     ],
        # },
        # {
        #     "time": 10,
        #     "type": "enemy_drone",
        #     "location": "top_right_edge",
        #     "behaviors": [
        #         {
        #             "action": "move_square_wave",
        #             "params": {
        #                 "x_dist": 400,
        #                 "y_dist": 200,
        #                 "init_horizontal_dir": "left",
        #                 "x_speed": 200,
        #                 "y_speed": 300,
        #                 "shoot_rate": 0.1,
        #                 "ammo_count": 28,
        #                 "reload_time": 1.5,
        #                 "projectile_type": "enemy_shot",
        #             },
        #         },
        #     ],
        # },
        # {
        #     "time": 12,
        #     "type": "enemy_drone",
        #     "location": "top_left_edge",
        #     "behaviors": [
        #         {
        #             "action": "move_square_wave",
        #             "params": {
        #                 "x_dist": 400,
        #                 "y_dist": 200,
        #                 "init_horizontal_dir": "right",
        #                 "x_speed": 200,
        #                 "y_speed": 300,
        #                 "shoot_rate": 0.1,
        #                 "ammo_count": 28,
        #                 "reload_time": 1.5,
        #                 "projectile_type": "enemy_shot",
        #             },
        #         },
        #     ],
        # },
        {
            "time": 1,
            "type": "enemy_destroyer",
            "location": "top_center",
            "behaviors": [
                {
                    "action": "move_straight",
                    "params": {"speed": 80},
                },
            ],
        },
    ],
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
            "time": 1.5,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 2,
            "type": "asteroid_md",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 2,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 3,
            "type": "asteroid_sm",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 3.5,
            "type": "asteroid_sm",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 3.5,
            "type": "asteroid_sm",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 4,
            "type": "asteroid_sm",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 4.5,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 4.5,
            "type": "asteroid_md",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 5,
            "type": "asteroid_sm",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 5.5,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 6,
            "type": "asteroid_md",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 6.5,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 7.5,
            "type": "asteroid_sm",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 7.5,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 8,
            "type": "asteroid_md",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 8.5,
            "type": "asteroid_md",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 9,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        ### END SECTION 1 ###
        {
            "time": 11,
            "type": "asteroid_lg",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 11.5,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 11.5,
            "type": "asteroid_lg",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 12.5,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 13,
            "type": "asteroid_lg",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 13,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 14,
            "type": "asteroid_md",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 14.5,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 15,
            "type": "asteroid_lg",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 15,
            "type": "asteroid_sm",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 16,
            "type": "asteroid_lg",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 16,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 16.5,
            "type": "asteroid_md",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 17,
            "type": "asteroid_lg",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 18,
            "type": "asteroid_md",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 18,
            "type": "asteroid_sm",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 18.5,
            "type": "asteroid_lg",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 19,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 19.5,
            "type": "asteroid_md",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        ### END SECTION 2 ###
        {
            "time": 21,
            "type": "asteroid_xl",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 22.5,
            "type": "asteroid_xl",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 23,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 23.5,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 24,
            "type": "asteroid_sm",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 25,
            "type": "asteroid_md",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 25.5,
            "type": "asteroid_xl",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 26.5,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 27,
            "type": "asteroid_md",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 27.5,
            "type": "asteroid_sm",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 28.5,
            "type": "asteroid_xl",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 28.5,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 29,
            "type": "asteroid_sm",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        ### END SECTION 3 ###
        {
            "time": 31,
            "type": "asteroid_sm",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 32,
            "type": "asteroid_lg",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 32.5,
            "type": "asteroid_sm",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 33,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 33,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 34,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 35,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 35.5,
            "type": "asteroid_sm",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 36,
            "type": "asteroid_md",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 36,
            "type": "asteroid_md",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 37,
            "type": "asteroid_md",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 37.5,
            "type": "asteroid_sm",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 38,
            "type": "asteroid_sm",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 38.5,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 38.5,
            "type": "asteroid_sm",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 39,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        ### END SECTION 4 ####
        {
            "time": 41,
            "type": "bomb_ammo_pickup",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Enemy Drones Wave
        {
            "time": 46,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 46.5,
            "type": "asteroid_md",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 47,
            "type": "asteroid_sm",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 48,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 48.5,
            "type": "asteroid_sm",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 50,
            "type": "asteroid_sm",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 50,
            "type": "enemy_drone",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 50.5,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 52,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 52,
            "type": "asteroid_md",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 53,
            "type": "asteroid_sm",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 54,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 56,
            "type": "asteroid_sm",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 56.5,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 57,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 57,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 59,
            "type": "asteroid_sm",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 59,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 60,
            "type": "enemy_drone",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 60,
            "type": "enemy_drone",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 62,
            "type": "asteroid_sm",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 62.5,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 63,
            "type": "asteroid_sm",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 63.5,
            "type": "enemy_drone",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 63.5,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 65,
            "type": "bomb_ammo_pickup",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 66,
            "type": "health_pickup",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 68,
            "type": "power_level_pickup",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Enemy Ships Wave
        {
            "time": 72,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 73,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 74,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 75,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 76,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 77,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 78,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 79,
            "type": "enemy_ship",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 82,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 83,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 84,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 85,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 86,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 87,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 88,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 89,
            "type": "enemy_ship",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 92,
            "type": "bomb_ammo_pickup",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        {
            "time": 94,
            "type": "health_pickup",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
        #! Drones + Ships Wave
        {
            "time": 96,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 98,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 98,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 98.5,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 98.5,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 100,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 100.5,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 100.5,
            "type": "enemy_drone",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 102.5,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 103.5,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 105,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 105,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 107,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 107,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 109,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 109,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 109.5,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 109.5,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 110,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 113,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 114,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 114,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 116,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 116,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 116,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 119,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 119,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 120,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 120,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 120,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 120.5,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 120.5,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 121,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 123,
            "type": "enemy_ship",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 123,
            "type": "enemy_ship",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 124,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 124,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 124.5,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 124.5,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 125,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 125,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 125.5,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 127,
            "type": "enemy_drone",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 128,
            "type": "enemy_drone",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 128,
            "type": "enemy_drone",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 128.5,
            "type": "enemy_drone",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 128.5,
            "type": "enemy_drone",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 129,
            "type": "enemy_drone",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 129,
            "type": "enemy_drone",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 129.5,
            "type": "enemy_drone",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 129.5,
            "type": "enemy_drone",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 131,
            "type": "enemy_ship",
            "location": "top_left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
        {
            "time": 134,
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
