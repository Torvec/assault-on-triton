import pygame


def render_text(**kwargs):
    screen = kwargs["screen"]
    text = kwargs["text"]
    font_size = kwargs.get("font_size", 36)
    color = kwargs.get("color", "white")
    pos = kwargs.get("pos", (0, 0))
    align = kwargs.get("align", "center")
    font_name = kwargs.get("font_name", None)
    antialias = kwargs.get("antialias", False)

    font_map = {
        None: None,
        "spacegrotesk_bold": "assets/spacegrotesk_bold.ttf",
        "spacegrotesk_light": "assets/spacegrotesk_light.ttf",
        "spacegrotesk_medium": "assets/spacegrotesk_medium.ttf",
        "spacegrotesk_regular": "assets/spacegrotesk_regular.ttf",
        "spacegrotesk_semibold": "assets/spacegrotesk_semibold.ttf",
        "zendots": "assets/zendots_regular.ttf",
    }
    if font_name in font_map:
        font_path = font_map[font_name]
    else:
        raise ValueError(f"Unknown font_name '{font_name}'.")

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
