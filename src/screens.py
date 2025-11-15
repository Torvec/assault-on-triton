import sys
import pygame
from src.render_text import render_text


class Screen:

    def __init__(self, game):
        self.game = game
        self.updateable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.backgrounds = []

    def handle_event(self, events):
        pass

    def update(self, dt):
        for bg in self.backgrounds:
            bg.update(dt)
        self.updateable.update(dt)

    def draw(self, display_surface, game_surface):
        display_surface.fill("black")
        game_surface.fill("#0c0c12")

        for bg in self.backgrounds:
            bg.draw(game_surface)

        for obj in self.drawable:
            obj.draw(game_surface)


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

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="ASSAULT",
            font_name="zendots",
            font_size=84,
            antialias=True,
            pos=(
                game_surface.get_rect().center[0],
                game_surface.get_rect().center[1] - 188,
            ),
            align="midbottom",
        )
        render_text(
            screen=game_surface,
            text="ON",
            font_name="zendots",
            font_size=72,
            antialias=True,
            pos=(
                game_surface.get_rect().center[0],
                game_surface.get_rect().center[1] - 84 - 32,
            ),
            align="midbottom",
        )
        render_text(
            screen=game_surface,
            text="TRITON",
            font_name="zendots",
            font_size=84,
            antialias=True,
            pos=(
                game_surface.get_rect().center[0],
                game_surface.get_rect().center[1] - 32,
            ),
            align="midbottom",
        )
        menu_rect = pygame.Rect(
            0, 0, game_surface.get_width() * 0.75, game_surface.get_height() * 0.25
        )
        menu_rect.midtop = game_surface.get_rect().center
        pygame.draw.rect(game_surface, "grey4", menu_rect, border_radius=24)
        pygame.draw.rect(game_surface, "grey70", menu_rect, width=4, border_radius=24)
        for i, item in enumerate(self.menu_items):
            render_text(
                screen=game_surface,
                text=item,
                font_name="spacegrotesk_semibold",
                font_size=32,
                color="grey",
                pos=(menu_rect.midtop[0], menu_rect.midtop[1] + 8 + (i * 48)),
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

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="Options",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )
        render_text(
            screen=game_surface,
            text="scores go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
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

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="High Scores",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )
        render_text(
            screen=game_surface,
            text="scores go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
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

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="Credits",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, 64),
        )
        render_text(
            screen=game_surface,
            text="Credits go here",
            font_size=32,
            color="grey",
            pos=(game_surface.get_width() * 0.5, 128),
        )


class Thanks(Screen):
    def __init__(self, game):
        super().__init__(game)

    def handle_event(self, events):
        super().handle_event(events)
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.game.change_screen("Credits")

    def draw(self, display_surface, game_surface):
        super().draw(display_surface, game_surface)
        render_text(
            screen=game_surface,
            text="Thanks For Playing!",
            font_name="zendots",
            font_size=48,
            pos=(game_surface.get_width() * 0.5, game_surface.get_height() * 0.5),
        )
        render_text(
            screen=game_surface,
            text="[Enter] Credits",
            font_name="spacegrotesk_semibold",
            font_size=32,
            pos=(game_surface.get_width() * 0.5, game_surface.get_height() - 36),
        )
