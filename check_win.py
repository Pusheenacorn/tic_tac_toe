import math
from return_value import return_value
from equal import equal

DRAW = -1
NOT_OVER = 0 
PLAYER_1_WIN = 1
PLAYER_2_WIN = 2
def check_win(board, index):
    # return one of the four exit codes listed at the top
    if 0 not in board:
        return DRAW
    col = index % 3
    row = math.floor(index / 3) 
    cols = []
    rows = []
    for i in range(9):
        if i % 3 == col:
            cols.append(board[i])
        if math.floor(i / 3) == row:
            rows.append(board[i])
    if return_value(cols) != NOT_OVER:
        return return_value(cols)
    if return_value(rows) != NOT_OVER:
        return return_value(rows)
    if equal(board[0], board[4], board[8]) and board[0] != 0:
        return board[0]
    if equal(board[2], board[4], board[6]) and board[2] != 0:
        return board[2]
    return NOT_OVER