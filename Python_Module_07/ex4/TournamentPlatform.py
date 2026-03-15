#!/usr/bin/env python3

from .TournamentCard import TournamentCard


class TournamentPlatform():

    registered_cards: list[TournamentCard]
    matches_played: int

    def __init__(self) -> None:
        self.matches_played = 0
        self.registered_cards = []

    def register_card(self, card: TournamentCard) -> str:

        self.registered_cards.append(card)

        return ""

    def create_match(self, card1_id: str, card2_id: str) -> dict:

        card1 = None
        card2 = None

        for card in self.registered_cards:
            if card1_id == card.rank_id:
                card1 = card
            if card2_id == card.rank_id:
                card2 = card

        if not card1 or not card2:
            return None

        if not card2.defend(card1.attack(card2)["damage"])["still_alive"]:
            winner = card1
            card1.update_wins(1)
            loser = card2
            card2.update_losses(1)
        elif not card1.defend(card2.attack(card1)["damage"])["still_alive"]:
            winner = card2
            card2.update_wins(1)
            loser = card1
            card1.update_losses(1)
        else:
            winner = None
            loser = None

        self.matches_played += 1

        if winner and loser:

            return {'winner': winner.rank_id, 'loser': loser.rank_id,
                    'winner_rating': winner.calculate_rating(),
                    'loser_rating': loser.calculate_rating()}

        return {}

    def get_leaderboard(self) -> list:
        print("Tournament Leaderboard:")

        sort = [card for card in
                sorted(self.registered_cards, key=(lambda card: card.rating), reverse=True)]

        for i, card in enumerate(sort, start=1):
            print(f"{i}. {card.name} - Rating: "
                  f"{card.rating} ({card.wins}-{card.losses})")

        return sort

    def generate_tournament_report(self) -> dict:

        card_len = len(self.registered_cards)
        card_rating_sum = sum([card.rating for card in self.registered_cards])
        card_rating_avg = int(card_rating_sum / card_len)

        return {
            'total_cards': card_len, 'matches_played': self.matches_played,
            'avg_rating': card_rating_avg, 'platform_status': 'active'
        }
