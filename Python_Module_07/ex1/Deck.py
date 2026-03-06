#!/usr/bin/env python3


from ex0.Card import Card
import random


class Deck():
    card_list: list[Card]

    def __init__(self, name: str) -> None:

        if not name:
            raise ValueError("Card name cannot be empty.")
        self.name = name
        self.card_list = []

    def add_card(self, card: Card) -> None:
        self.card_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.card_list:
            if card.name == card_name:
                self.card_list.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.card_list)

    def draw_card(self) -> Card:
        out_card = self.card_list[0]
        self.remove_card(out_card.name)
        print("Drew:", out_card.name, f"({out_card.type})")
        return out_card

    def get_deck_stats(self) -> dict:
        count_cards = 0
        count_creatures = 0
        count_spells = 0
        count_artefacts = 0
        cost_list: list[int] = []
        for card in self.card_list:
            if card.type == "Creature":
                count_creatures += 1
            if card.type == "Spell":
                count_spells += 1
            if card.type == "Artefact":
                count_artefacts += 1
            cost_list.append(card.cost)
            count_cards += 1
        cost_sum = sum(cost_list)
        cost_num = len(cost_list)
        cost_avg = cost_sum / cost_num
        return {'total_cards': count_cards, 'creatures': count_creatures,
                'spells': count_spells, 'artifacts': count_artefacts,
                'avg_cost': cost_avg}
