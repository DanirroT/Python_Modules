#!/usr/bin/env python3


from ex0.Card import Card


class SpellCard(Card):
    effect_type: str

    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str):

        super().__init__(name, rarity, cost)

        self.type = "Spell"

        if not effect_type or effect_type == "":
            raise ValueError("Card effect type cannot be empty.")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["mana"])
        print("Playable:", playable)
        if playable:
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': self.effect_type}
        return {}

    def resolve_effect(self, targets: list) -> dict:
        if isinstance(targets[0], str):
            target_list = targets
        if isinstance(targets[0], Card):
            target_list = [card.name for card in targets]
        return {'targets': target_list, 'effect': self.effect_type}
