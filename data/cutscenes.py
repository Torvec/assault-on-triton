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
    "sub_boss_intro": [
        {
            "time": 0,
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 540},
                "speed": 150,
            },
        },
        {
            "time": 1.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_1"},
        },
        {
            "time": 4,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_2"},
        },
        {
            "time": 6.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_3"},
        },
        {
            "time": 9.0,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_4"},
        },
        {
            "time": 11.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_5"},
        },
    ],
    "sub_boss_defeat": [
        {
            "time": 0,
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 540},
                "speed": 150,
            },
        },
        {
            "time": 1.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_1"},
        },
        {
            "time": 4,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_2"},
        },
        # TODO: Add an explosion event for the sub boss sprite
        {
            "time": 6.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_3"},
        },
        {
            "time": 9.0,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_4"},
        },
        {
            "time": 11.5,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_5"},
        },
        {
            "time": 14,
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_6"},
        },
    ],
    "level_boss_intro": {},
    "level_boss_defeat": {},
    "outro_1": {},
    "outro_2": {},
}
