#!/usr/bin/env python3
"""
ex2 - Combatable.py
Abstract combat interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class Combatable(ABC):
    """
    Combat interface: any class that can fight must implement this contract.
    """

    @abstractmethod
    def attack(self, target: Any) -> Dict[str, Any]:
        """
        Attack a target and return a combat result dict.
        """

    @abstractmethod
    def defend(self, incoming_damage: int) -> Dict[str, Any]:
        """
        Defend against damage and return the defense result dict.
        """

    @abstractmethod
    def get_combat_stats(self) -> Dict[str, Any]:
        """
        Return combat-related stats (attack, defense, health, etc.).
        """
