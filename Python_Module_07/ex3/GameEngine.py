#!/usr/bin/env python3


from .GameStrategy import GameStrategy
from .CardFactory import CardFactory

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class GameEngine():

    factory: CardFactory
    strategy: GameStrategy

    turns_simulated: int = 0

    targets: list[CreatureCard]
    hand: list[Card]

    def set_targets(self, targets: list[CreatureCard]) -> None:
        self.targets = targets.copy()

    def set_hand(self, hand: list[Card]) -> None:
        self.hand = hand.copy()

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy
                         ) -> None:
        self.factory = factory()
        print("Factory:", self.factory.__class__.__name__)
        self.strategy = strategy()
        print("Strategy:", self.strategy.__class__.__name__)

    def simulate_turn(self) -> dict:
        prioritized_targets = self.strategy.prioritize_targets(self.targets)
        self.turns_simulated += 1
        return self.strategy.execute_turn(self.hand, prioritized_targets)

    def get_engine_status(self) -> dict:
        return {'turns_simulated': self.turns_simulated,
                'strategy_used': self.strategy.get_strategy_name(),
                'total_damage': self.strategy.total_damage,
                'cards_created': self.factory.cards_created}
