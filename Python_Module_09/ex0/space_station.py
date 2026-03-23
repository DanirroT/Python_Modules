#!/usr/bin/env python3


from typing import Optional
from pydantic import BaseModel, ValidationError, Field
from datetime import date


class SpaceStation(BaseModel):

    station_id: str = Field(min_length=3, max_length=10)  # len 3-10
    name: str = Field(min_length=1, max_length=50)  # len 1-50
    crew_size: int = Field(ge=1, le=20)  # val 1-20
    power_level: float = Field(ge=0, le=100)  # val 0.0-100.0 (%)
    oxygen_level: float = Field(ge=0, le=100)  # val 0.0-100.0 (%)
    last_maintenance: date = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)  # max_len = 200


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


# if (min == 0 and max == 100
#    and field_float < min and field_float > max):
#    print("SpaceStation Oxygen Level be a percentage.")


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
        # print("corrent:", error)
        # print()

        error_type = error["type"]
        field = error["loc"][0]
        msg = error["msg"]
        input = error["input"]
        get_expected = error.get("ctx")
        # print("get expected:", get_expected)
        expected = (list(get_expected.values())[0]
                    if get_expected else get_expected)

        # print("unpacked:", error_type, field, msg, input, expected)
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
            bool_error(error_type, field, msg, input)
        else:
            print("Unknown error:", error)


if __name__ == "__main__":

    print("Space Station Data Validation")

    print("========================================")

    input_dict = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": str(date.today()),
        "notes": ""
    }

    space_station_1 = SpaceStation(**input_dict)

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

    input_dict_wrong = {
        "station_id": "ISS_null",
        "name": "Off Brand ISS",
        "crew_size": 25,
        "power_level": 20.5,
        "oxygen_level": 2.3,
        "last_maintenance": str(date.today()),
        "notes": ""
    }

    input_dict_extremely_wrong = {
        "station_id": "123",
        "name": "12345678901234567890123456789012345678901234567890",
        "crew_size": "1",
        "power_level": -5,
        "oxygen_level": 500,
        "is_operational": "no",
        "last_maintenance": "str(date.today())",
        "notes": ""
    }

    try:
        space_station_2 = SpaceStation(**input_dict_wrong)
    except ValidationError as e:
        error_processing(e.errors())
