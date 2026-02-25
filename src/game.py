import pygame
import data.settings as s
from src.screens import Start, Options, Scoreboard, Credits, Thanks
from src.gameplay_screen import GamePlay
from src.score_store import ScoreStore


class Game:

    def __init__(self, display_surface):
        self.display_surface = display_surface
        self.game_surface = pygame.Surface((s.BASE_GS_WIDTH, s.BASE_GS_HEIGHT))
        self.scale_factor = self.get_scale_factor()
        self.scaled_gs = self.scale_game_surface(self.scale_factor)
        self.scaled_gs_rect = self.scaled_gs.get_rect(
            center=self.display_surface.get_rect().center
        )
        self.ui_surface = pygame.Surface(self.scaled_gs.get_size(), pygame.SRCALPHA)
        self.ui_surface_rect = self.ui_surface.get_rect(
            topleft=self.scaled_gs_rect.topleft
        )
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_store = ScoreStore()
        self.running = True
        self.screens = {
            "Start": Start,
            "GamePlay": GamePlay,
            "Options": Options,
            "Scoreboard": Scoreboard,
            "Credits": Credits,
            "Thanks": Thanks,
        }
        self.change_screen("Start")

    def change_screen(self, screen_name):
        if screen_name not in self.screens:
            raise ValueError(f"Unknown scene: {screen_name}")
        self.current_screen = self.screens[screen_name](self)

    def get_scale_factor(self):
        scale_w = self.display_surface.get_width() // s.BASE_GS_WIDTH
        scale_h = self.display_surface.get_height() // s.BASE_GS_HEIGHT
        return max(1, min(scale_w, scale_h))

    def scale_game_surface(self, scale):
        return pygame.transform.scale(
            self.game_surface,
            (
                self.game_surface.get_width() * scale,
                self.game_surface.get_height() * scale,
            ),
        )

    def run(self):
        """
        Main game loop that handles events, updates game state, and renders.

        The loop performs the following steps each frame:
        1. Process pygame events (quit, input, etc.)
        2. Handle screen-specific events
        3. Update current screen state
        4. Render game objects to low-res game surface
        5. Scale game surface to display resolution
        6. Render UI elements to high-res UI surface
        7. Composite both surfaces to display
        8. Maintain target framerate
        """
        while self.running:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.current_screen.handle_event(events)
            self.current_screen.update(self.dt)
            self.current_screen.draw(self.game_surface)

            pygame.transform.scale(
                self.game_surface, self.scaled_gs.get_size(), self.scaled_gs
            )

            self.display_surface.fill("black")
            self.ui_surface.fill((0, 0, 0, 0))

            self.display_surface.blit(self.scaled_gs, self.scaled_gs_rect)

            self.current_screen.draw_ui(self.ui_surface, self.scale_factor)
            self.display_surface.blit(self.ui_surface, self.ui_surface_rect)

            pygame.display.flip()
            self.dt = self.clock.tick(s.TARGET_FPS) / 1000
        pygame.quit()
