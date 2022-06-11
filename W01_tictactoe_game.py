"""
1. Name: 
    Hilmar Orozco
2. Class Name:
    CSE 210-13 Programming with Classes.
3. Assignment Name: 
    CSE_210_tictactoe_solution.py
4. Assignment Description:
    This is a tic tac toe game program.
"""

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print("\n       |       |    ")
    print(f"   {board[0]}   |   {board[1]}   |   {board[2]}")
    print("       |       |    \n-------+-------+-------")
    print("       |       |    ")
    print(f"   {board[3]}   |   {board[4]}   |   {board[5]}")
    print("       |       |    \n-------+-------+-------")
    print("       |       |    ")
    print(f"   {board[6]}   |   {board[7]}   |   {board[8]}")
    print("       |       |    \n")
    
def has_winner(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])

def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player

def next_player(current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"

def main():
    player = next_player("")
    board = create_board()
    while not (has_winner(board)):
        display_board(board)
        make_move(player, board)
        player = next_player(player)
    display_board(board)
    print("Good game. Thanks for playing!") 

main()