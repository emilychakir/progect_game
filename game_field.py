import consts
import random


def make_board():
    board = []
    for x in range(consts.BOARD_ROWS):
        row = []
        for y in range(consts.BOARD_COLS):
            row.append(consts.E)
        board.append(row)
    return board


board = make_board()


def place_current_mine(tuple, board):
    print(tuple)
    tuple_x = tuple[0]
    tuple_y = tuple[1]

    if board[tuple_x][tuple_y] == consts.E and board[tuple_x][tuple_y + 1] == consts.E and board[tuple_x][tuple_y + 2] == consts.E:
        print("asdasdsda")
        for i in range(consts.MINE_COLS):
            board[tuple_x][tuple_y + i] = consts.M
        return board
    return False




def places_with_flag():
    list_of_flag_places = []
    x_flag = consts.flag_row
    y_flag = consts.flag_col
    for x in range(x_flag, x_flag + consts.FLAG_ROWS):
        for y in range(y_flag, y_flag + consts.FLAG_COLS):
            tup = (x, y)
            list_of_flag_places.append(tup)
    return list_of_flag_places


places_of_flag = places_with_flag()



def starting_pos_soldier():
    places_of_soldier = []
    for x in range(consts.SOLDIER_ROWS):
        for y in range(consts.SOLDIER_COLS):
            tup = (x, y)
            places_of_soldier.append(tup)
    return places_of_soldier


soldier_location = starting_pos_soldier()



def place_mines(places_of_flag, places_of_soldier):
    counter = 0
    while counter < 20:
        rand_x = random.randint(0, consts.BOARD_ROWS - 1)
        rand_y = random.randint(0, consts.BOARD_COLS - 3)
        print(rand_x)
        print(rand_y)
        tup = (rand_x, rand_y)
        if tup not in places_of_soldier and tup not in places_of_flag and place_current_mine(tup, board) != False:
            counter += 1
    return board



place_mines(places_of_flag, soldier_location)


def print_board():
    for i in range(len(board)):
        print(board[i])
        print()

print_board()

print(places_of_flag)