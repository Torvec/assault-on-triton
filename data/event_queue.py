EVENT_QUEUE = [
    {
        "type": "spawn_entity",
        "params": {
            "type": "player",
            "location": "player_spawn",
        },
    },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "intro"},
    },
    {
        "type": "show_message",
        "params": {"message_id": "mission_start"},
    },
    {
        "type": "trigger_wave",
        "params": {"wave_id": "wave_sequence_1"},
    },
    {
        "type": "show_message",
        "params": {"message_id": "mid_boss_incoming"},
    },
    # {
    #     "type": "spawn_entity",
    #     "params": {
    #         "type": "mid_boss",
    #         "location": "top_center",
    #     },
    # },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "mid_boss_intro"},
    },
    # {
    #     "type": "trigger_battle",
    #     "params": {"battle_id": "mid_boss"},
    # },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "mid_boss_defeat"},
    },
    {
        "type": "trigger_wave",
        "params": {
            "wave_id": "wave_sequence_2",
        },
    },
    {
        "type": "show_message",
        "params": {"message_id": "end_boss_incoming"},
    },
    # {
    #     "type": "spawn_entity",
    #     "params": {
    #         "type": "end_boss",
    #         "location": "top_center",
    #     },
    # },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "end_boss_intro"},
    },
    # {
    #     "type": "trigger_battle",
    #     "params": {"battle_id": "end_boss"},
    # },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "end_boss_defeat"},
    },
    {
        "type": "trigger_mission_complete",
        "params": {},
    },
    {
        "type": "trigger_cutscene",
        "params": {"cutscene_id": "outro"},
    },
    {
        "type": "show_message",
        "params": {"message_id": "to_be_continued"},
    },
]
