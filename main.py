import pygame.display
from sys import exit
import screen
import screen
import consts
import game_field
import soldier
from soldier import player

Screen = screen.screen
state = {
    "is_window_open": True,
    "living" : True,
    "win" : False
# "state": consts.RUNNING_STATE
}

def handle_user_events():
    if check_touch_flag(soldier.create_solider_body(), game_field.places_with_flag()):
        state["living"] = False
    if check_touch_mines(soldier.create_solider_legs(), game_field.mines_places()):
        state["win"] = True
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if soldier.player["position_y"] >=  1:
                    soldier.player["position_y"] -= 1

            elif event.key == pygame.K_DOWN:
                if soldier.player["position_y"] < consts.BOARD_ROWS - 1:
                    soldier.player["position_y"] += 1




            elif event.key == pygame.K_LEFT:
                if soldier.player["position_x"] >= 1:
                    soldier.player["position_x"] -= 1


            elif event.key == pygame.K_RIGHT:
                if soldier.player["position_x"] < consts.BOARD_COLS - 1:
                 soldier.player["position_x"] += 1



pygame.display.set_caption('the flag')
# flags = game_field.places_with_flag()
# body = soldier.create_solider_body()
# legs = soldier.create_solider_legs()
# mines = game_field.mines_places()

def check_touch_flag(body, flags):
    for body_place in body:
        if body_place in flags:
            return True
    return False

def check_touch_mines(legs, mines):
    for leg_place in legs:
        if leg_place in mines:
            return True
    return False

# def check_if_location_legal():
#     if soldier.player["position_x"]+1>consts.BOARD_COLS:


def main():

    pygame.init()


    while state["is_window_open"]:
        handle_user_events()
        screen.draw_game(soldier.soldier_location())




if __name__ == '__main__':
    main()




