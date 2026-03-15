#!/usr/bin/env python3

from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform

if __name__ == "__main__":

    print("=== DataDeck Tournament Platform ===")

    print()

    print("Registering Tournament Cards...")

    print()

    tornament = TournamentPlatform()

    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 4, 6,
                                 "Melee", "dragon_001", 1200, 0, 0)

    fire_dragon.get_tournament_stats()

    print()

    ice_wizard = TournamentCard("Ice Wizard", 4, "Rare", 4, 2, 2,
                                "Ranged", "wizard_001", 1150, 0, 0)

    ice_wizard.get_tournament_stats()

    print()

    tornament.register_card(fire_dragon)

    tornament.register_card(ice_wizard)

    print("Creating tournament match...")

    print(tornament.create_match("dragon_001", "wizard_001"))

    print()

    tornament.get_leaderboard()

    print()

    print("Platform Report:")

    print(tornament.generate_tournament_report())

    print()

    print("=== Tournament Platform Successfully Deployed! ===")

    print("All abstract patterns working together harmoniously!")
