import tkinter as tk
from tkinter import messagebox
from board import Board
from ai import AI

class TicTacToeUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe - AI vs Human")
        self.window.resizable(False, False)
        self.window.configure(bg="#1e1e2e")
        self.board = Board()
        self.ai = AI(ai_player='O', human_player='X')
        self.buttons = []
        self.game_over = False
        self.human_score = 0
        self.ai_score = 0
        self.draw_score = 0

        self.build_ui()
        self.window.mainloop()

    def build_ui(self):
        # Title
        tk.Label(
            self.window,
            text="Tic Tac Toe",
            font=("Arial", 26, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4",
            pady=10
        ).pack()

        # Scoreboard
        score_frame = tk.Frame(self.window, bg="#1e1e2e")
        score_frame.pack(pady=5)

        tk.Label(score_frame, text="You (X)", font=("Arial", 12, "bold"),
                 bg="#1e1e2e", fg="#89b4fa").grid(row=0, column=0, padx=20)
        tk.Label(score_frame, text="Draw", font=("Arial", 12, "bold"),
                 bg="#1e1e2e", fg="#a6e3a1").grid(row=0, column=1, padx=20)
        tk.Label(score_frame, text="AI (O)", font=("Arial", 12, "bold"),
                 bg="#1e1e2e", fg="#f38ba8").grid(row=0, column=2, padx=20)

        self.human_score_label = tk.Label(score_frame, text="0",
                 font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#89b4fa")
        self.human_score_label.grid(row=1, column=0, padx=20)

        self.draw_score_label = tk.Label(score_frame, text="0",
                 font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#a6e3a1")
        self.draw_score_label.grid(row=1, column=1, padx=20)

        self.ai_score_label = tk.Label(score_frame, text="0",
                 font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#f38ba8")
        self.ai_score_label.grid(row=1, column=2, padx=20)

        # Status label
        self.status_label = tk.Label(
            self.window,
            text="Your turn! (X)",
            font=("Arial", 14),
            bg="#1e1e2e",
            fg="#cdd6f4",
            pady=8
        )
        self.status_label.pack()

        # Game grid
        frame = tk.Frame(self.window, bg="#1e1e2e")
        frame.pack()

        for i in range(9):
            btn = tk.Button(
                frame,
                text=' ',
                font=("Arial", 28, "bold"),
                width=5,
                height=2,
                bg="#313244",
                fg="#cdd6f4",
                activebackground="#45475a",
                relief="flat",
                command=lambda idx=i: self.human_move(idx)
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.buttons.append(btn)

        # Restart button
        tk.Button(
            self.window,
            text="Restart Game",
            font=("Arial", 12, "bold"),
            pady=6,
            width=15,
            bg="#89b4fa",
            fg="#1e1e2e",
            activebackground="#74c7ec",
            relief="flat",
            command=self.restart_game
        ).pack(pady=12)

    def human_move(self, index):
        if self.game_over or self.board.grid[index] != ' ':
            return

        self.board.make_move(index, 'X')
        self.buttons[index].config(text='X', fg='#89b4fa')

        if self.check_game_over():
            return

        self.status_label.config(text="AI is thinking...")
        self.window.update()

        ai_move = self.ai.get_best_move(self.board)
        self.board.make_move(ai_move, 'O')
        self.buttons[ai_move].config(text='O', fg='#f38ba8')

        if self.check_game_over():
            return

        self.status_label.config(text="Your turn! (X)")

    def highlight_winning_cells(self):
        # Highlight the winning combination in yellow
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in win_conditions:
            if all(self.board.grid[i] == self.board.current_winner for i in combo):
                for i in combo:
                    self.buttons[i].config(bg="#f9e2af")

    def check_game_over(self):
        if self.board.current_winner:
            self.highlight_winning_cells()
            self.game_over = True
            if self.board.current_winner == 'X':
                self.human_score += 1
                self.human_score_label.config(text=str(self.human_score))
                self.status_label.config(text="You win! 🎉")
                messagebox.showinfo("Game Over", "Congratulations, you win!")
            else:
                self.ai_score += 1
                self.ai_score_label.config(text=str(self.ai_score))
                self.status_label.config(text="AI wins!")
                messagebox.showinfo("Game Over", "AI wins! Better luck next time.")
            return True

        if self.board.is_full():
            self.game_over = True
            self.draw_score += 1
            self.draw_score_label.config(text=str(self.draw_score))
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            return True

        return False

    def restart_game(self):
        self.board = Board()
        self.game_over = False
        self.status_label.config(text="Your turn! (X)")
        for btn in self.buttons:
            btn.config(text=' ', bg="#313244")

if __name__ == "__main__":
    TicTacToeUI()