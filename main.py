import pygame.display
from sys import exit
import  time
from pygame import event
import os
os.environ["SDL_VIDEO_CENTERED"] = "1"

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
    "win" : False,
    "current_screen" : Screen
# "state": consts.RUNNING_STATE
}
clock = pygame.time.Clock()
press_start_time = None


def handle_user_events():
    press_start_time = None

    for event in pygame.event.get():

        if check_touch_flag(soldier.create_solider_body(), game_field.places_with_flag()):
            state["win"] = True


        if check_touch_mines(soldier.create_solider_legs(), game_field.mines_places()):
            state["living"] = False



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
                screen.draw_matrix()
                screen.location_of_night_soldier(soldier.soldier_location())
                pygame.display.flip()
                pygame.time.wait(1000)

            elif event.key == pygame.K_1 :
                press_start_time = time.time()
                if event.type == pygame.KEYUP:
                    duration = time.time() - press_start_time

                    # Determine if it was long or short
                    if duration >= consts.LONG_PRESS_THRESHOLD:
                        print(f"Long Press detected! (Duration: {duration:.2f} seconds)")
                    else:
                        print(f"Short Press detected! (Duration: {duration:.2f} seconds)")




            # elif event.key == pygame.K_2:
            #
            # elif event.key == pygame.K_3:
            #
            # elif event.key == pygame.K_4:
            #
            # elif event.key == pygame.K_5:
            #
            # elif event.key == pygame.K_6:
            #
            # elif event.key == pygame.K_7:
            #
            # elif event.key == pygame.K_8:
            #
            # elif event.key == pygame.K_9:


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




