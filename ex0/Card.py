from abc import ABC, abstractmethod
from typing import Any, Dict


class Card(ABC):
    """
    Abstract base class representing a generic card.
    """

    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Play the card and modify the game state.
        """

    def get_card_info(self) -> Dict[str, object]:
        """
        Return basic card information.
        """
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.__class__.__name__.replace("Card", ""),
        }

    def is_playable(self, available_mana: int) -> bool:
        """
        Check if the card can be played with the given mana.
        """
        return available_mana >= self.cost
