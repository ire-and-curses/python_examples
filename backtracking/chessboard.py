#!/usr/bin/env python

'''
chessboard.py - Solution to the 8 queens chess problem.

This module implements a chessboard and a recursive search algorithm to find a
solution for the problem of placing 8 queens on a chessboard, without any queen
attacking any other.

This search is interesting, because it is a fundamental searching technique
that can be applied to any discrete tree. It is efficient because it stops searching
each branch as soon as a solution is determined to be impossible.

Author: Eric Saunders
April 2011
'''

class Board(object):
    '''
        Representation of a chessboard for the 8 queens problem. Squares are stored
        according to the following layout:

        56  57  58  59  60  61  62  63   | 7
        48  49  50  51  52  53  54  55   | 6
        40  41  42  43  44  45  46  47   | 5  R
        32  33  34  35  36  37  38  39   | 4  a
        24  25  26  27  28  29  30  31   | 3  n
        16  17  18  19  20  21  22  23   | 2  k
         8   9  10  11  12  13  14  15   | 1  s
         0   1   2   3   4   5   6   7   | 0
        ---------------------------------|---
         0   1   2   3   4   5   6   7   |
         a   b   c   d   e   f   g   h   |
                     Files
    '''


    def __init__(self):
        pass

    def num_to_rank_and_file(self, square):
        '''Convert a square number to numeric rank and file positions.'''

        rank = square / 8
        file = square % 8

        return rank, file


    def find_rank(self, square):
        '''Find every square sharing the same rank as the provided square.'''

        rank, file = self.num_to_rank_and_file(square)
        return range(rank*8, (rank+1)*8)


    def find_file(self, square):
        '''Find every square sharing the same file as the provided square.'''

        rank, file = self.num_to_rank_and_file(square)
        return range(file, 64-(7-file), 8)


    def find_left_diagonal(self, square):
        '''Find every square sharing the left-right south-north diagonal with the
           provided square.'''

        rank, file = self.num_to_rank_and_file(square)

        start_limiter = rank
        end_limiter   = file
        if file <= rank:
            start_limiter = file
            end_limiter   = rank

        # Left-Right South-North diagonal
        start_square = square - (9 * start_limiter)
        end_square   = square + (9 * (7-end_limiter))
        lr_diagonal  = range(start_square, end_square+1, 9)

        return lr_diagonal


    def find_right_diagonal(self, square):
        '''Find every square sharing the right-left south-north diagonal with the
           provided square.'''

        rank, file = self.num_to_rank_and_file(square)

        start_limiter = 7-file
        end_limiter   = 7-rank
        if file + rank <= 7:
            start_limiter = rank
            end_limiter   = file

        # Right-Left South-North diagonal
        start_square = square - (7 * (start_limiter))
        end_square   = square + (7 * (end_limiter))
        rl_diagonal  = range(start_square, end_square+1, 7)

        return rl_diagonal


    def num_to_algebraic(self, square):
        '''Convert a square number to an algebraic (chess notation) representation,
           for human consumption.'''

        rank, file = self.num_to_rank_and_file(square)

        alg_file = "abcdefgh"[file]
        alg_rank = rank + 1

        return alg_file + str(alg_rank)


    def ascii_board(self, queen_positions):
        '''Create an ascii chessboard, with queen positions marked.'''

        # A row of the board, stored in a list to allow modification
        grid_row_list = ['-|'] * 8

        # Construct the chessboard as a list of lists
        grid_list = []
        for i in range(8):
            grid_list.append(grid_row_list[:])

        # Place the queens on the chessboard
        for queen_square in queen_positions:
            rank, file = self.num_to_rank_and_file(queen_square)
            grid_list[rank][file] = 'Q|'


        # Construct the final ascii chessboard
        return self._make_ascii_board(grid_list)


    def _make_ascii_board(self, grid_list):
        '''Given a list of lists representing a board, construct an ascii string
           representation of a chessboard, for printing.'''

        # The top and bottom of the chessboard
        grid_edge = "-" * 17 + "\n"

        # Add the top edge of the board
        grid = "" + grid_edge

        # Reverse the order of the rows, to match algebraic numbering of ranks
        grid_list.reverse()

        # Convert each row from a list to a string, and add the rank number
        i = 1
        for row in grid_list:
            grid_row = "|" + "".join(row) + " " + str(9-i) + "\n"
            grid += grid_row
            i += 1

        # Add the bottom edge of the board
        grid += grid_edge

        # Add the file letters
        file_letters = " a b c d e f g h"
        grid += file_letters

        # Voila! An ascii string chessboard.
        return grid



class EightQueens(object):

    def __init__(self):
        self.solution       = []              # Where queens have been placed
        self.valid_squares  = set(range(64))  # Where a queen could be placed

        self.board = Board()


    def calculate_valid_squares(self):
        '''Find the set of squares not attacked by any currently placed queen.'''

        self.valid_squares = set(range(64))
        for queen_square in self.solution:
            rank_mask       = self.board.find_rank(queen_square)
            file_mask       = self.board.find_file(queen_square)
            left_diag_mask  = self.board.find_left_diagonal(queen_square)
            right_diag_mask = self.board.find_right_diagonal(queen_square)

            to_mask = set(rank_mask + file_mask + left_diag_mask + right_diag_mask)

            self.valid_squares = self.valid_squares - to_mask


    def next(self):
        # Don't provide more values if we have a full solution
        if len(self.solution) >= 8:
            return False

        # Return another square, or False if we've run out
        try:
            next_square = self.valid_squares.pop()
        except KeyError:
            next_square = False

        return next_square


    def make_move(self, move):
        self.solution.append(move)
        self.calculate_valid_squares()


    def undo_last_move(self):
        self.solution.pop()


    def reset(self):
        self.calculate_valid_squares()


    def is_solved(self):
        if len(self.solution) == 8:
            return True

        return False


if __name__ == '__main__':
    from discrete_solver import solve, verbose_solve

    problem = EightQueens()
    b = verbose_solve(problem)
    print b.solution

    algebraic_squares = []
    for square in problem.solution:
        alg_sq = problem.board.num_to_algebraic(square)
        algebraic_squares.append(alg_sq)

    print "\nFinal queen positions (algebraic):", ", ".join(algebraic_squares)
    print problem.board.ascii_board(problem.solution)

