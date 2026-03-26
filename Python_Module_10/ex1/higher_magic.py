#!/usr/bin/env python3

import functools
from typing import Any
from operator import add, mul
import itertools

def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(**kwargs) -> str:
        return ("Combined spell result: "
                + spell1(**kwargs)
                + spell2(**kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(**kwargs) -> int:
        return base_spell(**kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def conditioned(**kwargs) -> str:
        if condition(**kwargs):
            return (spell(**kwargs))
        else:
            return "Spell fizzled"
    return conditioned


def spell_sequence(spells: list[callable]) -> callable:
    def sequenceed(**kwargs) -> list:
        return [spell(**kwargs) for spell in spells]
    return sequenceed


def mold_earth(directions: str):
def shape_water(directions: str):
def fireball(targets: str):
def firebolt(targets: str):
def lightning_bolt(targets: str):
def shatter(targets: str):
def magic_missile(targets: str):
def misty_step(directions: str):
def wish(directions: str):

def check_spellslot(spellslot: int, spell_lvl: int, **kwargs):
{

}



def higher_magic() -> None:

    test_values = [19, 10, 18]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    combined = spell_combiner(mold_earth, shape_water)

    mult = 3

    amplefied = power_amplifier(magic_missile, mult)


    conditional = conditional_caster(condition, wish)

    conditional = conditional_caster(condition, firebolt)


    sequence = spell_sequence(spells)


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
