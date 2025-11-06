from src.gameplay.spawn_manager import SpawnManager
from src.gameplay.gameplay_states import GameplayState


class EventManager:

    def __init__(self, gameplay, timeline):
        self.gameplay = gameplay
        self.timeline = timeline
        self.timeline_time = 0.0
        self.timeline_index = 0
        self.is_paused = False
        self.event_handlers = {
            "trigger_cutscene": self.trigger_cutscene,
            "trigger_waves": self.trigger_waves,
            "trigger_battle": self.trigger_battle,
            "trigger_mission_complete": self.trigger_mission_complete,
            "spawn_entity": self.spawn_entity,
            "show_message": self.show_message,
            "show_dialogue": self.show_dialogue,
        }

    def trigger_cutscene(self, cutscene_id):
        self.gameplay.change_state(GameplayState.CUTSCENE)
        self.gameplay.cutscene_manager.start_cutscene(cutscene_id)

    def trigger_waves(self):
        play_state = self.gameplay.states[GameplayState.PLAY]
        play_state.is_battle = False
        self.gameplay.change_state(GameplayState.PLAY)

    def trigger_battle(self):
        play_state = self.gameplay.states[GameplayState.PLAY]
        play_state.is_battle = True
        self.gameplay.change_state(GameplayState.PLAY)

    def trigger_mission_complete(self):
        self.gameplay.change_state(GameplayState.MISSION_COMPLETE)

    def spawn_entity(self, type, location, behaviors):
        spawner = SpawnManager(self.gameplay, type, location, behaviors)
        spawner.spawn_entity()

    def show_message(self, message_id):
        self.gameplay.gameplay_ui.display_message(message_id)

    def show_dialogue(self, dialogue_id):
        self.gameplay.gameplay_ui.display_dialogue(dialogue_id)

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
        if self.is_paused:
            return

        self.timeline_time += dt
        self.process_timeline()
