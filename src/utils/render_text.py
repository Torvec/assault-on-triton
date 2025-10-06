import pygame
from src.config.assets import FONTS


def render_text(
    screen,
    text,
    font_size=36,
    color="white",
    pos=(0, 0),
    align="center",
    font_name=None,
    antialias=False,
):

    if font_name is None:
        font_path = None
    elif font_name in FONTS:
        font_path = FONTS[font_name]
    else:
        raise ValueError(
            f"Unknown font_name '{font_name}'. Available fonts: {', '.join(FONTS.keys())}"
        )

    font = pygame.font.Font(font_path, font_size)
    text_surface = font.render(text, antialias, color)
    text_rect = text_surface.get_rect()

    align_map = {
        "center": "center",
        "topleft": "topleft",
        "topright": "topright",
        "bottomleft": "bottomleft",
        "bottomright": "bottomright",
        "midtop": "midtop",
        "midbottom": "midbottom",
        "midleft": "midleft",
        "midright": "midright",
    }
    if align in align_map:
        setattr(text_rect, align_map[align], pos)
    else:
        raise ValueError(f"align must be one of: {', '.join(align_map.keys())}")

    screen.blit(text_surface, text_rect)

    return text_rect
