#!/usr/bin/env python3

from alchemy.grimoire.spellbook import record_spell
from alchemy.grimoire.validator import validate_ingredients


def ft_circular_curse() -> None:
    print()
    print("=== Circular Curse Breaking ===")

    print()

    print("Testing ingredient validation:")

    try:
        result = validate_ingredients("fire air")
    except AttributeError:
        result = "not exposed"
    print(f"validate_ingredients(\"fire air\"): {result}")

    try:
        result = validate_ingredients("dragon scales")
    except AttributeError:
        result = "not exposed"
    print(f"validate_ingredients(\"dragon scales\"): {result}")

    print()

    print("Testing spell recording with validation:")

    try:
        result = record_spell("Fireball", "fire air")
    except AttributeError:
        result = "not exposed"
    print(f"record_spell(\"Fireball\", \"fire air\"): {result}")

    try:
        result = record_spell("Dark Magic", "shadow")
    except AttributeError:
        result = "not exposed"
    print(f"record_spell(\"Dark Magic\", \"shadow\"): {result}")

    print()

    print("Testing late import technique:")

    from alchemy.grimoire.spellbook import record_spell as late_record_spell

    try:
        result = late_record_spell("Lightning", "air")
    except AttributeError:
        result = "not exposed"
    print(f"record_spell(\"Lightning\", \"air\"): {result}")

    print()

    print("Circular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
