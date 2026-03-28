#!/usr/bin/env python3


from typing import Any, Callable


def mage_counter() -> Callable:
    count = 0

    def add_return() -> int:
        nonlocal count
        count += 1
        return count
    return add_return


def spell_accumulator(initial_power: int) -> Callable:
    power = initial_power

    def add_return(aditional_power: int) -> int:
        nonlocal power
        power += aditional_power
        return power
    return add_return


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str) -> str:
        return enchantment_type + " " + item
    return enchant


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        nonlocal memory
        memory[key] = value

    def recall(key: str) -> Any:
        nonlocal memory
        return memory.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def scope_mysteries() -> None:

    print()

    print("Testing mage counter...")

    counter = mage_counter()

    for i in range(1, 4):
        print(f"Call {i}:", counter())

    print()

    print("Testing spell accumulator...")

    accumulator = spell_accumulator(1)

    for i in range(1, 4):
        print(f"Call {i}:", accumulator(3 * i))

    print()

    print("Testing enchantment factory...")

    flaming = enchantment_factory("Flaming")
    print(flaming("Sword"))

    frozen = enchantment_factory("Frozen")
    print(frozen("Shield"))

    print()

    print("Testing memory vault...")

    vault = memory_vault()

    mk_1, mv_1 = "Sword", "Sharp"
    mk_2, mv_2 = "Hammer", "Heavy"
    mk_3, mv_3 = "Spear", "Pointy"

    print("adding memory:", mk_1, mv_1)
    print("adding memory:", mk_2, mv_2)
    print("adding memory:", mk_3, mv_3)

    vault["store"](mk_1, mv_1)
    vault["store"](mk_2, mv_2)
    vault["store"](mk_3, mv_3)

    print("Retriving memory:", mk_1, vault["recall"](mk_1))
    print("Retriving memory:", mk_2, vault["recall"](mk_2))
    print("Retriving memory:", "mk_3", vault["recall"]("mk_3"))


if __name__ == "__main__":
    scope_mysteries()

"""
=== Exercise 2 Test Data ===
# Memory Depths Test Data
initial_powers = [43, 39, 29]
power_additions = [12, 9, 8, 7, 6]
enchantment_types = ['Shocking', 'Windy', 'Dark']
items_to_enchant = ['Shield', 'Wand', 'Sword', 'Staff']

=== Exercise 2 Test Data ===
# Memory Depths Test Data
initial_powers = [45, 40, 76]
power_additions = [18, 15, 6, 15, 19]
enchantment_types = ['Earthen', 'Radiant', 'Frozen']
items_to_enchant = ['Cloak', 'Staff', 'Sword', 'Wand']
"""
