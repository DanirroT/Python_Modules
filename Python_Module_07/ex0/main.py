#!/usr/bin/env python3


from .CreatureCard import CreatureCard

# for this project to work, use:
#   python -m ex0.main
# while in root


if __name__ == "__main__":

    print("=== DataDeck Card Foundation ===")

    print()

    print("Testing Abstract Base Class Design:")

    print()

    fire_dragon = CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5)

    print("CreatureCard Info:")
    print(fire_dragon.get_card_info())

    print()

    print("Playing Fire Dragon with 6 mana available:")

    print(fire_dragon.play({"mana": 6}))

    print()

    print("Fire Dragon attacks Goblin Warrior:")
    goblin_warior = CreatureCard('Goblin Warrior', 2, 'Common', 2, 1)

    print(fire_dragon.attack_target(goblin_warior))

    print("Testing insufficient mana (3 available):")

    fire_dragon.play({"mana": 3})

    print()

    print("Abstract pattern successfully demonstrated!")
