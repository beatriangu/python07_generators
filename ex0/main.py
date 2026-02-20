from __future__ import annotations

from .CreatureCard import CreatureCard


def main() -> None:
    """Demonstration of the Card abstract base class design."""

    print("\n=== DataDeck · Card Foundation (ex0) ===\n")

    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
    )

    # Display card information
    print("CreatureCard info:")
    print(creature.get_card_info())
    print()

    # Test playable state
    available_mana = 6
    print(f"Playing with {available_mana} mana available:")
    print("Playable:", creature.is_playable(available_mana))
    print("Play result:", creature.play({}))
    print()

    # Test combat
    print("Combat demonstration:")
    print(
        "Attack result:",
        creature.attack_target("Goblin Warrior"),
    )
    print()

    # Test insufficient mana
    available_mana = 3
    print(f"Testing insufficient mana ({available_mana} available):")
    print("Playable:", creature.is_playable(available_mana))
    print()

    print("Abstract pattern successfully demonstrated!\n")


if __name__ == "__main__":
    main()
