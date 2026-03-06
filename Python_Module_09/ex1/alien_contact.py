#!/usr/bin/env python3


# import json, csv

from typing import Optional
from datetime import date
from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum

# for this project to work, use:
#   python -m ex0.main
# while in root


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):

    contact_id: str = Field(min_length=5, max_length=15)  # len 5-15
    timestamp: date = Field()
    location: str = Field(min_length=3, max_length=100)  # len 3-100
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0, le=100)   # val 0-10
    duration_minutes: int = Field(ge=1, le=1440)  # val 1-1440 (1 day)
    witness_count: int = Field(ge=1, le=100)  # val 1-20
    message_received: Optional[str] = Field(default=None, max_length=500)
    # max_len = 500
    is_verified: bool = Field(default=False)

    """
    def __init__(self, contact_id: str, timestamp: str, location: str,
                 contact_type: ContactType, signal_strength: float,
                 duration_minutes: int, witness_count: int,
                 message_received: Optional[str] = None,
                 is_verified: bool = False) -> None:

        try:

            self.contact_id = self.str_len_check(contact_id, 5, 15)

            self.timestamp = timestamp

            self.location = self.str_len_check(location, 3, 100)

            if contact_type not in ContactType():
                raise ValueError(
                    "Given AlienContact ContactType is not known.")
            self.contact_type = contact_type

            self.signal_strength = self.float_val_check(signal_strength, 0, 10)

            self.duration_minutes = self.int_val_check(
                duration_minutes, 1, 1440)

            self.witness_count = self.int_val_check(witness_count, 3, 100)

            if message_received:
                self.message_received = self.str_len_check(
                    message_received, 0, 500)
            else:
                self.message_received = None

            self.is_verified = True if is_verified else False

            self.validate_inputs()

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

    @model_validator
    def validate_inputs(self) -> None:

        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with \"AC\"" "(Alien Contact)")

        if self.contact_type == "physical" and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == "telepathic" and not self.is_verified:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")


if __name__ == "__main__":

    print("Alien Contact Log Validation")

    print("========================================")

    alien_contact_1 = AlienContact(
        "AC_2024_001", str(date(2030, 5, 6)), "Area 51, Nevada",
        ContactType.RADIO, 8.5, 45, 5, "'Greetings from Zeta Reticuli'")

    print("Valid contact report:")

    print("ID:", alien_contact_1.contact_id)
    print("Type:", alien_contact_1.contact_type)
    print(f"Location: {alien_contact_1.location} people")
    print(f"Signal: {alien_contact_1.duration_minutes} minutes")
    print(f"Duration: {alien_contact_1.signal_strength:.1f}%")
    print("Witnesses:", alien_contact_1.witness_count)
    print("Message:", alien_contact_1.message_received)

    print()

    print("========================================")

    print("Expected validation error:")

    try:
        alien_contact_2 = AlienContact(
            "AC_2024_null", str(date.today()), "Area 52,",
            ContactType.TELEPATHIC, 2.5, 3, 1, "'They are WHAT?'")
    except ValidationError as e:
        error_processing(e.errors())
