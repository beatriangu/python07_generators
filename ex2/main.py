#!/usr/bin/env python3
"""
Exercise 2 demo script (required).
Run from repo root:
    python3 -m ex2.main
"""

from __future__ import annotations

from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', "
          "'get_magic_stats']\n")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Epic",
        attack_power=5,
        defense=3,
        mana=4,
        combat_type="melee",
    )

    print("Playing Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(5)}\n")

    print("Magic phase:")
    print(
        f"Spell cast: "
        f"{elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {elite.channel_mana(3)}")

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
