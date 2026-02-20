from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

        self.hand: list = []
        self.battlefield: list = []

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        self.factory = factory
        self.strategy = strategy

        themed = factory.create_themed_deck(size=3)
        self.hand = themed["hand"]
        self.battlefield = themed["battlefield"]
        self.cards_created = len(self.hand)

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise RuntimeError("Engine not configured")

        result = self.strategy.execute_turn(
            self.hand,
            self.battlefield,
        )

        self.turns_simulated += 1
        self.total_damage += int(
            result["actions"]["damage_dealt"]
        )

        return result

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            strategy_name = None
        else:
            strategy_name = self.strategy.get_strategy_name()

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
