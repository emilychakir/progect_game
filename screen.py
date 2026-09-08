import  pygame
import consts
import random
import game_field
from consts import CELL_SIZE
def make_screen():
        screen = pygame.display.set_mode(
                (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
        return screen

def draw_background(screen):
        screen.fill(consts.BACKGROUND_COLOR)


def draw_bush(bush_img):
        counter = 0
        while counter < 20:
                rand_x = random.randint(0, consts.BOARD_ROWS - 1)
                rand_y = random.randint(0, consts.BOARD_COLS - 3)
                print(rand_x)
                print(rand_y)
                tup = (rand_x, rand_y)
                if tup not in game_field.places_with_flag() and tup not in game_field.starting_pos_soldier() and game_field.place_current_mine(tup,game_field.board) != False:
                        counter += 1
                        display_surface = pygame.display.set_mode((consts.bush_ROWS,consts.bush_COLS))
                        display_surface.blit(bush_img,(consts.bush_ROWS,consts.bush_COLS))
                        pygame.display.flip()


def draw_starting_location(img_solider,img_flag):
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

def draw_matrix(board1, light_green=None):
        for r in range(consts.BOARD_ROWS):
                for c in range(consts.BOARD_COLS):
                        pygame.draw.rect(board1,light_green,(c*CELL_SIZE, r*CELL_SIZE,CELL_SIZE,CELL_SIZE),1)


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)

    pygame.display.flip()