#!/usr/bin/env python3


from typing import Optional

# import json, csv

from datetime import datetime, date

# for this project to work, use:
#   python -m ex0.main
# while in root


class SpaceStation():

    station_id: str  # len 3-10
    name: str  # len 1-50
    crew_size: int  # val 1-20
    power_level: float  # val 0.0-100.0 (%)
    oxygen_level: float  # val 0.0-100.0 (%)
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = None  # max_len = 200

    def __init__(self, station_id: str, name: str, crew_size: int,
                 power_level: float, oxygen_level: float,
                 last_maintenance: datetime, is_operational: bool = True,
                 notes: Optional[str] = None) -> None:

        class_name = self.__class__.__name__ + " "

        try:

            self.station_id = self.str_len_check(
                class_name + "ID", station_id, 3, 10)

            self.name = self.str_len_check(
                class_name + "Crew Size", name, 1, 50)

            self.crew_size = self.int_val_check(
                class_name + "Crew Size", crew_size, 1, 20)

            self.power_level = self.float_val_check(
                class_name + "Power Level", power_level, 0, 100)

            self.oxygen_level = self.float_val_check(
                class_name + "Power Level", oxygen_level, 0, 100)

            self.last_maintenance = last_maintenance

            self.is_operational = True if is_operational else False

            if notes:
                self.notes = self.str_len_check(
                    class_name + "notes", notes, 0, 200)
            else:
                self.notes = None

        except ValueError as e:
            print(e)

    @staticmethod
    def str_len_check(field_name: str, field_input: str, min: int, max: int
                      ) -> str:
        if not field_input or field_input == "":
            raise ValueError(f"{field_name} cannot be empty.")
        if len(field_input) < min:
            raise ValueError(f"{field_name} too short (min={min}).")
        if len(field_input) > max:
            raise ValueError(f"{field_name} too long (max={max}).")

        return field_input

    @staticmethod
    def int_val_check(field_name: str, field_input: int, min: int, max: int
                      ) -> int:
        try:
            field_int = int(field_input)
        except ValueError:
            raise ValueError(f"{field_name} must be numeric.")
        if field_int < min:
            if min == 0:
                raise ValueError(f"{field_name} must be positive.")
            raise ValueError(f"{field_name} too short (min={min}).")
        if field_int > max:
            if max == 0:
                raise ValueError(f"{field_name} must be negative.")
            raise ValueError(f"{field_name} too long (max={max}).")

        return field_int

    @staticmethod
    def float_val_check(field_name: str, field_input: float, min: int, max: int
                        ) -> float:
        try:
            field_float = float(field_input)
        except ValueError:
            raise ValueError(f"{field_name} must be numeric.")
        if (min == 0 and max == 100
                and field_float < min and field_float > max):
            raise ValueError("SpaceStation Oxygen Level be a percentage.")
        if field_float < min:
            if min == 0:
                raise ValueError(f"{field_name} must be positive.")
            raise ValueError(f"{field_name} too small (min={min}).")
        if field_float > max:
            if max == 0:
                raise ValueError(f"{field_name} must be negative.")
            raise ValueError(f"{field_name} too large (max={max}).")

        return field_float


if __name__ == "__main__":

    print("Space Station Data Validation")

    print("========================================")

    space_station_1 = SpaceStation(
        "ISS001", "International Space Station",
        6, 85.5, 92.3, datetime.now())

    print("Valid station created:")

    print("ID:", space_station_1.station_id)
    print("Name:", space_station_1.name)
    print(f"Crew: {space_station_1.crew_size} people")
    print(f"Power: {space_station_1.power_level:.1f}%")
    print(f"Oxygen: {space_station_1.oxygen_level:.1f}%")
    print("Status:", "Operational"
          if space_station_1.is_operational else "Offline")

    print()

    print("========================================")

    print("Expected validation error:")

    space_station_2 = SpaceStation(
        "ISS_null", "Off Brand ISS",
        60, 20.5, 2.3, datetime.now())
