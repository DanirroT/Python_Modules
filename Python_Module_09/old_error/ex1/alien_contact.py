#!/usr/bin/env python3


from typing import Optional

# import json, csv

from datetime import datetime, date
from enum import Enum

# for this project to work, use:
#   python -m ex0.main
# while in root


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact():

    contact_id: str  # len 5-15
    timestamp: datetime
    location: str  # len 3-100
    contact_type: ContactType
    signal_strength: float  # val 0-10
    duration_minutes: int  # val 1-1440 (1 day)
    witness_count: int  # val 1-100
    message_received: Optional[str] = None  # max_len = 500
    is_verified: bool = False

    def __init__(self, contact_id: str, timestamp: str, location: str,
                 contact_type: ContactType, signal_strength: float,
                 duration_minutes: int, witness_count: int,
                 message_received: Optional[str] = None,
                 is_verified: bool = False) -> None:

        class_name = self.__class__.__name__ + " "

        try:

            self.contact_id = self.str_len_check(
                class_name + "ID", contact_id, 5, 15)

            self.timestamp = timestamp

            self.location = self.str_len_check(
                class_name + "location", location, 3, 100)

            if contact_type not in ContactType():
                raise ValueError(
                    "Given AlienContact ContactType is not known.")
            self.contact_type = contact_type

            self.signal_strength = self.float_val_check(
                class_name + "ID", signal_strength, 0, 10)

            self.duration_minutes = self.int_val_check(
                class_name + "duration_minutes", duration_minutes, 1, 1440)

            self.witness_count = self.int_val_check(
                class_name + "location", witness_count, 3, 100)

            if message_received:
                self.message_received = self.str_len_check(
                    class_name + "message_received", message_received, 0, 500)
            else:
                self.message_received = None

            self.is_verified = True if is_verified else False

            self.validate_inputs()

        except ValueError as e:
            print(e)

    @staticmethod
    def str_len_check(field_name: str, field_input: str, min: int, max: int
                      ) -> str:
        if not field_input:
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
        "AC_2024_001", datetime.now(), "Area 51, Nevada",
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

    alien_contact_2 = AlienContact(
        "AC_2024_null", datetime.now(), "Area 52,",
        ContactType.TELEPATHIC, 2.5, 3, 1, "'They are WHAT?'")
