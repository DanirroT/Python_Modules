#!/usr/bin/env python3


from abc import ABC, abstractmethod
from ex0.Card import Card


class Combatable(ABC):


    power: int
    defense: int
    health: int
    combat_type: str

    @abstractmethod
    def __init__(self, power: int, defense: int, health: int, combat_type: str, **kwargs
                 ) -> None:
        super().__init__(**kwargs)
        try:
            power_int = int(power)
        except ValueError:
            raise ValueError("Card power must be numeric.")
        if power_int < 0:
            raise ValueError("Card power must be positive.")
        self.power = power_int

        try:
            defense_int = int(defense)
        except ValueError:
            raise ValueError("Card defense must be numeric.")
        if defense_int < 0:
            raise ValueError("Card defense must be positive.")
        self.defense = defense_int

        try:
            health_int = int(health)
        except ValueError:
            raise ValueError("Card health must be numeric.")
        if health_int < 0:
            raise ValueError("Card health must be positive.")
        self.health = health

        if not combat_type or combat_type == "":
            raise ValueError("Card combat type cannot be empty.")
        self.combat_type = combat_type

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = min(incoming_damage, self.defense)
        damage_taken = (incoming_damage - damage_blocked
                        if incoming_damage - damage_blocked > 0 else 0)

        self.health -= damage_taken

        if self.health <= 0:
            still_alive = False
        else:
            still_alive = True
            self.health -= damage_taken
        return {'defender': self.name, 'damage_taken': damage_taken,
                'damage_blocked': damage_blocked, 'still_alive': still_alive}

    def get_combat_stats(self) -> dict:
        return self.__dict__

    def attack(self, target) -> dict:
        if isinstance(target, Card):
            target_name = target.name
        else:
            target_name = target

        return {'attacker': self.name, 'target': target_name,
                'damage': self.power, 'combat_type': self.combat_type}
