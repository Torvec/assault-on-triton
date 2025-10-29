from src.gameplay.spawn_manager import SpawnManager


class EventManager:

    def __init__(self, gameplay, timeline):
        self.gameplay = gameplay
        self.timeline = timeline
        self.timeline_time = 0
        self.timeline_index = 0
        self.timeline_time_paused = False
        self.event_handlers = {
            "spawn_entity": self.spawn_entity,
            "show_message": self.show_message,
            "show_dialogue": self.show_dialogue,
            "disable_player_controls": self.disable_player_controls,
            "enable_player_controls": self.enable_player_controls,
            "move_player_to": self.move_player_to,
            "pause_timeline": self.pause_event_timeline,
            "resume_timeline": self.resume_event_timeline,
        }

    def spawn_entity(self, type, location, behaviors):
        spawner = SpawnManager(self.gameplay, type, location, behaviors)
        spawner.spawn_entity()

    def show_message(self, message_id):
        self.gameplay.gameplay_ui.display_message(message_id)

    def show_dialogue(self, dialogue_id):
        self.gameplay.gameplay_ui.display_dialogue(dialogue_id)

    def disable_player_controls(self):
        self.gameplay.player.controls_enabled = False

    def enable_player_controls(self):
        self.gameplay.player.controls_enabled = True

    def move_player_to(self, x, y, speed):
        self.gameplay.player.move_player_to(x, y, speed)

    def pause_event_timeline(self):
        self.timeline_time_paused = True

    def resume_event_timeline(self):
        self.timeline_time_paused = False

    def handle_event(self, event):
        event_name = event["event"]
        params = event.get("params", {})
        handler = self.event_handlers.get(event_name)
        if handler:
            handler(**params)
        else:
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
