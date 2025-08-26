from src.spawner import Spawner


class WaveManager:
    def __init__(self):
        self.waves = [
            {"asteroids": 4, "enemy_ships": 0, "boss": 0},  # Wave 01
            {"asteroids": 8, "enemy_ships": 0, "boss": 0},  # Wave 02
            {"asteroids": 12, "enemy_ships": 0, "boss": 0},  # Wave 03
            {"asteroids": 16, "enemy_ships": 0, "boss": 0},  # Wave 04
            {"asteroids": 20, "enemy_ships": 2, "boss": 0},  # Wave 05
            {"asteroids": 24, "enemy_ships": 4, "boss": 0},  # Wave 06
            {"asteroids": 28, "enemy_ships": 6, "boss": 0},  # Wave 07
            {"asteroids": 32, "enemy_ships": 8, "boss": 0},  # Wave 08
            {"asteroids": 36, "enemy_ships": 10, "boss": 0},  # Wave 09
            {"asteroids": 0, "enemy_ships": 0, "boss": 1},  # Wave 10
            {"asteroids": 40, "enemy_ships": 10, "boss": 0},  # Wave 11
            {"asteroids": 42, "enemy_ships": 10, "boss": 0},  # Wave 12
            {"asteroids": 44, "enemy_ships": 10, "boss": 0},  # Wave 13
            {"asteroids": 46, "enemy_ships": 10, "boss": 0},  # Wave 14
            {"asteroids": 48, "enemy_ships": 12, "boss": 0},  # Wave 15
            {"asteroids": 50, "enemy_ships": 14, "boss": 0},  # Wave 16
            {"asteroids": 52, "enemy_ships": 16, "boss": 0},  # Wave 17
            {"asteroids": 54, "enemy_ships": 18, "boss": 0},  # Wave 18
            {"asteroids": 56, "enemy_ships": 20, "boss": 0},  # Wave 19
            {"asteroids": 0, "enemy_ships": 0, "boss": 1},  # Wave 20
            {"asteroids": 58, "enemy_ships": 22, "boss": 0},  # Wave 21
            {"asteroids": 60, "enemy_ships": 24, "boss": 0},  # Wave 22
            {"asteroids": 62, "enemy_ships": 26, "boss": 0},  # Wave 23
            {"asteroids": 64, "enemy_ships": 28, "boss": 0},  # Wave 24
            {"asteroids": 64, "enemy_ships": 30, "boss": 0},  # Wave 25
            {"asteroids": 64, "enemy_ships": 32, "boss": 0},  # Wave 26
            {"asteroids": 64, "enemy_ships": 34, "boss": 0},  # Wave 27
            {"asteroids": 64, "enemy_ships": 36, "boss": 0},  # Wave 28
            {"asteroids": 64, "enemy_ships": 36, "boss": 0},  # Wave 29
            {"asteroids": 0, "enemy_ships": 0, "boss": 1},  # Wave 30
        ]
        self.current_wave = 1
        # self.spawner = Spawner(
        #     self.game, self.play_area_rect, self.waves[self.current_wave]
        # )

    def set_current_wave(self, num):
        self.current_wave = num

    def next_wave(self):
        self.current_wave += 1

    def show_target_count(self):
        wave = self.waves[self.current_wave - 1]
        targets = wave["asteroids"] + wave["enemy_ships"] + wave["boss"]
        return targets

    def show_current_wave(self):
        return self.current_wave

    def update(self):
        pass
