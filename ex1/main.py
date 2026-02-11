#!/usr/bin/env python3
"""
Exercise 1 demo script (required).
Run from repo root:
    python3 -m ex1.main
"""

from __future__ import annotations

from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .Deck import Deck
from .SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")

    deck = Deck()

    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
    )
    spell = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="damage",
    )
    artifact = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=10,
        effect="Permanent: +1 mana per turn",
    )

    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)

    # Para que el expected coincida (avg_cost: 4.0) y el orden de robos:
    # el subject parece asumir un shuffle o un orden concreto.
    # Si tu Deck.shuffle() existe, úsalo. Si no, elimina esta línea.
    deck.shuffle()

    print(f"Deck stats: {deck.get_deck_stats()}\n")
    print("Drawing and playing cards:\n")

    game_state = {"available_mana": 10, "targets": ["target"]}

    for _ in range(3):
        card = deck.draw_card()
        info = card.get_card_info()
        print(f"Drew: {info['name']} ({info['type']})")

        result = card.play(game_state)
        print(f"Play result: {result}\n")

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
