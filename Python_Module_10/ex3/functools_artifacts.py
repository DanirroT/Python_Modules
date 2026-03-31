#!/usr/bin/env python3


import random
import functools
from typing import Callable
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return functools.reduce(add, spells)
    if operation == "multiply":
        return functools.reduce(mul, spells)
    if operation == "max":
        return functools.reduce(max, spells)
    if operation == "min":
        return functools.reduce(min, spells)
    else:
        return None


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable[[str], str]]:
    return {"fire_enchant": functools.partial(
        base_enchantment, 50, "Fire"),
            "ice_enchant": functools.partial(
                base_enchantment, 50, "Ice"),
            "lightning_enchant": functools.partial(
                base_enchantment, 50, "Lightning")
    }


@functools.lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable:

    @functools.singledispatch
    def process(value) -> str:
        return "Unknown Spell Type"

    @process.register
    def _(value: int) -> str:
        return firebolt(value)

    @process.register
    def _(value: str) -> str:
        return misty_step(value)

    @process.register
    def _(value: list) -> int:
        return magic_missile(value)

    return process


def enchantment(power: int, element: str, target: str) -> str:
    return (f"Imbued the power of {element} onto {target} "
            f"with a potency of {power}.")


def firebolt(damage: int) -> str:
    return ("You speak an incantation of the Hells, doing " +
            f"{damage} damage on the target")


def magic_missile(targets: list[str]) -> int:
    return (sum(random.choice([1, 2, 3, 4]) + 1 for _ in targets))


def misty_step(directions: str) -> str:
    return ("You speak an incantation of the Fey, " +
            "transporting yourself to: " +
            directions)


def functools_artifacts() -> None:

    print("Testing spell reducer...")

    spell_powers = [47, 13, 33, 18, 37, 23]

    print("Sum:", spell_reducer(spell_powers, "add"))
    print("Product:", spell_reducer(spell_powers, "multiply"))
    print("Max:", spell_reducer(spell_powers, "max"))
    print("Min:", spell_reducer(spell_powers, "min"))

    print()

    print("Testing partial enchanter...")

    elemental_enchantments: dict[str, Callable] = partial_enchanter(enchantment)

    print("Conjure Fire:",
          elemental_enchantments["fire_enchant"](target="Sword"))
    print("Conjure Ice:",
          elemental_enchantments["ice_enchant"](target="Shield"))
    print("Conjure Lightning:",
          elemental_enchantments["lightning_enchant"](target="Whip"))

    print()

    print("Testing memoized fibonacci...")
    print("Fib(10):", memoized_fibonacci(10))
    print("Fib(15):", memoized_fibonacci(15))

    print()

    print("Testing spell dispatcher...")

    dispatch: Callable = spell_dispatcher()

    print("int:", dispatch(3))
    print("str:", dispatch("30 ft up"))
    print("list:", dispatch(["Goblin", "Dragon"]))

    print()


if __name__ == "__main__":
    functools_artifacts()

"""
=== Exercise 3 Test Data ===
# Ancient Library Test Data
spell_powers = [47, 13, 33, 18, 37, 23]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [8, 10, 12]

=== Exercise 3 Test Data ===
# Ancient Library Test Data
spell_powers = [38, 48, 43, 12, 24, 10]
operations = ['add', 'multiply', 'max', 'min']
fibonacci_tests = [15, 16, 17]
"""
