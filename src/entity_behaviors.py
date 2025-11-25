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
