import pygame
from src.scenes import GamePlay
from src.score_manager import ScoreManager

GS_WIDTH = 608
SB_WIDTH = 656
SB_R_OFFSET = 1264


class Game:

    def __init__(self, screen):
        self.screen = screen
        self.sidebar_l_surface = pygame.Surface((SB_WIDTH, self.screen.get_height()))
        self.game_surface = pygame.Surface((GS_WIDTH, self.screen.get_height()))
        self.gs_w = self.game_surface.get_width()
        self.gs_h = self.game_surface.get_height()
        self.sidebar_r_surface = pygame.Surface((SB_WIDTH, self.screen.get_height()))
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.score_manager = ScoreManager()
        #! self.set_scene(Start(self))
        self.set_scene(GamePlay(self))
        self.running = True

    def set_scene(self, new_scene):
        self.current_scene = new_scene

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
            self.screen.blit(self.sidebar_l_surface, (0, 0))
            self.screen.blit(self.game_surface, game_surface_rect.topleft)
            self.screen.blit(self.sidebar_r_surface, (SB_R_OFFSET, 0))

            pygame.display.flip()

            self.dt = self.clock.tick(60) / 1000

        pygame.quit()  # * Note: Doesn't need sys.exit() after this because it is the end of the file and nothing is running
