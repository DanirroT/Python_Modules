#!/usr/bin/env python3

from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> None:
    return ("Philosopher\'s stone created using " +
            f"{lead_to_gold()} and {healing_potion()}")


def elixir_of_life() -> None:
    return "Elixir of life: eternal youth achieved!"
