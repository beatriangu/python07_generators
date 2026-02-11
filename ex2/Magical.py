#!/usr/bin/env python3
"""
ex2 - Magical.py
Abstract magic interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict, List


class Magical(ABC):
    """
    Magic interface: any class that can use magic must implement
    this contract.
    """

    @abstractmethod
    def cast_spell(
        self,
        spell_name: str,
        targets: List[Any],
    ) -> Dict[str, Any]:
        """
        Cast a spell on targets and return a spell result dict.
        """

    @abstractmethod
    def channel_mana(self, amount: int) -> Dict[str, Any]:
        """
        Add mana to the internal pool (or channel it) and return a
        result dict.
        """

    @abstractmethod
    def get_magic_stats(self) -> Dict[str, Any]:
        """
        Return magic-related stats (mana, max mana, known spells, etc.).
        """
