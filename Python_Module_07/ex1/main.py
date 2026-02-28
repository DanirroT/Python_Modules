#!/usr/bin/env python3


from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck

# for this project to work, use:
#   python -m ex1.main
# while in root

if __name__ == "__main__":

    print("=== DataDeck Deck Builder ===")

    print()

    print("Building deck with different card types...")

    deck = Deck('3 Deck')

    # 3, 2, 5

    deck.add_card(SpellCard("Lightning Bolt", 4, "Common",
                            "Deal 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 4, "Common", 5,
                               "Permanent: +1 mana per turn"))
    deck.add_card(CreatureCard('Fire Dragon', 4, 'Legendary', 7, 5))

    print("Deck stats:", deck.get_deck_stats())

    print()

    print("Drawing and playing cards:")

    print()
    print("Play result:", deck.draw_card().play({"mana": 10}))
    print()
    print("Play result:", deck.draw_card().play({"mana": 10}))
    print()
    print("Play result:", deck.draw_card().play({"mana": 10}))
    print()

    print("Polymorphism in action: Same interface, different card behaviors!")
