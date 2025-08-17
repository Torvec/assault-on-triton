class Scene():
    def __init__(self, screen, dt):
        self.screen = screen
        self.dt = dt

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill("black")