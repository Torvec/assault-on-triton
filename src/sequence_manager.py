class SequenceManager:
    def __init__(self):
        self.event_sequence = [
            {"T": 0, "action": lambda: print("Spawn Player at T-0")},
            {"T": 5, "action": lambda: print("Spawn Asteroids at T-5")},
            {"T": 10, "action": lambda: print("Spawn Enemy Ships at T-10")},
            {"T": 20, "action": lambda: print("The End at T-20")},

        ]
        self.time = 0

    def run_sequence(self, dt):
        self.time += dt
        while self.event_sequence and self.time >= self.event_sequence[0]["T"]:
            action = self.event_sequence.pop(0)
            action["action"]()
