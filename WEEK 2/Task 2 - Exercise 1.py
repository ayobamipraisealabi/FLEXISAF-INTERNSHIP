import random 

# Code to define the game board
board = [" " for _ in range(9)]

def print_board():
    for row in [board[i:i + 3] for i in range(0, 9, 3)]:
        print("| "+" | ".join(row) +" |")
    print()

# Code to input player's move on board
def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10):
            move = int(move) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        else:
            print("Invalid input. Try again.")
    
# Code for AI's move
def ai_move():
    available_moves = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available_moves)  
    board[move] = "O"

# Code to check for win
def check_win(player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # cols
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# Code to check for a tie
def check_tie():
    return " " not in board

# Code for player to input name and display board
name = input("Enter your name: ")
print("Welcome to 'Tic -Tac - Toe',", name)

# Code to explain how to play
print("To pick a position, enter a number between 1 and 9.")
print("These numbers correspond with the respective positions on the board")
print_board()

# Main code
while True:
    player_move()
    print("You made your move!")
    print_board()

    if check_win("X"):
        print("You win!")
        break

    if check_tie():
        print("It's a tie!")
        break
        

    ai_move()
    print("AI has made its move:")
    print_board()

    if check_win("O"):
        print("AI wins! ")
        break
        
    if check_tie():
        print("It's a tie!")
        break








