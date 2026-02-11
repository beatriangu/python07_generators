from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")

    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
    )

    print("CreatureCard Info:")
    print(creature.get_card_info(), "\n")

    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(6))
    print("Play result:", creature.play({}), "\n")

    print("Fire Dragon attacks Goblin Warrior:")
    print("Attack result:", creature.attack_target("Goblin Warrior"), "\n")

    print("Testing insufficient mana (3 available):")
    print("Playable:", creature.is_playable(3), "\n")

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
