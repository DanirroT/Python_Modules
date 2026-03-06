#!/usr/bin/env python3

from typing import Optional

from ex0.Card import Card
from ex1.Deck import Deck

from .AggressiveStrategy import AggressiveStrategy  # F401
from .FantasyCardFactory import FantasyCardFactory  # F401
from .GameEngine import GameEngine  # F401


# for this project to work, use:
#   python -m ex3.main
# while in root

class Player():

    name: str
    mana: int
    health: int

    oponents: list["Player"]

    hand: list[Card]
    field: list[Card]
    deck: Deck
    game_state: dict[str, int]

    def __init__(self, name: str):

        if not name:
            raise ValueError("Player name cannot be empty.")
        self.name = name

        self.mana = 0
        self.health = 20

        self.hand = []
        self.field = []

    def set_oponents(self, oponents: list["Player"]) -> None:
        self.oponents = oponents

    def set_deck(self, deck: Deck, shuffe: Optional[bool] = True) -> None:
        self.deck = deck
        if shuffe:
            deck.shuffle()

    def draw(self, quantity: int) -> None:
        self.add_hand(self.deck.draw_card())

    def add_hand(self, card: Card) -> None:
        self.hand.append(card)

    def play_card(self, p_card: Card) -> None:
        for h_card in self.hand:
            if p_card == h_card:
                if h_card.play({"mana": self.mana}):
                    self.field.append(h_card)
                    self.hand.remove(h_card)
                    return

    def set_hand(self, hand: list[Card]) -> None:
        self.hand = hand

    def set_field(self, field: list[Card]) -> None:
        self.field = field

    def get_hand(self) -> list[str]:
        return [f"{card.name} ({card.name})" for card in self.hand]

    def get_field(self) -> list[str]:
        return [f"{card.name} ({card.name})" for card in self.field]

    def get_all_targets(self) -> list[list["Player" | Card]]:
        output_list: list[list["Player" | Card]] = []

        for opponent in self.oponents:
            line_list = [opponent] + opponent.field
            output_list.append(line_list)

        return output_list


if __name__ == "__main__":

    print("=== DataDeck Game Engine ===")

    print()

    print("Configuring Fantasy Card Game...")

    engine = GameEngine()

    player_1 = Player("Frankan")

    player_2 = Player("Eryn")

    player_1.set_oponents([player_2])

    player_2.set_oponents([player_1])

    print("player 1 targets", player_1.get_all_targets())

    engine.configure_engine(FantasyCardFactory, AggressiveStrategy)

    print("Available types:", engine.factory.get_supported_types())

    print()

    print("Simulating aggressive turn...")

    print(engine.simulate_turn())

    print()

    print()

    print("Game Report:")

    print(engine.get_engine_status())

    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")

#         return ([card.name
  #                for opponent in self.oponents
    #              for card in opponent.field]
      #           + [opponent.name for opponent in self.oponents])
