from __future__ import annotations

from typing import Any

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        defense: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name=name, cost=cost, rarity=rarity)

        self.card_id = card_id
        self.attack_power = attack_power
        self.defense = defense

        self._wins = 0
        self._losses = 0
        self._rating = rating

    # -------- Card --------
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament card enters competitive battlefield",
        }

    # -------- Combatable --------
    def attack(self, target: Any) -> dict[str, Any]:
        target_name = getattr(target, "name", None)
        if not isinstance(target_name, str) or not target_name:
            target_name = str(target)

        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict[str, Any]:
        blocked = min(self.defense, incoming_damage)
        taken = incoming_damage - blocked

        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": True,
        }

    def get_combat_stats(self) -> dict[str, int]:
        return {
            "attack_power": self.attack_power,
            "defense": self.defense,
        }

    # -------- Rankable --------
    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins = wins

    def update_losses(self, losses: int) -> None:
        self._losses = losses

    def get_rank_info(self) -> dict[str, Any]:
        return {
            "rating": self._rating,
            "wins": self._wins,
            "losses": self._losses,
            "record": f"{self._wins}-{self._losses}",
        }

    # -------- Helpers --------
    def apply_rating_delta(self, delta: int) -> None:
        self._rating = max(1, self._rating + delta)

    def get_tournament_stats(self) -> dict[str, Any]:
        info = self.get_rank_info()

        return {
            "id": self.card_id,
            "name": self.name,
            "interfaces": ["Card", "Combatable", "Rankable"],
            "rating": info["rating"],
            "record": info["record"],
        }
