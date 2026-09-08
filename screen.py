import  pygame

import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))



def draw_bush(bush_img):

        display_surface = pygame.display.set_mode((consts.bush_ROWS,consts.bush_COLS))
        display_surface.blit(bush_img,(consts.bush_ROWS,consts.bush_COLS))
        pygame.display.flip()


def starting_location(img_solider,img_flag):
        # creating the display surface
        display_surface_flag = pygame.display.set_mode((consts.flag_row,consts.flag_col))
        display_surface_solider = pygame.display.set_mode((consts.flag_row, consts.flag_col))
        # putting our first image surface on
        # display surface
        display_surface_solider.blit(img_solider, (0, 0))

        # putting our second image surface on
        # display surface
        display_surface_flag.blit(img_flag, (300, 300))

        # updating the display
        pygame.display.flip()