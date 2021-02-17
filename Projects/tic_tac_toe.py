# This is my 1St project

# to display the board
def display_board(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


# fuction for single game of tictactoe
def single_game(current_player):
    # its tictactoe representation

    values = [" " for x in range(9)]

    # stores the positions taken by X and O
    # it stores symbol inserted by user as a key:value pair of X and O
    values = {"X": [], "O": []}


while True:
    display_board(values)
