# COSC 1336, Lab 10, Problem 3
# Robert Morales

import random

# Utility functions for working with the board

def board_create():
    """ Creates a tic-tac-toe board. """
    return [[' ' for col in range(3)] for row in range(3)]

def board_copy(board):
    """ Creates a copy of a tic-tac-toe board. """
    return [[board[rx][cx] for cx in range(3)] for rx in range(3)]

def board_get_row(board, rx):
    """ Returns all symbols in the specified row. """
    return board[rx][0:]

def board_get_col(board, cx):
    """ Returns all symbols in the specified column. """
    return [row[cx] for row in board]

def board_get_symbol(board, rx, cx):
    """ Returns the symbol at the row and column indices. """
    return board[rx][cx]

def board_get_symbols(board, cells):
    """
    Return all symbols in the specified sequence of element positions.

    Parameter 'cells' is expected to be a list of row and column
    indices in tuples.
    """
    return [board[rx][cx] for rx,cx in cells]

def board_has_symbol(sym, board, rx, cx):
    """ Determines if the board contains the symbol at the specified cell. """
    return sym == board[rx][cx]

def board_set_symbol(sym, board, rx, cx):
    """ Assigns the symbol to the specified cell in the board. """
    board[rx][cx] = sym

def board_get_blanks(board):
    """ Returns the row and column indices of all blank symbols in the board. """
    return [(rx, cx) for rx in range(3) for cx in range(3) \
            if board[rx][cx] == ' ']

def board_count_blanks(board):
    """ Determines the number of blank symbols in the board. """
    return len([col for row in board for col in row if col == ' '])

def board_get_corners(board):
    """ Returns the symbols in each corner of the board. """
    return [board[rx][cx] for rx in [0,-1] for cx in [0,-1]]

def print_board(board):
    print()
    for rx in range(3):
        for cx in range(3):
            print(' ',board[rx][cx], end='', sep='')
            if cx < 2:
                print(' ','|', end='', sep='')
        print()
        if rx < 2:
            print('-----------')
    print()

# End of utility functions

def get_user_move(board):
    chose_move = False
    prompt = 'Enter your move: '

    while not chose_move:
        try:
            row, col = [int(val) for val in input(prompt).split(',')]
            if (not (-3 < row < 3)) or (not (-3 < col < 3)):
                print("Invalid data. Check your typing and try again.\n")
            elif board_has_symbol(' ', board, row, col):
                board_set_symbol('x', board, row, col)
                chose_move = True
            else:
                print("I'm sorry, that spot is taken.  Try again.")
        except (IndexError, ValueError):
            print("Invalid input. Please try again.")
            print("Your move should have both row & column: 0,0; 0,1; etc.\n")

def choose_computer_move(board):
    blanks = board_get_blanks(board)

    # determine if we can win by placing 'o' in all the blanks
    for rx, cx in blanks:
        board_set_symbol('o', board, rx, cx)
        over, winner = calc_game_over(board)
        if over and winner == 'o':
            print("Computer's move: {},{}".format(rx, cx))
            return
        else:
            board_set_symbol(' ', board, rx, cx)

    # block opponent from winning on their next move
    for rx, cx in blanks:
        board_set_symbol('x', board, rx, cx)
        over, winner = calc_game_over(board)
        if over and winner == 'x':
            board_set_symbol('o', board, rx, cx)
            print("Computer's move: {},{}".format(rx, cx))
            return
        else:
            board_set_symbol(' ', board, rx, cx)

    # block opponent's fork
    if board_has_symbol('o', board, 1, 1) and 'x' in board_get_corners(board):
        # avoid playing a corner
        for rx, cx in [(0,1), (1,0), (1,2), (2,1)]:
            if board_has_symbol(' ', board, rx, cx):
                board_set_symbol('o', board, rx, cx)
                print("Computer's move: {},{}".format(rx, cx))
                return

    # go for the center
    if (1,1) in blanks:
        board_set_symbol('o', board, 1, 1)
        print("Computer's move: 1,1")
        return

    # choose an empty corner
    for rx, cx in [(0,0), (0,2), (2,0), (2,2)]:
        if board_has_symbol(' ', board, rx, cx):
            board_set_symbol('o', board, rx, cx)
            print("Computer's move: {},{}".format(rx, cx))
            return

    # choose an empty side
    for rx, cx in [(0,1), (1,0), (1,2), (2,1)]:
        if board_has_symbol(' ', board, rx, cx):
            board_set_symbol('o', board, rx, cx)
            print("Computer's move: {},{}".format(rx, cx))
            return

    # this shouldn't ever happen
    raise RuntimeError("Bork bork bork!!")

def calc_game_over(board):
    winning_player = ' '
    game_over = False
    symbols = (['x', 'x', 'x'], ['o', 'o', 'o'])

    # check each row for a win
    for r in [0, 1, 2]:
        if board_get_row(board, r) in symbols:
            game_over = True
            winning_player = board_get_symbol(board, r, 0)
            break

    # check each column for a win
    if not game_over:
        for c in [0, 1, 2]:
            if board_get_col(board, c) in symbols:
                game_over = True
                winning_player = board_get_symbol(board, 0, c)
                break

    # check diagonals for a win
    if not game_over:
        if (board_get_symbols(board, [(0,0),(1,1),(2,2)]) in symbols) or \
           (board_get_symbols(board, [(0,2),(1,1),(2,0)]) in symbols):
            game_over = True
            winning_player = board_get_symbol(board, 1, 1)

    # check for a tie
    if not game_over:
        game_over = board_count_blanks(board) == 0

    return game_over, winning_player

def main():
    board = board_create()
    game_over = False
    while not game_over:
        print_board(board)
        get_user_move(board)
        game_over, winner = calc_game_over(board)
        if not game_over:
            choose_computer_move(board)
            game_over, winner = calc_game_over(board)

    print_board(board)

    if winner == ' ':
        print("Game ended in a tie.")
    else:
        print("Game over. Winner:", winner)

main()
