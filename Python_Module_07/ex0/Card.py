
from abc import ABC, abstractmethod


class Card(ABC):
    name: str
    rarity: str
    type: str
    cost: int

    @abstractmethod
    def __init__(self, name: str, cost: int, rarity: str, **kwargs) -> None:

        super().__init__(**kwargs)

        if not name:
            raise ValueError("Card name cannot be empty.")
        self.name = name

        if not rarity:
            raise ValueError("Card rarity cannot be empty.")
        self.rarity = rarity

        self.type = "Typeless"

        try:
            cost_int = int(cost)
        except ValueError:
            raise ValueError("Card cost must be numeric.")
        if cost_int < 0:
            raise ValueError("Card cost must be positive.")
        self.cost = cost_int

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["mana"])
        print("Playable:", playable)
        if playable:
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'Card was played'}
        return {}

    def get_card_info(self) -> dict:
        return self.__dict__

    def is_playable(self, available_mana: int) -> bool:
        if available_mana < self.cost:
            return False
        return True
