#!/usr/bin/env python3
"""
ex1 - SpellCard.py
Concrete card type: SpellCard
"""

from __future__ import annotations

from typing import Dict, List

from ex0.Card import Card


class SpellCard(Card):
    """
    Concrete implementation of a spell card.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        effect_type: str,
    ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> Dict:
        """
        Play the spell and return a result dict.
        """
        effect_result = self.resolve_effect(
            targets=game_state.get("targets", [])
        )
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": effect_result["effect"],
        }

    def resolve_effect(self, targets: List) -> Dict:
        """
        Resolve the spell effect against given targets.
        """
        if self.effect_type == "damage":
            return {
                "effect": "Deal 3 damage to target",
                "targets": targets,
            }

        if self.effect_type == "heal":
            return {
                "effect": "Restore 3 health to target",
                "targets": targets,
            }

        return {
            "effect": "Apply a mysterious effect",
            "targets": targets,
        }
