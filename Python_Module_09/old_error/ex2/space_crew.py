#!/usr/bin/env python3


# from typing import Optional

# import json, csv

from datetime import date
from enum import Enum

# for this project to work, use:
#   python -m ex0.main
# while in root


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMANDER = "commander"


class CrewMember():
    member_id: str  # len 3-10
    name: str  # val 2-50
    rank: Rank
    age: int  # val 18-80
    specialization: str  # len 3-30
    years_experience: int  # val 0-50
    is_active: bool = True

    def __init__(self, member_id: str, name: str, rank: Rank, age: int,
                 specialization: str, years_experience: int,
                 is_active: bool = True) -> None:

        class_name = self.__class__.__name__ + " "

        try:

            self.member_id = self.str_len_check(
                class_name + "ID", member_id, 3, 10)

            self.name = self.str_len_check(
                class_name + "name", name, 2, 50)

            if rank not in Rank():
                raise ValueError(
                    "Given CrewMember Rank is not known.")
            self.rank = rank

            self.age = self.int_val_check(
                class_name + "age", age, 18, 80)

            self.specialization = self.str_len_check(
                class_name + "mission specialization", specialization, 3, 30)

            self.years_experience = self.int_val_check(
                class_name + "years of experience", years_experience, 5, 50)

            self.is_active = True if is_active else False

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


class SpaceMission():
    mission_id: str  # len 5-15 characters
    mission_name: str  # len 3-100 characters
    destination: str  # len 3-50 characters
    launch_date: datetime
    duration_days: int  # int 1-3650 days (max 10 years)
    crew: list[CrewMember]  # len min 1 max 12
    mission_status: str = "planned"
    budget_millions: float  # val 1.0-10000.0 million dollars

    def __init__(self, mission_id: str, mission_name: str, destination: str,
                 launch_date: datetime, duration_days: int,
                 crew: list[CrewMember], budget_millions: float,
                 mission_status: str = "planned") -> None:

        class_name = self.__class__.__name__ + " "

        try:

            self.mission_id = self.str_len_check(
                class_name + "ID", mission_id, 5, 15)

            self.mission_name = self.str_len_check(
                class_name + "mission name", mission_name, 3, 100)

            self.destination = self.str_len_check(
                class_name + "destination", destination, 3, 50)

            self.launch_date = launch_date

            self.duration_days = self.int_val_check(
                class_name + "duration", duration_days, 1, 3650)

            if len(crew) < 1:
                raise ValueError(
                    "SpaceMission crew must have at least one member.")
            if len(crew) > 12:
                raise ValueError(
                    "SpaceMission crew has too many people (max=12).")
            self.crew = crew

            self.mission_status = self.str_len_check(
                class_name + "mission status", mission_status, 1, 50)

            self.budget_millions = self.float_val_check(
                class_name + "budget", budget_millions, 1, 10000)

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

    @model_validator
    def validate_inputs(self) -> None:

        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with \"M\"")

        comander = False
        for member in self.crew:
            if (member.is_active == "captain"
                    and member.is_active == "commander"):
                comander = True
                break
        if not comander:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            crew_size_50 = len(self.crew) / 2
            experienced = 0
            for member in self.crew:
                if member.years_experience:
                    experienced += 1

            if crew_size_50 < experienced:
                raise ValueError(
                    "Long missions (> 365 days) need 50%"
                    "experienced crew (5+ years)")

        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                    "All crew members must be active")


if __name__ == "__main__":

    print("Space Mission Crew Validation")

    print("========================================")

    sara = CrewMember(
        "E1984", "Sarah Connor", Rank.COMANDER, 47, "Mission Command", 9)
    john = CrewMember(
        "E1994", "John Smith", Rank.LIEUTENANT, 44, "Navigation", 6)
    alice = CrewMember(
        "E2003", "Alice Johnson", Rank.OFFICER, 28, "Engineering", 3)
    frank = CrewMember(
        "M2025", "Frank Lee", Rank.CADET, 21, "Smuggler", 0)

    space_mission_1 = SpaceMission(
        "M2024_MARS", "Mars Colony Establishment", "Mars",
        date(2030, 5, 6), 900, [sara, john, alice], 2500)

    print("Valid mission created:")

    print("Mission:", space_mission_1.mission_name)
    print("ID:", space_mission_1.mission_id)
    print("Destination:", space_mission_1.destination)
    print(f"Duration: {space_mission_1.duration_days} days")
    print(f"Budget: ${space_mission_1.budget_millions}M")
    print("Crew size:", len(space_mission_1.crew))
    print("Crew members:")
    for member in space_mission_1.crew:
        print(f"- {member.name} ({member.rank}) - {member.specialization}")

    print()

    print("========================================")

    print("Expected validation error:")

    space_station_2 = SpaceMission(
        "M2024_URANUS", "Uranus Exploration", "Uranus",
        date.today(), 2000, [alice, frank], 70 - 1)
