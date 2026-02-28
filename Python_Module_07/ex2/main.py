#!/usr/bin/env python3


from ex2.EliteCard import EliteCard

# for this project to work, use:
#   python -m ex1.main
# while in root

if __name__ == "__main__":

    print("=== DataDeck Ability System ===")

    print()

    print("""EliteCard capabilities:
- Card: ['play', 'get_card_info', 'is_playable']
- Combatable: ['attack', 'defend', 'get_combat_stats']
- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']
""")

    arcane_warrior = EliteCard("Arcane Warrior", 6, "Very Rare",
                               5, 5, 6, "melee", 14)

    print("Deck stats:", deck.get_deck_stats())

    print()

    print(arcane_warrior.play({"mana": 10}))

    print()

    print("Combat phase:")

    print("Attack result:", arcane_warrior.attack("Enemy"))

    print("Defense result:", arcane_warrior.defend(5))

    print()

    print("Magic phase:")

    print("Spell cast:", arcane_warrior.cast_spell("Fireball", ['Enemy1', 'Enemy2']))

    print()

    print("Mana channel:", arcane_warrior.channel_mana(3))

    print()

    print("Polymorphism in action: Same interface, different card behaviors!")
