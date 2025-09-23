import pygame


def move_straight(entity, dt):
    entity.position.y += entity.speed * dt


def move_angled(entity, dt, **kwargs):
    angle = kwargs.get("angle", 0)
    velocity_factor = kwargs.get("velocity_factor", 1.0)

    # Sets up a flag so that the changing of direction only happens once and not continuously
    if not hasattr(entity, "_angled_velocity_set"):
        base_velocity = (
            pygame.Vector2(0, 1) * entity.speed
        )
        entity.velocity = base_velocity.rotate(angle) * velocity_factor
        entity._angled_velocity_set = True
        
    entity.position += entity.velocity * dt


def rotate_constantly(entity, dt):
    entity.rotation += entity.rotation_speed * dt
