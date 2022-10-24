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
    def check_winner(entries):
        # if every item in the list is the same (all X's / O's)
        if len(set(entries)) == 1 and EMPTY not in entries: 
            winner = X if X in entries else O
            return winner
        else:
            return None

    for j in range(3):
        diag1 = []
        diag2 = []
        vert = []

        for i in range(3):
            horiz = board[i]

            vert.append(horiz[j])

            # check for winner horizontally 
            if check_winner(horiz) != None: return check_winner(horiz)

            diag_dict = {0:2, 1:1, 2:0}

            # check if the board is filled out diagonally
            try:
                # create list of diagonal values
                diag1.append(horiz[i])
                diag2.append(horiz[diag_dict[i]])
            except:
                return None

        # check for winner diagonally 
        if check_winner(diag1) != None: return check_winner(diag1)
        if check_winner(diag2) != None: return check_winner(diag2)
        
        # check for winner vertically 
        if check_winner(vert) != None: return check_winner(vert)


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    flat_board = [play for row in board for play in row] 

    # if there is a winner or no more available moves
    if winner(board) != None or EMPTY not in flat_board:
        return True
    else:
        return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # if the game is finished
    if terminal(board): 
        if winner(board) != None:
            if winner(board) == X: return 1
            else: return -1
        # if there isn't a winner
        else: return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def maximise(board):
        optimal_action = ()

        # if game over, return utility of final board 
        if terminal(board): return utility(board)
        
        x = -5

        # for all possible moves
        for action in actions(board):
            # get minimised utility of board
            min_utility = minimise(result(board, action))
            
            # avoids int not subcript error AND list not comparable to tuple error 
            if isinstance(min_utility, list):
                min_utility = min_utility[0]
            # if outcome is better than current best outcome
            if min_utility > x:
                x = min_utility
                optimal_action = action 
        return [x, optimal_action]

    def minimise(board):
        optimal_action = ()
        if terminal(board): return ["Game Over", utility(board)]

        x = 5

        for action in actions(board):
            max_utility = maximise(result(board, action))
            
            if isinstance(max_utility, list):
                max_utility = max_utility[0]
            
            if max_utility < x:
                x = max_utility
                optimal_action = action 
        return [x, optimal_action]

    if player(board) == X:
        return maximise(board)[1]
    if player(board) == O:
        return minimise(board)[1]


example_board = [[X, X, X],
                [O, O, X],
                [X, O, O]]

print(f"minimax is {minimax(example_board)}") 