#!/usr/bin/env python3

from .GameEngine import GameEngine
from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory

from ex0.CreatureCard import CreatureCard


# for this project to work, use:
#   python -m ex3.main
# while in root


if __name__ == "__main__":

    print("=== DataDeck Game Engine ===")

    print()

    print("Configuring Fantasy Card Game...")

    engine = GameEngine()

    engine.configure_engine(FantasyCardFactory, AggressiveStrategy)

    engine.set_targets([CreatureCard('Enemy Player', 0, 'Player', 0, 20)])
    engine.set_hand(list(engine.factory.create_themed_deck(3).values()))

    print("Available types:", engine.factory.get_supported_types())

    print()

    print("Simulating aggressive turn...")

    hand_listing = ', '.join([f'{card.name} ({card.cost})'
                              for card in engine.hand])

    print(f"Hand: [{hand_listing}]")

    print()

    print("Turn execution:")

    print("Strategy:", engine.strategy.__class__.__name__)

    print("Actions:", engine.simulate_turn())

    print()

    print("Game Report:")

    print(engine.get_engine_status())

    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
