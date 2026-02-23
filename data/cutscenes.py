CUTSCENE = {
    "intro": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 108, "y": 180},
                "speed": 100,
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
    "mid_boss_intro": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 108, "y": 200},
                "speed": 100,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_intro_1_1"},
        },
        # {
        #     "action": "move_entity_to_loc",
        #     "params": {
        #         "entity_name": "mid_boss",
        #         "location": {"x": 108, "y": 90},
        #         "speed": 100,
        #     },
        # },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_intro_1_2"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_intro_1_3"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_intro_1_4"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_intro_1_5"},
        },
    ],
    "mid_boss_defeat": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 108, "y": 200},
                "speed": 100,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_defeat_1_1"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_defeat_1_2"},
        },
        # {
        #     "action": "explode_entity",
        #     "params": {"entity_name": "mid_boss"},
        # },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_defeat_1_3"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_defeat_1_4"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_defeat_1_5"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "mid_boss_defeat_1_6"},
        },
    ],
    "end_boss_intro": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 108, "y": 200},
                "speed": 100,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "end_boss_intro_1_1"},
        },
        # {
        #     "action": "move_entity_to_loc",
        #     "params": {
        #         "entity_name": "end_boss",
        #         "location": {"x": 108, "y": 90},
        #         "speed": 100,
        #     },
        # },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "end_boss_intro_1_2"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "end_boss_intro_1_3"},
        },
    ],
    "end_boss_defeat": [
        {
            "action": "move_entity_to_loc",
            "params": {
                "entity_name": "player",
                "location": {"x": 108, "y": 200},
                "speed": 100,
            },
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "end_boss_defeat_1_1"},
        },
        {
            "action": "show_dialogue",
            "params": {"dialogue_id": "end_boss_defeat_1_2"},
        },
        # {
        #     "action": "explode_entity",
        #     "params": {"entity_name": "end_boss"},
        # },
        # {
        #     "action": "show_dialogue",
        #     "params": {"dialogue_id": "end_boss_defeat_1_3"},
        # },
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
                "location": {"x": 108, "y": -40},
                "speed": 100,
            },
        },
    ],
}
