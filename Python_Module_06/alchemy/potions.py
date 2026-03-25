#!/usr/bin/env python3

from . import elements


def healing_potion() -> str:
    return ("Healing potion brewed with " +
            f"{elements.create_fire()} and {elements.create_water()}")


def strength_potion() -> str:
    return ("Strength potion brewed with " +
            f"{elements.create_earth()} and {elements.create_fire()}")


def invisibility_potion() -> str:
    return ("Invisibility potion brewed with " +
            f"{elements.create_air()} and {elements.create_water()}")


def wisdom_potion() -> str:
    return ("Wisdom potion brewed with all elements: " +
            f"{elements.create_fire()}, {elements.create_water()}, " +
            f"{elements.create_earth()} and {elements.create_air()}")
