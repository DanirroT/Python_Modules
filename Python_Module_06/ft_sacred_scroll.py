#!/usr/bin/env python3

import alchemy.elements as elements
import alchemy


def ft_sacred_scroll() -> None:
    print()
    print("=== Sacred Scroll Mastery ===")
    print()
    print("Testing direct module access:")

    try:
        result = elements.create_fire()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.elements.create_fire(): {result}")

    try:
        result = elements.create_water()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.elements.create_water(): {result}")

    try:
        result = elements.create_earth()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.elements.create_earth(): {result}")

    try:
        result = elements.create_air()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.elements.create_air(): {result}")

    print()
    print("Testing package-level access (controlled by __init__.py):")

    try:
        result = alchemy.create_fire()
        print(f"alchemy.create_fire(): {result}")
    except AttributeError:
        print("alchemy.create_fire(): AttributeError - not exposed")
    try:
        result = alchemy.create_water()
        print(f"alchemy.create_water(): {result}")
    except AttributeError:
        print("alchemy.create_water(): AttributeError - not exposed")
    try:
        result = alchemy.create_earth()
        print(f"alchemy.create_earth(): {result}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")
    try:
        result = alchemy.create_air()
        print(f"alchemy.create_air(): {result}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print()
    print("Package metadata:")
    print(alchemy.__version__)
    print(alchemy.__author__)


if __name__ == "__main__":
    ft_sacred_scroll()
