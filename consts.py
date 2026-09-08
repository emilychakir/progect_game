import pygame.image

BOARD_ROWS = 25
BOARD_COLS = 50
E = "E"
M = "M"
BACKGROUND_COLOR = (129,199,132)

CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

# flag
FLAG_ROWS = 3
FLAG_COLS = 4
flag_row = BOARD_ROWS - FLAG_ROWS
flag_col = BOARD_COLS - FLAG_COLS
flag_loc_x = WINDOW_WIDTH - FLAG_COLS * CELL_SIZE
flag_loc_y = WINDOW_HEIGHT - FLAG_ROWS * CELL_SIZE

# soldier
# STARTING_POS_X = 0
# STARTING_POS_Y = 0
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

# mines
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

bush_img=pygame.image.load('grass.png')
img_soldier=pygame.image.load('soldier.png')
flag_img=pygame.image.load('flag.png')


#bush
bush_ROWS = 1
bush_COLS = 3
bush_img = pygame.image.load("grass.png")
img_solider = pygame.image.load("soldier.png")
flag_img = pygame.image.load("flag.png")

soldier = pygame.transform.scale(img_solider, (40, 80))
flag = pygame.transform.scale(flag_img, (80, 60))
bush = pygame.transform.scale(bush_img, (60, 40))




