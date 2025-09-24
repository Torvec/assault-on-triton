import pygame


def single_formation(fwd_pos, count, spacing):
    return [fwd_pos]


def wall_formation(fwd_pos, count, spacing):
    positions = []

    for i in range(count):
        offset_x = (i - count // 2) * spacing
        positions.append(fwd_pos + pygame.Vector2(offset_x, 0))

    return positions


def column_formation(fwd_pos, count, spacing):
    positions = []

    max_forward_offset = (count // 2) * spacing
    adjusted_center = pygame.Vector2(fwd_pos.x, fwd_pos.y - max_forward_offset)

    for i in range(count):
        offset_y = (i - count // 2) * spacing
        positions.append(adjusted_center + pygame.Vector2(0, offset_y))

    return positions


def echelon_l_formation(fwd_pos, count, spacing):
    positions = []

    max_forward_offset = (count // 2) * spacing * 0.7
    adjusted_center = pygame.Vector2(fwd_pos.x, fwd_pos.y - max_forward_offset)

    for i in range(count):
        offset = (i - count // 2) * spacing * 0.7
        positions.append(adjusted_center + pygame.Vector2(-offset, offset))

    return positions


def echelon_r_formation(fwd_pos, count, spacing):
    positions = []

    max_forward_offset = (count // 2) * spacing * 0.7
    adjusted_center = pygame.Vector2(fwd_pos.x, fwd_pos.y - max_forward_offset)

    for i in range(count):
        offset = (i - count // 2) * spacing * 0.7
        positions.append(adjusted_center + pygame.Vector2(offset, offset))

    return positions


def reverse_v_formation(fwd_pos, count, spacing):
    positions = []

    pairs = (count - 1) // 2
    max_offset = pairs * spacing * 0.5
    adjusted_center = pygame.Vector2(fwd_pos.x, fwd_pos.y - max_offset)

    positions.append(adjusted_center)

    for i in range(1, pairs + 1):
        distance = i * spacing
        positions.append(adjusted_center + pygame.Vector2(-distance, distance * 0.5))
        positions.append(adjusted_center + pygame.Vector2(distance, distance * 0.5))

    if count % 2 == 0:
        positions.append(adjusted_center + pygame.Vector2(0, spacing * 1.5))

    return positions


def forward_v_formation(fwd_pos, count, spacing):
    positions = []

    positions.append(fwd_pos)

    pairs = (count - 1) // 2
    for i in range(1, pairs + 1):
        distance = i * spacing
        positions.append(fwd_pos + pygame.Vector2(-distance, -distance * 0.5))
        positions.append(fwd_pos + pygame.Vector2(distance, -distance * 0.5))

    if count % 2 == 0:
        positions.append(fwd_pos + pygame.Vector2(0, -spacing * 1.5))

    return positions


def diamond_formation(fwd_pos, count, spacing):
    positions = []

    formation_front = pygame.Vector2(fwd_pos.x, fwd_pos.y - spacing)

    offsets = [
        pygame.Vector2(0, -spacing),  # Top
        pygame.Vector2(-spacing, 0),  # Left
        pygame.Vector2(spacing, 0),  # Right
        pygame.Vector2(0, spacing),  # Bottom (will be at fwd_pos)
    ]

    for offset in offsets:
        positions.append(formation_front + offset)

    return positions


def circle_formation(fwd_pos, count, spacing):
    positions = []
    radius = spacing * 1.5
    adjusted_center = pygame.Vector2(fwd_pos.x, fwd_pos.y - radius)

    for i in range(count):
        angle = (i / count) * 360
        offset = pygame.Vector2(radius, 0).rotate(angle)
        positions.append(adjusted_center + offset)

    return positions


def x_formation(fwd_pos, count, spacing):
    positions = []

    formation_front = pygame.Vector2(fwd_pos.x, fwd_pos.y - spacing)

    offsets = [
        pygame.Vector2(-spacing, -spacing),  # Top Left
        pygame.Vector2(spacing, -spacing),  # Top Right
        pygame.Vector2(0, 0),  # Center
        pygame.Vector2(-spacing, spacing),  # Bottom Left
        pygame.Vector2(spacing, spacing),  # Bottom Right
    ]

    for offset in offsets:
        positions.append(formation_front + offset)

    return positions
