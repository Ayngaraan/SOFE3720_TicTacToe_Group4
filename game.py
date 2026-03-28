from board import Board
from ai import AI

def play_game():
    board = Board()
    ai = AI(ai_player='O', human_player='X')

    print("\nWelcome to Tic Tac Toe!")
    print("You are X, the AI is O")
    print("Board positions are numbered like this:")
    print(" 0 | 1 | 2 ")
    print("---|---|---")
    print(" 3 | 4 | 5 ")
    print("---|---|---")
    print(" 6 | 7 | 8 \n")

    current_player = 'X'  # Human goes first

    while True:
        board.display()

        if current_player == 'X':
            # Human's turn
            while True:
                try:
                    move = int(input("\nYour move (0-8): "))
                    if move in board.available_moves():
                        break
                    else:
                        print("That cell is taken or invalid. Try again.")
                except ValueError:
                    print("Please enter a number between 0 and 8.")

        else:
            # AI's turn
            print("\nAI is thinking...")
            move = ai.get_best_move(board)
            print(f"AI chose position {move}")

        board.make_move(move, current_player)

        # Check if game is over
        if board.current_winner:
            board.display()
            if board.current_winner == 'X':
                print("\nYou win! Congratulations!")
            else:
                print("\nAI wins! Better luck next time.")
            break

        if board.is_full():
            board.display()
            print("\nIt's a draw!")
            break

        # Switch turns
        current_player = 'O' if current_player == 'X' else 'X'

    play_again = input("\nPlay again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()

if __name__ == "__main__":
    play_game()