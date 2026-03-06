#!/usr/bin/env python3


# from typing import Optional

# import json, csv

from typing import Optional
from datetime import date
from pydantic import BaseModel, ValidationError, Field, model_validator
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


class CrewMember(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)  # len 3-10
    name: str = Field(min_length=1, max_length=50)  # len 1-50
    crew_size: int = Field(ge=1, le=20)  # val 1-20
    power_level: float = Field(ge=0, le=100)  # val 0.0-100.0 (%)
    oxygen_level: float = Field(ge=0, le=100)  # val 0.0-100.0 (%)
    last_maintenance: date = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)  # max_len = 200

    member_id: str  # len 3-10
    name: str  # val 2-50
    rank: Rank
    age: int  # val 18-80
    specialization: str  # len 3-30
    years_experience: int  # val 0-50
    is_active: bool = True

    """
    def __init__(self, member_id: str, name: str, rank: Rank, age: int,
                 specialization: str, years_experience: int,
                 is_active: bool = True) -> None:

        try:

            self.member_id = self.str_len_check(member_id, 3, 10)

            self.name = self.str_len_check(name, 2, 50)

            if rank not in Rank():
                raise ValueError(
                    "Given CrewMember Rank is not known.")
            self.rank = rank

            self.age = self.int_val_check(age, 18, 80)

            self.specialization = self.str_len_check(specialization, 3, 30)

            self.years_experience = self.int_val_check(years_experience, 5, 50)

            self.is_active = True if is_active else False

        except ValueError as e:
            print(e)"""

def str_error(error_type: str, field: str, msg: str, input_raw: str,
              expected: int | None) -> None:

    input_processed = len(input_raw)

    if error_type == "string_too_short":
        if not input_processed:
            print(f"'{field}' cannot be empty.")
        else:
            print(
                f"'{field}' should be larger than or equal to {expected} char.",
                  f"Got {input_processed}")
    elif error_type == "string_too_long":
        print(
            f"'{field}' should be smaller than or equal to {expected} char.",
                  f"Got {input_processed}")
    else:
        print("Unknown Error:", msg)


def int_error(error_type: str, field: str, msg: str, input_raw: int,
              expected: int | None) -> None:

    input_processed = input_raw

    if error_type == "int_parsing":
        print(f"'{field}' must an intager. Got {input_processed}")
    elif error_type == "less_than_equal":
        if expected == 0:
            print(
                f"'{field}' must be positive. Got {input_processed}")
        else:
            print(
                f"'{field}' should be less than or equal to {expected}.",
                  f"Got {input_processed}")
    elif error_type == "greater_than_equal":
        if expected == 0:
            print(
                f"'{field}' must be negative. Got {input_processed}")
        else:
            print(
                f"'{field}' should be greater than or equal to {expected}.",
                  f"Got {input_processed}")
    else:
        print("Unknown Error:", msg)


def float_error(error_type: str, field: str, msg: str, input_raw: float,
                expected: float | None) -> None:

    input_processed = input_raw

    if error_type == "float_parsing":
        print(f"'{field}' must an intager. Got {input_processed}")
    elif error_type == "less_than_equal":
        if expected == 0:
            print(
                f"'{field}' must be positive. Got {input_processed}")
        else:
            print(
                f"'{field}' should be less than or equal to {expected}.",
                  f"Got {input_processed}")
    elif error_type == "greater_than_equal":
        if expected == 0:
            print(
                f"'{field}' must be negative. Got {input_processed}")
        else:
            print(f"'{field}' should be greater than or equal to {expected}.",
                  f"Got {input_processed}")
    else:
        print("Unknown Error:", msg)


#    if (min == 0 and max == 100
#            and field_float < min and field_float > max):
#        print("SpaceStation Oxygen Level be a percentage.")


def bool_error(error_type: str, field: str, msg: str, input_raw: bool,
               expected: bool | None) -> None:

    input_processed = input_raw

    if error_type == "bool_parsing":
        print(f"'{field}' must a valid boolean. Got {input_processed}")
    else:
        print("Unknown Error:", msg)


def date_error(error_type: str, field: str, msg: str, input_raw: date,
               expected: str | None) -> None:

    input_processed = input_raw

    if error_type == "date_from_datetime_parsing":
        print(f"'{field}' must be a valid date. Got {input_processed}")
    else:
        print("Unknown Error:", msg)


def error_processing(error_details: list[dict[str, Any]]) -> None:

    # print()
    # print()
    # print("\n".join(error_details))
    # print("ALL:", error_details, sep="\n")
    # print()
    # print()

    for error in error_details:

        # print()
        print("corrent:", error)
        # print()

        error_type = error["type"]
        field = error["loc"][0]
        msg = error["msg"]
        input = error["input"]
        get_expected = error.get("ctx")
        print("get expected:", get_expected)
        expected = (list(get_expected.values())[0]
                    if get_expected else get_expected)

        print("unpacked:", error_type, field, msg, input, expected)
        # print()

        if field in ["station_id", "name", "notes"]:
            str_error(error_type, field, msg, input, expected)
        elif field in ["crew_size"]:
            int_error(error_type, field, msg, input, expected)
        elif field in ["power_level", "oxygen_level"]:
            float_error(error_type, field, msg, input, expected)
        elif field in ["last_maintenance"]:
            date_error(error_type, field, msg, input, expected)
        elif field in ["is_operational"]:
            bool_error(error_type, field, msg, input, expected)
        else:
            print("Unknown error:", error)


class SpaceMission():
    mission_id: str  # len 5-15 characters
    mission_name: str  # len 3-100 characters
    destination: str  # len 3-50 characters
    launch_date: str
    duration_days: int  # int 1-3650 days (max 10 years)
    crew: list[CrewMember]  # len min 1 max 12
    mission_status: str = "planned"
    budget_millions: float  # val 1.0-10000.0 million dollars

    def __init__(self, mission_id: str, mission_name: str, destination: str,
                 launch_date: str, duration_days: int,
                 crew: list[CrewMember], budget_millions: float,
                 mission_status: str = "planned") -> None:

        try:

            self.mission_id = self.str_len_check(mission_id, 5, 15)

            self.mission_name = self.str_len_check(mission_name, 3, 100)

            self.destination = self.str_len_check(destination, 3, 50)

            self.launch_date = launch_date

            self.duration_days = self.int_val_check(duration_days, 1, 3650)

            if len(crew) < 1:
                raise ValueError(
                    "SpaceMission crew must have at least one member.")
            if len(crew) > 12:
                raise ValueError(
                    "SpaceMission crew has too many people (max=12).")
            self.crew = crew

            self.mission_status = self.str_len_check(mission_status, 1, 50)

            self.budget_millions = self.float_val_check(
                budget_millions, 1, 10000)

        except ValueError as e:
            print(e)

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
        str(date(2030, 5, 6)), 900, [sara, john, alice], 2500)

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

    try:
        space_station_2 = SpaceMission(
            "M2024_URANUS", "Uranus Exploration", "Uranus",
            str(date.today()), 2000, [alice, frank], 70 - 1)
    except ValidationError as e:
        error_processing(e.errors())
