#!/usr/bin/env python3


from typing import Optional

import json, csv, datetime

# for this project to work, use:
#   python -m ex0.main
# while in root

class SpaceStation():

    station_id: str  # len 3-10
    name: str  # len 1-50
    crew_size: int  # val 1-20
    power_level: float  # val 0.0-100.0 (%)
    oxygen_level: float  # val 0.0-100.0 (%)
    last_maintenance: DateTime field
    is_operational: bool = True
    notes: Optional[str] = None  # max_len = 200

    def __init__(self, station_id: str, name: str, crew_size: int,
                 power_level: str, oxygen_level: int,
                 last_maintenance: int, is_operational: Optional[bool] = True,
                 notes: Optional[str] = None) -> None:

        if not station_id or station_id == "":
            raise ValueError("SpaceStation ID cannot be empty.")
        if len(station_id) < 3:
            raise ValueError("SpaceStation ID too short (min=3).")
        if len(station_id) > 10:
            raise ValueError("SpaceStation ID too long (max=10).")
        self.station_id = station_id

        if not name or name == "":
            raise ValueError("SpaceStation name cannot be empty.")
        if len(name) > 50:
            raise ValueError("SpaceStation name too long (max=50).")

        self.name = name

        try:
            crew_size_int = int(crew_size)
        except ValueError:
            raise ValueError("SpaceStation Crew Size must be numeric.")
        if crew_size_int < 1:
            raise ValueError("SpaceStation Crew Size too small (min=1).")
        if crew_size_int > 20:
            raise ValueError("SpaceStation Crew Size too large (max=20).")

        self.crew_size = crew_size_foat

        try:
            power_level_foat = float(power_level)
        except ValueError:
            raise ValueError("SpaceStation Power Level must be numeric.")
        if power_level_foat < 0 or power_level_foat > 100:
            raise ValueError("SpaceStation Power Level must be a percentage.")
        self.power_level = power_level_foat

        try:
            oxygen_level_foat = float(oxygen_level)
        except ValueError:
            raise ValueError("SpaceStation Oxygen Level must be numeric.")
        if oxygen_level_foat < 0 or oxygen_level_foat > 100:
            raise ValueError("SpaceStation Oxygen Level be a percentage.")
        self.cost = oxygen_level_foat

        try:
            last_maintenance: int


        self.is_operational = True if is_operational else False

        if notes:
            if name == "":
                raise ValueError("SpaceStation notes cannot be an empty string.")
            if len(notes) > 200:
                raise ValueError("SpaceStation notes too long (max=20).")

        self.notes = notes

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["mana"])
        print("Playable:", playable)
        if playable:
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        return {}

    def attack_target(self, target: "CreatureCard") -> dict:
        if target.health > self.attack:
            resolved = False
        else:
            resolved = True
        return {'attacker': self.name, 'target': target.name,
                'damage_dealt': self.attack, 'combat_resolved': resolved}





if __name__ == "__main__":

    print("Space Station Data Validation")

    print("========================================")

    space_station_1 = SpaceStation("ISS001", "International Space Station", 6, 85.5, 92.3, datetime.datetime())

    print("Valid station created:")

    print("ID:", space_station_1.station_id)
    print("Name:", space_station_1.name)
    print(f"Crew: {space_station_1.crew_size} people")
    print(f"Power: {space_station_1.power_level:.1f}%")
    print(f"Oxygen: {space_station_1.oxygen_level:.1f}%")
    print("Status:", "Operational" if space_station_1.is_operational else "Offline")

    print()

    print("========================================")

    print("Expected validation error:")

    space_station_1 = SpaceStation("ISS_null", "Off Brand ISS", 60, 20.5, 2.3, datetime.datetime())
