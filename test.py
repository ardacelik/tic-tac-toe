import unittest
import random

from my_game import space_check, full_board_check


class TestSpaceCheck(unittest.TestCase):

    def test_space_check(self):
        '''
        Test to show that if the position is free
        '''
        board = [' '] * 10
        position = 1
        result = space_check(board, position)
        self.assertEqual(result, True)

    def test_full_board_check(self):
        '''
        Test to check if the board is full
        '''
        # board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']
        board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        result = full_board_check(board)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
