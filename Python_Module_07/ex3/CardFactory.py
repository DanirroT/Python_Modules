#!/usr/bin/env python3


import random
from abc import ABC, abstractmethod
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard


class CardFactory(ABC):

    cards_created: int = 0

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            card = CreatureCard("Unknown", 0, "Unknown", 0, 0)
        if isinstance(name_or_power, int):
            card = CreatureCard("Unknown", 0, "Unknown", name_or_power, 0)
        if isinstance(name_or_power, str):
            card = CreatureCard(name_or_power, 0, "Unknown", 0, 0)
        return card

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            card = SpellCard("Unknown", 0, "Unknown", "None")
        if isinstance(name_or_power, int):
            card = SpellCard("Unknown", 0, "Unknown", "None")
        if isinstance(name_or_power, str):
            card = SpellCard(name_or_power, 0, "Unknown", "None")
        return card

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if not name_or_power:
            card = ArtifactCard("Unknown", 0, "Unknown", 0, "None")
        if isinstance(name_or_power, int):
            card = ArtifactCard("Unknown", 0, "Unknown", 0, "None")
        if isinstance(name_or_power, str):
            card = ArtifactCard(name_or_power, 0, "Unknown", 0, "None")
        return card

    @abstractmethod
    def create_themed_deck(self, size: int) -> dict:
        out_dict: dict = {}

        create_types = {
            "Creature": self.create_creature,
            "Spell": self.create_spell,
            "Artefact": self.create_artifact
        }

        for i in range(size):
            c_type = random.choice(("Creature", "Spell", "Artefact"))
            created_card = create_types[c_type]()
            out_dict[i] = created_card
        return out_dict

    @abstractmethod
    def get_supported_types(self) -> dict:
        pass

        out_dict: dict[str, list[str]] = {}

        for card in deck:
            if isinstance(card, CreatureCard):
                if not out_dict.get("creatures"):
                    out_dict["creatures"] = []
                out_dict["creatures"].append(card.name)

            if isinstance(card, SpellCard):
                if not out_dict.get("spells"):
                    out_dict["spells"] = []
                out_dict["spells"].append(card.name)

            if isinstance(card, ArtifactCard):
                if not out_dict.get("artifacts"):
                    out_dict["artifacts"] = []
                out_dict["artifacts"].append(card.name)

        return out_dict
