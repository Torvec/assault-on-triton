STREAK_TIMER_MAX = 2
STREAK_TIMER_MIN = 0.4
DECREMENT_AMOUNT = 0.1


class ScoreManager:
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.score_store = ""
        self.streak_timer = STREAK_TIMER_MAX
        self.multiplier = 1

    def inc_score(self, amount):
        self.score += amount * self.multiplier

    def set_multiplier(self, num):
        self.multiplier += num

    def set_streak_timer(self):
        self.streak_timer = STREAK_TIMER_MAX - (self.multiplier - 1) * DECREMENT_AMOUNT
        if self.streak_timer <= STREAK_TIMER_MIN:
            self.streak_timer = STREAK_TIMER_MIN

    def handle_streak_timer(self, dt):
        self.streak_timer -= dt
        if self.streak_timer <= 0 and self.multiplier > 1:
            self.multiplier -= 1
            self.set_streak_timer()
        if self.multiplier == 1:
            self.streak_timer = STREAK_TIMER_MAX

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
