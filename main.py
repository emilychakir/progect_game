import pygame.display
from sys import exit
import screen
from screen import draw_bush
import consts
import game_field
import soldier

state = {
    "is_window_open": True,
    # "state": consts.RUNNING_STATE
}


pygame.display.set_caption('the flag')
flags = game_field.places_with_flag()
body = soldier.create_solider_body()
legs = soldier.create_solider_legs()
mines = game_field.mines_places()

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
    screen.draw_bush(consts.bush_img)
    screen.starting_location(consts.img_solider, consts.flag_img)
    while state["is_window_open"]:
        screen.draw_game()



if __name__ == '__main__':
    main()

def handle_user_events():
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            state["is_window_open"] = False

        elif event.type == pygame.KEYUP:
            soldier.player["position_x"] -= 1

        elif event.type == pygame.KEYDOWN:
            soldier.player["position_x"] += 1

        elif event.type == pygame.K_LEFT:
            soldier.player["position_y"] -= 1

        elif event.type == pygame.K_RIGHT :
            soldier.player["position_y"] += 1


