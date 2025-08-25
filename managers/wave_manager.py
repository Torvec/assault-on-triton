import pygame
import random
from ui.render_text import render_text

"""
Needs to:
- Keep track of the current wave
- Increment the wave count when all targets are destroyed
- Provide a way to display the current wave
- 
"""

class WaveManager():
    def __init__(self, game, dt):
        self.game = game
        self.dt = dt
        self.current_wave = 1
        self.num_of_targets = 10
        self.max_targets = 20
        self.count_up_timer = 0.00
        self.count_down_timer = 3.00

    def display_current_wave(self):
        return self.current_wave
    
    def display_num_of_targets(self):
        return self.num_of_targets
    
    def inc_wave_number(self):
        self.current_wave += 1

    def count_up(self, dt):
        self.count_up_timer += dt

    def count_down(self, dt):
        self.count_down_timer -= dt
        if self.count_down_timer <= 0:
            self.count_down_timer = 0

    def display_count_up(self):
        render_text(
            screen=self.game.screen,
            text=f"Time: {self.count_up_timer}",
            pos=(self.game.screen // 2, 36)
        )

    def display_count_down(self):
        render_text(
            screen=self.game.screen,
            text=f"Next Wave Starts in: {self.count_down_timer}",
            pos=(self.game.screen_w // 2, self.game.screen_h // 2)
        )

    def reset_count_down(self):
        self.count_down_timer = 3.00

    def reset_count_up(self):
        self.count_up_timer = 0.00

    def update(self):
        pass

    def draw(self):
        pass