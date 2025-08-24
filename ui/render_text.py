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

    font = pygame.font.Font(font_name, font_size)
    text_surface = font.render(text, antialias, color)
    text_rect = text_surface.get_rect()

    match align:
        case "center":
            text_rect.center = pos
        case "topleft":
            text_rect.topleft = pos
        case "topright":
            text_rect.topright = pos
        case "bottomleft":
            text_rect.bottomleft = pos
        case "bottomright":
            text_rect.bottomright = pos
        case "midtop":
            text_rect.midtop = pos
        case "midbottom":
            text_rect.midbottom = pos
        case "midleft":
            text_rect.midleft = pos
        case "midright":
            text_rect.midright = pos
        case _:
            raise ValueError(
                "align must be one of: center, topleft, topright, bottomleft, bottomright, midtop, midbottom, midleft, midright"
            )
        
    screen.blit(text_surface, text_rect)
    
    return text_rect
