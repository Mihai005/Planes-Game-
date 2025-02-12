# ✈️ Planes: Game Rules

## 📜 Description
Planes is a classic strategic game played on graph paper. The goal of the game is to identify and shoot down all of the opponent's planes before they find yours.

## 📌 Rules

### 📌 Game Board
- The game is played on a **10x10** grid.
- Each cell is identified by:
  - A **number** on the X-axis (from 1 to 10).
  - A **letter** on the Y-axis (from A to J).
- Each player has **two boards**:
  1. **Their own board** (where they place their planes).
  2. **The opponent’s board** (where they try to locate the opponent’s planes).

### ✈️ Placing the Planes
- Each player places **3 identical planes** on their board without the opponent seeing their positions.
- Planes **must not exceed** the grid boundaries.
- The standard shape of a plane is as follows:

```
  X  
 XXX 
  X  
  X  
```
(X represents the cells occupied by the plane, with the center being the cockpit.)

---

## 🎯 Gameplay

### 🔄 Turns
1. The active player selects a coordinate (e.g., **B4**) and asks the opponent what is there.
2. The opponent checks their board and responds with one of the following:

| Response | Meaning |
|---------|-------------|
| **Air** | No part of a plane is in this cell. |
| **Hit** | The cell is part of a plane but not the cockpit. |
| **Destroyed** | The cell contains a plane’s cockpit. The entire plane is considered destroyed. |

3. The game continues until a player **destroys all three of the opponent's planes**.

---

## 🏆 End of the Game
- The winner is the first player to successfully identify and **destroy all three planes** of their opponent.

## 🎨 Example Grid
```
    1  2  3  4  5  6  7  8  9 10
 A  .  .  .  .  .  .  .  .  .  .
 B  .  .  .  X  .  .  .  .  .  .
 C  .  .  X  X  X  .  .  .  .  .
 D  .  .  .  X  .  .  .  .  .  .
 E  .  .  .  X  .  .  .  .  .  .
 F  .  .  .  .  .  .  .  .  .  .
 G  .  .  .  .  .  .  .  .  .  .
 H  .  .  .  .  .  .  .  .  .  .
 I  .  .  .  .  .  .  .  .  .  .
 J  .  .  .  .  .  .  .  .  .  .
```

---

## 💡 Strategic Tips
- Try to **vary your plane placements** to avoid being predictable.
- Attack in a **systematic pattern** to efficiently cover the board.
- Once you find part of a plane, investigate nearby areas to locate the cockpit.

---

🔹 **Play smart and have fun!** 🎮✨
