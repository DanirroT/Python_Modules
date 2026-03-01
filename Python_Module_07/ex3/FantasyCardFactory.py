#!/usr/bin/env python3

from .CardFactory import CardFactory


import random
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class FantasyCardFactory(CardFactory):

    def __init__(self):
        self.supported_types = {'creatures': ['dragon', 'goblin'],
                                'spells': ['fireball'],
                                'artifacts': ['mana_ring']}

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            card = CreatureCard("Unknown", 0, "Unknown", 0, 0)
        if isinstance(name_or_power, int):
            card = CreatureCard("Unknown", 0, "Unknown", name_or_power, 0)
        if isinstance(name_or_power, str):
            card = CreatureCard(name_or_power, 0, "Unknown", 0, 0)
        return card

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            card = SpellCard("Unknown", 0, "Unknown", "None")
        if isinstance(name_or_power, int):
            card = SpellCard("Unknown", 0, "Unknown", "None")
        if isinstance(name_or_power, str):
            card = SpellCard(name_or_power, 0, "Unknown", "None")
        return card

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            card = ArtifactCard("Unknown", 0, "Unknown", 0, "None")
        if isinstance(name_or_power, int):
            card = ArtifactCard("Unknown", 0, "Unknown", 0, "None")
        if isinstance(name_or_power, str):
            card = ArtifactCard(name_or_power, 0, "Unknown", 0, "None")
        return card

    def create_themed_deck(self, size: int) -> dict:
        out_dict: dict = {}
        create_types = self.get_supported_types()
        for i in range(size):
            c_type = random.choice(("Creature", "Spell", "Artefact"))
            created_card = create_types[c_type]()
            out_dict[i] = created_card
        return out_dict

    def get_supported_types(self) -> dict:
        return self.supported_types
