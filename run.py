
import random
print("Hello and welcome to Octi's")
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
print(
"""
                                    # #  ( )
                                  ___#_#___|__
                              _  |____________|  _
                       _=====| | |            | | |==== _
                 =====| |.---------------------------. | |====
   <--------------------'   .  .  .  .  .  .  .  .   '--------------/
     \                                                             /
      \_______________________________________________WWS_________/
  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
   wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
"""
)
while True:
    try:
        grid_size = int(input("How big would you like the grid to be?"))
        break
    except ValueError:
        print("Numbers please!")


def build_board(size):
    return[["O" for x in range(size)] for x in range(size)]

def print_board(board):
    for x in board:
        print(*x)

board = build_board(grid_size)
print_board(board)

def build_ship(size):
    lenght_ship = random.randint(2, size)
    orientation = random.randint(0, 1)

    if orientation == 0:

        row_ship = [random.randint(0, size - 1)] * lenght_ship

        col = random.randint(0, size - lenght_ship)

        col_ship = list(range(col, col + lenght_ship))

        coords = tuple(zip(row_ship, col_ship))
    else:
        col_ship = [random.randint(0, size - 1)] * lenght_ship
        row = random.randint(0, size - lenght_ship)
        row_ship = list(range(row,row + lenght_ship))
        coords =tuple(zip(row_ship, col_ship))
    print(coords)
    return list(coords)

ship = build_ship(grid_size); ship

def user_guess():
    while True:
        try:
            row = int(input("Guess Row "))-1
            col = int(input("Guess Collumn "))-1
            return (row, col)
            break
        except ValueError:
            print("Numbers Please!")

def update_board( guess, board, ship, guesses):
    if guess in guesses:
        print("You already gussed that.")
        return board
    guesses.append(guess)
    if guess in ship:
        print("You hit my battle ship!")
        board[guess[0]][guess[1]] ="X"
        ship.remove(guess)
        return board
    try:
        board[guess[0]][guess[1]] ="*"
        print("Miss!")
        return board
    except IndexError:
        print("Ups, that is out of the ocean!")
        return board
guesses = []
our_guess = user_guess()
board = update_board(our_guess, board, ship, guesses)
print_board(board)

def main():
    board = build_board(grid_size)
    guesses = []
    while len(ship) > 0:
        board = update_board(user_guess(),board, ship, guesses)
        print_board(board)
    print("You sunk my battle ship!")
    return
main()
