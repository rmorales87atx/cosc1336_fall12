# COSC 1336, Lab 10, Problem 3 (enhanced)
# Robert Morales

import tkinter as tk
import tkinter.messagebox as msgbox
import random
from itertools import permutations

class Board:
    """
    Class representing a TicTacToe board.
    """

    def __init__(self):
        """ Initializes the board object. """
        self.__data = [[None]]

    def create(self, size = 3):
        """ Creates a TicTacToe board with the given size. """
        if size < 3:
            raise ValueError('board size must be ≥ 3')
        self.__data = [[None for col in range(size)] for row in range(size)]
        return self

    def assign(self, data):
        """ Initializes the TicTacToe board from existing data. """
        if len(data) != len(data[0]):
            raise ValueError("array must be square")
        if len(data) < 3:
            raise ValueError('board size must be ≥ 3')
        self.__data = [[col for col in row] for row in data]
        return self

    def copy(self):
        """ Returns a copy of the TicTacToe board's data. """
        return [[col for col in row] for row in self.__data]

    def size(self):
        """ Returns the number of rows and number of columns. """
        return len(self.__data)

    def row(self, row_index):
        """ Returns all symbols in the specified row. """
        return [el for el in self.__data[row_index]]

    def col(self, col_index):
        """ Returns all symbols in the specified column. """
        return [row[col_index] for row in self.__data]

    def symbol(self, row_index, col_index):
        """ Returns the specified symbol at the row and column indices. """
        return self.__data[row_index][col_index]

    def symbols(self, positions):
        """ Returns symbols at all specified row/column positions. """
        return [self.__data[rx][cx] for rx,cx in positions]

    def is_blank(self, row_index, col_index):
        """ Determines if the specified cell is blank. """
        return self.__data[row_index][col_index] is None

    def set_symbol(self, sym, row_index, col_index):
        """ Assigns the symbol to the specified cell in the board. """
        self.__data[row_index][col_index] = sym

    def blanks(self):
        """ Returns the row and column indices of all blank symbols. """
        return [(rx, cx) for rx, row in enumerate(self.__data) \
                         for cx, col in enumerate(row) if col is None]

    def num_blanks(self):
        """ Return the number of blank symbols. """
        return len([col for row in self.__data for col in row if col is None])

    def diagonal(self, direction):
        """
        Returns an iterator for all symbols in the specified diagonal pattern.
        """
        size = self.size()
        temp = []
        if direction in ('left', '<'):
            for rx in range(size-1, -1, -1):
                yield self.__data[rx][rx]
        elif direction in ('right', '>'):
            for rx in range(size):
                yield self.__data[rx][size-rx-1]
        else:
            raise ValueError("invalid input: `direction` should be 'left' or 'right'")

    def midpoint(self):
        """ Returns the center position of the board. """
        idx = self.size() // 2
        return (idx, idx)

    def corners(self):
        """ Returns an iterator for the symbols in each corner of the board. """
        for rx in [0,-1]:
            for cx in [0,-1]:
                yield self.__data[rx][cx]

    def side(self, side):
        """
        Returns an iterator for all symbols from one side of the board.
        The 'side' parameter is a string that specifies either top, bottom,
        left, or right. The symbols '^', '_', '<', and '>' can also be used.
        """
        size = len(self.__data)
        if side in ('^', 'top'):
            for cx in range(1,size-1):
                yield self.__data[0][cx]
        elif side in ('_', 'bottom'):
            for cx in range(1,size-1):
                yield self.__data[-1][cx]
        elif side in ('<', 'left'):
            for rx in range(1,size-1):
                yield self.__data[rx][0]
        elif side in ('>', 'right'):
            for rx in range(1,size-1):
                yield self.__data[rx][-1]
        else:
            raise ValueError("invalid request")

    def side_positions(self):
        """
        Returns an iterator for the row/column indices of 
        all side positions on the board.
        """
        sides = [(x,y) for x in [0,-1] for y in list(range(1, self.size()-1))]
        for i in range(len(sides)):
            for p in permutations(sides[i]):
                yield p

    def __str__(self):
        """ Returns the TicTacToe board as an ASCII drawing. """
        strings = []
        strings.append('')
        for rx in range(self.size()):
            row_str = ''
            for cx in range(self.size()):
                sym = self.get_symbol(rx, cx) or ' '
                row_str += ' ' + sym
                if cx < self.num_cols()-1:
                    row_str += ' |'
            strings.append(row_str)
            if rx < self.num_rows()-1:
                strings.append(('-----' * (self.num_cols()-1)) + '-')
        strings.append('')
        return str.join('\n', strings)

class Game:
    def __init__(self):
        """ Initializes the Game object. """
        self.board = None
        self.sym_user = None
        self.sym_cpu = None

    def new(self, size = 3, symbols = ('X', 'O')):
        """
        Creates a new game.

        By default a 3x3 board is created with symbols 'X' representing
        the user and 'O' representing the computer. These parameters
        can be changed via 'size' and 'symbols', respectively.
        """

        self.sym_user, self.sym_cpu = symbols
        self.board = Board()
        self.board.create(size)

    def move_user(self, row, col):
        """ Places the user's move. """
        try:
            over, winner = self.status()
            if (not over) and self.board.is_blank(row, col):
                self.board.set_symbol(self.sym_user, row, col)
                return True
            else:
                return False
        except IndexError:
            raise IndexError("invalid row/column index")

    def move_computer(self):
        """
        Chooses the CPU's move using a predetermined strategy.
        """
        over, winner = self.status()
        if over:
            return (None, None)

        board = self.board
        blanks = board.blanks()

        # the following symbol aliases are used for typing convenience
        X = self.sym_user
        O = self.sym_cpu

        # determine if we can win by placing 'o' in all the blanks
        for rx, cx in blanks:
            board.set_symbol(O, rx, cx)
            over, winner = self.status()
            if over and winner == O:
                return (rx, cx)
            else:
                board.set_symbol(None, rx, cx)

        # block opponent from winning on their next move
        for rx, cx in blanks:
            board.set_symbol(X, rx, cx)
            over, winner = self.status()
            if over and winner == X:
                board.set_symbol(O, rx, cx)
                return (rx, cx)
            else:
                board.set_symbol(None, rx, cx)

        # block opponent's fork, if we have the midpoint
        rx, cx = board.midpoint()
        if board.symbol(rx, cx) == O and X in board.corners():
            # avoid playing a corner!
            for rx, cx in board.side_positions():
                if board.is_blank(rx, cx):
                    board.set_symbol(O, rx, cx)
                    return (rx, cx)

        # go for the center
        rx, cx = board.midpoint()
        if board.is_blank(rx, cx):
            board.set_symbol(O, rx, cx)
            return (rx, cx)

        # choose an empty corner
        for rx, cx in [(0,0), (0,-1), (-1,0), (-1,-1)]:
            if board.is_blank(rx, cx):
                board.set_symbol(O, rx, cx)
                return (rx, cx)

        # choose an empty side
        for rx, cx in board.side_positions():
            if board.is_blank(rx, cx):
                board.set_symbol(O, rx, cx)
                return (rx, cx)

        # choose randomly, if there's absolutely nothing left...
        rx, cx = random.choice(blanks)
        board.set_symbol(O, rx, cx)
        return (rx, cx)

    def status(self):
        """
        Returns the status of the game.

        The status consists of two values: a Boolean indicating if the
        game is considered over, due to either a tie or a win, and a
        string containing the winner (if there is no tie).
        """
        over = False
        winner = None
        board = self.board
        symbols = ([self.sym_user] * board.size(),
                   [self.sym_cpu] * board.size())

        # check each row for a win
        for rx in range(board.size()):
            if board.row(rx) in symbols:
                over = True
                winner = board.symbol(rx, 0)
                break

        # check each column for a win
        if not over:
            for cx in range(board.size()):
                if board.col(cx) in symbols:
                    over = True
                    winner = board.symbol(0, cx)
                    break

        # check diagonals for a win
        if not over:
            if (board.diagonal('<') in symbols) or (board.diagonal('>') in symbols):
                over = True
                mid_row, mid_col = board.midpoint()
                winner = board.symbol(mid_row, mid_col)

        # check for a tie
        if not over:
            over = board.num_blanks() == 0

        return over, winner

    def is_over(self):
        """ Shortcut method to determine if the game is over. """
        if None in (self.board, self.sym_user, self.sym_cpu):
            return True

        over, winner = self.status()
        return over

class Application:
    def __init__(self, parent):
        self.bsize = 3
        self.syms = ('X', 'O')
        self.game = Game()

        # main frame: TicTacToe button board
        # contains sub-frames for each row of buttons

        self.frame1 = tk.Frame(parent)
        self.buttons = [[None for cx in range(self.bsize)] \
                        for rx in range(self.bsize)]

        for rx in range(self.bsize):
            row_frame = tk.Frame(self.frame1)
            for cx in range(self.bsize):
                btn = tk.Button(row_frame, text='')
                btn['command'] = lambda rx=rx, cx=cx: self.button_click(rx, cx)
                btn['width'] = 12
                btn['height'] = btn['width'] // 2
                btn['disabledforeground'] = btn['fg']
                btn['state'] = tk.DISABLED
                btn.pack()
                self.buttons[rx][cx] = btn
            row_frame.pack(side='left')

        self.frame2 = tk.Frame(parent)
        self.frame2_button1 = tk.Button(self.frame2, text="New Game", command=self.new_game)
        self.frame2_button1.pack(side=tk.LEFT)
        self.frame2.pack()

        self.frame3 = tk.Frame(parent)
        self.status = tk.StringVar()
        self.frame3_label1 = tk.Label(parent, textvariable=self.status)
        self.frame3_label1.pack(side='bottom')
        self.frame3.pack()
        self.frame1.pack()

        self.set_status("Click [New Game] to begin.")

    def new_game(self):
        game = self.game

        if not game.is_over() and not msgbox.askyesno("Warning!", "The game isn't over yet.\nDo you want to abandon this game and start another?"):
            return

        self.game.new(self.bsize, self.syms)

        size = game.board.size()
        for rx in range(size):
            for cx in range(size):
                btn = self.buttons[rx][cx]
                btn['text'] = ''
                btn['state'] = tk.NORMAL
                btn['cursor'] = 'hand1'

        self.set_status("Select a move.")

    def set_status(self, fmt, *args):
        self.status.set(fmt.format(*args))

    def mark_button(self, rx, cx):
        btn = self.buttons[rx][cx]
        btn["text"] = self.game.board.symbol(rx, cx)
        btn["state"] = tk.DISABLED
        btn['cursor'] = 'arrow'

    def button_click(self, row_index, col_index):
        game = self.game

        if game.move_user(row_index, col_index):
            #print(game.board)
            self.mark_button(row_index, col_index)

            over, winner = game.status()

            if not over:
                cpu_rx, cpu_cx = game.move_computer()
                #print(game.board)
                over, winner = game.status()

                if cpu_rx < 0:
                    cpu_rx += game.board.size()
                if cpu_cx < 0:
                    cpu_cx += game.board.size()

                self.set_status("You played {},{}; CPU played {},{}", row_index,
                    col_index, cpu_rx, cpu_cx)

                self.mark_button(cpu_rx, cpu_cx)

            if over:
                if winner is None:
                    self.set_status("Game ended in a tie.")
                elif winner == game.sym_user:
                    self.set_status("You won!")
                elif winner == game.sym_cpu:
                    self.set_status("You lost.")
        else:
            msgbox.showerror('TicTacToe', 'Invalid move.')

root = tk.Tk()
app = Application(root)
root.mainloop()
