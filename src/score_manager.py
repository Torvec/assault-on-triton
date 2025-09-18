from src.score_store import ScoreStore


class ScoreManager:
    def __init__(self):
        self.score_store = ScoreStore()
        self.init_score_manager()
        
    def init_score_manager(self):
        self.score = 0
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
            self.streak_meter_delay_decay_timer = 3

    def handle_streak_meter_inc(self, amount):
        self.streak_meter += amount
        if self.streak_meter > self.streak_meter_threshold:
            remainder = self.streak_meter - self.streak_meter_threshold
            self.streak_meter = 0
            self.streak_meter += remainder
            self.handle_multiplier(1)

    def handle_streak_meter_dec(self):
        if self.multiplier > 1:
            self.handle_multiplier(-1)
        self.streak_meter = 0

    def handle_multiplier(self, num):
        if num < 0:
            self.streak_meter_threshold /= self.multiplier
            self.streak_meter_decay_amount /= self.multiplier
            self.multiplier += num
        else:
            self.multiplier += num
            self.streak_meter_threshold *= self.multiplier
            self.streak_meter_decay_amount *= self.multiplier

    def update_streak_meter_decay(self, dt):
        # Delay timer is triggered when the player increases the score in handle_score, delay timer can't go below 0
        if self.streak_meter_delay_decay_timer > 0:
            self.streak_meter_delay_decay_timer -= dt
            if self.streak_meter_delay_decay_timer < 0:
                self.streak_meter_delay_decay_timer = 0

        # When the delay timer is finished, the streak starts to decay based off of a set amount per frame
        if self.streak_meter > 0 and self.streak_meter_delay_decay_timer == 0:
            self.streak_meter -= self.streak_meter_decay_amount * dt

            # If the meter goes equal or below 0 and the multiplier is greater than 1 it will decrease the multiplier and handle the threshold as well as set the meter back to 100% to continue decreasing until it hits 0 at multiplier x1
            if self.streak_meter <= 0:
                if self.multiplier > 1:
                    self.streak_meter_threshold /= self.multiplier
                    self.streak_meter_decay_amount /= self.multiplier
                    self.multiplier -= 1
                    self.streak_meter = self.streak_meter_threshold
                else:
                    self.streak_meter = 0

    
