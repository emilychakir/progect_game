import consts

solider_mat = []

def create():
    global solider_grid
    solider_mat = []
    for col in range(consts.SOLDIER_BODY_ROWS,consts.SOLDIER_BODY_ROWS+ consts.SOLDIER_BODY_ROWS):
        for row in range(consts.SOLDIER_COLS):
                # create each cell as instance of Cell,
                # with the concatenated col and row numbers
                # as the name, then add the cell.name to cell_list
                cell = Cell(str(col) + '_' + str(row))
                solider_grid.append(cell.name)