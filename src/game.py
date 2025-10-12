import pygame
from src.score_store import ScoreStore
from src.config.settings import DISPLAY


class Game:

    def __init__(self, screen):
        self.config = DISPLAY
        self.screen = screen
        self.sidebar_l_surface = pygame.Surface(
            (self.config["sidebar_width"], self.screen.get_height())
        )
        self.game_surface = pygame.Surface(
            (self.config["game_surface_width"], self.screen.get_height())
        )
        self.gs_w = self.game_surface.get_width()
        self.gs_h = self.game_surface.get_height()
        self.sidebar_r_surface = pygame.Surface(
            (self.config["sidebar_width"], self.screen.get_height())
        )
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_store = ScoreStore()
        self.set_scene("Start")
        self.running = True

    def set_scene(self, scene_name):
        match scene_name:
            case "Start":
                from src.menus.start_menu import Start

                self.current_scene = Start(self)
            case "GamePlay":
                from src.gameplay.gameplay import GamePlay

                self.current_scene = GamePlay(self)
            case "GameOver":
                from src.menus.game_over import GameOver

                self.current_scene = GameOver(self)
            case "Options":
                from src.menus.options_menu import Options

                self.current_scene = Options(self)
            case "Scoreboard":
                from src.menus.scoreboard import Scoreboard

                self.current_scene = Scoreboard(self)
            case "Credits":
                from src.menus.credits import Credits

                self.current_scene = Credits(self)
            case _:
                raise ValueError(f"Unknown scene: {scene_name}")

    def run(self):
        while self.running:
            events = pygame.event.get()

            self.current_scene.update(self.dt, events)
            self.current_scene.draw(
                self.game_surface, self.sidebar_l_surface, self.sidebar_r_surface
            )

            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            # height = self.screen.get_height()
            # width = int(height * ASPECT_RATIO)
            # scaled_game_surface = pygame.transform.smoothscale(
            #     self.game_surface, (width, height)
            # )
            # game_surface_rect = scaled_game_surface.get_rect(
            #     center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
            # )
            # self.screen.fill("black")
            # self.screen.blit(scaled_game_surface, game_surface_rect.topleft)

            game_surface_rect = self.game_surface.get_rect(
                center=(self.screen.get_width() // 2, self.screen.get_height() // 2)
            )
            self.screen.blit(
                self.sidebar_l_surface, (self.config["sidebar_left_offset"], 0)
            )
            self.screen.blit(self.game_surface, game_surface_rect.topleft)
            self.screen.blit(
                self.sidebar_r_surface, (self.config["sidebar_right_offset"], 0)
            )

            pygame.display.flip()

            self.dt = self.clock.tick(self.config["target_fps"]) / 1000

        pygame.quit()  # * Note: Doesn't need sys.exit() after this because it is the end of the file and nothing is running
