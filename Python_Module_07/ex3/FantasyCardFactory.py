#!/usr/bin/env python3

from .CardFactory import CardFactory


import random
from typing import Callable
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    creatures: dict[tuple[str, int], Callable[[], CreatureCard]] = {
        ('Fire Dragon', 7): lambda:
        CreatureCard('Fire Dragon', 5, 'Legendary', 7, 5),
        ('Goblin Warrior', 3): lambda:
        CreatureCard('Goblin Warrior', 2, 'Common', 3, 1)
    }

    spells: dict[tuple[str, int], Callable[[], SpellCard]] = {
        ("Lightning Bolt", 5): lambda:
        SpellCard("Lightning Bolt", 3, "Common", "Deal 5 damage to target")
    }

    artifacts: dict[tuple[str, int], Callable[[], ArtifactCard]] = {
        ("mana_ring", 0): lambda:
        ArtifactCard("Mana Ring", 2, "Common", 5,
                     "Permanent: +1 mana per turn")
    }

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            self.cards_created += 1
            return random.choice(list(self.creatures.values()))()

        for (name, power), constructor in self.creatures.items():
            if name == name_or_power:
                self.cards_created += 1
                return constructor()
            if power == name_or_power:
                self.cards_created += 1
                return constructor()

        return None

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            self.cards_created += 1
            return random.choice(list(self.spells.values()))()

        for (name, power), constructor in self.spells.items():
            if name == name_or_power:
                self.cards_created += 1
                return constructor()
            if power == name_or_power:
                self.cards_created += 1
                return constructor()

        return None

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            self.cards_created += 1
            return random.choice(list(self.artifacts.values()))()

        for (name, power), constructor in self.artifacts.items():
            if name == name_or_power:
                self.cards_created += 1
                return constructor()
            if power == name_or_power:
                self.cards_created += 1
                return constructor()

        return None

    def create_themed_deck(self, size: int) -> dict[int, Card]:
        out_dict: dict[int, Card] = {}
        for i in range(size):
            create_funct = random.choice((self.create_creature,
                                          self.create_spell,
                                          self.create_artifact))
            out_dict[i] = create_funct()
        return out_dict

    def get_supported_types(self) -> dict[str, list[str]]:
        return {'creatures': ['dragon', 'goblin'],
                'spells': ['fireball'],
                'artifacts': ['mana_ring']}
