# 🐍 Retro Snake Game

A classic Snake game implementation written in Python using the `turtle` graphics library. This project demonstrates Object-Oriented Programming (OOP), file I/O for high scores, and event-driven programming.

![Gameplay Screenshot](snake_self_coll.png)
![Gameplay Screenshot](snake_wall_collison.png)

## 🎮 Features

* **Classic Gameplay**: Smooth movement and collision mechanics.
* **High Score System**: Persists the highest score to a local file (`highscore.txt`), so you can challenge yourself across sessions.
* **OOP Design**: Clean code structure separating `Snake`, `Food`, and `Scoreboard` logic.
* **Responsive Controls**: Supports both Arrow keys and WASD.

## 🛠️ How to Run

1.  **Ensure Python is installed.** (This project uses the standard library, so no `pip install` is needed).
2.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/snake-game-portfolio.git](https://github.com/YOUR_USERNAME/snake-game-portfolio.git)
    cd snake-game-portfolio
    ```
3.  **Run the game:**
    ```bash
    python snake.py
    ```

## 🏗️ Code Structure

| Class | Responsibility |
| :--- | :--- |
| **`Snake`** | Manages the snake's body segments, movement, and growth logic. |
| **`Food`** | Handles rendering the food and randomizing its location. |
| **`Scoreboard`** | Tracks current score, reads/writes high score to file, and updates the UI. |

## 🚀 Controls

* **Up /: Move Up
* **Down /: Move Down
* **Left / : Move Left
* **Right /: Move Right

## 🔮 Future Improvements

* Add difficulty levels (increasing speed).
* Add obstacles/walls in the middle of the screen.
* Implement a "Golden Apple" for bonus points.
