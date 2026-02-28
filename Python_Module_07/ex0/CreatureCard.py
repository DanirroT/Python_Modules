#!/usr/bin/env python3


from .Card import Card


class CreatureCard(Card):
    attack: int
    health: int

    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:

        super().__init__(name, rarity, cost)

        self.type = "Creature"

        try:
            attack_int = int(attack)
        except ValueError:
            raise ValueError("Card attack must be numeric.")
        if attack_int < 0:
            raise ValueError("Card attack must be positive.")
        self.attack = attack_int

        try:
            health_int = int(health)
        except ValueError:
            raise ValueError("Card health must be numeric.")
        if health_int < 0:
            raise ValueError("Card health must be positive.")
        self.health = health

    def play(self, game_state: dict) -> dict:
        playable = self.is_playable(game_state["mana"])
        print("Playable:", playable)
        if playable:
            return {'card_played': self.name, 'mana_used': self.cost,
                    'effect': 'Creature summoned to battlefield'}
        return {}

    def attack_target(self, target: "CreatureCard") -> dict:
        if target.health > self.attack:
            resolved = False
        else:
            resolved = True
        return {'attacker': self.name, 'target': target.name,
                'damage_dealt': self.attack, 'combat_resolved': resolved}
