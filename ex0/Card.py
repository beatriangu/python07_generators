from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Card(ABC):
    """Abstract base class for all card types."""

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("cost must be a non-negative integer")
        if not isinstance(rarity, str) or not rarity.strip():
            raise ValueError("rarity must be a non-empty string")

        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict[str, Any]) -> dict[str, Any]:
        """Execute the card effect and return a result payload."""
        raise NotImplementedError

    def get_card_info(self) -> dict[str, Any]:
        """Return base card information. Subclasses may extend this dict."""
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.removesuffix("Card"),
        }

    def is_playable(self, available_mana: int) -> bool:
        """Return True if there is enough mana to play this card."""
        if not isinstance(available_mana, int):
            raise TypeError("available_mana must be an integer")
        return available_mana >= self.cost
