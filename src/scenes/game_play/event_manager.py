from src.scenes.game_play.spawn_manager import SpawnManager


class EventManager:

    def __init__(self, game_play, timeline):
        self.game_play = game_play
        self.timeline = timeline
        self.current_time = 0
        self.current_index = 0
        self.is_paused = False

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def spawn_entities(self, type, count, location, formation, behaviors):
        spawn_manager = SpawnManager(
            self.game_play, type, count, location, formation, behaviors
        )
        spawn_manager.spawn_entity()

    def show_message(self, text):
        print(text)

    def handle_event(self, event):
        event_name = event["event"]
        params = event.get("params", {})
        if event_name == "spawn_entities":
            self.spawn_entities(**params)
        elif event_name == "show_message":
            self.show_message(**params)
        else:
            print(f"Unknown event type: {event_name}")

    def process_timeline(self):
        while (
            self.current_index < len(self.timeline)
            and self.current_time >= self.timeline[self.current_index]["time"]
        ):
            event_data = self.timeline[self.current_index]
            self.handle_event(event_data)
            self.current_index += 1

    def update(self, dt):
        if self.is_paused:
            return

        self.current_time += dt
        self.process_timeline()
