#!/usr/bin/env python3
"""
ex2 - EliteCard.py
Multiple inheritance implementation: Card + Combatable + Magical
"""

from __future__ import annotations

from typing import Any, Dict, List

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Elite card: combines combat + magic using multiple inheritance.
    Must implement Card + Combatable + Magical contracts.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        mana: int,
        combat_type: str = "melee",
    ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)
        self.attack_power = attack_power
        self.defense = defense
        self.mana = mana
        self.combat_type = combat_type

    # -------- Card requirement --------
    def play(self, game_state: dict) -> dict:
        """
        Required by Card.
        Keep simple but consistent: check mana when provided.
        """
        available = int(game_state.get("available_mana", self.mana))
        playable = available >= self.cost
        mana_used = self.cost if playable else 0

        return {
            "card_played": self.name,
            "mana_used": mana_used,
            "type": "Elite Card",
            "playable": playable,
        }

    # -------- Combatable interface --------
    def attack(self, target: Any) -> Dict[str, Any]:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": self.combat_type,
        }

    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        blocked = max(0, self.defense)
        taken = max(0, incoming_damage - blocked)

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True,
        }

    def get_combat_stats(self) -> Dict[str, Any]:
        return {
            "attack": self.attack_power,
            "defense": self.defense,
            "combat_type": self.combat_type,
        }

    # -------- Magical interface --------
    def cast_spell(
        self,
        spell_name: str,
        targets: List[Any],
    ) -> Dict[str, Any]:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": [str(t) for t in targets],
            "mana_used": 4,
        }

    def channel_mana(self, amount: int) -> Dict[str, Any]:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana,
        }

    def get_magic_stats(self) -> Dict[str, Any]:
        return {
            "mana": self.mana,
        }
