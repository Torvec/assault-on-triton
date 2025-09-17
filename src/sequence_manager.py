from src.spawn_manager import SpawnManager
from src.entities import Asteroid, EnemyDrone, EnemyShip, Missile


class SequenceManager:
    def __init__(self, game_play):
        self.game_play = game_play
        self.setup_sequence()

    def setup_sequence(self):
        self.event_sequence = [
            {
                "event": 0,
                "action": [
                    lambda: SpawnManager(self.game_play, Asteroid, 20, 1.25),
                    lambda: SpawnManager(self.game_play, EnemyShip, 10, 0.8),
                    lambda: SpawnManager(self.game_play, EnemyDrone, 16, 0.4),
                    lambda: SpawnManager(self.game_play, Missile, 12, 1.0),
                ],
            },
            # {
            #     "event": 1,
            #     "action": [
            #         lambda: SpawnManager(self.game_play, EnemyDrone, 8, 0.75),
            #         lambda: SpawnManager(self.game_play, EnemyShip, 4, 1.5),
            #     ],
            # },
            # {
            #     "event": 2,
            #     "action": [
            #         lambda: SpawnManager(self.game_play, EnemyDrone, 12, 0.5),
            #         lambda: SpawnManager(self.game_play, EnemyShip, 8, 1.0),
            #         lambda: SpawnManager(self.game_play, Missile, 10, 1.2),
            #     ],
            # },
            # {
            #     "event": 3,
            #     "action": [
            #         lambda: SpawnManager(self.game_play, Asteroid, 20, 1.25),
            #         lambda: SpawnManager(self.game_play, EnemyShip, 10, 0.8),
            #         lambda: SpawnManager(self.game_play, EnemyDrone, 16, 0.4),
            #         lambda: SpawnManager(self.game_play, Missile, 12, 1.0),
            #     ],
            # },
        ]
        self.current_event = 0
        self.event_active = False

    def reset_sequence(self):
        self.setup_sequence()

    def set_current_event(self):
        self.current_event += 1
        self.event_active = False

    def run_sequence(self):
        if self.event_sequence and self.current_event < len(self.event_sequence):
            if not self.event_active:
                current_action = self.event_sequence[self.current_event]
                for action in current_action["action"]:
                    action()
                self.event_active = True
        else:
            return
