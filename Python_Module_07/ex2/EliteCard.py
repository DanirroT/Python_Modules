#!/usr/bin/env python3


from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical





class EliteCard(Card, Combatable, Magical):

    def __init__(self, name: str, cost: int, rarity: str,
                 power: int, defense: int, health: int, combat_type: str,
                 mana: int, **kwargs) -> None:

        super().__init__(name=name, rarity=rarity, cost=cost, power=power, defense=defense, health=health, combat_type=combat_type, mana=mana, 
                         **kwargs)

        self.type = "Elite Card"

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["mana"])
        print("Playable:", playable)
        if playable:
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'EliteCard was summoned'}
        return {}

    def attack(self, target) -> dict:
        return super().attack(target)

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return super().cast_spell(spell_name, targets)
