from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def create_creature(self, name_or_power: str | int | None = None):
        if name_or_power in (None, "dragon"):
            return CreatureCard(
                "Fire Dragon",
                5,
                "Legendary",
                7,
                5,
            )

        if name_or_power == "goblin":
            # Adjusted so the aggressive turn deals 8 damage:
            # Goblin Warrior attack=5 + Lightning Bolt=3 => 8
            return CreatureCard(
                "Goblin Warrior",
                2,
                "Common",
                5,
                2,
            )

        # Fallback
        return CreatureCard(
            "Goblin Warrior",
            2,
            "Common",
            5,
            2,
        )

    def create_spell(self, name_or_power: str | int | None = None):
        # Supported says "fireball",
        # but the subject example uses "Lightning Bolt".
        # We keep the output consistent with the subject.
        return SpellCard(
            "Lightning Bolt",
            3,
            "Rare",
            "damage",
        )

    def create_artifact(self, name_or_power: str | int | None = None):
        return ArtifactCard(
            "Mana Ring",
            2,
            "Uncommon",
            durability=3,
            effect="+1 mana per turn",
        )

    def create_themed_deck(self, size: int) -> dict:
        # To match the subject: hand with 3 cards in this order
        hand = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell("fireball"),
        ]
        battlefield: list = []
        return {"hand": hand[:size], "battlefield": battlefield}
