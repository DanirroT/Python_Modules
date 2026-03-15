#!/usr/bin/env python3

from abc import ABC, abstractmethod


class Rankable(ABC):

    rank_id: str
    wins: int
    losses: int
    original_rating: int
    rating: int

    def __init__(self, rank_id: str, rating: int, wins: int, losses: int,
                 **kwargs) -> None:

        super().__init__(**kwargs)

        self.rank_id = rank_id
        self.original_rating = rating
        self.rating = rating
        self.wins = wins
        self.losses = losses

    @abstractmethod
    def calculate_rating(self) -> int:
        self.rating = (self.original_rating
                       + (self.wins * 16)
                       - (self.losses * 16))

        return self.rating

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        self.wins += wins

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        self.losses += losses

    @abstractmethod
    def get_rank_info(self) -> dict:
        return {"rating": self.rating,
                "wins": self.wins, "losses": self.losses}
