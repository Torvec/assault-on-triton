class ScoreManager:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.score_store = ""
        self.multiplier = 1
        self.max_streak_timer = 2
        self.min_streak_timer = 0.4
        self.decrement_amount = 0.1
        self.streak_timer = self.max_streak_timer

    def inc_score(self, amount):
        self.score += amount * self.multiplier

    def set_multiplier(self, num):
        self.multiplier += num

    def set_streak_timer(self):
        self.streak_timer = (
            self.max_streak_timer - (self.multiplier - 1) * self.decrement_amount
        )
        if self.streak_timer <= self.min_streak_timer:
            self.streak_timer = self.min_streak_timer

    def handle_streak_timer(self, dt):
        self.streak_timer -= dt
        if self.streak_timer <= 0 and self.multiplier > 1:
            self.set_multiplier(-1)
            self.set_streak_timer()
        if self.multiplier == 1:
            self.streak_timer = self.max_streak_timer

    def create_score_store(self):
        # Creates the json file that stores all scores from highest to lowest if one is not found
        pass

    def load_score(self):
        # Accesses the score from the json file and parses it
        pass

    def save_score(self):
        # Saves the current score to the json file and places in the correct order
        pass

    def clear_scores(self):
        self.create_score_store()
