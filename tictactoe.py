"""
Tic Tac Toe Player
"""

import math

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
    countx = 0
    for row in board:
        for cell in row:
            if cell == X:
                countx += 1
    
    counto = 0
    for row in board:
        for cell in row:
            if cell == O:
                counto += 1
    if countx == counto:
        return X
    elif countx == counto + 1:
        return O
    else:
        raise ValueError("Invalid Board State")
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_actions.add((i,j))
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    deep_board = [list(sublist) for sublist in board]
    if board[action[0]][action[1]] is not EMPTY:
        raise Exception("Invalid Move Error")
    if board[action[0]][action[1]] == EMPTY:
        deep_board[action[0]][action[1]] = player(board)
    return deep_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][0] == board[i][1] == board[i][2]:
                return board[i][0]
            if board[0][j] == board[1][j] == board[2][j]:
                return board[0][j]
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[2][0]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        utilityscore = 1
    elif winner(board) == 'O':
        utilityscore = -1
    else:
        utilityscore = 0
    return utilityscore


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    def maxvalue(board):
        if terminal(board) == True:
            return utility(board)
        v = float('-inf')
        for action in actions(board):
            v = max(v,minvalue(result(board,action)))
        return v

    def minvalue(board):
        if terminal(board) == True:
            return utility(board)
        v = float('inf')
        for action in actions(board):
            v = min(v,maxvalue(result(board,action)))
        return v

    if player(board) == X:
        return max(actions(board), key=lambda action: minvalue(result(board, action)))
    else:
        return min(actions(board), key=lambda action: maxvalue(result(board, action)))
