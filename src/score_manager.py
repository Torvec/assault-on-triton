class ScoreManager:
    def __init__(self):
        self.score = 0
        self.score_store = ""
        self.high_score = 14224100
        self.multiplier = 1
        self.streak_meter = 0
        self.streak_meter_threshold = 10
        self.streak_meter_decay_amount = 1
        self.streak_meter_delay_decay_timer = 0

    def handle_score(self, amount):
        if amount < 0:
            self.score += amount
        else:
            self.score += amount * self.multiplier
            self.streak_meter_delay_decay_timer = 4

    def handle_streak_meter_inc(self, amount):
        self.streak_meter += amount
        if self.streak_meter > self.streak_meter_threshold:
            remainder = self.streak_meter - self.streak_meter_threshold
            self.streak_meter = 0
            self.streak_meter += remainder
            self.multiplier += 1
            self.streak_meter_threshold *= self.multiplier

    def handle_streak_meter_dec(self):
        if self.multiplier > 1:
            self.streak_meter_threshold /= self.multiplier
            self.multiplier -= 1
        self.streak_meter = 0

    def update_streak_meter_decay(self, dt):
        # Delay timer is triggered when the player increases the score in handle_score, delay timer can't go below 0
        if self.streak_meter_delay_decay_timer > 0:
            self.streak_meter_delay_decay_timer -= dt
            if self.streak_meter_delay_decay_timer < 0:
                self.streak_meter_delay_decay_timer = 0

        # When the delay timer is finished, the streak starts to decay based off of a set amount per frame
        if self.streak_meter > 0 and self.streak_meter_delay_decay_timer == 0:
            decay_amount = self.streak_meter_decay_amount * self.multiplier
            self.streak_meter -= decay_amount * dt

            # If the meter goes equal or below 0 and the multiplier is greater than 1 it will decrease the multiplier and handle the threshold as well as set the meter back to 100% to continue decreasing until it hits 0 at multiplier x1
            if self.streak_meter <= 0:
                if self.multiplier > 1:
                    self.streak_meter_threshold /= self.multiplier
                    self.multiplier -= 1
                    self.streak_meter = self.streak_meter_threshold
                else:
                    self.streak_meter = 0

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
