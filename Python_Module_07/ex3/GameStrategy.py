#!/usr/bin/env python3


from abc import ABC, abstractmethod


class GameStrategy(ABC):

    total_damage: int = 0

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        pass
