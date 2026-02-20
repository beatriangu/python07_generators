from __future__ import annotations

import random
from typing import Dict, List

from .TournamentCard import TournamentCard


class TournamentPlatform:
    """
    Tournament manager that:
    - registers TournamentCard instances
    - creates matches
    - updates wins/losses and rating using an ELO system
    - provides leaderboard and platform report
    """

    def __init__(self) -> None:
        self._cards: Dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Register a TournamentCard in the platform.
        Idempotent: registering the same card_id again
        returns the same id.
        """
        if not isinstance(card, TournamentCard):
            raise TypeError("card must be a TournamentCard")

        if card.card_id in self._cards:
            return card.card_id

        self._cards[card.card_id] = card
        return card.card_id

    @staticmethod
    def _expected_score(rating_a: int, rating_b: int) -> float:
        """
        ELO expected score:
        E = 1 / (1 + 10^((Rb - Ra)/400))
        """
        return 1.0 / (
            1.0 + 10 ** ((rating_b - rating_a) / 400.0)
        )

    @staticmethod
    def _elo_new_rating(
        old_rating: int,
        score: float,
        expected: float,
        k_factor: int,
    ) -> int:
        """
        ELO rating update:
        R_new = R_old + K * (S - E)
        """
        new_val = old_rating + (
            k_factor * (score - expected)
        )
        return int(round(new_val))

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Create and resolve a match between two
        registered TournamentCards.
        """
        if card1_id not in self._cards or card2_id not in self._cards:
            raise ValueError(
                "Both card IDs must be registered"
            )

        if card1_id == card2_id:
            raise ValueError(
                "A card cannot play against itself"
            )

        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]

        if c1.attack_power > c2.attack_power:
            winner, loser = c1, c2
        elif c2.attack_power > c1.attack_power:
            winner, loser = c2, c1
        else:
            winner, loser = random.choice(
                [(c1, c2), (c2, c1)]
            )

        k_factor = 37

        r1_old = c1.calculate_rating()
        r2_old = c2.calculate_rating()

        e1 = self._expected_score(r1_old, r2_old)
        e2 = self._expected_score(r2_old, r1_old)

        if winner is c1:
            s1, s2 = 1.0, 0.0
        else:
            s1, s2 = 0.0, 1.0

        r1_new = self._elo_new_rating(
            r1_old,
            s1,
            e1,
            k_factor,
        )
        r2_new = self._elo_new_rating(
            r2_old,
            s2,
            e2,
            k_factor,
        )

        winner_old = winner.calculate_rating()
        loser_old = loser.calculate_rating()

        c1.apply_rating_delta(r1_new - r1_old)
        c2.apply_rating_delta(r2_new - r2_old)

        winner.update_wins(
            winner.get_rank_info()["wins"] + 1
        )
        loser.update_losses(
            loser.get_rank_info()["losses"] + 1
        )

        self._matches_played += 1

        return {
            "winner": winner.card_id,
            "loser": loser.card_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
            "winner_old_rating": winner_old,
            "loser_old_rating": loser_old,
        }

    def get_leaderboard(self) -> List[dict]:
        ordered = sorted(
            self._cards.values(),
            key=lambda c: c.calculate_rating(),
            reverse=True,
        )

        leaderboard: List[dict] = []
        for idx, card in enumerate(ordered, start=1):
            info = card.get_rank_info()
            leaderboard.append(
                {
                    "rank": idx,
                    "name": card.name,
                    "rating": info["rating"],
                    "record": info["record"],
                    "id": card.card_id,
                }
            )

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self._cards)
        avg_rating = 0

        if total_cards > 0:
            avg_rating = sum(
                card.calculate_rating()
                for card in self._cards.values()
            ) // total_cards

        return {
            "total_cards": total_cards,
            "matches_played": self._matches_played,
            "avg_rating": avg_rating,
            "platform_status": "active",
        }
