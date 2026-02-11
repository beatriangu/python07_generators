#!/usr/bin/env python3
"""
ex1 - ArtifactCard.py
Concrete card type: ArtifactCard
"""

from __future__ import annotations

from typing import Dict

from ex0.Card import Card


class ArtifactCard(Card):
    """
    Concrete implementation of an artifact card.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> Dict:
        """
        Play the artifact and return a result dict.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect,
        }

    def activate_ability(self) -> Dict:
        """
        Activate the artifact ability and return a result dict.
        """
        if self.durability <= 0:
            return {
                "artifact": self.name,
                "activated": False,
                "durability": self.durability,
            }

        self.durability -= 1
        return {
            "artifact": self.name,
            "activated": True,
            "durability": self.durability,
        }
