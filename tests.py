
import random

grid_size = input("How big would you like the grid to be?")
board = []

for i in range(int (grid_size)):
    board.append(["O"] *int (grid_size))
def print_board(board):
    for x in board:
        print(" ". join(x))

print_board(board)

def random_row(board):
    return random.randint(0,len(board)-1)

def random_col(board):
    return random.randint(0,len(board)-1)

ship_row = random_row(board)
ship_col = random_col(board)

guess_row = int(input("Guess Row: "))-1
guess_col = int(input("Guess Column: "))-1

print(ship_row)
print(ship_col)

if guess_row == ship_row and guess_col == ship_col:
    print("Congratulations you sank my battle ship!")
else:
    if guess_row > int(grid_size)-1 or guess_col > int(grid_size)-1:
        print("What are you aming at?")
    else:
        print("No luck!")
        board[guess_row][guess_col]="X"
        print_board(board)
