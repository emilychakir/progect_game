import  pygame
import random
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_background():
        screen.fill(consts.BACKGROUND_COLOR)

def draw_bush():
    x = random.randint(0 + 30, consts.WINDOW_WIDTH - 30)
    y = random.randint(0 + 20, consts.WINDOW_HEIGHT - 20)
    screen.blit(consts.bush, (x, y))




def flag_location():
        screen.blit(consts.flag, (consts.flag_loc_x,  consts.flag_loc_y))



def draw_game():
    draw_background()
    draw_bush()
    flag_location()
    # starting_location(consts.img_solider, consts.flag_img)

    pygame.display.flip()
