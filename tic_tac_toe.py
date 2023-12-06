from basic_fun import *

# WHILE LOOP TO KEEP RUNNING THE GAME
start = True
while start:
    print("Welcome to TicTac Game")
    # Play the Game

    ## SET EVERYTHING UP (BOARD, WHOS FIRST,CHOOSE THE MARKER X,O)

    the_board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = first_choice()
    print(turn + " will go first")
    Game_on = True
    # GAME PLAY
    while Game_on:
        # PLAYER ONE TURN
        if turn == "player 1":
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # Place the maker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("The player 1 has won")
                Game_on = False
            else:
                # or check there is a tie
                if full_board_check(the_board):
                    print("The game is tie!")
                else:
                    # or No tie and No win  then next player turn
                    turn = "player 2"
        else:
            # PLAYER TWO TURN
            # show the board
            display_board(the_board)
            # choose the position
            position = player_choice(the_board)
            # Place the maker on the position
            place_marker(the_board, player2_marker, position)
            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("The player 2 has won")
                Game_on = False
            else:
                if full_board_check(the_board):
                    print("The game is tie!")
                else:
                    turn = "player 1"
    start = replay()

print("----THE END----")
