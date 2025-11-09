CUTSCENE = {
    "intro": [
        {
            "time": 0,
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 540},
                "speed": 200,
            },
        },
        {
            "time": 1.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_1"},
        },
        {
            "time": 4,
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_2"},
        },
        {
            "time": 6.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_3"},
        },
        {
            "time": 9.0,
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_4"},
        },
    ],
    "sub_boss_intro": {},
    "sub_boss_defeat": {},
    "level_boss_intro": {},
    "level_boss_defeat": {},
    "outro_1": {},
    "outro_2": {},
}
