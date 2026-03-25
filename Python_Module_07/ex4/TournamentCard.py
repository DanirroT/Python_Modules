#!/usr/bin/env python3


from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name: str, cost: int, rarity: str,
                 power: int, defense: int, health: int, combat_type: str,
                 rank_id: str, rating: int, wins: int, losses: int,
                 **kwargs) -> None:

        super().__init__(name=name, cost=cost, rarity=rarity,
                         power=power, defense=defense, health=health,
                         combat_type=combat_type,
                         rank_id=rank_id, rating=rating, wins=wins,
                         losses=losses,
                         **kwargs)

    def play(self, game_state: dict) -> dict:
        return super().play(game_state)

    def attack(self, target) -> dict:
        return super().attack(target)

    def calculate_rating(self) -> int:
        return super().calculate_rating()

    def update_wins(self, wins: int) -> None:
        super().update_wins(wins)

    def update_losses(self, losses: int) -> None:
        super().update_losses(losses)

    def get_rank_info(self) -> dict:
        return super().get_rank_info()

    def get_tournament_stats(self) -> dict:
        print(f"{self.name} (ID: {self.rank_id})")

        interfacing = [cls.__name__ for cls in self.__class__.__bases__]

        print(f"- Interfaces: {interfacing})")
        print(f"- Rating: {self.rating}")
        print(f"- Record: {self.wins}-{self.losses}")

        return {
            "Name": self.name,
            "ID": self.rank_id,
            "Interfaces": [cls.__name__
                           for cls in self.__class__.__bases__],
            "Rating": self.rating,
            "Record": (self.wins, self.losses)
        }
