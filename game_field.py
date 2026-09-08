import consts
board = []
def make_board():
    for x in range(consts.BOARD_ROWS):
        row = []
        for y in range(consts.BOARD_COLS):
            board[x][y] = consts.E

print(make_board())
