import consts
board = []
def make_board():
    for x in range(consts.BOARD_ROWS):
        for y in range(consts.BOARD_COLS):
            board[x][y] = consts.E
