#Legend
# X for placing ship and hit battleship
# ' ' for available space
# '-' for missed shot


from random import randint
#import emoji module
import emoji 

# will hold computer generated hidden ships
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
# will hold player's guesses and record hits and misses
GUESS_BOARD = [[' '] * 8 for x in range(8)] 

letters_to_numbers = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}

def print_board(board):
    """
    Defines the board size
    """
    print('  A B C D E F G H')
    print('  ---------------')
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def create_ships(board):
    """
    Computer generates 5 ships in 5 unique locations on the hidden board.
    """
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Asks user for an input/ guess.
    """
    while True:
        row = input("\nPlease enter a ship row from 1 to 8:\n")
        if row and row in '12345678':
            row = int(row)
            break
        else:
            print(" Sorry,you've entered a wrong number.\n")
            continue

    while True:
        column = input("\nPlease enter a ship column from A to H:\n").upper()
        if column and column in 'ABCDEFGH':
            break
        else:
            print(" Sorry,you've entered a wrong letter.\n")
            continue
    return int(row) - 1, letters_to_numbers[column]   # ask user what row and column he will want to guess the location


def count_hit_ships(board):
    """
    Counts every time the user has a hit and 
    if he hits all 5 ships prints that 
    the game is over.
    """ 
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count


create_ships(HIDDEN_BOARD)
print_board(HIDDEN_BOARD)  #to test if you can win or lose
turns = 10
while turns > 0:
    print("   " + "\U0001F30A \U0001F6A2 " * 8)
    print("\U0001F30A  WELCOME to the BATTLESHIPS GAME!\U0001F6A2")
    print("   " + "\U0001F30A \U0001F6A2 " * 8)
    print("\n")
    print("The Rules:\n")
    print("There are only 5 small battleships hiding on the sea\n and you have to locate them and shoot them down.")
    print(" - You have 10 shots only.")
    print(" - Every time you locate a ship and sink it,\n an X will appear on the board in front of you.") 
    print(" - Every time you miss a shot,\n a - will appear on the board in front of you.")
    print(" - Once you've run out of shots or sank all 5 ships the game's over.")
    print("Good luck!\nLET'S PLAY!\n")
    print_board(GUESS_BOARD)
    row, column = get_ship_location()
    if GUESS_BOARD[row][column] == '-':
        print(" You already guessed that...\U0001F641\n")
    elif HIDDEN_BOARD[row][column] == 'X':
        print(" Congrats!\U0001F973 You've hit a battleship!\U0001F6A2\n")
        GUESS_BOARD[row][column] = 'X'
        turns -= 1
    else:
        print(" Sorry, you've missed!\U0001F641\n")
        GUESS_BOARD[row][column] = '-'
        turns -= 1
    if count_hit_ships(GUESS_BOARD) == 5:
        print(" Congrats, you have sunk all the battleships!\U0001F973\n")
        print(" \U0001F973 " * 10)
        break
    print(f" You have {turns} shots remaining.\n")
    if turns == 0:
        print(" Sorry, you've run out of shots, the game's over \U0001F641")
        break
