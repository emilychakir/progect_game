import  pygame
import random
import consts
import soldier
import game_field

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



def draw_lose_message():
    draw_message("you lost", consts.LOSE_FONT_SIZE,
                 consts.LOSE_COLOR, consts.LOSE_LOCATION)


def draw_win_message():
    draw_message("you won", consts.WIN_FONT_SIZE,
                 consts.WIN_COLOR, consts.WIN_LOCATION)

def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_NAME, font_size)
    text_img = font.render(message, True, color)

    def draw_matrix(board1):
        screen.fill((0, 0, 0))
        for r in range(consts.BOARD_ROWS):
            for c in range(consts.BOARD_COLS):
                pygame.draw.rect(screen,
                                 (144, 238, 144),
                                 (c * consts.CELL_SIZE,
                                  r * consts.CELL_SIZE,
                                  consts.CELL_SIZE,
                                  consts.CELL_SIZE),
                                 1)
        for mine in range(len(game_field.mines_places)):
            mine = game_field.mines_places[mine]
            pygame.draw.rect(screen,
                             (136, 8, 8),
                             (mine[0] * consts.CELL_SIZE,
                              mine[1] * consts.CELL_SIZE,
                              consts.CELL_SIZE,
                              consts.CELL_SIZE),
                             )

    screen.blit(text_img, location)
def draw_game(tuple_location):
    draw_background()
    draw_bush(location)
    flag_location()
    location_of_soldier(tuple_location)
    # starting_location(consts.img_solider, consts.flag_img)
    pygame.display.flip()
