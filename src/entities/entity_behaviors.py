from src.entities.entity_directions import DIRECTION_DOWN


def move_straight(entity, dt):
    entity.position += DIRECTION_DOWN * entity.speed * dt


def move_angled(entity, dt, **kwargs):
    angle = kwargs.get("angle", 0)
    velocity_factor = kwargs.get("velocity_factor", 1.0)

    # Sets up a flag so that the changing of direction only happens once and not continuously
    if not hasattr(entity, "_angled_velocity_set"):

        base_velocity = DIRECTION_DOWN * entity.speed
        entity.velocity = base_velocity.rotate(angle) * velocity_factor
        entity._angled_velocity_set = True

    entity.position += entity.velocity * dt


def rotate_constantly(entity, dt):
    entity.rotation += entity.rotation_speed * dt


def shoot(entity, dt, **kwargs):
    if entity.shoot_timer > 0:
        return

    entity.shoot_timer = entity.shoot_cooldown

    shot_pos = entity.position + DIRECTION_DOWN * entity.rect.height // 2
    from src.entities.projectile import EnemyShot

    shot_l = EnemyShot(
        shot_pos.x - entity.shot_offset_pos, shot_pos.y, entity.game_play, entity
    )
    shot_r = EnemyShot(
        shot_pos.x + entity.shot_offset_pos, shot_pos.y, entity.game_play, entity
    )
    shot_l.velocity = DIRECTION_DOWN * shot_l.speed
    shot_r.velocity = DIRECTION_DOWN * shot_r.speed
    shot_l.sound()
