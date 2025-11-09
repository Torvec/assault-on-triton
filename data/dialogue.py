CAST = {
    "commander": {
        "name": "Commander",
        "portrait": "commander_portrait",
        "location": "bottom",
    },
    "hero": {
        "name": "Lt. Hiro",
        "portrait": "hero_portrait",
        "location": "bottom",
    },
    "enemy_captain": {
        "name": "Cpt. Zigg",
        "portrait": "hero_portrait",
        "location": "top",
    },
    "enemy_commander": {
        "name": "Admiral Wick",
        "portrait": "hero_portrait",
        "location": "top",
    },
}

SCRIPTED = {
    #! Level Intro
    "intro_1_1": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "Entering the debris field now.",
        "duration": 2.5,
        "location": CAST["hero"]["location"],
    },
    "intro_1_2": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Clear as many asteroids as you can!",
        "duration": 2.5,
        "location": CAST["commander"]["location"],
    },
    "intro_1_3": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "On it, Commander!",
        "duration": 2.5,
        "location": CAST["hero"]["location"],
    },
    "intro_1_4": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Good Luck out there!",
        "duration": 2.5,
        "location": CAST["commander"]["location"],
    },
    #! Sub-Boss Intro
    "sub_boss_intro_1_1": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "A large enemy vessel is approaching!",
        "duration": 2.5,
        "location": CAST["commander"]["location"],
    },
    "sub_boss_intro_1_2": {
        "speaker": CAST["enemy_captain"]["name"],
        "portrait": CAST["enemy_captain"]["portrait"],
        "text": "Time to meet your maker, you pest!",
        "duration": 2.5,
        "location": CAST["enemy_captain"]["location"],
    },
    "sub_boss_intro_1_3": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "Bring it on! I won't go down easily!",
        "duration": 2.5,
        "location": CAST["hero"]["location"],
    },
    "sub_boss_intro_1_4": {
        "speaker": CAST["enemy_captain"]["name"],
        "portrait": CAST["enemy_captain"]["portrait"],
        "text": "All cannons, target that fighter ship!",
        "duration": 2.5,
        "location": CAST["enemy_captain"]["location"],
    },
    "sub_boss_intro_1_5": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Take him down Lieutenant!",
        "duration": 2.5,
        "location": CAST["commander"]["location"],
    },
    #! Sub-Boss Defeat
    "sub_boss_defeat_1_1": {
        "speaker": CAST["enemy_captain"]["name"],
        "portrait": CAST["enemy_captain"]["portrait"],
        "text": "NO! How could I be defeated?!",
        "duration": 2.5,
        "location": CAST["enemy_captain"]["location"],
    },
    "sub_boss_defeat_1_2": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "You never stood a chance!",
        "duration": 2.5,
        "location": CAST["hero"]["location"],
    },
    "sub_boss_defeat_1_3": {
        "speaker": CAST["enemy_captain"]["name"],
        "portrait": CAST["enemy_captain"]["portrait"],
        "text": "Aaagghhhhhh!!!",
        "duration": 2.5,
        "location": CAST["enemy_captain"]["location"],
    },
    "sub_boss_defeat_1_4": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Good Job, Lieutenant!",
        "duration": 2.5,
        "location": CAST["commander"]["location"],
    },
    "sub_boss_defeat_1_5": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Stay sharp, there are more enemies incoming!",
        "duration": 2.5,
        "location": CAST["commander"]["location"],
    },
    "sub_boss_defeat_1_6": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "Aye Aye Commander, I got this!",
        "duration": 2.5,
        "location": CAST["hero"]["location"],
    },
    #! Level Boss Intro
    "level_boss_intro_1_1": {
        "speaker": "",
        "portrait": "",
        "text": "",
        "duration": "",
        "location": "",
    },
    #! Level Boss Defeat
    "level_boss_defeat_1_1": {
        "speaker": "",
        "portrait": "",
        "text": "",
        "duration": "",
        "location": "",
    },
    #! Outro
    "outro_1_1": {
        "speaker": "",
        "portrait": "",
        "text": "",
        "duration": "",
        "location": "",
    },
}

DYNAMIC = {}
