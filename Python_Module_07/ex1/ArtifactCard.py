#!/usr/bin/env python3


from ex0.Card import Card


class ArtifactCard(Card):
    durability: int
    effect: str

    def __init__(self, name: str, cost: int, rarity: str,
                 durability: int, effect: str) -> None:

        super().__init__(name, cost, rarity)

        self.type = "Artefact"

        try:
            durability_int = int(durability)
        except ValueError:
            raise ValueError("Card durability must be numeric.")
        if durability_int < 0:
            raise ValueError("Card durability must be positive.")
        self.durability = durability_int

        if not effect«:
            raise ValueError("Card effect cannot be empty.")
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["mana"])
        print("Playable:", playable)
        if playable:
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': self.effect}
        return {}

    def activate_ability(self) -> dict:
        return {'effect': self.effect}
