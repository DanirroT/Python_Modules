#!/usr/bin/env python3

from .GameStrategy import GameStrategy
from ex0.Card import Card

import re

from .main import Player


class AggressiveStrategy(GameStrategy):

    player: Player

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        return {}

    def get_strategy_name(self) -> str:
        return super().get_strategy_name()

    def prioritize_targets(self, available_targets: list[list["Player" | Card]]
                           ) -> list[tuple[str, str, Card, Player, Card, int]]:

        out_list: list[tuple[str, str, Card, Player, Card, int]] = []

        for attacker in self.player.field:

            to_list = None
            oponent = None
            chosen_target = None
            hp_remainin = None

            if attacker.type == "Creature":
                card_power = attacker.attack
            if attacker.type == "Artefact":
                if "damage" in card.effect:
                    match = re.search(r"(\d+)\sdamage", card.effect)
                    card_power = int(match.group(1))





            if to_list:
                out_list.append((
                    "field", attacker.type, attacker,
                    oponent, chosen_target, hp_remainin
                ))

        for card in self.player.hand:

            to_list = None
            oponent = None
            chosen_target = None
            hp_remainin = None

            if card.type == "Spell":
                if "damage" in card.effect:
                    match = re.search(r"(\d+)\sdamage", card.effect)
                    card_power = int(match.group(1))

                    for target in available_targets:
                        if target in out_list:
                            target_hp = out_list
                        else:



            if to_list:
                out_list.append((
                    "field", attacker.type, attacker,
                    oponent, chosen_target, hp_remainin
                ))






        priority_helath = 0
        priority_target: Card
        for target in available_targets:
            if priority_helath == 0 or target.health < priority_helath:
                priority_helath = target.health
                priority_target = target
        return out_list
