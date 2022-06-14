"""
1. Name: 
    Hilmar Orozco
2. Class Name:
    CSE 210-13 Programming with Classes.
3. Assignment Name: 
    CSE_210_tictactoe_game.py
4. Assignment Description:
    This is a tic tac toe game program.
"""
def display(board):
    print(f"\n       |       |\n   {board[0]}   |   {board[1]}   |   {board[2]}")
    print(f"       |       |\n-------+-------+-------\n       |       |") 
    print(f"   {board[3]}   |   {board[4]}   |   {board[5]}")
    print(f"       |       |\n-------+-------+-------\n       |       |")
    print(f"   {board[6]}   |   {board[7]}   |   {board[8]}\n       |       |") 
    
def turn(player):
    if player == "x":
        return "o"
    else:
        return "x"

def main():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = "x"
    
    while not (board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or board[2] == board[4] == board[6]):
    
        display(board)
        position = int(input(f"It is {player}'s turn to choose position: "))
        board[position - 1] = player
        player = turn(player)
        
    display(board)
    print("We have a winner!") 

main()