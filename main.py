import pygame.display
from sys import exit
import screen
from screen import draw_bush
import consts

pygame.display.set_caption('the flag')

def main():
    pygame.init()
    while True:
        screen.draw_bush(consts.bush_img)
        screen.draw_starting_location(consts.img_solider,consts.flag_img)
        for event in pygame.event.get():
            if event.type==pygame.quit():
                pygame.quit()
                exit()
        #draw all our elemnts
        #update everything



if __name__ == '__main__':
    main()

