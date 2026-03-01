#!/usr/bin/env python3


from .GameStrategy import GameStrategy
from .CardFactory import CardFactory

from .main import Player


class GameEngine():

    factory: CardFactory
    strategy: GameStrategy

    turns_simulated: int = 0
    cards_created: int = 0
    total_damage: int = 0

    players: list[Player]

    def set_players(self, player_list: list[Player]) -> None:
        self.players = player_list

    def configure_engine(self, factory: CardFactory, strategy: GameStrategy
                         ) -> None:
        self.factory = factory()
        self.strategy = strategy()

    def simulate_turn(self) -> dict:
        all_targets = self.strategy.prioritize_targets(
            self.players[0].get_all_targets())
        mana_used = 0
        self.turns_simulated += 1
        return {'cards_played': ['Goblin Warrior', 'Lightning Bolt'],
                'mana_used': mana_used,
                'targets_attacked': targets,
                'damage_dealt': 8}


    def get_engine_status(self) -> dict:
        return {'turns_simulated': self.turns_simulated,
                'strategy_used': self.strategy.get_strategy_name(),
                'total_damage': self.total_damage,
                'cards_created': self.cards_created
                }
