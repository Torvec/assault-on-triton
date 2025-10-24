from src.data.assets import IMAGES

CAST = {
    "commander": {"name": "Commander", "portrait": IMAGES["commander_portrait"]},
    "hero": {"name": "Lt. Hiro", "portrait": IMAGES["hero_portrait"]},
}

SCRIPTED = {
    "intro_1_1": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "Entering the debris field now.",
        "timer": 3,
        "location": "left",
    },
    "intro_1_2": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Clear as many asteroids as you can!",
        "timer": 3,
        "location": "right",
    },
    "intro_1_3": {
        "speaker": CAST["hero"]["name"],
        "portrait": CAST["hero"]["portrait"],
        "text": "On it, Commander!",
        "timer": 3,
        "location": "left",
    },
    "intro_1_4": {
        "speaker": CAST["commander"]["name"],
        "portrait": CAST["commander"]["portrait"],
        "text": "Good Luck out there!",
        "timer": 3,
        "location": "right",
    },
}

DYNAMIC = {}
