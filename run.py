#Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot


from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)] # will hold our ships
GUESS_BOARD = [[' '] * 8 for x in range(8)] # will hold our guesses: hits & misses

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):     # function to define the board
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'

def get_ship_location():
    row = input("Please enter a ship row from 1 to 8: ")
    while row not in '12345678':
        print("Please enter a valid row number (from 1 to 8): ")
        row = input("Please enter a ship row from 1 to 8: ")
    column = input("Please enter a ship column A to H: ").upper()
    while column not in 'ABCDEFGH':
        print("Please enter a valid column (from A to H): ")
        column = input("Please enter a ship column A to H: ").upper()
    return int(row) - 1, letters_to_numbers[column]   # ask user what row and column he will want to guess the location

def count_hit_ships(board): #it'll count every time you have a hit & if you hit all 5 the game is over
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(HIDDEN_BOARD)
turns = 10
print_board(HIDDEN_BOARD)
print_board(GUESS_BOARD)
#while turns > 0: