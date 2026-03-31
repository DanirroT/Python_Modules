#!/usr/bin/env python3


from typing import Optional
from datetime import date
from pydantic import BaseModel, ValidationError, Field, model_validator
from enum import Enum


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

    @model_validator(mode="after")
    def validate_inputs(self) -> "AlienContact":

        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with \"AC\" (Alien Contact)")

        if self.contact_type == "physical" and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        if self.contact_type == "telepathic" and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")

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

    print("Alien Contact Log Validation")

    print("========================================")

    alien_contact_1 = AlienContact(
        contact_id="AC_2024_001", timestamp=date(2030, 5, 6),
        location="Area 51, Nevada", contact_type=ContactType.RADIO,
        signal_strength=8.5, duration_minutes=45, witness_count=5,
        message_received="'Greetings from Zeta Reticuli'")

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
            contact_id="AC_2024_null", timestamp=date.today(),
            location="Area 52,", contact_type=ContactType.TELEPATHIC,
            signal_strength=2.5, duration_minutes=3, witness_count=1,
            message_received="'They are WHAT?'")
    except ValidationError as e:
        error_processing(e.errors())
