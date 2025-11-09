import pygame
from src.entities import (
    Player,
    AsteroidXL,
    AsteroidLG,
    AsteroidMD,
    AsteroidSM,
    EnemyDrone,
    EnemyShip,
    SubBoss,
    LevelBoss,
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
        self.boundary_handling_enabled = True
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

    def handle_boundaries(self, entity, action="kill"):
        if not self.boundary_handling_enabled:
            return

        play_area = self.gameplay.play_area_rect

        if action == "block":
            entity.position.x = max(
                play_area.left + entity.rect.width * 0.5,
                min(entity.position.x, play_area.right - entity.rect.width * 0.5),
            )
            entity.position.y = max(
                play_area.top + entity.rect.height * 0.5,
                min(entity.position.y, play_area.bottom - entity.rect.height * 0.5),
            )
        elif action == "kill" and (
            entity.rect.right < play_area.left
            or entity.rect.left > play_area.right
            or entity.rect.top > play_area.bottom
        ):
            entity.kill()

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
        "top_left_edge": (0.1, "top"),
        "top_far_left": (0.2, "top"),
        "top_left": (0.3, "top"),
        "top_center_left": (0.4, "top"),
        "top_center": (0.5, "top"),
        "top_center_right": (0.6, "top"),
        "top_right": (0.7, "top"),
        "top_far_right": (0.8, "top"),
        "top_right_edge": (0.9, "top"),
        "player_spawn": (0.5, "btm"),
    }

    entities = {
        "player": Player,
        "asteroid_xl": AsteroidXL,
        "asteroid_lg": AsteroidLG,
        "asteroid_md": AsteroidMD,
        "asteroid_sm": AsteroidSM,
        "enemy_drone": EnemyDrone,
        "enemy_ship": EnemyShip,
        "sub_boss": SubBoss,
        "level_boss": LevelBoss,
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

        if isinstance(self.location, str):
            offset_x, side_y = self.spawn_locations[self.location]
            offset_y = 128

            if side_y == "top":
                return pygame.Vector2(
                    play_area.left + (offset_x * play_area.width),
                    play_area.top - offset_y,
                )
            elif side_y == "btm":
                return pygame.Vector2(
                    play_area.left + (offset_x * play_area.width),
                    play_area.bottom,
                )

        elif isinstance(self.location, pygame.Vector2):
            # return self.location.copy()
            return self.location


class EventManager:

    def __init__(self, gameplay, events):
        self.gameplay = gameplay
        self.events = events
        self.current_index = 0
        self.current_event = None
        self.event_handlers = {
            "spawn_entity": self.handle_spawn_entity,
            "trigger_cutscene": self.handle_cutscene,
            "trigger_wave": self.handle_wave,
            "trigger_battle": self.handle_battle,
            "trigger_mission_complete": self.handle_mission_complete,
            "show_message": self.handle_message,
        }

    def start(self):
        print("Starting Event Queue")
        self.process_next()

    def process_next(self):
        if self.current_index >= len(self.events):
            print("Event queue complete")
            return

        self.current_event = self.events[self.current_index]
        event_type = self.current_event["type"]
        handler = self.event_handlers.get(event_type)

        if handler:
            print(f"Processing event {self.current_index}: {event_type}")
            handler(self.current_event)
        else:
            print(f"Unknown event type: {event_type}")
            self.on_event_complete()

    def on_event_complete(self):
        print(f"Event complete: {self.current_event['type']}")
        self.current_index += 1
        self.current_event = None
        self.process_next()

    def handle_spawn_entity(self, event):
        params = event.get("params", {})
        spawner = SpawnManager(
            self.gameplay,
            params["type"],
            params["location"],
            params.get("behaviors", []),
        )
        spawner.spawn_entity()
        self.on_event_complete()

    def handle_cutscene(self, event):
        params = event.get("params", {})
        self.gameplay.change_state(GameplayState.CUTSCENE)
        self.gameplay.cutscene_manager.start_cutscene(params["cutscene_id"])

    def handle_wave(self, event):
        params = event.get("params", {})
        self.gameplay.change_state(GameplayState.PLAY)
        self.gameplay.wave_manager.start_wave(params["wave_id"])

    def handle_battle(self, event):
        params = event.get("params", {})
        self.gameplay.change_state(GameplayState.PLAY)
        self.gameplay.battle_manager.start_battle(params["battle_id"])

    def handle_mission_complete(self, event):
        self.gameplay.change_state(GameplayState.MISSION_COMPLETE)

    def handle_message(self, event):
        params = event.get("params", {})
        self.gameplay.gameplay_ui.display_message(params["message_id"])


class CutsceneManager:
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.current_cutscene_id = None
        self.current_actions = None
        self.current_index = 0
        self.action_handlers = {
            "show_dialogue": self.handle_dialogue,
            "move_entity_to_loc": self.handle_move_entity_to_loc,
        }

    def start_cutscene(self, cutscene_id):
        from data.cutscenes import CUTSCENE

        print(f"Start Cutscene: {cutscene_id}")
        self.current_cutscene_id = cutscene_id
        self.current_actions = CUTSCENE.get(cutscene_id, [])
        self.current_index = 0
        self.process_next()

    def process_next(self):
        if self.current_index >= len(self.current_actions):
            print("Action queue complete")
            self.end_cutscene()
            return

        self.current_action = self.current_actions[self.current_index]
        action_type = self.current_action["action"]
        params = self.current_action.get("params", {})
        handler = self.action_handlers.get(action_type)

        if handler:
            print(f"Processing cutscene action {self.current_index}: {action_type}")
            handler(**params)
        else:
            print(f"Unknown action type: {action_type}")
            self.on_action_complete()

    def on_action_complete(self):
        print(f"Cutscene action complete: {self.current_action['action']}")
        self.current_index += 1
        self.process_next()

    def end_cutscene(self):
        print(f"End Cutscene: {self.current_cutscene_id}")
        self.current_cutscene_id = None
        self.current_actions = None
        self.current_index = 0
        self.gameplay.event_manager.on_event_complete()

    def handle_dialogue(self, dialogue_id):
        self.gameplay.gameplay_ui.display_dialogue(dialogue_id)

    def handle_move_entity_to_loc(self, entity_name, location, speed):
        entity = self.get_entity(entity_name)
        if entity is None:
            print(f"Entity '{entity_name}' not found")
            self.on_action_complete()
            return
        target_pos = pygame.Vector2(location["x"], location["y"])
        entity.scripted_movement(target_pos.x, target_pos.y, speed)

    def get_entity(self, entity_name):
        if entity_name == "player":
            return self.gameplay.player_group.sprite
        elif entity_name == "sub_boss":
            return self.gameplay.sub_boss_group.sprite
        elif entity_name == "level_boss":
            return self.gameplay.level_boss_group.sprite
        return None


class WaveManager:
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.current_wave = None
        self.wave_data = None
        self.wave_time = 0.0
        self.wave_index = 0

    def start_wave(self, wave_id):
        from data.enemy_waves import WAVE

        print(f"Starting wave: {wave_id}")
        self.current_wave = wave_id
        self.wave_data = WAVE.get(wave_id, [])

    def process_wave(self):
        if not self.wave_data:
            return

        while (
            self.wave_index < len(self.wave_data)
            and self.wave_time >= self.wave_data[self.wave_index]["time"]
        ):
            spawn_event = self.wave_data[self.wave_index]
            self.spawn_enemy(spawn_event)
            self.wave_index += 1

    def spawn_enemy(self, spawn_event):
        spawner = SpawnManager(
            self.gameplay,
            spawn_event["type"],
            spawn_event["location"],
            spawn_event.get("behaviors", []),
        )
        spawner.spawn_entity()

    def is_wave_complete(self):
        all_spawns_complete = self.wave_index >= len(self.wave_data)
        all_enemies_defeated = (
            len(self.gameplay.asteroids) == 0
            and len(self.gameplay.enemy_drones) == 0
            and len(self.gameplay.enemy_ships) == 0
        )
        return all_spawns_complete and all_enemies_defeated

    def end_wave(self):
        print(f"Wave Complete: {self.current_wave}")
        self.current_wave = None
        self.wave_data = None
        self.wave_time = 0.0
        self.wave_index = 0
        self.gameplay.event_manager.on_event_complete()

    def update(self, dt):
        if not self.wave_data:
            return

        self.wave_time += dt
        self.process_wave()

        if self.is_wave_complete():
            self.end_wave()


class BattleManager:
    def __init__(self, gameplay):
        self.gameplay = gameplay
        self.current_battle = None
        self.battle_entity = None

    def start_battle(self, battle_id):
        if battle_id == "sub_boss":
            self.battle_entity = self.gameplay.sub_boss_group.sprite
        elif battle_id == "level_boss":
            self.battle_entity = self.gameplay.level_boss_group.sprite
        else:
            print(f"Warning: Battle entity for {battle_id} not found!")

    def check_battle_complete(self):
        if self.battle_entity and not self.battle_entity.alive():
            self.end_battle()

    def end_battle(self):
        print(f"Ending battle: {self.battle_id}")
        self.battle_entity = None
        self.current_battle = None
        self.gameplay.event_manager.on_event_complete()

    def update(self, dt):
        if self.battle_entity:
            self.check_battle_complete()


class ScoreManager:

    def __init__(self, score_store):
        self.score_store = score_store
        self.score = 0
        self.multiplier = SCORING["initial_multiplier"]
        self.streak_meter = SCORING["initial_streak_meter"]
        self.streak_meter_threshold = SCORING["streak_threshold_base"]
        self.streak_meter_decay_amount = SCORING["streak_decay_base"]
        self.streak_meter_delay_decay_timer = 0

    def handle_score(self, amount):
        if amount < 0:
            self.score += amount
        else:
            self.score += amount * self.multiplier
            self.streak_meter_delay_decay_timer = SCORING["streak_delay"]

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
