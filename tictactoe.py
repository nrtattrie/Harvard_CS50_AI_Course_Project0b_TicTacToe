"""
Tic Tac Toe Player
"""
import copy
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
    Xs = 0
    Os = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                Xs += 1
            if board[i][j] == O:
                Os += 1
    if Os < Xs:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions_set = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions_set.add((i, j))
    return actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    temp = copy.deepcopy(board)
    if board[action[0]][action[1]] is EMPTY:
        if player(board) == X:
            temp[action[0]][action[1]] = X
        if player(board) == O:
            temp[action[0]][action[1]] = O
        return temp
    else:
        raise Exception("Invalid Action")


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if player(board) == X:
        last_move = O
    else:
        last_move = X

        # Testing horizontals
    if board[0][0] == last_move and board[0][1] == last_move and board[0][2] == last_move:
        return last_move
    if board[1][0] == last_move and board[1][1] == last_move and board[1][2] == last_move:
        return last_move
    if board[2][0] == last_move and board[2][1] == last_move and board[2][2] == last_move:
        return last_move
        # Testing Verticals
    if board[0][0] == last_move and board[1][0] == last_move and board[2][0] == last_move:
        return last_move
    if board[0][1] == last_move and board[1][1] == last_move and board[2][1] == last_move:
        return last_move
    if board[0][2] == last_move and board[1][2] == last_move and board[2][2] == last_move:
        return last_move
        # Testing Diagonals
    if board[0][0] == last_move and board[1][1] == last_move and board[2][2] == last_move:
        return last_move
    if board[0][2] == last_move and board[1][1] == last_move and board[2][0] == last_move:
        return last_move
        # If none of the above conditions are met, no winner yet
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Test whether X or O is a winner
    if winner(board) != None:
        return True

    # Test whether the board is filled
    if any(None in i for i in board):
        return False
    else:
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Test whether X has won
    if winner(board) == X:
        return 1
    # Test whether O has won
    if winner(board) == O:
        return -1
    # If neither X nor O has won, the game has terminated in a draw
    # Can use terminal function to see if board is full. If the
    # board is full, the terminal function will return true, meaning
    # the utility function should return 0.
    if terminal(board):
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Return none if the board is terminal
    if terminal(board):
        return None

    best_move = (-1, -1)

    # Max Player
    if player(board) == X:
        min_val = -1
        # Iterate through all possible actions on the board
        for action in actions(board):
            v = min_value(result(board, action))
            if v == 1:
                best_move = action
                break
            if min_val < v:
                # best_val = v
                best_move = action
        return best_move

    # Min Player
    if player(board) == O:
        max_val = 1
        for action in actions(board):
            v = max_value(result(board, action))
            if v == -1:
                best_move = action
                break
            if max_val > v:
                # best_val = v
                best_move = action
        return best_move


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        if v == -1:
            break
    return v


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -1
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        if v == 1:
            break
    return v
