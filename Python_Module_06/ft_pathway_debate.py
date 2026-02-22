#!/usr/bin/env python3

from alchemy.transmutation import lead_to_gold, stone_to_gem, philosophers_stone, elixir_of_life
import alchemy.transmutation


def ft_sacred_scroll() -> None:
    print()
    print("=== Pathway Debate Mastery ===")
    print()
    print("Testing Absolute Imports (from basic.py):")

    try:
        result = lead_to_gold()
    except AttributeError:
        result = "not exposed"
    print(f"lead_to_gold(): {result}")

    try:
        result = stone_to_gem()
    except AttributeError:
        result = "not exposed"
    print(f"stone_to_gem(): {result}")

    print()

    print("Testing Relative Imports (from advanced.py):")

    try:
        result = philosophers_stone()
    except AttributeError:
        result = "not exposed"
    print(f"philosophers_stone(): {result}")

    try:
        result = elixir_of_life()
    except AttributeError:
        result = "not exposed"
    print(f"elixir_of_life(): {result}")

    print()

    print("Testing Package Access:")
    
    try:
        result = alchemy.transmutation.lead_to_gold()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.transmutation.lead_to_gold(): {result}")

    try:
        result = alchemy.transmutation.philosophers_stone()
    except AttributeError:
        result = "not exposed"
    print(f"alchemy.transmutation.philosophers_stone(): {result}")

    print()

    print("Both pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_sacred_scroll()
