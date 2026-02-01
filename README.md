# Python Module 07 – Generators

This module is part of a structured Python learning path focused on
writing clear, robust and explainable Python code.

The goal of this module is to understand generators as a tool for
lazy evaluation and memory-efficient data processing.

---

## 🎯 Objectives

- Understand how `yield` works and how generators differ from lists
- Write generator functions and use generator expressions
- Process data in a streaming way (constant memory)
- Use `for` loops naturally with iterables and generators
- Explain when generators are the right choice

---

## 🧠 Topics covered

- Generator functions (`yield`)
- Generator expressions
- Lazy evaluation
- Streaming / data flow processing
- Iteration patterns and memory efficiency

---

## 🧪 Exercises overview

### Exercise 0 – First generator  
**Focus:** Generating values step by step with `yield`

### Exercise 1 – Streaming processing  
**Focus:** Processing large sequences without storing them

### Exercise 2 – Filtering streams  
**Focus:** Yielding only relevant events or values

### Exercise 3 – Comparing list vs generator  
**Focus:** Memory and performance awareness

---

## 🧩 Design principles

- Keep generators simple and easy to read
- Prefer streaming when storing data is unnecessary
- Avoid premature optimization: generators must stay explainable
- Clear naming and predictable output
- Learning-oriented solutions aligned with the subject

---

## 🛠️ Technical constraints

- Python 3.10+
- flake8 compliant
- Standard library only
- Clear separation between logic and execution
- Use of `main()` when applicable

---

## 📌 Notes

Generators are not about writing shorter code — they are about
controlling *when* values are produced and keeping memory usage stable.
This module focuses on understanding the "why" behind lazy evaluation
and streaming patterns.
