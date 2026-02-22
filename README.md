# 🃏 DataDeck — Python Module 07

**OOP · Abstract Base Classes · Multiple Inheritance · Polymorphism · Design Patterns · flake8**

DataDeck is a modular architecture inspired by Trading Card Games, designed to practice clean, extensible, and defendable object-oriented design in Python.

> Same interface. Different behavior. No `if/elif`. No `isinstance()`.

This project focuses on architecture — not gameplay.

---

## 🎯 Architectural Goals

- Program to interfaces, not implementations
- Add new card types without modifying the engine
- Encapsulate behavior inside objects
- Maintain low coupling and high cohesion
- Keep code flake8-clean and evaluation-ready

---

## 📚 Concepts Demonstrated

- Abstract Base Classes (ABC)
- Runtime polymorphism
- Controlled multiple inheritance
- Strategy Pattern
- Abstract Factory Pattern
- Open/Closed Principle

---

## 📦 Repository Structure


python07_datadeck/
├── ex0/ # ABC foundation
├── ex1/ # Polymorphism in collections
├── ex2/ # Multiple inheritance (interfaces)
├── ex3/ # Strategy + Factory
└── ex4/ # Ranking & orchestration


Run from repository root:

```bash
python3 -m ex0.main
python3 -m ex1.main
python3 -m ex2.main
python3 -m ex3.main
python3 -m ex4.main
🧩 Exercises Overview
🟢 ex0 — Card Foundation

Defines the Card abstract base class and the first concrete implementation.

Shared contract

Enforced behavior

Extensibility by design

🟡 ex1 — Polymorphic Deck

Stores different card types in a single collection:

card.play(game_state)

The engine never checks types — only the interface matters.

🔵 ex2 — Ability Composition

Introduces capability interfaces:

Combatable

Magical

Multiple inheritance is used intentionally to compose behavior.

🟣 ex3 — Strategy + Factory

Separates:

Object creation (Factory)

Behavior configuration (Strategy)

Engine orchestration

🔴 ex4 — Ranking & Tournament

Adds ranking capability without modifying the core system.

Demonstrates scalable, interface-driven design.

🛡 Key Takeaway

Behavior belongs inside objects.
The engine depends on contracts, not concrete classes.

This is not a card game.

It is an architecture exercise.

Author: Bea