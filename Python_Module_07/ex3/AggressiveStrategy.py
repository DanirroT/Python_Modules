#!/usr/bin/env python3

from .GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard

import re


class AggressiveStrategy(GameStrategy):

    def execute_turn(self, hand: list[Card], battlefield: list[CreatureCard]
                     ) -> dict:

        priorities = self.prioritize_targets(battlefield)

        atk_list: list[Card] = []

        atk_list = [card for card in sorted(hand, key=lambda c: c.cost)][:2]

        mana_cost = 0
        dmg_dealt = 0

        for card in atk_list:

            mana_cost += card.cost
            if isinstance(card, CreatureCard):
                dmg_dealt += card.attack

            elif isinstance(card, SpellCard):
                match = re.search(r"(\d+)\sdamage", card.effect_type)
                dmg_dealt += int(match.group(1)) if match else 0

            elif isinstance(card, ArtifactCard):
                match = re.search(r"(\d+)\sdamage", card.effect)
                dmg_dealt += int(match.group(1)) if match else 0

        self.total_damage += dmg_dealt

        atk_list_names = [card.name for card in atk_list]

        tgt_list_names = [target.name
                          for target in priorities][:1]

        return {'cards_played': atk_list_names,
                'mana_used': mana_cost,
                'targets_attacked': tgt_list_names,
                'damage_dealt': dmg_dealt}

    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: list[CreatureCard]
                           ) -> list[CreatureCard]:
        return sorted(available_targets, key=lambda t: (t.health, -t.attack))
