EVENTS = [
    {"time": 0, "event": "trigger_cutscene", "params": {"cutscene_id": "intro"}},
    {
        "time": 1,
        "event": "show_message",
        "params": {"message_id": "mission_start"},
    },
    # BEGIN ENEMY WAVES SEQUENCE 1
    {
        "time": 4,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "left-edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    # *
    # *
    # * MULTIPLE WAVES HERE
    # *
    # *
    # END ENEMY WAVES SEQUENCE 1
    {
        "time": 100,
        "event": "show_message",
        "params": {"message_id": "sub_boss_incoming"},
    },
    {
        "time": 103,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "sub_boss_intro"},
    },
    # BEGIN BATTLE SEQUENCE 1: SUB BOSS
    {"time": 104, "event": "trigger_battle", "params": {}},
    # END BATTLE SEQUENCE 1: SUB BOSS
    {
        "time": 105,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "sub_boss_defeat"},
    },
    # BEGIN ENEMY WAVES SEQUENCE 2
    {
        "time": 103,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "left-edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    # *
    # *
    # * MULTIPLE WAVES HERE
    # *
    # *
    # END ENEMY WAVES SEQUENCE 2
    {
        "time": 200,
        "event": "show_message",
        "params": {"message_id": "level_boss_incoming"},
    },
    {
        "time": 201,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "level_boss_intro"},
    },
    # BEGIN BATTLE SEQUENCE 2: LEVEL BOSS
    {"time": 202, "event": "trigger_battle", "params": {}},
    # END BATTLE SEQUENCE 2: LEVEL BOSS
    {
        "time": 203,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "level_boss_defeat"},
    },
    {
        "time": 204,
        "event": "trigger_mission_complete",
        "params": {},
    },
    # {
    #     "time": 205,
    #     "event": "show_mission_complete_overlay",
    #     "params": {},
    # },
    # {
    #     "time": 206,
    #     "event": "trigger_cutscene",
    #     "params": {"cutscene_id": "outro_2"},
    # },
    # {
    #     "time": 207,
    #     "event": "show_message",
    #     "params": {"message_id": "to_be_continued"},
    # },
    # TRANSITION TO NEW SCENE (I.E. MAIN MENU, THANKS FOR PLAYING, CREDITS, ETC.)
]

TIMELINE = [
    {"time": 0, "event": "trigger_intro", "params": {}},
    {"time": 100, "event": "trigger_outro", "params": {}},
    {
        "time": 0,
        "event": "move_player_to",
        "params": {"x": 304, "y": 540, "speed": 200},
    },
    {
        "time": 1.5,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_1"},
    },
    {
        "time": 4,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_2"},
    },
    {
        "time": 6.5,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_3"},
    },
    {
        "time": 9.0,
        "event": "show_dialogue",
        "params": {"dialogue_id": "intro_1_4"},
    },
    {"time": 11.5, "event": "enable_player_controls", "params": {}},
    {"time": 11.5, "event": "show_message", "params": {"message_id": "mission_start"}},
    {
        "time": 14,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "left_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 16,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_md",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 18,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_sm",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 20,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_sm",
            "location": "center_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 22,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_md",
            "location": "right_edge",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 24,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "far_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 26,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_md",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 28,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_sm",
            "location": "far_left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 30,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 32,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "center_right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 34,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_xl",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 36,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_xl",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "rotate_constantly", "params": {}},
            ],
        },
    },
    {
        "time": 38,
        "event": "spawn_entity",
        "params": {
            "type": "power_level_pickup",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
            ],
        },
    },
    {
        "time": 40,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 42,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 44,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 46,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 48,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 50,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 52,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 54,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 56,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 58,
        "event": "spawn_entity",
        "params": {
            "type": "power_level_pickup",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
            ],
        },
    },
    {
        "time": 60,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "left",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 62,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_drone",
            "location": "right",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 64,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
    {
        "time": 66,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "center",
            "behaviors": [
                {"action": "move_straight", "params": {"direction": "down"}},
                {"action": "shoot", "params": {}},
            ],
        },
    },
]
