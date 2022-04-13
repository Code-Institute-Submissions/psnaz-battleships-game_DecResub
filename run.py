#Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot


from random import randint

HIDDEN_BOARD = [[' '] * 8 for x in range(8)] # will hold our ships
GUESS_BOARD = [[' '] * 8 for x in range(8)] # will hold our guesses: hits & misses

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):     # function to define the board
    print('     A B C D E F G H')
    print('     ---------------')
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
    pass   # ask user what row and column he will want to guess the location

def count_hit_ships(): #it'll count every time you have a hit & if you hit all 5 the game is over
    pass

create_ships()
turns = 10
#while turns > 0: