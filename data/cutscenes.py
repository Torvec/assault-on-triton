CUTSCENE = {
    "intro": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 640},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_1"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_2"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_3"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "intro_1_4"},
        },
    ],
    "sub_boss_intro": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 720},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_1"},
        },
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "sub_boss",
                "location": {"x": 304, "y": 256},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_2"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_3"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_4"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_intro_1_5"},
        },
    ],
    "sub_boss_defeat": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 720},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_1"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_2"},
        },
        # TODO: Add an explosion event for the sub boss sprite
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_3"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_4"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_5"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "sub_boss_defeat_1_6"},
        },
    ],
    "level_boss_intro": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 720},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "level_boss_intro_1_1"},
        },
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "level_boss",
                "location": {"x": 304, "y": 256},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "level_boss_intro_1_2"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "level_boss_intro_1_3"},
        },
    ],
    "level_boss_defeat": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": 720},
                "speed": 150,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "level_boss_defeat_1_1"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "level_boss_defeat_1_2"},
        },
        # TODO: Add an explosion event for the sub boss sprite
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "level_boss_defeat_1_3"},
        },
    ],
    "outro": [
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "outro_1_1"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "outro_1_2"},
        },
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 304, "y": -128},
                "speed": 200,
            },
        },
    ],
    # "outro_2": {},
}
