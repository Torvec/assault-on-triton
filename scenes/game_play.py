import pygame
import sys
from scenes.scene import Scene
from entities.player import Player
from entities.asteroid import Asteroid
from utils.asteroid_spawn_manager import AsteroidSpawnManager
from entities.shot import Shot
from ui.render_text import render_text


class GamePlay(Scene):
    def __init__(self, game):
        super().__init__(game)
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        # Set containers attributes so the sprites automatically get added to the appropriate groups
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        AsteroidSpawnManager.containers = self.updateable
        Player.containers = (self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)

        self.play_area_rect = pygame.Rect(
            0, 0, self.game.screen_w, self.game.screen_h - 128
        )
        self.game_HUD_rect = pygame.Rect(
            0, self.game.screen_h - 128, self.game.screen_w, 128
        )

        self.asteroid_spawner = AsteroidSpawnManager(self.game, 10)
        self.player = Player(
            self.game, self.game.screen_w // 2, self.game.screen_h // 2
        )
        self.score = game.score_manager
        self.score.score = 0
        self.isPaused = False

    def pause_menu_controls(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.isPaused = not self.isPaused
            if self.isPaused:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.game.scene_manager.set_scene(GamePlay(self.game))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    from scenes.start import Start

                    self.game.scene_manager.set_scene(Start(self.game))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

    def pause_menu_display(self, screen):
        pause_menu_rect = pygame.Rect(
            0, 0, self.game.screen_w // 2, self.game.screen_h // 4
        )
        pause_menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2)
        pygame.draw.rect(screen, "grey4", pause_menu_rect)
        pygame.draw.rect(screen, "grey70", pause_menu_rect, width=4, border_radius=24)

        render_text(
            screen=self.game.screen,
            text="GAME PAUSED",
            font_size=64,
            pos=(pause_menu_rect.midtop[0], pause_menu_rect.midtop[1] + 64),
            align="midtop",
        )
        render_text(
            screen=self.game.screen,
            text="[ESC] Resume",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] - 36),
        )
        render_text(
            screen=self.game.screen,
            text="[1] Restart",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1]),
        )
        render_text(
            screen=self.game.screen,
            text="[2] Main Menu",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] + 36),
        )
        render_text(
            screen=self.game.screen,
            text="[Q] QUIT",
            color="grey",
            pos=(pause_menu_rect.center[0], pause_menu_rect.center[1] + 72),
        )

    def game_HUD(self):
        render_text(
            screen=self.game.screen,
            text=f"Lives: {self.player.lives}",
            color="grey90",
            pos=(self.game.screen_w // 4, self.game.screen_h - 64),
        )
        render_text(
            screen=self.game.screen,
            text=f"Score: {self.score.show_score()}",
            color="grey90",
            pos=(self.game.screen_w // 2, self.game.screen_h - 64),
        )
        render_text(
            screen=self.game.screen,
            text=f"Targets: {self.asteroid_spawner.show_target_amount()}",
            color="grey90",
            pos=(self.game.screen_w // 3, self.game.screen_h - 64),
        )

    def update(self, dt, events):

        self.pause_menu_controls(events)

        if not self.isPaused:
            super().update(dt)

            for asteroid in self.asteroids:
                if (
                    asteroid.collides_with(self.player)
                    and self.player.invincibleTime == 0
                ):
                    self.player.lives -= 1
                    asteroid.split()
                    if self.player.lives <= 0:
                        from scenes.game_over import GameOver

                        self.game.scene_manager.set_scene(GameOver(self.game))
                    self.player.respawn()

                for shot in self.shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        self.asteroid_spawner.target_amount -= 1
                        self.score.inc_score(1)

    def draw(self, screen):
        super().draw(screen)
        self.game_HUD()

        if self.isPaused:
            self.pause_menu_display(screen)
