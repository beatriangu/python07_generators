from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        # Prefer attacking the Enemy Player first
        if "Enemy Player" in available_targets:
            return [
                "Enemy Player",
                *[
                    t for t in available_targets
                    if t != "Enemy Player"
                ],
            ]
        return available_targets

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 5
        mana_used = 0
        cards_played: list[str] = []
        targets_attacked: list[str] = []
        damage_dealt = 0

        # 1) Play cheapest creature first
        creatures = [
            c for c in hand
            if c.get_card_info().get("type") == "Creature"
        ]
        spells = [
            c for c in hand
            if c.get_card_info().get("type") == "Spell"
        ]

        creatures.sort(key=lambda c: c.cost)
        spells.sort(key=lambda c: c.cost)

        for creature in creatures:
            if mana_used + creature.cost <= available_mana:
                mana_used += creature.cost
                cards_played.append(creature.name)
                battlefield.append(creature)

                info = creature.get_card_info()
                damage_dealt += int(info.get("attack", 0))
                break

        # 2) Then play cheapest spell if possible
        for spell in spells:
            if mana_used + spell.cost <= available_mana:
                mana_used += spell.cost
                cards_played.append(spell.name)

                damage_dealt += 3
                break

        # 3) Always prioritize Enemy Player
        targets = self.prioritize_targets(["Enemy Player"])
        targets_attacked.append(targets[0])

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets_attacked,
                "damage_dealt": damage_dealt,
            },
        }
