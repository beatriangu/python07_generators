from typing import Dict
from .Card import Card


class CreatureCard(Card):
    """
    Concrete implementation of a creature card.
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0 or health <= 0:
            raise ValueError("Attack and health must be positive integers")

        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """
        Play the creature card.
        """
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target: str) -> Dict[str, object]:
        """
        Perform an attack on a target.
        """
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True,
        }

    def get_card_info(self) -> Dict[str, object]:
        """
        Extend base card info with creature stats.
        """
        info = super().get_card_info()
        info.update({
            "attack": self.attack,
            "health": self.health,
        })
        return info
