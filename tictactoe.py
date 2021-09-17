"""
Tic Tac Toe Player
"""

import math
import copy

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
    Xcount, Ocount = 0 , 0
    for row in board:
        for column in row:
            if column == X:
                Xcount = Xcount + 1
            elif column == O:
                Ocount = Ocount + 1
    return X if Ocount == Xcount or Xcount < Ocount else O
            


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    action = tuple()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                action = (i , j)
                actions.add(action)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if board[action[0]][action[1]] != EMPTY :
        raise ValueError
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = X if player(board) == X else O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #horizontal
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        elif board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]
    if board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None :
        return True
    else :
        return not any(EMPTY in iterator for iterator in board)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X :
        return 1
    elif winner(board) == O :
        return -1
    else :
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == O:
        arr = min_value(board)
        return arr[1]
    else:
        arr = max_value(board)
        return arr[1]


def max_value(board):
    """
    Returns the max value of a given action
    """

    if terminal(board):
        return [utility(board), None]
    infinity = -math.inf
    for action in actions(board):
        pastmax = infinity
        arr = min_value(result(board,action))
        infinity = max(infinity, arr[0])
        if infinity != pastmax :
            actionx = action
        if infinity == 1 :
            return [infinity, actionx]
    return [infinity, actionx]


def min_value(board):
    """
    Returns the max value of a given action
    """
    
    if terminal(board):
        return [utility(board), None]
    infinity = math.inf
    for action in actions(board):
        pastmax = infinity
        arr = max_value(result(board,action))
        infinity = min(infinity, arr[0])
        if infinity != pastmax :
            actionx = action
        if infinity == -1 :
            return [infinity, actionx]
    return [infinity, actionx]