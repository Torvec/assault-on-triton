from src.spawn_manager import SpawnManager


class EventManager:

    def __init__(self, game_play, timeline):
        self.game_play = game_play
        self.timeline = timeline
        self.current_time = 0
        self.current_index = 0
        self.is_paused = False

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def spawn_enemies(self, type, count, location, formation):
        spawn_manager = SpawnManager(self.game_play, type, count, location, formation)
        spawn_manager.spawn_entity()

    def show_message(self, text):
        print(text)

    def end_level(self):
        if len(self.game_play.active_targets) == 0:
            from src.scenes import GameOver

            self.game_play.game.set_scene(GameOver(self.game_play.game))

    def update(self, dt):
        if self.is_paused:
            return

        self.current_time += dt

        while (
            self.current_index < len(self.timeline)
            and self.current_time >= self.timeline[self.current_index]["time"]
        ):
            event_data = self.timeline[self.current_index]
            event_name = event_data["event"]
            params = event_data.get("params", {})

            if event_name == "spawn_enemies":
                self.spawn_enemies(**params)
            elif event_name == "show_message":
                self.show_message(**params)
            elif event_name == "end_level":
                self.end_level()

            self.current_index += 1
