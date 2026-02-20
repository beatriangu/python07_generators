from __future__ import annotations

from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===\n")
    print("Registering Tournament Cards...\n")

    platform = TournamentPlatform()

    dragon = TournamentCard(
        card_id="dragon_001",
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack_power=7,
        defense=3,
        rating=1200,
    )

    wizard = TournamentCard(
        card_id="wizard_001",
        name="Ice Wizard",
        cost=4,
        rarity="Epic",
        attack_power=5,
        defense=4,
        rating=1150,
    )

    platform.register_card(dragon)
    platform.register_card(wizard)

    for card in (dragon, wizard):
        stats = card.get_tournament_stats()

        print(f"{stats['name']} (ID: {stats['id']}):")
        print(f" - Interfaces: {stats['interfaces']}")
        print(f" - Rating: {stats['rating']}")
        print(f" - Record: {stats['record']}\n")

    print("Creating tournament match...\n")

    result = platform.create_match(
        "dragon_001",
        "wizard_001",
    )

    print(
        "Match result: "
        f"{{'winner': '{result['winner']}', "
        f"'loser': '{result['loser']}', "
        f"'winner_rating': {result['winner_rating']}, "
        f"'loser_rating': {result['loser_rating']}}}\n"
    )

    print("Tournament Leaderboard:")

    leaderboard = platform.get_leaderboard()

    for row in leaderboard:
        print(
            f"{row['rank']}. {row['name']} - "
            f"Rating: {row['rating']} "
            f"({row['record']})"
        )

    print()

    print("Platform Report:")
    report = platform.generate_tournament_report()
    print(report)

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print(
        "All abstract patterns working together "
        "harmoniously!\n"
    )


if __name__ == "__main__":
    main()
