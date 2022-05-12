"""
from random import randit
"""

grid_size = input("How big would you like the grid to be?")
board = []

for i in range(0,5):
    board.append(["O"] *int(grid_size))
def print_board(board):
    for x in board:
        print(" ". join(x))

print_board(board)

def random_row(board):
    return randint(0,len(board)-1)

def random_col(board):
    return randint(0,len(board)-1)
ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Column: "))
