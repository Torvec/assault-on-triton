from data.assets import IMAGES

CAST = {
    "commander": {
        "name": "Commander",
        "portrait": IMAGES["commander_portrait"],
        "location": "bottom",
    },
    "hero": {
        "name": "Lt. Hiro",
        "portrait": IMAGES["hero_portrait"],
        "location": "bottom",
    },
    "test": {
        "name": "test",
        "portrait": IMAGES["commander_portrait"],
        "location": "top",
    },
}

SCRIPTED = {
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
    "enemy_test": {
        "speaker": CAST["test"]["name"],
        "portrait": CAST["test"]["portrait"],
        "text": "Come get some",
        "duration": 2.5,
        "location": CAST["test"]["location"],
    },
}

DYNAMIC = {}
