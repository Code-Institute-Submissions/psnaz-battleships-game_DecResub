"""
Legend
X for placing ship and hit battleship
' ' for available space
'-' for missed shot
"""

from random import randint
# import emoji module
import emoji


# will hold computer generated hidden ships
HIDDEN_BOARD = [[' '] * 8 for x in range(8)]
# will hold player's guesses and record hits and misses
GUESS_BOARD = [[' '] * 8 for x in range(8)]
# indexing horizontal row
letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
    }


def print_board(board):
    """
    Defines the board size
    """
    print('  A B C D E F G H')
    print(' ------------------')
    row_number = 1
    for row in board:
        print(f"{row_number}|{'|'.join(row)}|")
        row_number += 1


def create_ships(board):
    """
    Computer generates 5 ships in 5 unique locations
    on the hidden board marking them with an X.
    """
    for _ in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == 'X':
            ship_row, ship_column = randint(0, 7), randint(0, 7)
        board[ship_row][ship_column] = 'X'


def get_ship_location():
    """
    Asks user for an input/ guess of coordinates.
    Line 46 to 61 my code - came up together with the tutor
    to fix the bug so that an empty string - when player hits
    enter, wouldn't throw an error.
    """
    while True:
        #row = input("\n \U0001F447 Please enter a ship row from 1 to 8: ")
        row = input(emoji.emojize('\n :backhand_index_pointing_right: Please enter a ship row from 1 to 8: '))
        try:
            row = int(row)
            if row < 1 or row > 8:
                raise ValueError("Incorrect row value")
            break
        except ValueError:
            print(" Sorry, you've entered a wrong number.\n")
            continue

    while True:
        #column = input("\U0001F447 Enter a ship column from A to H: ").upper()
        column = input(emoji.emojize('\n :backhand_index_pointing_right: Please enter a ship column from A to H: ')).upper()
        if len(column) == 1 and column in 'ABCDEFGH':
            break
        else:
            print(" Sorry, you've entered a wrong letter.\n")
            continue

    return int(row) - 1, letters_to_numbers[column]


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


def main():
    """
    Runs all the functions
    The computer creates all the ships on the hidden board,
    as long as the player has more than 0 shots,
    he can shoot and hits and misses are being recorded.
    """
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print_board(HIDDEN_BOARD) # TO BE DELETED ONCE TESTING'S DONE!!!
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == '-':
            #print(" You already guessed that...\U0001F641\n")
            print(emoji.emojize('\nYou already guessed that...:slightly_frowning_face:'))
        elif HIDDEN_BOARD[row][column] == 'X':
            #print(" Awesome!\U0001F4A5 You've hit a battleship!\U0001F6A2\n")
            print(emoji.emojize("\n Awesome!:collision: You've hit a battleship!:ship:\n"))
            GUESS_BOARD[row][column] = 'X'
            turns -= 1
        else:
            #print(" Sorry, you've missed!\U0001F641\n")
            print(emoji.emojize("\n Sorry, you've missed!:slightly_frowning_face:\n"))
            GUESS_BOARD[row][column] = '-'
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            #print(" Congrats,\U0001F44F you have sunk all the battleships!\n")
            print(emoji.emojize('\n Congrats,:clapping_hands: you have sunk all the battleships!:flexed_biceps:\n'))
            #print(" \U0001F973 " * 10)  # my code
            print(emoji.emojize(':partying_face:') *10)
            break
        # my code f-string
        print(f" \U0001F9E8 You have {turns} shots remaining.\n")
        if turns == 0:
            #print("Sorry, you've run out of shots, game over\U0001F641\n")
            print(emoji.emojize("Sorry, you've run out of shots, game over:slightly_frowning_face:\n"))
            # my code
            #print("Here's where all the ships were hiding...\U0001F447\n")
            print(emoji.emojize("Here's where all the ships were hiding...:backhand_index_pointing_down:\n"))
            print_board(HIDDEN_BOARD)
            break


# welcome and rules - my code, removed from the while loop
#print("   " + "\U0001F30A \U0001F6A2 " * 8)
print(emoji.emojize(':water_wave: :ship: ') * 8)
#print("\U0001F30A  WELCOME to the BATTLESHIPS GAME!\U0001F6A2")
print(emoji.emojize(':water_wave: WELCOME to the BATTLESHIPS GAME! :ship:'))
#print("   " + "\U0001F30A \U0001F6A2 " * 8)
print(emoji.emojize(':water_wave: :ship: ') * 8)
print("\n")
#print(" \U0001F449 The Rules: \U0001F447\n")
print(emoji.emojize(' :backhand_index_pointing_right: The Rules: :backhand_index_pointing_down:\n'))
#print(" \U0001F449 There are only 5 small battleships hiding on")
print(emoji.emojize(' :backhand_index_pointing_right: There are only 5 small battleships hiding on'))
print("the sea and you have to locate them and shoot them down.\n")
#print(" \U0001F449 You have 10 shots only.\n")
print(emoji.emojize(' :backhand_index_pointing_right: You have 10 shots only.\n'))
#print(" \U0001F449 Every time you locate a ship and sink it,")
print(emoji.emojize(' :backhand_index_pointing_right: Every time you locate a ship and sink it,'))
print(" an 'X' will appear on the guess board in front of you.\n")
#print(" \U0001F449 Every time you miss a shot,")
print(emoji.emojize(' :backhand_index_pointing_right: Every time you miss a shot,'))
print("a '-' will appear on the board in front of you.\n")
#print(" \U0001F449 Once you've run out of shots or")
print(emoji.emojize(" :backhand_index_pointing_right: Once you've run out of shots or"))
print("sunk all 5 ships the game's over.\n")
#print(" Good luck!\U0001F340 LET'S PLAY!\n")
print(emoji.emojize(" Good luck!:four_leaf_clover: LET'S PLAY!\n"))
main()
