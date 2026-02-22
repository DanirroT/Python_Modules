#!/usr/bin/env python3

import alchemy.elements

from alchemy.elements import create_water

from alchemy.potions import healing_potion as heal

from alchemy.elements import create_earth
from alchemy.elements import create_fire
from alchemy.potions import strength_potion


def full_import() -> None:

    print("Method 1 - Full module import:")
    try:
        result = alchemy.elements.create_fire()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.elements.create_fire(): {result}")


def specific_import() -> None:

    print("Method 2 - Specific function import:")
    try:
        result = create_water()
    except AttributeError:
        result = "not exposed"
    print(f"elements.create_water(): {result}")


def aliased_import() -> None:

    print("Method 3 - Aliased import:")
    try:
        result = heal()
    except AttributeError:
        result = "not exposed"
    print(f"heal(): {result}")


def multiple_imports() -> None:

    print("Method 4 -  Multiple imports:")
    try:
        result = create_earth()
    except AttributeError:
        result = "not exposed"
    print(f"create_earth(): {result}")

    try:
        result = create_fire()
    except AttributeError:
        result = "not exposed"
    print(f"create_fire(): {result}")

    try:
        result = strength_potion()
    except AttributeError:
        result = "not exposed"
    print(f"strength_potion(): {result}")


def ft_import_transmutation() -> None:
    print()
    print("=== Import Transmutation Mastery ===")
    print()
    full_import()
    print()
    specific_import()
    print()
    aliased_import()
    print()
    multiple_imports()
    print()
    print("All import transmutation methods mastered!")


if __name__ == "__main__":
    ft_import_transmutation()
