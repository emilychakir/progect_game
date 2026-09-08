import  pygame
import random
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_background():
        screen.fill(consts.BACKGROUND_COLOR)

def locations():
    location = []
    for i in range(20):
        x = random.randint(0 + 30, consts.WINDOW_WIDTH - 30)
        y = random.randint(0 + 20, consts.WINDOW_HEIGHT - 20)
        tup = (x, y)
        location.append(tup)
    return location

location = locations()


def draw_bush(locations):
    for i in range(20):
        x = locations[i][0]
        y = locations[i][1]
        screen.blit(consts.bush, (x, y))



def flag_location():
        screen.blit(consts.flag, (consts.flag_loc_x,  consts.flag_loc_y))

def location_of_soldier(location):
    screen.blit(consts.soldier, (location[0], location[1]))

def draw_game():
    draw_background()
    draw_bush(location)
    flag_location()
    # starting_location(consts.img_solider, consts.flag_img)

    pygame.display.flip()
