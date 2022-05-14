
import random

print(
"""
888             888   888   888                888     d8b
888             888   888   888                888     Y8P
888             888   888   888                888
88888b.  8888b. 888888888888888 .d88b. .d8888b 88888b. 88888888b.
888 "88b    "88b888   888   888d8P  Y8b88K     888 "88b888888 "88b
888  888.d888888888   888   88888888888"Y8888b.888  888888888  888
888 d88P888  888Y88b. Y88b. 888Y8b.         X88888  888888888 d88P
88888P" "Y888888 "Y888 "Y888888 "Y8888  88888P'888  88888888888P"
                                                          888
                                                          888
                                                          888      
"""
)


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
print(ship_row +1)
print(ship_col +1)

for turn in range(4):
    print("Turn", turn+1)

    guess_row = int(input("Guess Row: "))-1
    guess_col = int(input("Guess Column: "))-1

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations you sank my battle ship!")
        break
    else:
        if guess_row > int(grid_size)-1 or guess_col > int(grid_size)-1:
            print("What are you aming at?")
        elif board[guess_row][guess_col]=="X":
            print("You gussed that one alrady!")
        else:
            print("No luck!")
            board[guess_row][guess_col]="X"
            if turn == 3:
                print("Game Over.")
        print_board(board)
