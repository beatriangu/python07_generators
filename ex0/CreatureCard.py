from __future__ import annotations

from typing import Any

from .Card import Card


class CreatureCard(Card):
    """Concrete implementation of a creature card."""

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        # Validate: integers (avoid floats/strings) and strictly positive.
        # bool is a subclass of int, so exclude it explicitly.
        if type(attack) is not int:
            raise TypeError("attack must be an integer")
        if type(health) is not int:
            raise TypeError("health must be an integer")
        if attack <= 0 or health <= 0:
            raise ValueError(
                "attack and health must be positive integers"
            )

        self.attack = attack
        self.health = health

    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Play the creature card and return the effect payload."""
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: str) -> dict[str, Any]:
        """Attack a target and return a combat result payload."""
        if not isinstance(target, str) or not target.strip():
            raise ValueError("target must be a non-empty string")

        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> dict[str, Any]:
        """Return base card info extended with creature stats."""
        info = super().get_card_info()
        info.update({"attack": self.attack, "health": self.health})
        return info
