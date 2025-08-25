class SceneManager:
    def __init__(self, initial_scene):
        self.current_scene = initial_scene

    def set_scene(self, new_scene):
        self.current_scene = new_scene

    def update(self, dt, events):
        self.current_scene.update(dt, events)

    def draw(self, screen):
        self.current_scene.draw(screen)
