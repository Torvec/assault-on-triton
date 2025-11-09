EVENTS = [
    {
        "time": 0,
        "event": "spawn_entity",
        "params": {"type": "player", "location": "player_spawn", "behaviors": []},
    },
    {"time": 0.1, "event": "trigger_cutscene", "params": {"cutscene_id": "intro"}},
    {"time": 1, "event": "trigger_waves", "params": {}},
    {
        "time": 1,
        "event": "show_message",
        "params": {"message_id": "mission_start"},
    },
    #! BEGIN ENEMY WAVES SEQUENCE 1
    {
        "time": 4,
        "event": "spawn_entity",
        "params": {
            "type": "asteroid_lg",
            "location": "top_left_edge",
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
    #! END ENEMY WAVES SEQUENCE 1
    {
        "time": 10,
        "event": "show_message",
        "params": {"message_id": "sub_boss_incoming"},
    },
    {
        "time": 13,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "sub_boss_intro"},
    },
    #! BEGIN BATTLE SEQUENCE 1: SUB BOSS
    {"time": 14, "event": "trigger_battle", "params": {"battle_id": "sub_boss"}},
    #! END BATTLE SEQUENCE 1: SUB BOSS
    {
        "time": 15,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "sub_boss_defeat"},
    },
    #! BEGIN ENEMY WAVES SEQUENCE 2
    {
        "time": 16,
        "event": "spawn_entity",
        "params": {
            "type": "enemy_ship",
            "location": "top_center",
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
    #! END ENEMY WAVES SEQUENCE 2
    {
        "time": 20,
        "event": "show_message",
        "params": {"message_id": "level_boss_incoming"},
    },
    {
        "time": 24,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "level_boss_intro"},
    },
    #! BEGIN BATTLE SEQUENCE 2: LEVEL BOSS
    {"time": 25, "event": "trigger_battle", "params": {"battle_id": "level_boss"}},
    #! END BATTLE SEQUENCE 2: LEVEL BOSS
    {
        "time": 26,
        "event": "trigger_cutscene",
        "params": {"cutscene_id": "level_boss_defeat"},
    },
    # {
    #     "time": 204,
    #     "event": "trigger_mission_complete",
    #     "params": {},
    # },
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

EVENT_QUEUE = [
    {
        "type": "spawn_entity",
        "params": {"type": "player", "location": "player_spawn", "behaviors": []},
    },
    {"type": "trigger_cutscene", "params": {"cutscene_id": "intro"}},
    {
        "type": "show_message",
        "params": {"message_id": "mission_start"},
    },
    {"type": "trigger_waves", "params": {"wave_id": "wave_sequence_1"}},
    {
        "type": "show_message",
        "params": {"message_id": "sub_boss_incoming"},
    },
    {"type": "trigger_cutscene", "params": {"cutscene_id": "sub_boss_intro"}},
    # ! Current implementation isn't going to work the way i want it to, should only need an ID and then the battlemanager can get the rest of of the info from enemy_battles.py, i don't want it in the event queue directly
    # {"type": "trigger_battle", "params": {"battle_id": "sub_boss"}},
    {"type": "trigger_cutscene", "params": {"cutscene_id": "sub_boss_defeat"}},
    {"type": "trigger_waves", "params": {"wave_id": "wave_sequence_2"}},
    {
        "type": "show_message",
        "params": {"message_id": "level_boss_incoming"},
    },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "level_boss_intro"},
    },
    # ! Current implementation isn't going to work the way i want it to, should only need an ID and then the battlemanager can get the rest of of the info from enemy_battles.py, i don't want it in the event queue directly
    # {"type": "trigger_battle", "params": {"battle_id": "level_boss"}},
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "level_boss_intro"},
    },
    {"type": "trigger_mission_complete", "params": {}},
]
