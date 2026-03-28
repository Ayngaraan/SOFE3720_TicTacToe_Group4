class Board:
    def __init__(self):
        # Creates a 3x3 grid filled with empty spaces
        self.grid = [' ' for _ in range(9)]
        self.current_winner = None

    def display(self):
        # Prints the board in a readable format
        for i in range(0, 9, 3):
            print(f" {self.grid[i]} | {self.grid[i+1]} | {self.grid[i+2]} ")
            if i < 6:
                print("---|---|---")

    def available_moves(self):
        # Returns a list of empty cell indexes
        return [i for i, spot in enumerate(self.grid) if spot == ' ']

    def make_move(self, index, player):
        # Places the player's mark if the cell is empty
        if self.grid[index] == ' ':
            self.grid[index] = player
            if self.check_winner(index, player):
                self.current_winner = player
            return True
        return False

    def check_winner(self, index, player):
        # All possible winning combinations
        win_conditions = [
            [0,1,2], [3,4,5], [6,7,8],  # rows
            [0,3,6], [1,4,7], [2,5,8],  # columns
            [0,4,8], [2,4,6]            # diagonals
        ]
        for combo in win_conditions:
            if all(self.grid[i] == player for i in combo):
                return True
        return False

    def is_full(self):
        return ' ' not in self.grid