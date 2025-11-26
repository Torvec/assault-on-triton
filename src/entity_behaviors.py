import math
import pygame
from src.entities import DIRECTION_DOWN, EnemyShot


def move_straight(entity, angle=0, velocity_factor=1.0, dt=0):
    direction = DIRECTION_DOWN.rotate(angle)

    if not hasattr(entity, "_angle_set"):
        entity.velocity = direction * entity.speed * velocity_factor
        entity._angle_set = True
    entity.position += entity.velocity * dt


def move_to_location(entity, x, y, speed, dt):
    target = pygame.Vector2(x, y)
    direction = target - entity.position
    distance = direction.length()

    if distance < 5:  # Threshold to prevent jittering
        entity.position = target.copy()
        entity.velocity = pygame.Vector2(0, 0)
        if not hasattr(entity, "_location_reached"):
            entity._location_reached = True
            entity.gameplay.cutscene_manager.on_action_complete()
        return

    if distance > 0:
        direction.normalize_ip()
        entity.velocity = direction * speed
        entity.position += entity.velocity * dt


def move_square_wave(entity, v_dist, h_dist, init_horiz_direction, v_speed, h_speed, dt):
    directions = {
        "left": -1,
        "right": 1
    }

    if not hasattr(entity, "_horiz_direction"):
        entity._horiz_dirction = directions[init_horiz_direction]

    """
    Switch direction: vertical (down only), horizontal (left and right)
        Vertical to Horizontal switch happens when v_dist reached
        Horizontal to Vertical switch happens when h_dist reached
        Horizontal direction switches after h_dist reached also (left becomes right, right becomes left)
    Separate speeds for vertical and horizontal movement (can be equal)

    """


def move_sine_wave(entity, frequency, amplitude, speed, dt):
    if not hasattr(entity, "_sine_time"):
        entity._sine_time = 0

    entity._sine_time += dt

    vx = math.sin(entity._sine_time * frequency) * amplitude
    vy = speed
    entity.velocity = pygame.Vector2(vx, vy)
    entity.position += entity.velocity * dt


def move_saw_wave(entity, v_speed, h_speed, init_direction, dt):
    directions = {
        "left": -1,
        "right": 1,
    }
    if not hasattr(entity, "_saw_dir"):
        entity._saw_dir = directions[init_direction]

    if entity.position.x <= 0:
        entity._saw_dir = directions["right"]
    elif entity.position.x >= entity.gameplay.play_area_rect.width:
        entity._saw_dir = directions["left"]

    entity.velocity = pygame.Vector2(h_speed * entity._saw_dir, v_speed)
    entity.position += entity.velocity * dt


def move_arc(entity, pivot_point, direction, speed, dt):
    pass


def move_circular(entity, radius_x, radius_y, center, direction, speed, dt):
    pass


def move_side_to_side(entity, speed, dt):
    if entity.position.x == entity.gameplay.play_area_rect.width:
        entity.position -= entity.velocity * speed * dt
    elif entity.position.x == 0:
        entity.position += entity.velocity * speed * dt


def rotate_constantly(entity, dt):
    entity.rotation += entity.rotation_speed * dt


def shoot(entity, dt):
    if entity.shoot_timer > 0:
        return

    entity.shoot_timer = entity.shoot_cooldown

    shot_pos = entity.position + DIRECTION_DOWN * entity.rect.height // 2

    shot_l = EnemyShot(
        shot_pos.x - entity.shot_offset_pos, shot_pos.y, entity.gameplay, entity
    )
    shot_r = EnemyShot(
        shot_pos.x + entity.shot_offset_pos, shot_pos.y, entity.gameplay, entity
    )
    shot_l.velocity = DIRECTION_DOWN * shot_l.speed
    shot_r.velocity = DIRECTION_DOWN * shot_r.speed
    shot_l.sound()
