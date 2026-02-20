# Tic-Tac-Toe Engine

A clean, object-oriented implementation of the classic Tic-Tac-Toe game designed for the terminal. This project demonstrates modular Python programming, state management, and robust user-input handling.


## 🚀 Features
* **Object-Oriented Design:** The game logic is encapsulated within a `TicTacToe` class, making the code reusable and easy to test.
* **Input Validation:** Handles invalid coordinates and non-integer inputs gracefully to prevent crashes.
* **Dynamic UI:** A real-time updating ASCII board that renders in the terminal.
* **Cross-Platform:** Automatic screen clearing support for both Windows and Unix-based systems (Linux/macOS).

## 🛠️ Technical Overview
The project is split into two primary modules to maintain a "Separation of Concerns":

1.  **`ticTacToe.py` (The Engine):** * Manages the $3 \times 3$ grid state.
    * Contains logic for win detection (rows, columns, and diagonals).
    * Handles move validation and board saturation checks.
2.  **`ticTacToeMain.py` (The Controller):** * Manages the game loop and player turns.
    * Handles terminal I/O and user interactions.

## 📥 Installation & Running
1. **Clone the repository:**
   bash:
   git clone [https://github.com/Pratap-Raju/PyTactics.git](https://github.com/YOUR_USERNAME/PyTactics.git)
   cd PyTactics
    python ticTacToeMain.py

## 🎮 How to Play
* Players alternate turns between X and O.
* When prompted, enter the Row (0-2) and Column (0-2) of your desired move.
* The game ends when a player gets three in a row or the board is full (Draw).

├── ticTacToe.py      # Core Game Logic Class
├── ticTacToeMain.py  # Main Game Loop & UI Controller
└── README.md         # Project Documentation

 Author: 
 Pratap Kolukuluri
