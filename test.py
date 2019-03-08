import unittest
import random

from my_game import space_check, full_board_check


class TestSpaceCheck(unittest.TestCase):
    '''
    Test to show that if there is an empty space on the board, True is returned
    '''
    def test_space_check(self):
        board = [' '] * 10
        position = 1
        result = space_check(board, position)
        self.assertEqual(result, True)
    
    def test_full_board_check(self):
        # board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'X']
        board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
        result = full_board_check(board)
        self.assertEqual(result, False)




if __name__ == '__main__':
    unittest.main()
