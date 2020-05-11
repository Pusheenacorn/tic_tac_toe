
DRAW = -1
NOT_OVER = 0 
PLAYER_1_WIN = 1
PLAYER_2_WIN = 2

from check_win import check_win
from place import place
from print_board import print_board


def main():
    board = [0, 0, 0,
             0, 0, 0,
             0, 0, 0]
    player = 1
    print("Welcome to Tic Tac Toe!")
    while True:
        print("-------------------------------------")
        print_board(board)
        print("Player {} turn.".format(player))
        index = int(input("Enter the index of where you would like to place a chip: "))
        place(board, player, index)
        winner = check_win(board, index)
        if winner == PLAYER_1_WIN or winner == PLAYER_2_WIN:
            print("Congratulations to player {} for winning!".format(winner))
            break
        elif winner == DRAW:
            print("Uh oh, no one won.")
            break
        player = 1 if player == 2 else 2

if __name__ == "__main__":
    main()
