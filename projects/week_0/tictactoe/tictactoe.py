"""
Tic Tac Toe Player
"""

import math
from collections import Counter
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    flat_board = [play for row in board for play in row] # flatten the board
    count_dict = Counter(flat_board) # count the plays 

    # assuming X always starts 
    if board == initial_state or count_dict[X] == count_dict[O]: return X
    else: return O

# flat_board = [play for row in initial_state() for play in row]

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # create list of all board coordinates 
    all_moves = [(j, i) for j in range(3) for i in range(3)]

    # check if the board is the initial board, in which case all moves are available
    if board == initial_state(): return all_moves

    # will put the board in order, right to left, top row to bottom 
    flat_board = [play for row in board for play in row]

    # gets list of indices where no one has played 
    free_move_idx = [i for i, val in enumerate(flat_board) if val is None]
    
    # returns board spaces that have not been played 
    available_moves = [move for idx, move in enumerate(all_moves) if idx in free_move_idx]

    return available_moves

example_board = [[1, O, O],
                [X, O, X],
                [X, O, X]]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # create deep copy of board
    board_copy = deepcopy(board)

    # check whose turn it is 
    current_player = player(board_copy)

    # if that action is valid on the given board 
    if action in actions(board_copy):
        # place player marker there
        board_copy[action[0]][action[1]] = current_player
        return board_copy
    else:
        raise Exception("Invalid action")

# print(result(example_board, (2,2)))

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # diag_1 = []
    for j in range(3):

        vert = []

        for i in range(3):
            horiz = board[i]

            vert.append(horiz[j])

            # check for winner horizontally 
            if len(set(horiz)) == 1 and EMPTY not in horiz: 
                winner = X if X in horiz else O
                return winner

            # check for winner diagonally 
            # diag_1.append(horiz[i])

        if len(set(vert)) == 1 and EMPTY not in vert: 
            winner = X if X in vert else O
            return winner 

print(f"winner is {winner(example_board)}")

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
