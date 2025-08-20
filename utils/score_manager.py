class ScoreManager():
    def __init__(self):
        self.score = 0
        self.high_score = 0
        self.score_store = ''

    def inc_score(self, amount):
        self.score += amount
        return self.score
    
    def show_score(self):
        return self.score
    
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