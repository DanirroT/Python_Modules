#!/usr/bin/env python3


from datetime import datetime
from typing import Callable
import functools


def spell_timer(func: Callable) -> Callable:
    @functools.wraps(func)
    def timer(*args, **kwargs):
        start_time = datetime.now()
        print(f"Casting {func.__name__}...")
        result = func(*args, **kwargs)
        end_time = datetime.now()
        print(f"""Spell completed in {(end_time - start_time).microseconds
                                      / 1000000} seconds...""")
        return result
    return timer


def power_validator(min_power: int) -> Callable:
    def factory(func: Callable) -> Callable:
        def validator(*args, **kwargs):
            if args[-1] >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return validator
    return factory


def retry_spell(max_attempts: int) -> Callable:
    def factory(func: Callable) -> Callable:
        def retry(*args, **kwargs):
            success = False
            for i in range(max_attempts):
                try:
                    result = func(*args, **kwargs)
                    success = True
                    break
                except Exception:
                    print("Spell failed, retrying... "
                          f"(attempt {i+1}/{max_attempts})")
                    continue
            if success:
                return result
            return f"Spell casting failed after {max_attempts} attempts"
        return retry
    return factory


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        for char in name:
            if not char.isalpha() and not char.isspace():
                return False
        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with power {power}"


def fireball(targets: list[str]) -> str:
    return ("You speak an encantation of the Hells, raining Fire upon: " +
            ", ".join(targets))


def experimental_spell() -> str:
    return f"Created Infinity {1 / 0}"


def decorator_mastery() -> None:

    print("Testing spell timer...")

    timer = spell_timer(fireball)
    print(timer(["Dragon", "Kobold"]))

    print()

    print("Testing retry spell...")

    re_try_3 = retry_spell(3)

    re_try = re_try_3(experimental_spell)

    print(re_try())

    print()

    mageguild = MageGuild()

    print("Testing validate mage name...")

    print(mageguild.validate_mage_name("Karsus of Netheril"))

    print(mageguild.validate_mage_name("Mistra, the 3rd"))

    print()

    print("Testing cast spell...")

    print(mageguild.cast_spell("Lightning", 15))

    print(mageguild.cast_spell("Campfire", 8))


if __name__ == "__main__":
    decorator_mastery()

"""
=== Exercise 4 Test Data ===
# Master's Tower Test Data
test_powers = [5, 22, 6, 12]
spell_names = ['heal', 'shield', 'darkness', 'lightning']
mage_names = ['Kai', 'Sage', 'Riley', 'Alex', 'Rowan', 'Phoenix']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']

=== Exercise 4 Test Data ===
# Master's Tower Test Data
test_powers = [12, 26, 26, 28]
spell_names = ['shield', 'tornado', 'darkness', 'meteor']
mage_names = ['Riley', 'Phoenix', 'Rowan', 'Jordan', 'Nova', 'Storm']
invalid_names = ['Jo', 'A', 'Alex123', 'Test@Name']
"""
