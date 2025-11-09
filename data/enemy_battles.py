"""
Anatomy of a Battle:
Spawn the entity off screen and move it to the play area
Battle ends when on_event_complete is called, which will only be called after the boss is defeated
"""

BATTLE = {
    "sub-boss": [{"entity": "sub_boss"}],
    "level-boss": [{"entity": "level_boss"}],
}
