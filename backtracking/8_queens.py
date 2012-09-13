#!/usr/bin/env python

'''
8_queens.py - Solution to the 8 queens chess problem.

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
        self.queen_positions   = []              # Where queens have been placed
        self.valid_squares     = set(range(64))  # Where a queen could be placed
        self.tried_squares     = set()           # Squares blacklisted for placement
        self.remaining_squares = self.valid_squares - self.tried_squares


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


    def calculate_valid_squares(self):
        '''Find the set of squares not attacked by any currently placed queen.'''

        self.valid_squares = set(range(64))
        for queen_square in self.queen_positions:
            rank_mask       = self.find_rank(queen_square)
            file_mask       = self.find_file(queen_square)
            left_diag_mask  = self.find_left_diagonal(queen_square)
            right_diag_mask = self.find_right_diagonal(queen_square)

            to_mask = set(rank_mask + file_mask + left_diag_mask + right_diag_mask)

            self.valid_squares = self.valid_squares - to_mask
            self.remaining_squares = self.valid_squares - self.tried_squares

        return self.valid_squares


    def place_queen_at(self, square):
        '''Place a queen on the target square, and redetermine the valid squares.'''

        self.queen_positions.append(square)
        self.calculate_valid_squares()


    def remove_last_queen(self):
        '''Remove the last placed queen, and redetermine the valid squares.'''

        last_square = self.queen_positions.pop()
        self.calculate_valid_squares()

        return last_square


    def update_remaining_squares(self):
        self.remaining_squares = self.valid_squares - self.tried_squares


    def ignore_square(self, square):
        '''Add a square to the blacklist.'''

        self.tried_squares.add(square)
        self.remaining_squares = self.valid_squares - self.tried_squares


    def num_to_algebraic(self, square):
        '''Convert a square number to an algebraic (chess notation) representation,
           for human consumption.'''

        rank, file = self.num_to_rank_and_file(square)

        alg_file = "abcdefgh"[file]
        alg_rank = rank + 1

        return alg_file + str(alg_rank)


    def ascii_board(self):
        '''Create an ascii chessboard, with queen positions marked.'''

        # A row of the board, stored in a list to allow modification
        grid_row_list = ['-|'] * 8

        # Construct the chessboard as a list of lists
        grid_list = []
        for i in range(8):
            grid_list.append(grid_row_list[:])

        # Place the queens on the chessboard
        for queen_square in self.queen_positions:
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



r_level = 0
def place_queens(n_queens, board):
    ''' Recursive solver for the 8 queens problem. The steps involved:
        1) Find where we could place a queen.
        2) Place a queen.
        3) Repeat.

        Backtracking: If we are unable to place a queen (no valid squares remain),
        we immediately stop searching that sub-branch, and backtrack. We store the
        failed attempt in a blacklist. When there are no valid squares that have not
        already been tried (and blacklisted), we know this branch is not a solution.
        We backtrack (de-recurse) again, and try a different square from the level
        above.

        n_queens - The total number of queens to try and place.
        board    - The current state of the board.
        r_level  - A counter tracking our recursion level (diagnostic only).
        '''

    global r_level

    print "\nTop of place_queens. Recursion level =", r_level

    while n_queens > -1:

        # Find the set of squares still awaiting exploration
        board.update_remaining_squares()
        #remaining_squares = board.valid_squares - board.tried_squares
        print "Board.remaining:", board.remaining_squares

        # If there's nothing else to try...
        if len(board.remaining_squares) == 0:
            #... then this branch is a dead end
            print "No remaining squares in this search branch - backtracking..."

            # Undo the last move, and add it to the ignore list
            square = board.remove_last_queen()
            alg_sq = board.num_to_algebraic(square)
            board.ignore_square(square)

            print "Picked up queen %d from square %d (%s)." % (n_queens+1, square, alg_sq)

            # Backtrack the search (de-recurse) a step
            return board


        # Grab the next candidate square, and place a queen there
        square = board.remaining_squares.pop()
        board.place_queen_at(square)
        alg_sq = board.num_to_algebraic(square)
        print "Placed queen %d at square %d (%s)." % (n_queens, square, alg_sq)
        n_queens -= 1


        # It's time to place the next queen in this branch
        print "Recursing..."
        r_level += 1

        # Store the current ignore list at this scope; clear it for the sub-branch
        current_ignored = board.tried_squares.copy()
        board.tried_squares.clear()

        # Recurse to try and place the next queen
        board = place_queens(n_queens, board)

        # Back from trying that branch - update the list of squares we've tried
        r_level -= 1
        print "\nBack from recursion. Current recursion level =", r_level
        board.tried_squares = board.tried_squares | current_ignored

        # Get the number of queens left to be placed
        n_queens = 7 - len(board.queen_positions)


    # We've left the loop - all the queens have been placed!
    print "All queens successfully placed."
    return board



if __name__ == '__main__':

    # The number of queens to place
    n_queens = 8

    # Create the board, and place the queens
    board = Board()
    board = place_queens(n_queens, board)

    # Print the details of the final configuration
    algebraic_squares = []
    for pos in board.queen_positions:
        alg_sq = board.num_to_algebraic(pos)
        algebraic_squares.append(alg_sq)

    print "\nFinal queen positions (algebraic):", ", ".join(algebraic_squares)
    print board.ascii_board()
