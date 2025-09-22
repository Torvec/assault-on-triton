class ScoreStore:
    _instance = None

    def __new__(cls):
        """
        __new__ is called before __init__ when creating an object.
        This method controls the actual creation of the instance.
        """
        # Check if we've already created an instance
        if cls._instance is None:
            # First time: create a new instance using the parent class's __new__
            cls._instance = super(ScoreStore, cls).__new__(cls)
            # Set a flag to track if this instance has been initialized yet
            cls._instance._initialized = False
        # Always return the same instance (whether newly created or existing)
        return cls._instance

    def __init__(self):
        """
        __init__ gets called every time someone does ScoreStore(),
        but we only want to initialize the data once.
        """
        if self._initialized:
            return

        self.high_score = (
            14224100  #! Placeholder until i can retrieve from a file of saved scores
        )
        self.current_score = 0
        self._initialized = True

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
