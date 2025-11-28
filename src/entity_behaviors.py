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


def move_square_wave(entity, x_dist, y_dist, init_horizontal_dir, x_speed, y_speed, dt):
    directions = {"left": -1, "right": 1}
    axis = ("x", "y")

    if not hasattr(entity, "_sqwave_state"):
        entity._sqwave_state = {
            "current_y_dist": 0,
            "current_x_dist": 0,
            "current_horizontal_dir": directions[init_horizontal_dir],
            "current_axis": axis[1],
        }
    state = entity._sqwave_state

    # y axis movement
    if state["current_axis"] == axis[1]:
        state["current_y_dist"] += y_speed * dt
        entity.velocity = DIRECTION_DOWN * y_speed
        if state["current_y_dist"] >= y_dist:
            state["current_axis"] = axis[0]
            state["current_y_dist"] = 0

    # x axis movement
    elif state["current_axis"] == axis[0]:
        state["current_x_dist"] += x_speed * dt
        entity.velocity = pygame.Vector2(state["current_horizontal_dir"] * x_speed, 0)
        if state["current_x_dist"] >= x_dist:
            state["current_axis"] = axis[1]
            state["current_horizontal_dir"] *= -1
            state["current_x_dist"] = 0

    entity.position += entity.velocity * dt


def move_sine_wave(entity, frequency, amplitude, speed, dt):
    if not hasattr(entity, "_sine_time"):
        entity._sine_time = 0

    entity._sine_time += dt

    vx = math.sin(entity._sine_time * frequency) * amplitude
    vy = speed
    entity.velocity = pygame.Vector2(vx, vy)
    entity.position += entity.velocity * dt


def move_saw_wave(entity, x_speed, y_speed, init_direction, dt):
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

    entity.velocity = pygame.Vector2(x_speed * entity._saw_dir, y_speed)
    entity.position += entity.velocity * dt


def move_arc(entity, pivot_point, direction, speed, dt):
    directions = {"ccw": -90, "cw": 90}
    radius = entity.position - pivot_point
    tangent_direction = radius.rotate(directions[direction]).normalize()
    entity.velocity = tangent_direction * speed
    entity.position += entity.velocity * dt


def move_circular(entity, radius_x, radius_y, center, direction, speed, dt):

    if not hasattr(entity, "_circle_time"):
        entity._circle_time = 0

    angular_speed = speed / max(radius_x, radius_y)
    directions = {
        "cw": angular_speed,
        "ccw": -angular_speed
    }

    entity._circle_time += dt * directions[direction]
    angle = entity._circle_time

    x = center[0] + radius_x * math.cos(angle)
    y = center[1] + radius_y * math.sin(angle)
    entity.position = pygame.Vector2(x, y)


def move_side_to_side(entity, speed, dt):
    if entity.position.x == entity.gameplay.play_area_rect.width:
        entity.position -= entity.velocity * speed * dt
    elif entity.position.x == 0:
        entity.position += entity.velocity * speed * dt


def rotate_constantly(entity, dt):
    entity.rotation += entity.rotation_speed * dt


def shoot(entity, dt):
    """
    - Change this to shift responsibility from the entity to this behavior as far as fire rate goes
    - Change this to be able to accomodate at least one and more than two shot origins, 
    the entity will define where the shots originate from and this will create them in the correct locations accordingly
    - define a method in the entity class to instantiate the shot instead of doing it here so this module doesn't require importing the EnemyShot
    """
    if entity.shoot_timer > 0:
        return

    entity.shoot_timer = entity.shoot_cooldown

    shot_pos = entity.position + DIRECTION_DOWN * entity.rect.height * 0.5
    shot_l = EnemyShot(
        shot_pos.x - entity.shot_offset_pos, shot_pos.y, entity.gameplay, entity
    )
    shot_r = EnemyShot(
        shot_pos.x + entity.shot_offset_pos, shot_pos.y, entity.gameplay, entity
    )
    shot_l.velocity = DIRECTION_DOWN * shot_l.speed
    shot_r.velocity = DIRECTION_DOWN * shot_r.speed
    shot_l.sound()
