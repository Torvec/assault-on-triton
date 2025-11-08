import pygame
from src.entities import (
    Player,
    AsteroidXL,
    AsteroidLG,
    AsteroidMD,
    AsteroidSM,
    EnemyDrone,
    EnemyShip,
    HealthPickup,
    ExtraLifePickup,
    PowerLevelPickup,
    OverdrivePickup,
    BombAmmoPickup,
    InvulnerabilityPickup,
)
from src.gameplay_states import GameplayState
from data.settings import SCORING


class CollisionManager:

    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.sprite_groups = {
            "asteroids": self.gameplay.asteroids,
            "enemy_drones": self.gameplay.enemy_drones,
            "enemy_ships": self.gameplay.enemy_ships,
            "missiles": self.gameplay.missiles,
            "shots": self.gameplay.shots,
            "bombs": self.gameplay.bombs,
            "explosions": self.gameplay.explosions,
            "pickups": self.gameplay.pickups,
        }

    @property
    def player(self):
        """Dynamically get the player sprite from the player_group."""
        return self.gameplay.player_group.sprite

    def handle_shots(self, shot_type, colliders):
        for shot in shot_type:
            shot_v_colliders = shot.collides_with(colliders)
            if shot_v_colliders:
                for collider in shot_v_colliders:
                    collider.take_damage(shot.damage)
                    shot.kill()

    def handle_explosives(self, explosive_type, colliders):
        for explosive in explosive_type:
            if explosive.collides_with(colliders):
                explosive.explode()

    def handle_explosions(self, explosion_type, colliders):
        for explosion in explosion_type:
            explosion_v_colliders = explosion.collides_with(colliders)
            if explosion_v_colliders:
                for collider in explosion_v_colliders:
                    collider.take_damage(explosion.damage)

    def filter_by_owner(self, group, is_player=True):
        if is_player:
            return [e for e in self.sprite_groups[group] if e.owner == self.player]
        return [e for e in self.sprite_groups[group] if e.owner != self.player]

    def update(self):
        if not self.player:
            return

        self.hostiles = [
            *self.sprite_groups["asteroids"],
            *self.sprite_groups["enemy_drones"],
            *self.sprite_groups["enemy_ships"],
        ]
        if self.hostiles:
            player_v_hostiles = self.player.collides_with(self.hostiles)
            if player_v_hostiles:
                for hostile in player_v_hostiles:
                    self.player.take_damage(5)
                    hostile.take_damage(1)
        if self.sprite_groups["pickups"]:
            player_v_pickups = self.player.collides_with(self.sprite_groups["pickups"])
            if player_v_pickups:
                for pickup in player_v_pickups:
                    pickup.apply()
        if not any(
            [
                self.sprite_groups["shots"],
                self.sprite_groups["bombs"],
                self.sprite_groups["missiles"],
                self.sprite_groups["explosions"],
            ]
        ):
            return
        player_shots = self.filter_by_owner("shots", is_player=True)
        enemy_shots = self.filter_by_owner("shots", is_player=False)
        player_bombs = self.filter_by_owner("bombs", is_player=True)
        enemy_bombs = self.filter_by_owner("bombs", is_player=False)
        player_missiles = self.filter_by_owner("missiles", is_player=True)
        enemy_missiles = self.filter_by_owner("missiles", is_player=False)
        player_explosions = self.filter_by_owner("explosions", is_player=True)
        enemy_explosions = self.filter_by_owner("explosions", is_player=False)
        player_bomb_colliders = [
            *self.hostiles,
            *enemy_shots,
            *enemy_bombs,
            *enemy_missiles,
            *enemy_explosions,
        ]
        enemy_bomb_colliders = [
            self.player,
            *player_shots,
            *player_bombs,
            *player_missiles,
            *player_explosions,
        ]
        enemy_missile_colliders = [self.player, *player_bombs, *player_explosions]
        self.handle_shots(player_shots, self.hostiles)
        self.handle_shots(enemy_shots, [self.player])
        self.handle_explosives(player_bombs, player_bomb_colliders)
        self.handle_explosives(enemy_bombs, enemy_bomb_colliders)
        self.handle_explosives(enemy_missiles, enemy_missile_colliders)
        self.handle_explosions(player_explosions, self.hostiles)
        self.handle_explosions(enemy_explosions, [self.player])


class SpawnManager:

    spawn_locations = {
        "left_edge": 0.1,
        "far_left": 0.2,
        "left": 0.3,
        "center_left": 0.4,
        "center": 0.5,
        "center_right": 0.6,
        "right": 0.7,
        "far_right": 0.8,
        "right_edge": 0.9,
        "player_spawn": 0,
    }

    entities = {
        "player": Player,
        "asteroid_xl": AsteroidXL,
        "asteroid_lg": AsteroidLG,
        "asteroid_md": AsteroidMD,
        "asteroid_sm": AsteroidSM,
        "enemy_drone": EnemyDrone,
        "enemy_ship": EnemyShip,
        "health_pickup": HealthPickup,
        "extra_life_pickup": ExtraLifePickup,
        "power_level_pickup": PowerLevelPickup,
        "overdrive_pickup": OverdrivePickup,
        "bomb_ammo_pickup": BombAmmoPickup,
        "invulnerability_pickup": InvulnerabilityPickup,
    }

    def __init__(self, gameplay, entity_name, location, behaviors):
        self.gameplay = gameplay
        self.entity_name = entity_name
        self.location = location
        self.behaviors = behaviors

    def spawn_entity(self):
        position = self.calc_position()
        entity_class = self.entities[self.entity_name]
        entity = entity_class(position.x, position.y, self.gameplay)
        if self.behaviors:
            for behavior in self.behaviors:
                entity.behaviors.append(behavior)

    def calc_position(self):
        play_area = self.gameplay.play_area_rect

        if isinstance(self.location, pygame.Vector2):
            return self.location.copy()

        elif isinstance(self.location, dict):
            x = self.location["x"]
            y = self.location["y"]
            return pygame.Vector2(x, y)

        elif self.location == "player_spawn":
            return pygame.Vector2(
                play_area.width * 0.5,
                play_area.height,
            )

        elif isinstance(self.location, str):
            offset_x = self.spawn_locations[self.location]
            return pygame.Vector2(
                play_area.left + (offset_x * play_area.width),
                play_area.top - 128,
            )

        return pygame.Vector2(play_area.centerx, play_area.top - 128)


class EventManager:

    def __init__(self, gameplay, timeline):
        self.gameplay = gameplay
        self.timeline = timeline
        self.timeline_time = 0.0
        self.timeline_index = 0
        self.is_paused = False
        self.event_handlers = {
            "trigger_cutscene": self.trigger_cutscene,
            "trigger_waves": self.trigger_waves,
            "trigger_battle": self.trigger_battle,
            "trigger_mission_complete": self.trigger_mission_complete,
            "spawn_entity": self.spawn_entity,
            "show_message": self.show_message,
            "show_dialogue": self.show_dialogue,
        }

    def trigger_cutscene(self, cutscene_id):
        self.gameplay.change_state(GameplayState.CUTSCENE)
        self.gameplay.cutscene_manager.start_cutscene(cutscene_id)

    def trigger_waves(self):
        play_state = self.gameplay.states[GameplayState.PLAY]
        play_state.is_battle = False
        self.gameplay.change_state(GameplayState.PLAY)

    def trigger_battle(self):
        play_state = self.gameplay.states[GameplayState.PLAY]
        play_state.is_battle = True
        self.gameplay.change_state(GameplayState.PLAY)

    def trigger_mission_complete(self):
        self.gameplay.change_state(GameplayState.MISSION_COMPLETE)

    def spawn_entity(self, type, location, behaviors):
        spawner = SpawnManager(self.gameplay, type, location, behaviors)
        spawner.spawn_entity()

    def show_message(self, message_id):
        self.gameplay.gameplay_ui.display_message(message_id)

    def show_dialogue(self, dialogue_id):
        self.gameplay.gameplay_ui.display_dialogue(dialogue_id)

    def handle_event(self, event):
        event_name = event["event"]
        params = event.get("params", {})
        handler = self.event_handlers.get(event_name)
        if handler:
            handler(**params)
        else:
            print(f"Unknown event type: {event_name}")

    def process_timeline(self):
        while (
            self.timeline_index < len(self.timeline)
            and self.timeline_time >= self.timeline[self.timeline_index]["time"]
        ):
            current_event = self.timeline[self.timeline_index]
            self.handle_event(current_event)
            self.timeline_index += 1

    def update(self, dt):
        if self.is_paused:
            return

        self.timeline_time += dt
        self.process_timeline()


class ScoreManager:

    def __init__(self, score_store):
        self.data = SCORING
        self.score_store = score_store
        self.score = 0
        self.multiplier = self.data["initial_multiplier"]
        self.streak_meter = self.data["initial_streak_meter"]
        self.streak_meter_threshold = self.data["streak_threshold_base"]
        self.streak_meter_decay_amount = self.data["streak_decay_base"]
        self.streak_meter_delay_decay_timer = 0

    def handle_score(self, amount):
        if amount < 0:
            self.score += amount
        else:
            self.score += amount * self.multiplier
            self.streak_meter_delay_decay_timer = self.data["streak_delay"]

    def handle_streak_meter_inc(self, amount):
        self.streak_meter += amount
        if self.streak_meter > self.streak_meter_threshold:
            remainder = self.streak_meter - self.streak_meter_threshold
            self.streak_meter = 0
            self.streak_meter += remainder
            self.handle_multiplier(1)

    def handle_streak_meter_dec(self):
        if self.multiplier > 1:
            self.handle_multiplier(-1)
        self.streak_meter = 0

    def handle_multiplier(self, num):
        if num < 0:
            self.streak_meter_threshold /= self.multiplier
            self.streak_meter_decay_amount /= self.multiplier
            self.multiplier = max(1, self.multiplier + num)
        else:
            self.multiplier += num
            self.streak_meter_threshold *= self.multiplier
            self.streak_meter_decay_amount *= self.multiplier

    def update_streak_meter_decay(self, dt):
        # Delay timer is triggered when the player increases the score in handle_score, delay timer can't go below 0
        if self.streak_meter_delay_decay_timer > 0:
            self.streak_meter_delay_decay_timer -= dt
            if self.streak_meter_delay_decay_timer < 0:
                self.streak_meter_delay_decay_timer = 0

        # When the delay timer is finished, the streak starts to decay based off of a set amount per frame
        if (
            self.streak_meter > 0 or self.multiplier > 1
        ) and self.streak_meter_delay_decay_timer == 0:
            self.streak_meter -= self.streak_meter_decay_amount * dt

            # If the meter goes equal or below 0 and the multiplier is greater than 1 it will decrease the multiplier and handle the threshold as well as set the meter back to 100% to continue decreasing until it hits 0 at multiplier x1
            if self.streak_meter <= 0:
                if self.multiplier > 1:
                    self.streak_meter_threshold /= self.multiplier
                    self.streak_meter_decay_amount /= self.multiplier
                    self.multiplier -= 1
                    self.streak_meter = self.streak_meter_threshold
                else:
                    self.streak_meter = 0

    def store_score(self, score):
        self.score_store.current_score = score
