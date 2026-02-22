🧭 MAP.md — Python Module 07 · DataDeck 🃏

OOP · ABC · Polymorphism · Multiple Inheritance · Design Patterns · flake8

🎯 Propósito del módulo

DataDeck no es un juego de cartas.

Es un laboratorio progresivo de arquitectura orientada a contratos que demuestra:

Diseño desacoplado

Polimorfismo real

Composición de capacidades

Aplicación práctica de patrones de diseño

Cumplimiento del principio Open/Closed

Extensibilidad sin modificación del núcleo

El foco no es el dominio (cartas).
El foco es el diseño.

🌱 Evolución conceptual

El sistema evoluciona desde:

if isinstance(card, CreatureCard):

hacia:

card.play(game_state)

El comportamiento:

❌ No se decide por tipo
✅ Se delega al propio objeto mediante contrato

Esto elimina:

if

elif

isinstance

Acoplamiento rígido

🧠 Principio Rector

El motor depende de interfaces, no de implementaciones.

Las subclases encapsulan su comportamiento.
El núcleo del sistema permanece estable.

Nuevas cartas no requieren modificar el motor.

✔ Open/Closed Principle
✔ Bajo acoplamiento
✔ Alta cohesión
✔ Extensibilidad real

🧩 Arquitectura General
Relaciones principales

Deck contiene Card → composición

CreatureCard / SpellCard / ArtifactCard → herencia

EliteCard → herencia múltiple controlada

GameEngine → inyección de dependencias (Factory + Strategy)


```md
## 🏗 Diagrama estructural

```text
+----------------+
|     Deck       |
+----------------+
| - _cards: list |
+----------------+
| + add_card()   |
| + draw_card()  |
| + shuffle()    |
+--------+-------+
         |
         | contains
         v
+----------------------+
| <<abstract>> Card    |
+----------------------+
| - name               |
| - cost               |
| - rarity             |
+----------------------+
| + play()             |
| + is_playable()      |
| + get_card_info()    |
+----------+-----------+
           ^
-----------|-------------------
|          |                  |
+-------------+  +-------------+  +-------------+
| CreatureCard|  | SpellCard   |  | ArtifactCard|
+-------------+  +-------------+  +-------------+
| - attack    |  | - spell_type|  | - durability|
| - health    |  |             |  |             |
+-------------+  +-------------+  +-------------+

x0 — Card Foundation
🎯 Objetivo

Definir un contrato formal usando abc.ABC.

Decisiones clave

play() es abstracto.

No se permite instanciar una carta incompleta.

El contrato es explícito.

Resultado

Arquitectura basada en contrato formal, no en convención implícita.

🟡 ex1 — Deck Builder
🎯 Objetivo

Gestionar múltiples tipos de carta sin condicionales por tipo.

card = deck.draw_card()
card.play(game_state)

El motor no sabe:

Si es criatura

Si es spell

Si es artefacto

Solo conoce el contrato Card.

✔ Polimorfismo real
✔ Eliminación de condicionales por tipo
✔ Responsabilidad distribuida

🟠 ex2 — Ability Layer
🧩 Problema

Algunas cartas pueden:

Atacar

Defender

Lanzar hechizos

Canalizar magia

💡 Solución

Separar capacidades en interfaces independientes:

Combatable

Magical

class EliteCard(Card, Combatable, Magical):

Estas interfaces representan habilidades, no identidad.

Beneficios

Composición flexible

Contratos formales por capacidad

Polimorfismo por interfaz

Evita clases monolíticas

✔ Diseño modular
✔ Separación de responsabilidades

🟣 ex3 — Engine Layer

Aquí el sistema pasa de estructura a orquestación.

🏭 Abstract Factory

Responsabilidad:

Crear familias coherentes de cartas

Encapsular la lógica de creación

Reducir acoplamiento

El motor depende de CardFactory, no de clases concretas.

♟ Strategy Pattern

Responsabilidad:

Definir cómo se ejecuta un turno

Permitir cambiar comportamiento dinámicamente

engine.configure_engine(factory, strategy)

Cambiar estrategia ≠ modificar motor.

🔥 Por qué Factory + Strategy es potente

Factory controla qué existe

Strategy controla cómo se usa

Separación clara entre:

Construcción

Comportamiento

✔ Alta configurabilidad
✔ Bajo acoplamiento
✔ Escalabilidad limpia

🔴 ex4 — Extensibilidad

Se introduce un nuevo contrato:

class Rankable(ABC):

Permite:

Sistema de torneos

Ranking

Sistema ELO

Métricas adicionales

Sin modificar las capas anteriores.

💡 Demostración real del principio Open/Closed.

🧠 Design Trade-offs
1️⃣ ABC vs Duck Typing

Decisión: usar Abstract Base Classes.

Ventajas:

Contrato explícito

Errores detectados temprano

Arquitectura clara

Trade-off:

Mayor formalismo

Más código estructural

2️⃣ Herencia múltiple vs Composición pura

Decisión: herencia múltiple controlada.

Ventajas:

Capacidades como contratos formales

Polimorfismo por interfaz

Trade-off:

Requiere entender el MRO

Puede volverse compleja si se abusa

3️⃣ Patrones vs Simplicidad

Decisión: aplicar Factory + Strategy.

Ventajas:

Bajo acoplamiento

Configuración dinámica

Escalabilidad

Trade-off:

Mayor abstracción

Curva de comprensión inicial

🧠 Conceptos dominados

Programación contra interfaces

Inversión de dependencias

Separación de responsabilidades

Polimorfismo real

Herencia múltiple controlada

Patrones clásicos de diseño

Open/Closed Principle

Arquitectura extensible

🧪 Estándares de calidad

Python 3.10+

Tipado explícito

flake8 limpio

Sin condicionales por tipo

Ejecución modular:

python3 -m exX.main

