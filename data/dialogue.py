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
}

DYNAMIC = {}
