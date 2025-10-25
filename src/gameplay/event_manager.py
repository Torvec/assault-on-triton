from src.gameplay.spawn_manager import SpawnManager


class EventManager:

    def __init__(self, game_play, timeline):
        self.game_play = game_play
        self.timeline = timeline
        self.timeline_time = 0
        self.timeline_index = 0
        self.timeline_time_paused = False

    def spawn_entity(self, type, location, behaviors):
        spawner = SpawnManager(self.game_play, type, location, behaviors)
        spawner.spawn_entity()

    def show_message(self, message_id):
        self.game_play.game_play_hud.display_message(message_id)

    def show_dialogue(self, dialogue_id):
        self.game_play.game_play_hud.display_dialogue(dialogue_id)

    def control_player(self):
        # Disable controls
        # Take control of player
        # Move player to desired location
        # etc.
        pass

    def pause_event_timeline(self):
        self.timeline_time_paused = True
        print("Timeline timer is paused")
        print(self.timeline_time_paused)

    def resume_event_timeline(self):
        self.timeline_time_paused = False
        print("Timeline timer resumed")
        print(self.timeline_time_paused)

    def handle_event(self, event):
        event_name = event["event"]
        params = event.get("params", {})
        match event_name:
            case "spawn_entity":
                self.spawn_entity(**params)
            case "show_message":
                self.show_message(**params)
            case "show_dialogue":
                self.show_dialogue(**params)
            case "control_player":
                self.control_player(**params)
            case "pause_timeline":
                self.pause_event_timeline(**params)
            case "resume_timeline":
                self.resume_event_timeline(**params)
            case _:
                print(f"Unknown event type: {event_name}")

    def process_timeline(self):
        while (
            self.timeline_index < len(self.timeline)
            and self.timeline_time >= self.timeline[self.timeline_index]["time"]
        ):
            current_event = self.timeline[self.timeline_index]
            self.handle_event(current_event)
            self.timeline_index += 1

    def update(self, dt):
        if not self.timeline_time_paused:
            self.timeline_time += dt
            self.process_timeline()
