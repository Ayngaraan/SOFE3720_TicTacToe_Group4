# Tic Tac Toe AI

A Tic Tac Toe game with an unbeatable AI opponent built using the Minimax algorithm with Alpha-Beta Pruning.

## Course
SOFE 3720 - Artificial Intelligence | Winter 2026

## How to Run

Make sure Python is installed, then run:

```bash
python ui.py
```

## How to Play
- You are **X**, the AI is **O**
- Click any cell to make your move
- The AI will respond instantly
- Click **Restart Game** to play again

## AI Algorithm
The AI uses **Minimax with Alpha-Beta Pruning** to evaluate all possible game states and always make the optimal move. It is theoretically unbeatable — the best outcome a human can achieve is a draw.

## Project Structure
```
board.py  - Board logic, move validation, win detection
ai.py     - Minimax algorithm with Alpha-Beta Pruning
game.py   - CLI version of the game
ui.py     - Graphical interface built with tkinter
```

## Technologies
- Python 3
- Tkinter (built-in Python GUI library)
