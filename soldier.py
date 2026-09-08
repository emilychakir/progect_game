import consts

player = {
        "position_x": 0,
        "position_y": 0,
        "health": 3
}

def create_solider_body():
    list_of_solider_body_places = []
    x_solider = player["position_x"]
    y_solider = player["position_y"]
    for x in range(x_solider, x_solider + consts.SOLDIER_BODY_ROWS):
        for y in range(y_solider, y_solider + consts.SOLDIER_COLS):
            tup = (x, y)
            list_of_solider_body_places.append(tup)
    return list_of_solider_body_places

def create_solider_legs():
    list_of_solider_leg_places = []
    x_solider = player["position_x"]
    y_solider = player["position_y"] + consts.SOLDIER_BODY_ROWS
    for x in range(x_solider, x_solider + consts.SOLDIER_FEET_ROWS):
        for y in range(y_solider, y_solider + consts.SOLDIER_COLS):
            tup = (x, y)
            list_of_solider_leg_places.append(tup)
    return list_of_solider_leg_places
def soldier_location():





