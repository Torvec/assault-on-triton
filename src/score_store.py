class ScoreStore:

    def __init__(self):
        self.high_score = 142241  #! Placeholder
        self.current_score = 0

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
