# this is miniproject no.1

# display the board
def dislpay_board(board):
    print("\t " + board[7] + "|" + board[8] + "|" + board[9])
    print("\t------------------")
    print("\t " + board[4] + "|" + board[5] + "|" + board[6])
    print("\t------------------")
    print("\t " + board[1] + "|" + board[2] + "|" + board[3])


# user input
def usr_input():
    place = "WRONG"
    sign = ""
    acceptable_range = range(0, 10)
    in_range = False

    # check right sign form user
    while sign != "X".lower() and sign != "O".lower():
        sign = input("\n\tChoose your marking 'X' or 'O': ")
    # to check if input is a digit and its in the range

    while not place.isdigit() or in_range == False:
        place = input("\n\tEnter the place(0-9) where to insert your symbol: ")
        if not place.isdigit():
            print("\n\tSorry, wrong input!")
        if place.isdigit():
            if int(place) in acceptable_range:
                in_range = True
            else:
                print("\n\tNumber not in range!")
                in_range = False


def insert_values():
    pass


usr_input()
board = ["#", "x", "o", "x", "o", "x", "x", "o", "x", "x", "o", "x"]
dislpay_board(board)
