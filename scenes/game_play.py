import pygame
import sys
from scenes.scene import Scene
from entities.player import Player
from entities.asteroid import Asteroid
from utils.asteroid_spawn_manager import AsteroidSpawnManager
from entities.shot import Shot
from ui.render_text import render_text

# Game play loop
# Start
# 1 Player given objective message (Destroy X asteroids/enemy ships, defend planet from asteroids for x mins, defend space station/ship, etc.)
# 2 Player spawns in from center or from side they came in on and can move/shoot
# 3 Targets spawn in at certain intervals/amounts
# 4 Player destroys targets
# 5 Objective accomplished message
# 6 Player chooses which direction to go next (up, down, left, right) but can't go to a previous stage
# Back to 1


class GamePlay(Scene):
    def __init__(self, game, screen, dt):
        super().__init__(game, screen, dt)
        self.asteroids = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        # Set containers attributes so the sprites automatically get added to the appropriate groups
        Asteroid.containers = (self.asteroids, self.updateable, self.drawable)
        AsteroidSpawnManager.containers = self.updateable
        Player.containers = (self.updateable, self.drawable)
        Shot.containers = (self.shots, self.updateable, self.drawable)

        self.asteroid_spawner = AsteroidSpawnManager(self.game, 10)
        self.player = Player(
            self.game, self.game.screen_w // 2, self.game.screen_h // 2
        )
        self.score = game.score_manager
        self.score.score = 0
        self.isPaused = False

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.isPaused = not self.isPaused
            if self.isPaused:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
                    self.game.scene_manager.set_scene(
                        GamePlay(self.game, self.screen, self.dt)
                    )
                if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
                    from scenes.start import Start

                    self.game.scene_manager.set_scene(
                        Start(self.game, self.screen, self.dt)
                    )
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

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

                        self.game.scene_manager.set_scene(
                            GameOver(self.game, self.screen, self.dt)
                        )
                    self.player.respawn()

                for shot in self.shots:
                    if shot.collides_with(asteroid):
                        shot.kill()
                        asteroid.split()
                        self.asteroid_spawner.target_amount -= 1
                        self.score.inc_score(1)

    def draw(self, screen):
        super().draw(screen)

        render_text(
            self.screen,
            f"Lives: {self.player.lives}",
            32,
            "grey90",
            (self.game.screen_w // 4, self.game.screen_h - 64),
        )
        render_text(
            self.screen,
            f"Score: {self.score.show_score()}",
            32,
            "grey90",
            (self.game.screen_w // 2, self.game.screen_h - 64),
        )
        render_text(
            self.screen,
            f"Targets: {self.asteroid_spawner.show_target_amount()}",
            32,
            "grey90",
            (self.game.screen_w // 3, self.game.screen_h - 64),
        )

        if self.isPaused:

            pause_menu_rect = pygame.Rect(
                0, 0, self.game.screen_w // 2, self.game.screen_h // 4
            )
            pause_menu_rect.center = (self.game.screen_w // 2, self.game.screen_h // 2)
            pygame.draw.rect(screen, "grey4", pause_menu_rect)
            pygame.draw.rect(
                screen, "grey70", pause_menu_rect, width=4, border_radius=24
            )

            render_text(
                self.screen,
                "GAME PAUSED",
                64,
                "white",
                (pause_menu_rect.midtop[0], pause_menu_rect.midtop[1] + 64),
                align="midtop",
            )
            render_text(
                self.screen,
                "[ESC] Resume",
                36,
                "grey",
                (pause_menu_rect.center[0], pause_menu_rect.center[1] - 36),
            )
            render_text(
                self.screen,
                "[1] Restart",
                36,
                "grey",
                (pause_menu_rect.center[0], pause_menu_rect.center[1]),
            )
            render_text(
                self.screen,
                "[2] Main Menu",
                36,
                "grey",
                (pause_menu_rect.center[0], pause_menu_rect.center[1] + 36),
            )
            render_text(
                self.screen,
                "[Q] QUIT",
                36,
                "grey",
                (pause_menu_rect.center[0], pause_menu_rect.center[1] + 72),
            )
