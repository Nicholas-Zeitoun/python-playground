import os

# initialize the board
board = [' '] * 9
players = ['X', 'O']
current_player = players[0]
game_over = False

# define the functions for the game
def print_board():
    os.system('clear') # clear the console
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def get_move():
    while True:
        move = input(f"Player {current_player}, enter your move (0-8): ")
        if move.isdigit() and int(move) >= 0 and int(move) <= 8 and board[int(move)] == ' ':
            return int(move)
        print("Invalid move. Try again.")

def check_win():
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return True
    if board[2] == board[4] == board[6] != ' ':
        return True
    return False

def check_tie():
    return ' ' not in board

# start the game
while not game_over:
    print_board()
    move = get_move()
    board[move] = current_player
    if check_win():
        print_board()
        print(f"Player {current_player} wins!")
        game_over = True
    elif check_tie():
        print_board()
        print("It's a tie!")
        game_over = True
    else:
        current_player = players[(players.index(current_player) + 1) % 2]
