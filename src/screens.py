import sys
import pygame
from src.render_text import render_text


class Screen:

    def __init__(self, game):
        self.game = game
        self.backgrounds = []

    def handle_event(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, game_surface):
        game_surface.fill("#0c0c12")

    def draw_ui(self, ui_surface, scale_factor):
        pass


class Start(Screen):

    menu_items = [
        "[Enter] PLAY",
        "[O] OPTIONS",
        "[S] SCORES",
        "[C] CREDITS",
        "[Q] QUIT",
    ]

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_RETURN:
                        self.game.change_screen("GamePlay")
                    case pygame.K_o:
                        self.game.change_screen("Options")
                    case pygame.K_s:
                        self.game.change_screen("Scoreboard")
                    case pygame.K_c:
                        self.game.change_screen("Credits")
                    case pygame.K_q:
                        pygame.quit()
                        sys.exit()

    def update(self, dt):
        super().update(dt)

    def draw(self, game_surface):
        super().draw(game_surface)

    def draw_ui(self, ui_surface, scale_factor):
        super().draw_ui(ui_surface, scale_factor)
        render_text(
            screen=ui_surface,
            text="ASSAULT",
            font_name="zendots",
            font_size=32,
            scale_factor=scale_factor,
            antialias=True,
            pos=(
                ui_surface.get_rect().center[0],
                ui_surface.get_rect().center[1] - 88 * scale_factor,
            ),
            align="midbottom",
        )
        render_text(
            screen=ui_surface,
            text="ON",
            font_name="zendots",
            font_size=24,
            scale_factor=scale_factor,
            antialias=True,
            pos=(
                ui_surface.get_rect().center[0],
                ui_surface.get_rect().center[1] - 64 * scale_factor,
            ),
            align="midbottom",
        )
        render_text(
            screen=ui_surface,
            text="TRITON",
            font_name="zendots",
            font_size=32,
            scale_factor=scale_factor,
            antialias=True,
            pos=(
                ui_surface.get_rect().center[0],
                ui_surface.get_rect().center[1] - 32 * scale_factor,
            ),
            align="midbottom",
        )
        menu_rect = pygame.Rect(
            0, 0, ui_surface.get_width() * 0.75, ui_surface.get_height() * 0.4
        )
        menu_rect.midtop = ui_surface.get_rect().center
        pygame.draw.rect(ui_surface, "grey4", menu_rect, border_radius=12)
        pygame.draw.rect(ui_surface, "grey70", menu_rect, width=2, border_radius=12)
        for i, item in enumerate(self.menu_items):
            render_text(
                screen=ui_surface,
                text=item,
                font_name="spacegrotesk_semibold",
                font_size=18,
                scale_factor=scale_factor,
                color="grey",
                pos=(
                    menu_rect.midtop[0],
                    menu_rect.midtop[1] + 8 + (i * 24 * scale_factor),
                ),
                align="midtop",
            )


class Options(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, game_surface):
        super().draw(game_surface)

    def draw_ui(self, ui_surface, scale_factor):
        super().draw_ui(ui_surface, scale_factor)
        render_text(
            screen=ui_surface,
            text="Options",
            font_name="zendots",
            font_size=32,
            scale_factor=scale_factor,
            pos=(ui_surface.get_width() * 0.5, 32 * scale_factor),
        )
        render_text(
            screen=ui_surface,
            text="scores go here",
            font_size=24,
            scale_factor=scale_factor,
            color="grey",
            pos=(ui_surface.get_width() * 0.5, 64 * scale_factor),
        )


class Scoreboard(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, game_surface):
        super().draw(game_surface)

    def draw_ui(self, ui_surface, scale_factor):
        super().draw_ui(ui_surface, scale_factor)
        render_text(
            screen=ui_surface,
            text="High Scores",
            font_name="zendots",
            font_size=24,
            scale_factor=scale_factor,
            pos=(ui_surface.get_width() * 0.5, 32 * scale_factor),
        )
        render_text(
            screen=ui_surface,
            text="scores go here",
            font_size=24,
            scale_factor=scale_factor,
            color="grey",
            pos=(ui_surface.get_width() * 0.5, 64 * scale_factor),
        )


class Credits(Screen):

    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.game.change_screen("Start")

    def update(self, dt):
        super().update(dt)

    def draw(self, game_surface):
        super().draw(game_surface)

    def draw_ui(self, ui_surface, scale_factor):
        super().draw_ui(ui_surface, scale_factor)
        render_text(
            screen=ui_surface,
            text="Credits",
            font_name="zendots",
            font_size=32,
            scale_factor=scale_factor,
            pos=(ui_surface.get_width() * 0.5, 32 * scale_factor),
        )
        render_text(
            screen=ui_surface,
            text="Credits go here",
            font_size=24,
            scale_factor=scale_factor,
            color="grey",
            pos=(ui_surface.get_width() * 0.5, 64 * scale_factor),
        )


class Thanks(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        super().handle_event(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.game.change_screen("Credits")

    def draw(self, game_surface):
        super().draw(game_surface)

    def draw_ui(self, ui_surface, scale_factor):
        super().draw_ui(ui_surface, scale_factor)
        render_text(
            screen=ui_surface,
            text="Thanks For Playing!",
            font_name="zendots",
            font_size=32,
            scale_factor=scale_factor,
            pos=(
                ui_surface.get_width() * 0.5,
                ui_surface.get_height() * 0.5 * scale_factor,
            ),
        )
        render_text(
            screen=ui_surface,
            text="[Enter] Credits",
            font_name="spacegrotesk_semibold",
            font_size=24,
            scale_factor=scale_factor,
            pos=(
                ui_surface.get_width() * 0.5,
                ui_surface.get_height() - 36 * scale_factor,
            ),
        )
