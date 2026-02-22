#!/usr/bin/env python3

from . import elements


def healing_potion() -> None:
    return ("Healing potion brewed with " +
            f"{elements.create_fire()} and {elements.create_water()}")


def strength_potion() -> None:
    return ("Strength potion brewed with " +
            f"{elements.create_earth()} and {elements.create_fire()}")


def invisibility_potion() -> None:
    return ("Invisibility potion brewed with " +
            f"{elements.create_air()} and {elements.create_water()}")


def wisdom_potion() -> None:
    return ("Wisdom potion brewed with all elements: " +
            f"{elements.create_fire()}, {elements.create_water()}, " +
            f"{elements.create_earth()} and {elements.create_air()}")
