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
    row = input("\nPlease enter a ship row from 1 to 8:\n")
    while row not in '12345678':
        print("Sorry, you've entered a wrong number.\n")
        row = input("Please try again. Enter a ship row from 1 to 8:\n")
    column = input("Please enter a ship column A to H:\n").upper()
    while column not in 'ABCDEFGH':
        print("Sorry, you've entered a wrong letter.\n")
        column = input("Please try again. Enter a ship column from A to H:\n").upper()
    return int(row) - 1, letters_to_numbers[column]   # ask user what row and column he will want to guess the location

def count_hit_ships(board): #it'll count every time you have a hit & if you hit all 5 the game is over
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_BOARD)
# print_board(HIDDEN_BOARD) to test if you can win or lose
turns = 10
while turns > 0:
    print("Welcome to the Battleship Game!\n")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print("You already guessed that...\n")
    elif HIDDEN_BOARD[row][column] == 'X':
        print("Congrats! You've hit a battleship!\n")
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print("Sorry, you've missed!\n")
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print("Congrats, you have sunk all the battleships!\n")
        break
    print(f"You have {turns} shots remaining\n")
    if turns == 0:
        print("Sorry, you've run out of shots, the game's over :-(")
        break
