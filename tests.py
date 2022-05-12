grid_size = input("How big would you like the grid to be?")
board = []

for i in range(0,5):
    board.append(["O"] *int(grid_size))
def print_board(board):
    for x in board:
        print(" ". join(x))

print_board(board)
