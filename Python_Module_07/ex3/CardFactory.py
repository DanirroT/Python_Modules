#!/usr/bin/env python3


import random
from abc import ABC, abstractmethod
from ex0.Card import Card


class CardFactory(ABC):

    cards_created: int = 0

    @abstractmethod
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        pass

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
