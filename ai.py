from board import Board

class AI:
    def __init__(self, ai_player, human_player):
        self.ai_player = ai_player        # AI plays as 'O'
        self.human_player = human_player  # Human plays as 'X'

    def get_best_move(self, board):
        # Starts the minimax search and returns the best move index
        best_score = float('-inf')
        best_move = None

        for move in board.available_moves():
            board.make_move(move, self.ai_player)
            score = self.minimax(board, False, float('-inf'), float('inf'))
            board.grid[move] = ' '          # undo the move
            board.current_winner = None     # reset winner

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, is_maximizing, alpha, beta):
        # Base cases — check if the game is already over
        if board.current_winner == self.ai_player:
            return 1       # AI wins = good
        if board.current_winner == self.human_player:
            return -1      # Human wins = bad
        if board.is_full():
            return 0       # Draw = neutral

        if is_maximizing:
            # AI's turn — wants to maximize score
            best_score = float('-inf')
            for move in board.available_moves():
                board.make_move(move, self.ai_player)
                score = self.minimax(board, False, alpha, beta)
                board.grid[move] = ' '
                board.current_winner = None
                best_score = max(score, best_score)
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break   # Beta cutoff — prune this branch
            return best_score

        else:
            # Human's turn — wants to minimize score
            best_score = float('inf')
            for move in board.available_moves():
                board.make_move(move, self.human_player)
                score = self.minimax(board, True, alpha, beta)
                board.grid[move] = ' '
                board.current_winner = None
                best_score = min(score, best_score)
                beta = min(beta, best_score)
                if beta <= alpha:
                    break   # Alpha cutoff — prune this branch
            return best_score