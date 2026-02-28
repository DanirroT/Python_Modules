#!/usr/bin/env python3


from abc import ABC, abstractmethod
from ex0.Card import Card


class Magical(ABC):
    mana: int

    @abstractmethod
    def __init__(self, mana: int, **kwargs) -> None:

        super().__init__(**kwargs)

        try:
            mana_int = int(mana)
        except ValueError:
            raise ValueError("Card mana must be numeric.")
        if mana_int < 0:
            raise ValueError("Card mana must be positive.")
        self.mana = mana_int

    def channel_mana(self, amount: int) -> dict:
        if self.mana - amount < 0:
            return {'channeled': 0, 'total_mana': self.mana}
        self.mana -= amount
        return {'channeled': amount, 'total_mana': self.mana}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 2
        if self.mana - mana_cost:
            return {'caster': self.name, 'spell': None,
                    'targets': [], 'mana_used': 0}
        self.mana -= mana_cost
        return {'caster': self.name, 'spell': spell_name,
                'targets': targets, 'mana_used': mana_cost}

    def get_magic_stats(self) -> dict:
        return self.__dict__
