STREAK_TIMER_MAX = 5.0
STREAK_TIMER_MIN = 1.0
DECREMENT_AMOUNT = 0.1
MULTIPLIER_MIN = 1
MULTIPLIER_MAX = 15

# Streak Meter: Increases by base points from enemy kills. When the meter reaches its threshold, the multiplier increases by 1 and the meter resets. Any remainder points overflow into the new meter.

# Threshold Scaling: The points required to fill the streak meter increase with each multiplier level to prevent runaway growth.

# Timer: A countdown runs while the streak meter is unfilled. If it reaches 0, the streak meter decays instead of hard-resetting. The decay percentage increases with the multiplier (e.g., at x3 the meter loses 25%, at x10 the meter loses 90%). If the meter is empty after decay, the multiplier decreases by 1. Taking damage always empties the meter and decreases the multiplier by 1.

# ALTERNATIVE TO TIMER: A constant tick instead of a variable length timer for each multiplier where the streak meter decreases by a set amount per tick and that amount increases as the multiplier increases. Example: at x3 the streak meter decreases by 2 points per tick (1 sec), at x6 the streak meter decreases by 5 points per tick, etc.

# Downtime Handling: The timer can freeze when no enemies are present to avoid punishing quiet sections.

# Bonus Points (Optional): Extra flat points can be awarded for burst actions (e.g., killing multiple enemies within a short window).

class ScoreManager:
    def __init__(self):
        self.score = 0
        self.score_store = ""
        self.high_score = 14224100
        self.streak_timer = STREAK_TIMER_MAX
        self.multiplier = MULTIPLIER_MIN

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