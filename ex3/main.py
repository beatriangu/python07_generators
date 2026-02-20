from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def format_hand(hand: list) -> str:
    parts = []
    for card in hand:
        info = card.get_card_info()
        parts.append(f"{info['name']} ({info['cost']})")
    return "[" + ", ".join(parts) + "]"


def main() -> None:
    print()
    print("=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print("Factory:", factory.__class__.__name__)
    print("Strategy:", strategy.get_strategy_name())
    print("Available types:", factory.get_supported_types())

    print("\nSimulating aggressive turn...")
    print("Hand:", format_hand(engine.hand))

    print("\nTurn execution:")
    turn_result = engine.simulate_turn()
    print("Strategy:", turn_result["strategy"])
    print("Actions:", turn_result["actions"])

    print("\nGame Report:")
    print(engine.get_engine_status())

    print(
        "\nAbstract Factory + Strategy Pattern: "
        "Maximum flexibility achieved!"
    )


if __name__ == "__main__":
    main()
