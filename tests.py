import unittest
from basic_fun import *


class Test_Tictactoe(unittest.TestCase):
    def test_player_input(self):
        player1, player2 = player_input()
        if player1 == "X":
            self.assertEqual(player2, 'O')
        else:
            self.assertEqual(player2, "X")

    def test_win_check(self):
        t_board = [" ", "X", "X", "X", "O", "X", "O", "X", "X", "O"]
        result = win_check(t_board, "X")
        self.assertEqual(result, True)

    def test_space_checker(self):
        t_board = [" ", "X", "X", "X", "O", " ", "O", "X", "X", "O"]
        result1 = space_check(t_board, 2)
        self.assertEqual(result1, False)
        result2 = space_check(t_board, 5)
        self.assertEqual(result2, True)

    def test_full_board_check(self):
        board1 = [" "] * 10
        result1 = full_board_check(board1)
        self.assertEqual(result1, False)
        board2 = ["#", "X", "O", "X", "X", "O", "X", "O", "X", "O", "X"]
        result2 = full_board_check(board2)
        self.assertEqual(result2, True)

    def test_player_choice(self):
        board1 = ["#", " ", "O", "X", "X", "O", "X", " ", "X", "O", "X"]
        result = player_choice(board1)
        self.assertEqual(result, 7)

    def test_first_choice(self):
        result = first_choice()
        if result == "player1":
            self.assertEqual(result, "player1")
        else:
            self.assertEqual(result, "player2")

    def test_replay(self):
        result = replay()
        if result:
            self.assertEqual(result, True)
        else:
            self.assertEqual(result,False)
