🃏 DataDeck — Python Module 07

OOP · Abstract Base Classes · Multiple Inheritance · Polymorphism · Design Patterns · flake8

DataDeck is a modular, Trading Card Game–inspired system built to practice clean, extensible, and defendable object-oriented design in Python.

Core idea:
Same interface, different behavior — without if/elif branching and without isinstance() checks.

This project is not about building a full game.
It is about designing an architecture that can grow without breaking.

🎯 Architectural Goal

Design a system where:

The engine depends on interfaces, not implementations

New card types can be added without modifying existing code

Behavior is delegated to objects, not centralized in conditionals

Code remains lint-clean and explainable

This module demonstrates:

Open/Closed Principle

Low coupling

High cohesion

Interface-based design

Runtime polymorphism

🧠 Key Learning Outcomes

By completing this module, I can:

Define explicit contracts using Abstract Base Classes (ABC)

Enforce behavior consistency across subclasses

Demonstrate real polymorphism (card.play(...))

Combine capabilities using multiple inheritance (interfaces)

Apply Strategy and Factory patterns properly

Organize a Python project as a package

Keep code flake8 clean and evaluation-ready

✅ Project Constraints

Python 3.10+

Standard library only

Fully flake8 compliant

Modular execution from repository root

Run pattern:

python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
📦 Repository Structure
python07_datadeck/
├── README.md
├── MAP.md
├── ex0/  # ABC foundation
├── ex1/  # Polymorphism in collections
├── ex2/  # Multiple inheritance (interfaces)
├── ex3/  # Strategy + Factory
└── ex4/  # Ranking & orchestration

Each exercise is self-contained and executable.

🧩 Exercise Breakdown
🟢 ex0 — Card Foundation

Abstract Base Class + First Concrete Implementation

Goal

Create a universal contract for all card types.

Core Design

Card (ABC):

play(game_state) → abstract

get_card_info() → shared implementation

is_playable() → shared validation logic

CreatureCard:

Adds attack and health

Implements play()

Extends behavior without breaking the contract

What It Demonstrates

Contracts prevent incomplete implementations

Subclasses define behavior

The system depends on abstraction

Run:

python3 -m ex0.main
🟡 ex1 — Deck Builder

Polymorphism in Action

Goal

Store multiple card types in the same collection and treat them uniformly.

Design

Deck stores Card references, not concrete types.

card = deck.draw_card()
card.play(game_state)

The deck does not know:

If it’s a creature

If it’s a spell

If it’s an artifact

Only the contract matters.

Demonstrates

Runtime polymorphism

Removal of conditional branching

Distributed responsibility

Run:

python3 -m ex1.main
🔵 ex2 — Ability Layer

Multiple Interfaces, Controlled Multiple Inheritance

Problem

Some cards can:

Attack

Defend

Cast spells

Channel mana

Solution

Separate capabilities into independent interfaces:

Combatable

Magical

class EliteCard(Card, Combatable, Magical)

These represent capabilities, not identity.

Demonstrates

Multiple inheritance used intentionally

Interface-driven design

Modular capability composition

Run:

python3 -m ex2.main
🟣 ex3 — Strategy + Factory

Behavior Configuration + Object Creation Abstraction

Strategy Pattern

Encapsulates turn execution logic.

engine.configure_engine(factory, strategy)

Changing strategy ≠ modifying engine.

Abstract Factory Pattern

Encapsulates card creation logic.

The engine depends on CardFactory, not concrete classes.

Why This Matters

Factory controls what exists

Strategy controls how it behaves

Separation of:

Construction

Behavior

Orchestration

Run:

python3 -m ex3.main
🔴 ex4 — Ranking & Tournament

Interfaces + System Orchestration

Goal

Introduce ranking capability without modifying the core system.

Rankable defines ranking behavior.

TournamentCard implements it.

TournamentPlatform orchestrates tournament flow.

Demonstrates

Interface-driven scalability

ELO-based ranking logic

Orchestration separated from entity logic

Run:

python3 -m ex4.main
🧠 Defense-Ready Explanations
Where is polymorphism?

Everywhere this appears:

card.play(game_state)

The engine never checks type.

Each subclass defines its own behavior.

Why avoid if card.type == ...?

Because:

Behavior belongs inside the object

Type-checking breaks Open/Closed

It centralizes logic and increases coupling

How do you extend the system?

Create a new subclass of Card

Implement play()

Optionally implement additional interfaces

No engine modification required

That is extensibility by design.

🧪 Linting

Run from repository root:

flake8

All exercises are flake8 compliant.

🏗 Architectural Summary

DataDeck demonstrates:

Programming to interfaces

Dependency inversion

Controlled multiple inheritance

Pattern application with purpose

Open/Closed Principle in practice

Clean, explainable, scalable OOP design

This is not a card game.

It is an architecture exercise.

👤 Author

Bea
