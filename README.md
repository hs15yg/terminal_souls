# ⚔️ Terminal Souls

**Terminal Souls** is a turn-based RPG battle engine built entirely in Python. Face off against challenging enemies in a terminal-based interface featuring dynamic health bars, colorful combat logs, and strategic decision-making.

---

## 🎮 Game Features

* **Turn-Based Combat:** Strategic gameplay where every move counts.
* **Dynamic UI:** Real-time health bars and visual feedback using ANSI colors.
* **Action Menu:**
    * ⚔️ **Attack:** Standard strike with a chance for critical damage.
    * 💊 **Heal:** Consume a potion to restore your HP.
    * ✨ **Special Ability:** High-risk, high-reward attack.
    * 💨 **Dodge:** avoid attacking the enemy.
* **Smart AI:** Enemies will prioritize healing when their health drops below 20%.
* **Polished Animations:** Smooth transitions using screen clearing and timed delays for an immersive experience.

---

## 🛠️ Architecture & Structure

The project is modularized into several Python files to ensure clean and maintainable code:

| File | Description |
| :--- | :--- |
| `main.py` | The entry point. Controls the core game loop and win/loss logic. |
| `headers.py` | Contains global configurations, game state (Player/Enemy stats), and UI templates. |
| `turns.py` | Manages the logic for both the Player and Enemy turn sequences. |
| `life.py` | Handles math logic for damage calculation, healing, and health bar rendering. |
| `check.py` | Validation module that monitors HP status and OS compatibility. |

---

## 🚀 How to Run

1.  **Prerequisites:**
    * Python 3.x installed on your system.
    * A terminal that supports ANSI escape codes (VS Code Terminal, Windows Terminal, Linux/Mac bash).

2.  **Execution:**
    Clone the repository and run the main file:
    ```bash
    python main.py
    ```

---

## 🕹️ Combat Mechanics

### Damage Calculation
Damage is randomized based on the action chosen. A **Critical Hit** system is implemented, giving a 10% chance to deal double damage on standard attacks.

### Healing System
Both the player and the enemy start with a limited amount of **Potions (3)**. Each potion restores **20 HP**. Use them wisely!

### Health Bars
The game features a visual representation of life:
- 💪 **Player:** `[##########]` (Max 100 HP)
- 🦹 **Enemy:** `[############]` (Max 120 HP)

---

## ✨ Credits
Developed as a lightweight RPG engine to demonstrate modular Python programming and terminal-based UI design.

**Soul of the Terminal awaits you!**
