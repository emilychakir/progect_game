import pygame.display
from sys import exit
from screen import draw_bush, make_screen
import consts
import soldier

pygame.display.set_caption('the flag')

def main():
    pygame.init()
    screen=make_screen()
    clock=pygame.time.Clock()
    soldier_body=soldier.create_solider_body()
    soldier_legs=soldier.create_solider_legs()
    mines=
    while True:
        screen.draw_bush(consts.bush_img)
        screen.starting_location(consts.img_solider,consts.flag_img)
        for event in pygame.event.get():
            if event.type==pygame.quit():
                pygame.quit()
                exit()
        #draw all our elemnts
        #update everything



if __name__ == '__main__':
    main()

