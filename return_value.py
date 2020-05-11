
DRAW = -1
NOT_OVER = 0 
PLAYER_1_WIN = 1
PLAYER_2_WIN = 2
def return_value(l): 
    if l[0] == l[1] and l[1] == l[2] and l[0] == l[2]:
        if l[0] == 0:
            return NOT_OVER
        if l[0] == 1:
            return PLAYER_1_WIN
        else:
            return PLAYER_2_WIN
    else:
        return NOT_OVER