# 🃏 DataDeck — Python Module 07
**OOP · Abstract Base Classes · Multiple Inheritance · Polymorphism · Patterns · flake8**

DataDeck is a mini Trading Card Game–style system built to practice **clean,
defendable OOP design** in Python.

> **Core idea:** *Same interface, different behavior* — without `if/elif`
> branching on the card type and without `isinstance()` checks.

This module is not about making a full game. It’s about building an
**extensible architecture** where adding new card types or behaviors does not
break the system.

---

## 🎯 Learning goals
By completing this module, I can:

- Design a shared contract using **Abstract Base Classes (ABC)**
- Extend behavior via **inheritance** and **method overriding**
- Demonstrate real **polymorphism** (`card.play(...)` works for all cards)
- Combine abilities using **multiple inheritance** (interfaces)
- Organize code as packages and run everything from the repo root
- Keep code **flake8 clean** and easy to explain in evaluation

---

## ✅ Project rules
- Python **3.10+**
- **Standard library only**
- **flake8** compliant
- Each exercise contains:
  - required files listed in the subject
  - an `__init__.py`
  - a `main.py` demo runnable from the repository root

Run pattern:
```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
📦 Repository structure
python07_datadeck/
├── __init__.py
├── en.subject7.pdf
├── README.md
├── MAP.md
├── ex0/
│   ├── __init__.py
│   ├── Card.py
│   ├── CreatureCard.py
│   └── main.py
├── ex1/
│   ├── __init__.py
│   ├── SpellCard.py
│   ├── ArtifactCard.py
│   ├── Deck.py
│   └── main.py
├── ex2/
│   ├── __init__.py
│   ├── Combatable.py
│   ├── Magical.py
│   ├── EliteCard.py
│   └── main.py
├── ex3/
│   ├── __init__.py
│   ├── GameStrategy.py
│   ├── AggressiveStrategy.py
│   ├── CardFactory.py
│   ├── FantasyCardFactory.py
│   ├── GameEngine.py
│   └── main.py
└── ex4/
    ├── __init__.py
    ├── Rankable.py
    ├── TournamentCard.py
    ├── TournamentPlatform.py
    └── main.py
🧩 Exercise overview
🟢 ex0 — Card Foundation (ABC + first concrete card)
Goal: build the universal card blueprint.

What’s inside

Card.py → Abstract Base Class defining the shared interface:

play(game_state: dict) -> dict (abstract)

get_card_info() -> dict (concrete)

is_playable(available_mana: int) -> bool (concrete)

CreatureCard.py → first concrete implementation:

adds attack and health

implements play(...)

adds attack_target(...) for combat demo

What it demonstrates

ABC enforces consistency: all card types must implement play()

Subclasses can extend the model without breaking the contract

Run:

python3 -m ex0.main
🟡 ex1 — Deck Builder (polymorphism in action)
Goal: store multiple card types in the same deck and treat them uniformly.

What’s inside

SpellCard.py → concrete card that resolves spell effects

ArtifactCard.py → concrete card with durability + activation behavior

Deck.py → management class:

add_card(card)

remove_card(card_name)

shuffle()

draw_card()

get_deck_stats()

What it demonstrates

Deck stores Card references, not “types”

Polymorphism happens here:

card = deck.draw_card()

card.play(game_state) executes the correct overridden method at runtime

Run:

python3 -m ex1.main
🔵 ex2 — Ability Layer (multiple interfaces)
Goal: combine multiple abilities using multiple inheritance (interfaces).

What’s inside

Combatable.py → abstract combat interface:

attack(target) -> dict

defend(incoming_damage: int) -> dict

get_combat_stats() -> dict

Magical.py → abstract magic interface:

cast_spell(spell_name: str, targets: list) -> dict

channel_mana(amount: int) -> dict

get_magic_stats() -> dict

EliteCard.py → multiple inheritance:

Card + Combatable + Magical

implements all required methods

What it demonstrates

One object can provide multiple capabilities (combat + magic)

Still keeps the same card contract: it can be played as a Card

Run:

python3 -m ex2.main
🟣 ex3 — Strategy + Factory (design patterns)
Goal: make gameplay behavior configurable and card creation extensible.

What’s inside

Strategy:

GameStrategy (interface)

AggressiveStrategy (one concrete strategy)

Factory:

CardFactory (interface)

FantasyCardFactory (one concrete factory)

GameEngine coordinates strategy + factory behavior

What it demonstrates

Strategy pattern: change behavior without changing the engine

Factory pattern: create families of cards without coupling

Run:

python3 -m ex3.main
🔴 ex4 — Ranking & Tournament (interfaces + orchestration)
Goal: simulate a simple tournament platform with ranking behavior.

What’s inside

Rankable.py → ranking interface

TournamentCard.py → card with ranking capability

TournamentPlatform.py → orchestrates tournaments and ranking flow

What it demonstrates

Interfaces allow scalable systems (cards can participate if rankable)

Clean orchestration: platform logic stays separate from card logic

Run:

python3 -m ex4.main
🧠 Defense-ready explanations
Where is polymorphism?
Deck and each main.py interact with cards through the same method:

card.play(game_state)

Each subclass decides internally what that means:

Creature summons

Spell resolves effect

Artifact applies passive effect

EliteCard mixes abilities

Why no if card.type == ...?
Because behavior belongs to the object itself.
If the deck needs type-checking, the design is leaking.

How do you extend the system?
Add a new card class that inherits from Card and implements play().
If needed, add an interface (like Magical) and implement it.
The rest of the system should work without modification.

🧪 Linting
Run from the repository root:

flake8
👤 Author
Bea



