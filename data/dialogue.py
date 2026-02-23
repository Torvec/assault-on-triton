import data.assets as assets

# CAST CONSTANTS
HERO_NAME = "Lt. Hiro"
CMDR_NAME = "Commander"
MID_BOSS_NAME = "Cpt. Zigg"
END_BOSS_NAME = "Admiral Wick"


SCRIPTED = {
    #! Level Intro
    "intro_1_1": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "Entering the debris field now.",
        "duration": 2.5,
    },
    "intro_1_2": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Clear as many asteroids as you can!",
        "duration": 2.5,
    },
    "intro_1_3": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "On it, Commander!",
        "duration": 2.5,
    },
    "intro_1_4": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Good Luck out there!",
        "duration": 2.5,
    },
    #! Mid Boss Intro
    "mid_boss_intro_1_1": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "A large enemy vessel is approaching!",
        "duration": 2.5,
    },
    "mid_boss_intro_1_2": {
        "speaker": MID_BOSS_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,  #! Temp
        "text": "Time to meet your maker, you pest!",
        "duration": 2.5,
    },
    "mid_boss_intro_1_3": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "Bring it on! I won't go down easily!",
        "duration": 2.5,
    },
    "mid_boss_intro_1_4": {
        "speaker": MID_BOSS_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,  #! Temp
        "text": "All cannons, target that fighter ship!",
        "duration": 2.5,
    },
    "mid_boss_intro_1_5": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Take him down Lieutenant!",
        "duration": 2.5,
    },
    #! Mid Boss Defeat
    "mid_boss_defeat_1_1": {
        "speaker": MID_BOSS_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,  #! Temp
        "text": "NO! How could I be defeated?!",
        "duration": 2.5,
    },
    "mid_boss_defeat_1_2": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "You never stood a chance!",
        "duration": 2.5,
    },
    "mid_boss_defeat_1_3": {
        "speaker": MID_BOSS_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,  #! Temp
        "text": "Aaagghhhhhh!!!",
        "duration": 2.5,
    },
    "mid_boss_defeat_1_4": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Good Job, Lieutenant!",
        "duration": 2.5,
    },
    "mid_boss_defeat_1_5": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Stay sharp, there are more enemies incoming!",
        "duration": 2.5,
    },
    "mid_boss_defeat_1_6": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "Aye Aye Commander, I got this!",
        "duration": 2.5,
    },
    #! End Boss Intro
    "end_boss_intro_1_1": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "The enemies battle station is approaching!",
        "duration": 2.0,
    },
    "end_boss_intro_1_2": {
        "speaker": END_BOSS_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "This worm thinks he can stop us?!",
        "duration": 2.0,
    },
    "end_boss_intro_1_3": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "You're about to find out!",
        "duration": 2.0,
    },
    #! End Boss Defeat
    "end_boss_defeat_1_1": {
        "speaker": END_BOSS_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "All systems are malfunctioning! How could this be?!",
        "duration": 2.0,
    },
    "end_boss_defeat_1_2": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "I'm just getting started!",
        "duration": 2.0,
    },
    "end_boss_defeat_1_3": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Test Text 3",
        "duration": 2.0,
    },
    #! Outro
    "outro_1_1": {
        "speaker": CMDR_NAME,
        "portrait": assets.COMMANDER_PORTRAIT_IMG,
        "text": "Well done Hiro! Keep fighting on!",
        "duration": 2.0,
    },
    "outro_1_2": {
        "speaker": HERO_NAME,
        "portrait": assets.HERO_PORTRAIT_IMG,
        "text": "Aye Aye Sir! All in a days work!",
        "duration": 2.0,
    },
}

DYNAMIC = {}
