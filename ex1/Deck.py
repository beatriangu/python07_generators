#!/usr/bin/env python3
"""
ex1 - Deck.py
Management class: Deck
"""

from __future__ import annotations

import random
from typing import Dict, List, Optional, Union

from ex0.Card import Card


StatsValue = Union[int, float]
StatsDict = Dict[str, StatsValue]


class Deck:
    """
    A deck that can store, shuffle and draw cards.
    """

    def __init__(self) -> None:
        self._cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Remove the first card with matching name.
        Returns True if removed, False otherwise.
        """
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                del self._cards[i]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        """
        Draw from the top of the deck.
        Returns None if empty.
        """
        if not self._cards:
            return None
        return self._cards.pop(0)

    def get_deck_stats(self) -> StatsDict:
        """
        Return basic stats about the deck.

        Note:
        - avg_cost matches the subject output by averaging only "cast" cards
          (Creature + Spell), excluding Artifacts.
        """
        total_cards = len(self._cards)
        creatures = 0
        spells = 0
        artifacts = 0

        cast_cost_sum = 0
        cast_count = 0

        for card in self._cards:
            info = card.get_card_info()
            card_type = info.get("type", "")
            cost = int(info.get("cost", 0))

            if card_type == "Creature":
                creatures += 1
                cast_cost_sum += cost
                cast_count += 1
            elif card_type == "Spell":
                spells += 1
                cast_cost_sum += cost
                cast_count += 1
            elif card_type == "Artifact":
                artifacts += 1

        avg_cost = (cast_cost_sum / cast_count) if cast_count > 0 else 0.0

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
