import pygame.display
from sys import exit

from pygame import event

import screen
import screen
import consts
import game_field
import soldier
from soldier import player

Screen = screen.Screen
state = {
    "is_window_open": True,
    "living" : True,
    "win" : False,
    "time_down" : 0.0,
    "time_elapsed" : 0.0,
    "long_or_short":"short"

# "state": consts.RUNNING_STATE
}



def handle_user_events():


    for event in pygame.event.get():


        if check_touch_flag(soldier.create_solider_body(), game_field.places_with_flag()):
            state["win"] = True


        if check_touch_mines(soldier.create_solider_legs(), soldier.player["mines_places"]):
            state["living"] = False

        # time_down = 0
        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif event.type == pygame.KEYDOWN:


            if event.key == pygame.K_UP:
                if soldier.player["position_y"] >=  1:
                    soldier.player["position_y"] -= 1

            elif event.key == pygame.K_DOWN:
                if soldier.player["position_y"] < consts.BOARD_ROWS - consts.SOLDIER_ROWS:
                    soldier.player["position_y"] += 1


            elif event.key == pygame.K_LEFT:
                if soldier.player["position_x"] >= 1:
                    soldier.player["position_x"] -= 1


            elif event.key == pygame.K_RIGHT:
                if soldier.player["position_x"] < consts.BOARD_COLS - consts.SOLDIER_COLS:
                 soldier.player["position_x"] += 1
            #
            elif event.key == pygame.K_RETURN:
                print("sdfdf")
                screen.draw_matrix()
                screen.location_of_night_soldier(soldier.soldier_location())
                pygame.display.flip()
                pygame.time.wait(1000)

            elif event.key == pygame.K_1:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_2:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_3:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_4:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_5:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_6:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_7:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_8:
                state["time_down"] = pygame.time.get_ticks()
            elif event.key == pygame.K_9:
                state["time_down"] = pygame.time.get_ticks()
        elif event.type == pygame.KEYUP:
            if state["time_down"]!= 0:
                state["time_elapsed"] = (pygame.time.get_ticks() - state["time_down"]) / 1000.0
                print("duration: ", state["time_elapsed"])
                state["time_down"] = 0

def check_time():
    if state["time_elapsed"]>1:
        state["long_or_short"] = "long"
    else:
        state["long_or_short"]="short"


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




def main():

    pygame.init()


    while state["is_window_open"]:
        handle_user_events()
        screen.draw_game(soldier.soldier_location(), state)



if __name__ == '__main__':
    main()




