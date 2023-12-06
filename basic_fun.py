from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print("  " + board[7] + " | " + board[8] + " | " + board[9] + " ")
    print("-------------")
    print("  " + board[4] + " | " + board[5] + " | " + board[6] + " ")
    print("-------------")
    print("  " + board[1] + " | " + board[2] + " | " + board[3] + " ")


def player_input():
    marker = " "

    '''
    OUTPUT= Player 1 marker , Player 2 marker
    '''

    while marker != "X" and marker != "O":
        marker = input("Choose marker X or O : ").upper()

    player1 = marker
    if player1 != "X":
        return "O", "X"
    else:
        return "X", "O"


def place_marker(board, mark, position):
    board[position] = mark


def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark or
            board[4] == board[5] == board[6] == mark or
            board[7] == board[8] == board[9] == mark or  # Checking all rows
            board[1] == board[4] == board[7] == mark or
            board[2] == board[5] == board[8] == mark or
            board[3] == board[6] == board[9] == mark or  # Checking all column
            board[1] == board[5] == board[9] == mark or  # Checking all diagonals
            board[3] == board[5] == board[7] == mark)


def first_choice():
    flip = random.randint(0, 1)
    if flip == 0:
        return "player1"
    else:
        return "player2"


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    # Board is full if return True
    return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = input("Choose the position within range(1-9) : ")
        if position.isdigit():
            return int(position)
        else:
            print("Please enter a valid number ")


def replay():
    choice = input("Play again? Yes or No : ").lower()
    return choice == "yes"
