#!/usr/bin/env python3

import random
from typing import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(**kwargs) -> str:
        return ("Combined spell result: "
                + spell1(**kwargs) + " : "
                + spell2(**kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(**kwargs) -> int:
        return base_spell(**kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditioned(**kwargs) -> str:
        if condition(**kwargs):
            return (spell(**kwargs))
        else:
            return "Spell fizzled"
    return conditioned


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequenced(**kwargs) -> list[Callable]:
        return [spell(**kwargs) for spell in spells]
    return sequenced


# Elemental Magic


def mold_earth(directions: str) -> str:
    return ("You speak an incantation of the Earth, Creating: " +
            directions)


def shape_water(directions: str) -> str:
    return ("You speak an incantation of the Depths, Creating: " +
            directions)


def control_flame(directions: str) -> str:
    return ("You speak an incantation of the Hells, Creating: " +
            directions)


def gust(directions: str) -> str:
    return ("You speak an incantation of the Storm, Creating: " +
            directions)


# Offensive Magic


def fireball(targets: list[str]) -> str:
    return ("You speak an incantation of the Hells, raining Fire upon: " +
            ", ".join(targets))


def firebolt(targets: list[str]) -> str:
    return ("You speak an incantation of the Hells, blasting flames on: " +
            ", ".join(targets))


def lightning_bolt(targets: list[str]) -> str:
    return ("You speak an incantation of the Storm, " +
            "striking Lightning upon: " +
            ", ".join(targets))


def shatter(targets: list[str]) -> str:
    return ("You speak an incantation of the Storm, " +
            "conjuring Thunder upon: " +
            ", ".join(targets))


def magic_missile(targets: list[str], **kwargs) -> int:
    return (sum(random.choice([1, 2, 3, 4]) + 1 for target in targets))


# Other Magics


def misty_step(directions: str, **kwargs) -> str:
    return ("You speak an incantation of the Fey, " +
            "transporting yourself to: " +
            directions)


def wish(directions: str) -> str:
    return ("You speak The AllWord. nothing stands " +
            "in your way as you state: " +
            directions)


# Magical Resources


def check_spellslot(spellslot: int, spell_lvl: int, **kwargs) -> bool:
    if spellslot < spell_lvl:
        return False
    return True


def higher_magic() -> None:

    # test_values = [19, 10, 18]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined = spell_combiner(mold_earth, shape_water)

    print(combined(directions="a mud statue"))

    mult = 3

    amplified = power_amplifier(magic_missile, mult)

    print("regular cast sample:",
          magic_missile(targets=[random.choice(test_targets),
                                 random.choice(test_targets)]))

    print("amplified cast sample:",
          amplified(targets=[random.choice(test_targets),
                             random.choice(test_targets)]))

    conditional_bad = conditional_caster(check_spellslot, wish)

    print(conditional_bad(spellslot=3, spell_lvl=9,
                          directions="All the Power in the WORLD"))

    conditional_good = conditional_caster(check_spellslot, misty_step)

    print(conditional_good(spellslot=0, spell_lvl=0, directions="30 ft North"))

    sequence = spell_sequence([magic_missile, magic_missile, magic_missile])

    print(sequence(targets=[random.choice(test_targets),
                            random.choice(test_targets)]))


if __name__ == "__main__":
    higher_magic()

"""
=== Exercise 1 Test Data ===
# Higher Realm Test Data
# Use these in your test functions:
test_values = [8, 18, 21]
test_targe 'blizzard']

=== Exercise 1 Test Data ===
# Higher Realm Test Data
# Use these in your test functions:
test_values = [19, 10, 18]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']
"""
