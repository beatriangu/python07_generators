from __future__ import annotations

from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Abstract ranking interface.

    Any class implementing Rankable must provide
    rating calculation and win/loss tracking behaviour.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Return the current rating as an integer.
        """
        raise NotImplementedError

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Update (set) the number of wins.
        """
        raise NotImplementedError

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Update (set) the number of losses.
        """
        raise NotImplementedError

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Return ranking-related information
        such as wins, losses, and rating.
        """
        raise NotImplementedError
