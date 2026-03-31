#!/usr/bin/env python3


from datetime import date
from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum


class Rank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):

    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field()
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):

    mission_id: str = Field(min_length=5, max_length=15)
    # len 5-15 characters
    mission_name: str = Field(min_length=3, max_length=100)
    # len 3-100 characters
    destination: str = Field(min_length=3, max_length=15)
    # len 3-50 characters
    launch_date: date = Field()
    duration_days: int = Field(ge=1, le=3650)  # int 1-3650 days (max 10 years)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    # len min 1 max 12
    mission_status: str = Field(min_length=3, max_length=10, default="planned")
    budget_millions: float = Field(ge=1, le=10000)
    # val 1.0-10000.0 million dollars

    @model_validator(mode="after")
    def validate_inputs(self) -> "SpaceMission":

        # print()
        # print(self.__dict__)
        # print()

        if not self.mission_id.startswith("M"):
            raise ValueError(
                "Mission ID must start with \"M\"")

        commander = False
        for member in self.crew:
            if not member.is_active:
                raise ValueError(
                    "All Members of the Crew must be currently Active")
            if (member.rank == Rank.COMMANDER
                    or member.rank == Rank.CAPTAIN):
                commander = True
                break
        if not commander:
            raise ValueError("Must have at least one Commander or Captain")

        if self.duration_days > 365:
            crew_size_50 = len(self.crew) / 2
            experienced = 0
            for member in self.crew:
                if member.years_experience > 5:
                    experienced += 1

            if crew_size_50 > experienced:
                raise ValueError(
                    "Long missions (> 365 days) need 50%"
                    " experienced crew (5+ years)")

        return self


def str_error(error_type: str, field: str, msg: str, input_raw: str,
              expected: int | None) -> None:

    input_processed = len(input_raw)

    if error_type == "string_too_short":
        if not input_processed:
            print(f"'{field}' cannot be empty.")
        else:
            print(
                f"'{field}' should be larger than or equal to {expected}",
                f"char. Got {input_processed}")
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
        print(f"'{field}' must an integer. Got {input_processed}")
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
        print(f"'{field}' must an integer. Got {input_processed}")
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


def bool_error(error_type: str, field: str, msg: str, input_raw: bool) -> None:

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


def error_processing(error_details: list) -> None:

    # print()
    # print()
    # print("\n".join(error_details))
    # print("ALL:", error_details, sep="\n")
    # print()
    # print()

    for error in error_details:

        # print()
        # print("current:", error)
        # print()

        error_type = error["type"]
        if not len(error["loc"]):
            field = None
        else:
            field = error["loc"][0]
        msg = error["msg"]
        input = error["input"]
        get_expected = error.get("ctx")
        # print("get expected:", get_expected)
        # print()
        expected = (list(get_expected.values())[0]
                    if get_expected else get_expected)

        # print("unpacked:", error_type, field, msg, input, expected)
        # print()
        if field is None:
            print(msg[len("Value error, "):])
        elif field in ["contact_id", "location", "message_received"]:
            str_error(error_type, field, msg, input, expected)
        elif field in ["duration_minutes", "witness_count"]:
            int_error(error_type, field, msg, input, expected)
        elif field in ["signal_strength", "oxygen_level"]:
            float_error(error_type, field, msg, input, expected)
        elif field in ["timestamp"]:
            date_error(error_type, field, msg, input, expected)
        elif field in ["is_verified"]:
            bool_error(error_type, field, msg, input)
        elif field in ["contact_type"]:
            print(error_type)
            if error_type == "bool_parsing":
                print(f"'{field}' must a valid ContactType. Got {input}")
            else:
                print("Unknown Error:", msg)

        else:
            print("Unknown error:", error)


if __name__ == "__main__":

    print("Space Mission Crew Validation")

    print("========================================")

    sara = CrewMember(
        member_id="E1984", name="Sarah Connor", rank=Rank.COMMANDER, age=47,
        specialization="Mission Command", years_experience=9)
    john = CrewMember(
        member_id="E1994", name="John Smith", rank=Rank.LIEUTENANT, age=44,
        specialization="Navigation", years_experience=6)
    alice = CrewMember(
        member_id="E2003", name="Alice Johnson", rank=Rank.OFFICER, age=28,
        specialization="Engineering", years_experience=3)
    frank = CrewMember(
        member_id="M2025", name="Frank Lee", rank=Rank.CADET, age=21,
        specialization="Smuggler", years_experience=0)

    space_mission_1 = SpaceMission(
        mission_id="M2024_MARS", mission_name="Mars Colony Establishment",
        destination="Mars", launch_date=date(2030, 5, 6), duration_days=900,
        crew=[sara, john, alice], budget_millions=2500)

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
            mission_id="M2024_URANUS", mission_name="Uranus Exploration",
            destination="Uranus", launch_date=date.today(), duration_days=2000,
            crew=[alice, frank], budget_millions=70 - 1)
    except ValidationError as e:
        error_processing(e.errors())
