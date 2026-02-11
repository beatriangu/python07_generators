
# 🧭 MAP.md — Python Module 07 · DataDeck 🃏
**OOP · Herencia · Polimorfismo · Diseño extensible · flake8**

Este documento es mi mapa de aprendizaje y diseño.
Explica qué hace cada pieza, cómo encaja y por qué está así.

---

## 🌱 Idea central del módulo

Pasar de:

❌ “tengo varias clases y hago if para distinguirlas”
a
✅ “todas son Card y el sistema funciona sin preguntar el tipo”

**Regla de oro (defensa):**
- El motor (Deck / main) solo conoce el contrato `Card`.
- Las subclases deciden el comportamiento.

---

## 🧩 Arquitectura del sistema (visión mental)

           ┌───────────────┐
           │     Deck       │
           │  (gestiona)    │
           └───────┬───────┘
                   │ contiene
                   ▼
      ┌──────────────────────────┐
      │          Card            │  (base / contrato)
      │ get_card_info()          │
      │ play(game_state)         │
      │ is_playable(game_state)  │
      └───────┬───────────┬──────┘
              │           │
              ▼           ▼
     ┌─────────────┐   ┌─────────────┐   ┌──────────────┐
     │ CreatureCard │   │  SpellCard  │   │ ArtifactCard  │
     │ ataque/vida  │   │ efecto tipo │   │ durabilidad   │
     │ combate       │  │ resolve()   │   │ habilidad      │
     └─────────────┘   └─────────────┘   └──────────────┘


**Deck = composición** (TIENE cartas)  
**Creature/Spell/Artifact = herencia** (SON una carta)

---

## 🟢 ex0 — Card Foundation (contrato + primera subclase)

### 🎯 Objetivo del ejercicio
Crear un contrato base (`Card`) y demostrar una subclase real (`CreatureCard`)
con comportamiento propio.

### 🧠 Qué piezas hay y qué hace cada una

#### `Card.py` (clase base: contrato)
- `__init__(name, cost, rarity)`
  → guarda atributos comunes a todas las cartas.
- `get_card_info()`
  → devuelve un dict consistente con info base (y la subclase puede extenderlo).
- `is_playable(game_state)` (o `can_play`)
  → decide si se puede jugar según `available_mana`.
- `play(game_state)`
  → método del contrato: cada subclase lo redefine.

✅ **Idea clave:** `Card` define **qué** se puede hacer con una carta, no **cómo**.

#### `CreatureCard.py` (subclase concreta)
- `__init__(attack, health, ...)`
  → añade stats propios de criatura.
- `get_card_info()`
  → devuelve la info base + `attack` y `health`.
- `play(game_state)`
  → gasta mana y devuelve un resultado tipo “summoned”.
- `attack_target(target_name)` (si existe)
  → demuestra comportamiento exclusivo de criatura.

✅ **Idea clave:** la subclase añade valor **SIN romper el contrato**.

#### `ex0/main.py` (script demo)
- Crea una criatura
- Imprime `get_card_info()`
- Prueba `is_playable()` con mana suficiente y no suficiente
- Ejecuta `play()`
- Simula un ataque

✅ `main()` solo orquesta y muestra la demo.

---

## 🟡 ex1 — Deck Builder (polimorfismo real)

### 🎯 Objetivo del ejercicio
El mazo (`Deck`) debe trabajar con cartas distintas **sin condicionales por tipo**:
- `CreatureCard`
- `SpellCard`
- `ArtifactCard`

### 🧠 Qué hace cada fichero

#### `Deck.py` (gestor del sistema)
- `__init__()`
  → crea `self._cards` como lista interna.
- `add_card(card: Card)`
  → mete cualquier objeto que cumpla el contrato `Card`.
- `remove_card(card_name)` (tu preferencia: `delete` si lo aplicas en el módulo)
  → elimina por nombre (gestión del mazo).
- `shuffle()`
  → mezcla el orden.
- `draw_card()`
  → saca la primera carta o `None` si está vacío.
- `get_deck_stats()`
  → analítica simple: total, tipos, coste medio.

✅ **Clave mental:** `Deck` no “juega cartas”, solo las gestiona.

#### `SpellCard.py` (carta concreta: hechizo)
- `__init__(spell_type, ...)`
  → define “damage”, “heal”, etc.
- `play(game_state)`
  → devuelve resultado y usa `resolve_effect()`.
- `resolve_effect(targets)`
  → construye la salida según tipo/targets.

✅ **Clave mental:** `Deck` no sabe nada del efecto; la carta sí.

#### `ArtifactCard.py` (carta concreta: efecto permanente)
- `__init__(durability, artifact_effect, ...)`
  → define durabilidad y efecto.
- `play(game_state)`
  → devuelve el efecto (permanente).
- `activate_ability()`
  → consume durabilidad y devuelve estado.

✅ **Clave mental:** es una carta “de estado”, por eso tiene durabilidad.

#### `ex1/main.py` (demo polimórfica)
Flujo:
1. `deck = Deck()`
2. crea 3 cartas (distintos tipos)
3. `deck.add_card(...)` para todas
4. imprime `deck.get_deck_stats()`
5. loop:
   - `card = deck.draw_card()`
   - `info = card.get_card_info()`
   - `result = card.play(game_state)`

✅ Aquí está el polimorfismo real:
- misma llamada `card.play(...)`
- distinto resultado según clase

---

## 🟠 ex2 — Ability Layer (múltiples interfaces + herencia múltiple)

> **Tema del ejercicio:** “Ability Layer: Multiple Interface Design”  
> Construimos un sistema flexible de habilidades usando **interfaces abstractas**
> combinables mediante **herencia múltiple**.

### 🎯 Objetivo del ejercicio
Diseñar **múltiples interfaces abstractas** que puedan combinarse para crear cartas
“élite” con **varias capacidades simultáneas** (combate + magia).

Pasamos de:
- “una carta tiene un solo rol”
a
- “una carta puede implementar varios roles sin mezclar responsabilidades”

### 🧠 Qué se aprende aquí (conceptos)
1) **Interfaces (ABCs) como capas de capacidad**
- `Combatable` define comportamiento de combate.
- `Magical` define comportamiento mágico.
- No son cartas “completas”: son **contratos de habilidad**.

2) **Separación de concerns**
- Combate y magia están separados: cada uno tiene su conjunto de métodos.
- Esto evita una clase monolítica tipo `MegaCard` con todo mezclado.

3) **Herencia múltiple con contrato claro**
- `EliteCard` hereda de:
  - `Card` (identidad de carta + coste/rareza + info)
  - `Combatable` (habilidad de ataque/defensa)
  - `Magical` (habilidad de lanzar hechizos/canalizar mana)
- Implementa **todos** los métodos abstractos.

✅ Resultado: una carta con varias habilidades sin ifs y sin acoplar Deck a tipos.

---

### 📦 Estructura de ex2
```text
ex2/
├── __init__.py
├── Combatable.py
├── Magical.py
├── EliteCard.py
└── main.py
✅ Import importante del subject:

EliteCard.py debe importar Card desde ex0:

from ex0.Card import Card

🧱 Contratos exactos (lo que exige el subject)
Combatable (interfaz abstracta)
Debe definir:

attack(self, target) -> dict

defend(self, incoming_damage: int) -> dict

get_combat_stats(self) -> dict

Interpretación mental:

attack() genera un resultado de ataque (quién, a quién, cuánto daño, tipo).

defend() aplica mitigación y reporta daño bloqueado/recibido.

get_combat_stats() expone stats de combate (damage base, armor, etc.).

✅ Combatable no decide cómo se juega la carta en el deck.
Solo define qué sabe hacer en combate.

Magical (interfaz abstracta)
Debe definir:

cast_spell(self, spell_name: str, targets: list) -> dict

channel_mana(self, amount: int) -> dict

get_magic_stats(self) -> dict

Interpretación mental:

cast_spell() devuelve resultado (caster, spell, targets, mana_used).

channel_mana() aumenta el mana interno o el estado mágico.

get_magic_stats() expone stats mágicas (mana actual, coste base, etc.).

✅ Magical define qué sabe hacer en magia sin mezclar combate.

EliteCard (herencia múltiple: Card + Combatable + Magical)
Debe implementar:

play(self, game_state: dict) -> dict

attack(self, target) -> dict

cast_spell(self, spell_name: str, targets: list) -> dict
(y también los otros abstractos: defend, channel_mana,
get_combat_stats, get_magic_stats, etc.)

Interpretación mental:

EliteCard es una carta “poderosa” porque acumula capacidades:

puede jugarse como carta (coste/rareza)

puede atacar/defender

puede lanzar magia y gestionar mana

✅ Esto demuestra por qué las interfaces son útiles: combinamos piezas
de comportamiento de forma modular.

🧠 ¿Dónde está el polimorfismo en ex2?
En dos niveles:

1) Polimorfismo como Card
EliteCard se puede tratar como Card:

get_card_info()

is_playable(game_state)

play(game_state)

El motor solo necesita el contrato Card.

2) Polimorfismo por capacidad (interfaces)
Otros sistemas podrían trabajar por interfaz:

Un “combat engine” puede operar con cualquier Combatable

Un “magic engine” puede operar con cualquier Magical

✅ Esto habilita diseño flexible: no dependes de la clase concreta,
dependes del contrato.

🧪 ex2/main.py — Demo requerida (cómo se demuestra)
El output esperado del subject muestra tres cosas:

A) “Introspección” de capacidades
Listar qué métodos aporta cada capa:

Card: play, get_card_info, is_playable

Combatable: attack, defend, get_combat_stats

Magical: cast_spell, channel_mana, get_magic_stats

✅ Mensaje defendible: “Esta carta cumple varios contratos”.

B) Playing la EliteCard
Se demuestra que es jugable como carta:

coste/mana → play(game_state) funciona

C) Fases: combate y magia
Combat phase:

attack("Enemy")

defend(incoming_damage)

Magic phase:

cast_spell("Fireball", ["Enemy1", "Enemy2"])

channel_mana(3)

✅ Cierra con un mensaje tipo:
“Multiple interface implementation successful!”

✅ Checklist rápido (antes de seguir)
 Cada directorio tiene __init__.py

 EliteCard hereda de Card, Combatable, Magical

 EliteCard implementa todos los abstract methods

 play() usa game_state y respeta available_mana

 Las funciones devuelven dict con claves claras (como output esperado)

 No hay if isinstance(...) para decidir comportamiento

 flake8 limpio

 python3 -m ex2.main funciona desde la raíz

🗣️ Mini defensa (60s)
“En ex2 introduzco una capa de habilidades mediante interfaces abstractas.
Defino Combatable y Magical como contratos separados para evitar mezclar
responsabilidades. Luego creo EliteCard que hereda de Card y de ambas
interfaces. Implemento todos los métodos, demostrando herencia múltiple y
polimorfismo por capacidad: un sistema puede tratarla como Card, o como
Combatable, o como Magical. Esto hace el diseño extensible: puedo crear
nuevas cartas combinando interfaces sin tocar el motor.”

❓Pregunta del subject (respuesta defendible)
¿Cómo habilitan múltiples interfaces un diseño flexible de cartas?

Permiten modelar habilidades como “capas” combinables.

Puedes crear nuevas cartas reusando contratos (Combatable, Magical)
sin duplicar lógica ni tocar otras clases.

Ventajas de separar combate y magia

Menos acoplamiento: cada módulo se centra en un tipo de habilidad.

Más reutilización: puedes crear una carta solo mágica o solo de combate.

Más mantenibilidad: cambios en magia no rompen combate (y viceversa).

Más extensibilidad: añadir Healable, Stealth, Utility es fácil.

