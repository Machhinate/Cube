import pygame
import cubeclass
import random
import time

# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [300, 500]
screen = pygame.display.set_mode(size)
pause = 20
step_pause = 0

# Set title of screen
pygame.display.set_caption("cube")

cube_map = [['0', '0', '0', 'w', 'w', 'w', '0', '0', '0'],
            ['0', '0', '0', 'w', 'w', 'w', '0', '0', '0'],
            ['0', '0', '0', 'w', 'w', 'w', '0', '0', '0'],
            ['r', 'r', 'r', 'b', 'b', 'b', 'o', 'o', 'o'],
            ['r', 'r', 'r', 'b', 'b', 'b', 'o', 'o', 'o'],
            ['r', 'r', 'r', 'b', 'b', 'b', 'o', 'o', 'o'],
            ['0', '0', '0', 'y', 'y', 'y', '0', '0', '0'],
            ['0', '0', '0', 'y', 'y', 'y', '0', '0', '0'],
            ['0', '0', '0', 'y', 'y', 'y', '0', '0', '0'],
            ['0', '0', '0', 'g', 'g', 'g', '0', '0', '0'],
            ['0', '0', '0', 'g', 'g', 'g', '0', '0', '0'],
            ['0', '0', '0', 'g', 'g', 'g', '0', '0', '0']]

C1 = cubeclass.Cube(cube_map)


def cube_updater():
    pygame.time.delay(pause)
    C1.display_cube(screen)
    pygame.display.flip()
    pygame.event.pump()
    pass


def solve():
    # variable for each stage of solving
    cross = False
    cross_edges = False
    first_layer = False
    second_layer = False
    top_cross = False
    top_face = False
    corners = False
    top_layer = False
    solved = False

    while not solved:

        while not cross:

            if C1.grid[0][4].status == 'b':
                rotate_white()
                rotate_blue()
                rotate_u_orange()

            if C1.grid[1][3].status == 'b':
                rotate_white()
                rotate_white()
                rotate_blue()
                rotate_orange()

            if C1.grid[1][5].status == 'b':
                rotate_blue()
                rotate_u_orange()

            if C1.grid[2][4].status == 'b':
                rotate_u_white()
                rotate_blue()
                rotate_orange()

            if C1.grid[3][1].status == 'b':
                rotate_u_white()
                rotate_blue()

            if C1.grid[3][7].status == 'b':
                rotate_white()
                rotate_blue()

            if C1.grid[4][0].status == 'b':
                rotate_u_blue()
                rotate_red()
                rotate_blue()
                rotate_u_white()
                rotate_blue()

            if C1.grid[4][2].status == 'b':
                rotate_u_blue()
                rotate_u_red()
                rotate_blue()
                rotate_u_white()
                rotate_blue()

            if C1.grid[4][6].status == 'b':
                rotate_orange()
                rotate_white()
                rotate_blue()

            if C1.grid[4][8].status == 'b':
                rotate_blue()
                rotate_orange()
                rotate_blue()
                rotate_u_yellow()
                rotate_u_blue()

            if C1.grid[5][1].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_yellow()
                rotate_u_blue()

            if C1.grid[5][7].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_u_yellow()
                rotate_u_blue()

            if C1.grid[6][4].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_u_yellow()
                rotate_blue()
                rotate_u_red()
                rotate_blue()
                rotate_blue()

            if C1.grid[7][3].status == 'b':
                rotate_u_blue()
                rotate_u_red()
                rotate_blue()
                rotate_blue()

            if C1.grid[7][5].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_yellow()
                rotate_yellow()
                rotate_blue()
                rotate_u_red()
                rotate_blue()
                rotate_blue()

            if C1.grid[8][4].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_yellow()
                rotate_blue()
                rotate_u_red()
                rotate_blue()
                rotate_blue()

            if C1.grid[9][4].status == 'b':
                rotate_green()
                rotate_green()
                rotate_white()
                rotate_white()
                rotate_blue()

            if C1.grid[10][3].status == 'b':
                rotate_ugreen()
                rotate_white()
                rotate_white()
                rotate_blue()

            if C1.grid[10][5].status == 'b':
                rotate_green()
                rotate_white()
                rotate_white()
                rotate_blue()

            if C1.grid[11][4].status == 'b':
                rotate_white()
                rotate_white()
                rotate_blue()

            if (C1.grid[3][4].status == 'b' and C1.grid[4][3].status == 'b' and
                    C1.grid[4][5].status == 'b' and C1.grid[5][4].status == 'b'):
                print('cross')
                cross = True

        while cross and not cross_edges:
            if not C1.grid[2][4].status == 'w':
                if C1.grid[2][4].status == 'r':
                    rotate_white()
                    rotate_white()
                    rotate_green()
                    rotate_red()
                    rotate_red()
                    rotate_ugreen()
                    rotate_white()
                    rotate_white()
                elif C1.grid[2][4].status == 'o':
                    rotate_white()
                    rotate_white()
                    rotate_ugreen()
                    rotate_orange()
                    rotate_orange()
                    rotate_green()
                    rotate_white()
                    rotate_white()
                else:
                    rotate_white()
                    rotate_white()
                    rotate_green()
                    rotate_green()
                    rotate_yellow()
                    rotate_yellow()
                    rotate_green()
                    rotate_green()
                    rotate_white()
                    rotate_white()

            if not C1.grid[4][2].status == 'r':
                if C1.grid[4][2].status == 'w':
                    rotate_red()
                    rotate_red()
                    rotate_ugreen()
                    rotate_white()
                    rotate_white()
                    rotate_green()
                    rotate_red()
                    rotate_red()
                elif C1.grid[4][2].status == 'o':
                    rotate_red()
                    rotate_red()
                    rotate_green()
                    rotate_green()
                    rotate_orange()
                    rotate_orange()
                    rotate_green()
                    rotate_green()
                    rotate_red()
                    rotate_red()
                else:
                    rotate_red()
                    rotate_red()
                    rotate_green()
                    rotate_yellow()
                    rotate_yellow()
                    rotate_ugreen()
                    rotate_red()
                    rotate_red()

            if not C1.grid[6][4].status == 'y':
                if C1.grid[6][4].status == 'w':
                    rotate_yellow()
                    rotate_yellow()
                    rotate_green()
                    rotate_green()
                    rotate_white()
                    rotate_white()
                    rotate_green()
                    rotate_green()
                    rotate_yellow()
                    rotate_yellow()
                elif C1.grid[6][4].status == 'o':
                    rotate_yellow()
                    rotate_yellow()
                    rotate_green()
                    rotate_orange()
                    rotate_orange()
                    rotate_ugreen()
                    rotate_yellow()
                    rotate_yellow()
                else:
                    rotate_yellow()
                    rotate_yellow()
                    rotate_ugreen()
                    rotate_red()
                    rotate_red()
                    rotate_green()
                    rotate_yellow()
                    rotate_yellow()

            if not C1.grid[4][6].status == 'o':
                if C1.grid[4][6].status == 'w':
                    rotate_orange()
                    rotate_orange()
                    rotate_green()
                    rotate_white()
                    rotate_white()
                    rotate_ugreen()
                    rotate_orange()
                    rotate_orange()
                elif C1.grid[4][6].status == 'y':
                    rotate_orange()
                    rotate_orange()
                    rotate_ugreen()
                    rotate_yellow()
                    rotate_yellow()
                    rotate_green()
                    rotate_orange()
                    rotate_orange()
                else:
                    rotate_orange()
                    rotate_orange()
                    rotate_green()
                    rotate_green()
                    rotate_red()
                    rotate_red()
                    rotate_green()
                    rotate_green()
                    rotate_orange()
                    rotate_orange()

            if (C1.grid[4][6].status == 'o' and C1.grid[6][4].status == 'y' and
                    C1.grid[4][2].status == 'r' and C1.grid[2][4].status == 'w'):

                cross_edges = True
                print("cross edges")

        pygame.time.delay(step_pause)

        while cross_edges and not first_layer:

            if C1.grid[0][3].status == 'b':
                if C1.grid[3][0].status == 'r':
                    rotate_white()
                    rotate_green()
                    rotate_u_white()

                elif C1.grid[3][0].status == 'y':
                    rotate_green()
                    rotate_red()
                    rotate_green()
                    rotate_u_red()

                elif C1.grid[3][0].status == 'o':
                    rotate_green()
                    rotate_green()
                    rotate_yellow()
                    rotate_green()
                    rotate_u_yellow()

                elif C1.grid[3][0].status == 'w':
                    rotate_ugreen()
                    rotate_orange()
                    rotate_green()
                    rotate_u_orange()

            if C1.grid[3][0].status == 'b':
                if C1.grid[11][3].status == 'r':
                    rotate_u_red()
                    rotate_ugreen()
                    rotate_red()

                elif C1.grid[11][3].status == 'y':
                    rotate_green()
                    rotate_u_yellow()
                    rotate_ugreen()
                    rotate_yellow()

                elif C1.grid[11][3].status == 'o':
                    rotate_green()
                    rotate_green()
                    rotate_u_orange()
                    rotate_ugreen()
                    rotate_orange()

                elif C1.grid[11][3].status == 'w':
                    rotate_ugreen()
                    rotate_u_white()
                    rotate_ugreen()
                    rotate_white()

            if C1.grid[11][3].status == 'b':
                if C1.grid[0][3].status == 'r':
                    rotate_white()
                    rotate_green()
                    rotate_green()
                    rotate_u_white()
                    rotate_ugreen()
                    rotate_white()
                    rotate_green()
                    rotate_u_white()

                if C1.grid[0][3].status == 'y':
                    rotate_green()
                    rotate_red()
                    rotate_green()
                    rotate_green()
                    rotate_u_red()
                    rotate_ugreen()
                    rotate_red()
                    rotate_green()
                    rotate_u_red()

                if C1.grid[0][3].status == 'o':
                    rotate_green()
                    rotate_green()
                    rotate_yellow()
                    rotate_green()
                    rotate_green()
                    rotate_u_yellow()
                    rotate_ugreen()
                    rotate_yellow()
                    rotate_green()
                    rotate_u_yellow()

                if C1.grid[0][3].status == 'w':
                    rotate_ugreen()
                    rotate_orange()
                    rotate_green()
                    rotate_green()
                    rotate_u_orange()
                    rotate_ugreen()
                    rotate_orange()
                    rotate_green()
                    rotate_u_orange()

            if (C1.grid[0][5].status == 'b' or C1.grid[11][5].status == 'b' or
                    C1.grid[3][8].status == 'b'):
                rotate_green()
                continue

            if (C1.grid[5][8].status == 'b' or C1.grid[8][5].status == 'b' or
                    C1.grid[9][5].status == 'b'):
                rotate_green()
                rotate_green()
                continue

            if (C1.grid[5][0].status == 'b' or C1.grid[8][3].status == 'b' or
                    C1.grid[9][3].status == 'b'):
                rotate_ugreen()
                continue

            if ((C1.grid[3][3].status == 'b' and C1.grid[3][2].status != 'r') or
                    C1.grid[2][3].status == 'b' or C1.grid[3][2].status == 'b'):
                rotate_white()
                rotate_green()
                rotate_u_white()
                continue

            if ((C1.grid[3][5].status == 'b' and C1.grid[2][5].status != 'w') or
                    C1.grid[2][5].status == 'b' or C1.grid[3][6].status == 'b'):
                rotate_orange()
                rotate_green()
                rotate_u_orange()
                continue

            if ((C1.grid[5][3].status == 'b' and C1.grid[6][3].status != 'y') or
                    C1.grid[6][3].status == 'b' or C1.grid[5][2].status == 'b'):
                rotate_red()
                rotate_green()
                rotate_u_red()
                continue

            if ((C1.grid[5][5].status == 'b' and C1.grid[5][6].status != 'o') or
                    C1.grid[5][6].status == 'b' or C1.grid[6][5].status == 'b'):
                rotate_yellow()
                rotate_green()
                rotate_u_yellow()
                continue

            if (C1.grid[3][3].status == 'b' and C1.grid[3][5].status == 'b' and
                    C1.grid[5][3].status == 'b' and C1.grid[5][5].status == 'b'):
                print("first layer")
                first_layer = True

        pygame.time.delay(step_pause)

        while first_layer and not second_layer:
            if C1.grid[11][4].status != 'g' and C1.grid[0][4].status != 'g':
                if C1.grid[11][4].status == 'r':
                    if C1.grid[0][4].status == 'y':
                        rotate_ugreen()
                        rotate_red()
                        rotate_ugreen()
                        rotate_u_red()
                        rotate_green()
                        rotate_green()
                        rotate_u_yellow()
                        rotate_green()
                        rotate_green()
                        rotate_yellow()

                        print('red yellow')

                    if C1.grid[0][4].status == 'w':
                        rotate_ugreen()
                        rotate_u_red()
                        rotate_green()
                        rotate_red()
                        rotate_green()
                        rotate_white()
                        rotate_ugreen()
                        rotate_u_white()
                        print('red white')

                if C1.grid[11][4].status == 'y':
                    if C1.grid[0][4].status == 'r':
                        rotate_u_yellow()
                        rotate_green()
                        rotate_yellow()
                        rotate_green()
                        rotate_red()
                        rotate_ugreen()
                        rotate_u_red()
                        print('yellow red')

                    if C1.grid[0][4].status == 'o':
                        rotate_yellow()
                        rotate_ugreen()
                        rotate_u_yellow()
                        rotate_green()
                        rotate_green()
                        rotate_u_orange()
                        rotate_green()
                        rotate_green()
                        rotate_orange()

                        print('yellow orange')

                if C1.grid[11][4].status == 'o':
                    if C1.grid[0][4].status == 'w':
                        rotate_green()
                        rotate_orange()
                        rotate_ugreen()
                        rotate_u_orange()
                        rotate_green()
                        rotate_green()
                        rotate_u_white()
                        rotate_green()
                        rotate_green()
                        rotate_white()
                        print('orange white')

                    if C1.grid[0][4].status == 'y':
                        rotate_green()
                        rotate_u_orange()
                        rotate_green()
                        rotate_orange()
                        rotate_green()
                        rotate_green()
                        rotate_yellow()
                        rotate_green()
                        rotate_green()
                        rotate_u_yellow()
                        print('orange yellow')

                if C1.grid[11][4].status == 'w':
                    if C1.grid[0][4].status == 'o':
                        rotate_green()
                        rotate_green()
                        rotate_u_white()
                        rotate_green()
                        rotate_white()
                        rotate_green()
                        rotate_green()
                        rotate_orange()
                        rotate_green()
                        rotate_green()
                        rotate_u_orange()
                        print('white orange')

                    if C1.grid[0][4].status == 'r':
                        rotate_green()
                        rotate_green()
                        rotate_white()
                        rotate_ugreen()
                        rotate_u_white()
                        rotate_green()
                        rotate_green()
                        rotate_u_red()
                        rotate_green()
                        rotate_green()
                        rotate_red()
                        print('white red')

            if C1.grid[10][5].status != 'g' and C1.grid[4][8].status != 'g':
                rotate_green()
                continue

            if C1.grid[9][4].status != 'g' and C1.grid[8][4].status != 'g':
                rotate_green()
                rotate_green()
                continue

            if C1.grid[10][3].status != 'g' and C1.grid[4][0].status != 'g':
                rotate_ugreen()
                continue

            if C1.grid[3][1].status != 'r' or C1.grid[1][3].status != 'w':
                rotate_white()
                rotate_ugreen()
                rotate_u_white()
                rotate_red()
                rotate_u_white()
                rotate_u_red()
                rotate_white()
                print('3,1;1,3')
                continue
            if C1.grid[5][7].status != 'o' or C1.grid[7][5].status != 'y':
                rotate_yellow()
                rotate_ugreen()
                rotate_u_yellow()
                rotate_orange()
                rotate_u_yellow()
                rotate_u_orange()
                rotate_yellow()
                print('5,7;7,5')
                continue
            if C1.grid[7][3].status != 'y' or C1.grid[5][1].status != 'r':
                rotate_red()
                rotate_ugreen()
                rotate_u_red()
                rotate_yellow()
                rotate_u_red()
                rotate_u_yellow()
                rotate_red()
                print('7,3;5,1')
                continue
            if C1.grid[3][7].status != 'o' or C1.grid[1][5].status != 'w':
                rotate_orange()
                rotate_ugreen()
                rotate_u_orange()
                rotate_white()
                rotate_u_orange()
                rotate_u_white()
                rotate_orange()
                print('3,7;1,5')
                continue

            second_layer = True
            print('second layer')

        pygame.time.delay(step_pause)

        while second_layer and not top_cross:

            if (C1.grid[10][3].status == 'g' and C1.grid[11][4].status == 'g' and
                    C1.grid[10][5].status == 'g' and C1.grid[9][4].status == 'g'):
                top_cross = True
                print("top_cross")
                continue

            elif (C1.grid[10][3].status == 'g' and C1.grid[11][4].status != 'g' and
                  C1.grid[10][5].status != 'g' and C1.grid[9][4].status == 'g'):
                rotate_white()
                rotate_green()
                rotate_orange()
                rotate_ugreen()
                rotate_u_orange()
                rotate_u_white()
                continue

            elif (C1.grid[10][3].status == 'g' and C1.grid[11][4].status != 'g' and
                  C1.grid[10][5].status == 'g' and C1.grid[9][4].status != 'g'):
                rotate_white()
                rotate_orange()
                rotate_green()
                rotate_u_orange()
                rotate_ugreen()
                rotate_u_white()
                continue

            elif (C1.grid[10][3].status != 'g' and C1.grid[11][4].status == 'g' and
                  C1.grid[10][5].status != 'g' and C1.grid[9][4].status == 'g'):
                rotate_orange()
                rotate_yellow()
                rotate_green()
                rotate_u_yellow()
                rotate_ugreen()
                rotate_u_orange()
                continue

            elif (C1.grid[10][3].status == 'g' and C1.grid[11][4].status == 'g' and
                  C1.grid[10][5].status != 'g' and C1.grid[9][4].status != 'g'):
                rotate_orange()
                rotate_green()
                rotate_yellow()
                rotate_ugreen()
                rotate_u_yellow()
                rotate_u_orange()
                continue

            elif (C1.grid[10][3].status != 'g' and C1.grid[11][4].status == 'g' and
                  C1.grid[10][5].status == 'g' and C1.grid[9][4].status != 'g'):
                rotate_yellow()
                rotate_green()
                rotate_red()
                rotate_ugreen()
                rotate_u_red()
                rotate_u_yellow()
                continue

            elif (C1.grid[10][3].status != 'g' and C1.grid[11][4].status != 'g' and
                  C1.grid[10][5].status == 'g' and C1.grid[9][4].status == 'g'):
                rotate_red()
                rotate_green()
                rotate_white()
                rotate_ugreen()
                rotate_u_white()
                rotate_u_red()
                continue

            else:
                rotate_red()
                rotate_green()
                rotate_white()
                rotate_ugreen()
                rotate_u_white()
                rotate_u_red()

        pygame.time.delay(step_pause)

        while top_cross and not top_face:

            if (C1.grid[9][3].status == 'g' and C1.grid[9][5].status == 'g' and
                    C1.grid[11][3].status == 'g' and C1.grid[11][5].status == 'g'):
                top_face = True
                print('top face')
                continue

            elif (C1.grid[9][3].status == 'g' and C1.grid[9][5].status != 'g' and
                  C1.grid[11][3].status != 'g' and C1.grid[11][5].status != 'g'):
                rotate_green()
                continue

            elif (C1.grid[9][3].status != 'g' and C1.grid[9][5].status != 'g' and
                  C1.grid[11][3].status == 'g' and C1.grid[11][5].status != 'g'):
                rotate_green()
                rotate_green()
                continue

            elif (C1.grid[9][3].status != 'g' and C1.grid[9][5].status != 'g' and
                  C1.grid[11][3].status != 'g' and C1.grid[11][5].status == 'g'):
                rotate_ugreen()
                continue

            elif (C1.grid[9][3].status != 'g' and C1.grid[9][5].status == 'g' and
                  C1.grid[11][3].status != 'g' and C1.grid[11][5].status != 'g' and
                  C1.grid[3][8].status == 'g'):
                rotate_u_white()
                rotate_ugreen()
                rotate_white()
                rotate_ugreen()
                rotate_u_white()
                rotate_green()
                rotate_green()
                rotate_white()

            elif (C1.grid[9][3].status != 'g' and C1.grid[9][5].status != 'g' and
                  C1.grid[11][3].status != 'g' and C1.grid[11][5].status != 'g' and
                  (C1.grid[8][5].status == 'g' and C1.grid[8][3].status != 'g')):
                rotate_green()
                rotate_green()

            else:
                rotate_red()
                rotate_green()
                rotate_u_red()
                rotate_green()
                rotate_red()
                rotate_green()
                rotate_green()
                rotate_u_red()

        pygame.time.delay(step_pause)

        while top_face and not corners:

            if (C1.grid[0][3].status == C1.grid[0][5].status and
                    C1.grid[8][3].status == C1.grid[8][5].status):
                print('corners')
                corners = True
                continue

            if (C1.grid[0][3].status == C1.grid[0][5].status and
                    C1.grid[8][3].status != C1.grid[8][5].status):
                print('corner swap')
                rotate_u_red()
                rotate_yellow()
                rotate_u_red()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_u_yellow()
                rotate_u_red()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_red()

            elif (C1.grid[3][8].status == C1.grid[5][8].status or
                  C1.grid[8][3].status == C1.grid[8][5].status or
                  C1.grid[5][0].status == C1.grid[3][0].status):
                rotate_green()

            else:
                print('else corner swap')
                rotate_u_red()
                rotate_yellow()
                rotate_u_red()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_u_yellow()
                rotate_u_red()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_red()

        pygame.time.delay(step_pause)

        while corners and not top_layer:

            if (C1.grid[3][8].status == C1.grid[4][8].status and
                    C1.grid[8][3].status == C1.grid[8][4].status and
                    C1.grid[5][0].status == C1.grid[4][0].status and
                    C1.grid[0][3].status == C1.grid[0][4].status):
                top_layer = True
                print('top layer')
                continue

            if (C1.grid[3][8].status == C1.grid[4][8].status or
                    C1.grid[8][3].status == C1.grid[8][4].status or
                    C1.grid[5][0].status == C1.grid[4][0].status):
                rotate_green()
                continue

            else:
                rotate_yellow()
                rotate_yellow()
                rotate_green()
                rotate_u_red()
                rotate_orange()
                rotate_yellow()
                rotate_yellow()
                rotate_red()
                rotate_u_orange()
                rotate_green()
                rotate_yellow()
                rotate_yellow()

        pygame.time.delay(step_pause)

        while top_layer and not solved:
            if C1.grid[0][4].status == C1.grid[1][4].status:
                print('solved')
                solved = True
                continue

            else:
                rotate_green()
                print('rotate')


def scramble():
    for i in range(20):
        move = random.randint(0, 11)

        if move == 0:
            rotate_green()
        elif move == 1:
            rotate_yellow()
        elif move == 2:
            rotate_blue()
        elif move == 3:
            rotate_red()
        elif move == 4:
            rotate_orange()
        elif move == 5:
            rotate_white()
        elif move == 6:
            rotate_ugreen()
        elif move == 7:
            rotate_u_yellow()
        elif move == 8:
            rotate_u_blue()
        elif move == 9:
            rotate_u_red()
        elif move == 10:
            rotate_u_orange()
        else:
            rotate_u_white()


def rotate_white(): #white
    # face corners

    hold = C1.grid[0][3].status
    C1.grid[0][3].status = C1.grid[2][3].status
    C1.grid[2][3].status = C1.grid[2][5].status
    C1.grid[2][5].status = C1.grid[0][5].status
    C1.grid[0][5].status = hold
    # face edges
    hold = C1.grid[0][4].status
    C1.grid[0][4].status = C1.grid[1][3].status
    C1.grid[1][3].status = C1.grid[2][4].status
    C1.grid[2][4].status = C1.grid[1][5].status
    C1.grid[1][5].status = hold
    # inside corners d
    hold = C1.grid[11][3].status
    C1.grid[11][3].status = C1.grid[3][2].status
    C1.grid[3][2].status = C1.grid[3][5].status
    C1.grid[3][5].status = C1.grid[3][8].status
    C1.grid[3][8].status = hold
    # outside corners d
    hold = C1.grid[11][5].status
    C1.grid[11][5].status = C1.grid[3][0].status
    C1.grid[3][0].status = C1.grid[3][3].status
    C1.grid[3][3].status = C1.grid[3][6].status
    C1.grid[3][6].status = hold
    # outside edges d
    hold = C1.grid[11][4].status
    C1.grid[11][4].status = C1.grid[3][1].status
    C1.grid[3][1].status = C1.grid[3][4].status
    C1.grid[3][4].status = C1.grid[3][7].status
    C1.grid[3][7].status = hold

    cube_updater()
    pass


def rotate_u_white(): #uwhite
    status = [C1.grid[0][3].status, C1.grid[0][4].status, C1.grid[0][5].status,
              C1.grid[1][5].status, C1.grid[2][5].status, C1.grid[2][4].status,
              C1.grid[2][3].status, C1.grid[1][3].status]
    status = status[2:] + status[0:2]

    C1.grid[0][3].status, C1.grid[0][4].status, C1.grid[0][5].status, \
        C1.grid[1][5].status, C1.grid[2][5].status, C1.grid[2][4].status, \
        C1.grid[2][3].status, C1.grid[1][3].status = status

    status = [C1.grid[11][5].status, C1.grid[11][4].status, C1.grid[11][3].status,
              C1.grid[3][6].status, C1.grid[3][7].status, C1.grid[3][8].status,
              C1.grid[3][3].status, C1.grid[3][4].status, C1.grid[3][5].status,
              C1.grid[3][0].status, C1.grid[3][1].status, C1.grid[3][2].status]
    status = status[3:] + status[0:3]

    C1.grid[11][5].status, C1.grid[11][4].status, C1.grid[11][3].status, \
        C1.grid[3][6].status, C1.grid[3][7].status, C1.grid[3][8].status, \
        C1.grid[3][3].status, C1.grid[3][4].status, C1.grid[3][5].status, \
        C1.grid[3][0].status, C1.grid[3][1].status, C1.grid[3][2].status = status

    cube_updater()
    pass


def rotate_yellow():  # yellow
    #face corners d
    hold = C1.grid[6][3].status
    C1.grid[6][3].status = C1.grid[8][3].status
    C1.grid[8][3].status = C1.grid[8][5].status
    C1.grid[8][5].status = C1.grid[6][5].status
    C1.grid[6][5].status = hold
    #face edges d
    hold = C1.grid[6][4].status
    C1.grid[6][4].status = C1.grid[7][3].status
    C1.grid[7][3].status = C1.grid[8][4].status
    C1.grid[8][4].status = C1.grid[7][5].status
    C1.grid[7][5].status = hold
    # inside corners d
    hold = C1.grid[9][5].status
    C1.grid[9][5].status = C1.grid[5][6].status
    C1.grid[5][6].status = C1.grid[5][3].status
    C1.grid[5][3].status = C1.grid[5][0].status
    C1.grid[5][0].status = hold
    # outside corners d
    hold = C1.grid[9][3].status
    C1.grid[9][3].status = C1.grid[5][8].status
    C1.grid[5][8].status = C1.grid[5][5].status
    C1.grid[5][5].status = C1.grid[5][2].status
    C1.grid[5][2].status = hold
    # outside edges d
    hold = C1.grid[9][4].status
    C1.grid[9][4].status = C1.grid[5][7].status
    C1.grid[5][7].status = C1.grid[5][4].status
    C1.grid[5][4].status = C1.grid[5][1].status
    C1.grid[5][1].status = hold

    cube_updater()
    pass


def rotate_u_yellow():  # yellow
    status = [C1.grid[6][3].status, C1.grid[6][4].status, C1.grid[6][5].status,
              C1.grid[7][5].status, C1.grid[8][5].status, C1.grid[8][4].status,
              C1.grid[8][3].status, C1.grid[7][3].status]
    status = status[2:] + status[0:2]

    C1.grid[6][3].status, C1.grid[6][4].status, C1.grid[6][5].status, \
        C1.grid[7][5].status, C1.grid[8][5].status, C1.grid[8][4].status, \
        C1.grid[8][3].status, C1.grid[7][3].status = status

    status = [C1.grid[5][5].status, C1.grid[5][4].status, C1.grid[5][3].status,
              C1.grid[5][8].status, C1.grid[5][7].status, C1.grid[5][6].status,
              C1.grid[9][3].status, C1.grid[9][4].status, C1.grid[9][5].status,
              C1.grid[5][2].status, C1.grid[5][1].status, C1.grid[5][0].status]

    status = status[3:] + status[0:3]

    C1.grid[5][5].status, C1.grid[5][4].status, C1.grid[5][3].status, \
        C1.grid[5][8].status, C1.grid[5][7].status, C1.grid[5][6].status, \
        C1.grid[9][3].status, C1.grid[9][4].status, C1.grid[9][5].status, \
        C1.grid[5][2].status, C1.grid[5][1].status, C1.grid[5][0].status = status

    cube_updater()
    pass


def rotate_red():  # red
    #face corners d
    hold = C1.grid[3][0].status
    C1.grid[3][0].status = C1.grid[5][0].status
    C1.grid[5][0].status = C1.grid[5][2].status
    C1.grid[5][2].status = C1.grid[3][2].status
    C1.grid[3][2].status = hold
    #face edges
    hold = C1.grid[3][1].status
    C1.grid[3][1].status = C1.grid[4][0].status
    C1.grid[4][0].status = C1.grid[5][1].status
    C1.grid[5][1].status = C1.grid[4][2].status
    C1.grid[4][2].status = hold
    # inside corners
    hold = C1.grid[2][3].status
    C1.grid[2][3].status = C1.grid[11][3].status
    C1.grid[11][3].status = C1.grid[8][3].status
    C1.grid[8][3].status = C1.grid[5][3].status
    C1.grid[5][3].status = hold
    # outside corners
    hold = C1.grid[0][3].status
    C1.grid[0][3].status = C1.grid[9][3].status
    C1.grid[9][3].status = C1.grid[6][3].status
    C1.grid[6][3].status = C1.grid[3][3].status
    C1.grid[3][3].status = hold
    # outside edges
    hold = C1.grid[1][3].status
    C1.grid[1][3].status = C1.grid[10][3].status
    C1.grid[10][3].status = C1.grid[7][3].status
    C1.grid[7][3].status = C1.grid[4][3].status
    C1.grid[4][3].status = hold

    cube_updater()
    pass


def rotate_u_red():
    status = [C1.grid[3][0].status, C1.grid[3][1].status, C1.grid[3][2].status,
              C1.grid[4][2].status, C1.grid[5][2].status, C1.grid[5][1].status,
              C1.grid[5][0].status, C1.grid[4][0].status]
    status = status[2:] + status[0:2]

    C1.grid[3][0].status, C1.grid[3][1].status, C1.grid[3][2].status, \
        C1.grid[4][2].status, C1.grid[5][2].status, C1.grid[5][1].status, \
        C1.grid[5][0].status, C1.grid[4][0].status = status

    status = [C1.grid[2][3].status, C1.grid[1][3].status, C1.grid[0][3].status,
              C1.grid[5][3].status, C1.grid[4][3].status, C1.grid[3][3].status,
              C1.grid[8][3].status, C1.grid[7][3].status, C1.grid[6][3].status,
              C1.grid[11][3].status, C1.grid[10][3].status, C1.grid[9][3].status]

    status = status[3:] + status[0:3]

    C1.grid[2][3].status, C1.grid[1][3].status, C1.grid[0][3].status, \
        C1.grid[5][3].status, C1.grid[4][3].status, C1.grid[3][3].status, \
        C1.grid[8][3].status, C1.grid[7][3].status, C1.grid[6][3].status, \
        C1.grid[11][3].status, C1.grid[10][3].status, C1.grid[9][3].status = status

    cube_updater()
    pass


def rotate_orange():  # orange
    # face corners d
    hold = C1.grid[3][6].status
    C1.grid[3][6].status = C1.grid[5][6].status
    C1.grid[5][6].status = C1.grid[5][8].status
    C1.grid[5][8].status = C1.grid[3][8].status
    C1.grid[3][8].status = hold
    # face edges
    hold = C1.grid[3][7].status
    C1.grid[3][7].status = C1.grid[4][6].status
    C1.grid[4][6].status = C1.grid[5][7].status
    C1.grid[5][7].status = C1.grid[4][8].status
    C1.grid[4][8].status = hold
    # inside corners
    hold = C1.grid[2][5].status
    C1.grid[2][5].status = C1.grid[5][5].status
    C1.grid[5][5].status = C1.grid[8][5].status
    C1.grid[8][5].status = C1.grid[11][5].status
    C1.grid[11][5].status = hold
    # outside corners
    hold = C1.grid[0][5].status
    C1.grid[0][5].status = C1.grid[3][5].status
    C1.grid[3][5].status = C1.grid[6][5].status
    C1.grid[6][5].status = C1.grid[9][5].status
    C1.grid[9][5].status = hold
    # outside edges
    hold = C1.grid[1][5].status
    C1.grid[1][5].status = C1.grid[4][5].status
    C1.grid[4][5].status = C1.grid[7][5].status
    C1.grid[7][5].status = C1.grid[10][5].status
    C1.grid[10][5].status = hold

    cube_updater()
    pass


def rotate_u_orange():
    status = [C1.grid[3][6].status, C1.grid[3][7].status, C1.grid[3][8].status,
              C1.grid[4][8].status, C1.grid[5][8].status, C1.grid[5][7].status,
              C1.grid[5][6].status, C1.grid[4][6].status]
    status = status[2:] + status[0:2]

    C1.grid[3][6].status, C1.grid[3][7].status, C1.grid[3][8].status, \
        C1.grid[4][8].status, C1.grid[5][8].status, C1.grid[5][7].status, \
        C1.grid[5][6].status, C1.grid[4][6].status = status

    status = [C1.grid[0][5].status, C1.grid[1][5].status, C1.grid[2][5].status,
              C1.grid[9][5].status, C1.grid[10][5].status, C1.grid[11][5].status,
              C1.grid[6][5].status, C1.grid[7][5].status, C1.grid[8][5].status,
              C1.grid[3][5].status, C1.grid[4][5].status, C1.grid[5][5].status]

    status = status[3:] + status[0:3]

    C1.grid[0][5].status, C1.grid[1][5].status, C1.grid[2][5].status, \
        C1.grid[9][5].status, C1.grid[10][5].status, C1.grid[11][5].status, \
        C1.grid[6][5].status, C1.grid[7][5].status, C1.grid[8][5].status, \
        C1.grid[3][5].status, C1.grid[4][5].status, C1.grid[5][5].status = status

    cube_updater()
    pass


def rotate_blue():  # blue
    # face corners d
    hold = C1.grid[3][3].status
    C1.grid[3][3].status = C1.grid[5][3].status
    C1.grid[5][3].status = C1.grid[5][5].status
    C1.grid[5][5].status = C1.grid[3][5].status
    C1.grid[3][5].status = hold
    # face edges
    hold = C1.grid[3][4].status
    C1.grid[3][4].status = C1.grid[4][3].status
    C1.grid[4][3].status = C1.grid[5][4].status
    C1.grid[5][4].status = C1.grid[4][5].status
    C1.grid[4][5].status = hold
    # inside corners
    hold = C1.grid[2][3].status
    C1.grid[2][3].status = C1.grid[5][2].status
    C1.grid[5][2].status = C1.grid[6][5].status
    C1.grid[6][5].status = C1.grid[3][6].status
    C1.grid[3][6].status = hold
    # outside corners
    hold = C1.grid[3][2].status
    C1.grid[3][2].status = C1.grid[6][3].status
    C1.grid[6][3].status = C1.grid[5][6].status
    C1.grid[5][6].status = C1.grid[2][5].status
    C1.grid[2][5].status = hold
    # outside edges
    hold = C1.grid[2][4].status
    C1.grid[2][4].status = C1.grid[4][2].status
    C1.grid[4][2].status = C1.grid[6][4].status
    C1.grid[6][4].status = C1.grid[4][6].status
    C1.grid[4][6].status = hold

    cube_updater()
    pass


def rotate_u_blue():
    status = [C1.grid[3][3].status, C1.grid[3][4].status, C1.grid[3][5].status,
              C1.grid[4][5].status, C1.grid[5][5].status, C1.grid[5][4].status,
              C1.grid[5][3].status, C1.grid[4][3].status]
    status = status[2:] + status[0:2]

    C1.grid[3][3].status, C1.grid[3][4].status, C1.grid[3][5].status, C1.grid[4][5].status, \
    C1.grid[5][5].status, C1.grid[5][4].status, C1.grid[5][3].status, C1.grid[4][3].status \
        = status

    status = [C1.grid[2][5].status, C1.grid[2][4].status, C1.grid[2][3].status,
              C1.grid[5][6].status, C1.grid[4][6].status, C1.grid[3][6].status,
              C1.grid[6][3].status, C1.grid[6][4].status, C1.grid[6][5].status,
              C1.grid[3][2].status, C1.grid[4][2].status, C1.grid[5][2].status]

    status = status[3:] + status[0:3]

    C1.grid[2][5].status, C1.grid[2][4].status, C1.grid[2][3].status, \
        C1.grid[5][6].status, C1.grid[4][6].status, C1.grid[3][6].status, \
        C1.grid[6][3].status, C1.grid[6][4].status, C1.grid[6][5].status, \
        C1.grid[3][2].status, C1.grid[4][2].status, C1.grid[5][2].status = status

    cube_updater()
    pass


def rotate_green():  # green
    # face corners d
    hold = C1.grid[9][3].status
    C1.grid[9][3].status = C1.grid[11][3].status
    C1.grid[11][3].status = C1.grid[11][5].status
    C1.grid[11][5].status = C1.grid[9][5].status
    C1.grid[9][5].status = hold
    # face edges
    hold = C1.grid[9][4].status
    C1.grid[9][4].status = C1.grid[10][3].status
    C1.grid[10][3].status = C1.grid[11][4].status
    C1.grid[11][4].status = C1.grid[10][5].status
    C1.grid[10][5].status = hold
    # inside corners d
    hold = C1.grid[8][3].status
    C1.grid[8][3].status = C1.grid[3][0].status
    C1.grid[3][0].status = C1.grid[0][5].status
    C1.grid[0][5].status = C1.grid[5][8].status
    C1.grid[5][8].status = hold
    # outside corners d
    hold = C1.grid[8][5].status
    C1.grid[8][5].status = C1.grid[5][0].status
    C1.grid[5][0].status = C1.grid[0][3].status
    C1.grid[0][3].status = C1.grid[3][8].status
    C1.grid[3][8].status = hold
    # outside edges d
    hold = C1.grid[8][4].status
    C1.grid[8][4].status = C1.grid[4][0].status
    C1.grid[4][0].status = C1.grid[0][4].status
    C1.grid[0][4].status = C1.grid[4][8].status
    C1.grid[4][8].status = hold

    cube_updater()
    pass


def rotate_ugreen():
    status = [C1.grid[9][3].status, C1.grid[9][4].status, C1.grid[9][5].status,
              C1.grid[10][5].status, C1.grid[11][5].status, C1.grid[11][4].status,
              C1.grid[11][3].status, C1.grid[10][3].status]
    status = status[2:] + status[0:2]

    C1.grid[9][3].status, C1.grid[9][4].status, C1.grid[9][5].status, \
        C1.grid[10][5].status, C1.grid[11][5].status, C1.grid[11][4].status, \
        C1.grid[11][3].status, C1.grid[10][3].status = status

    status = [C1.grid[8][5].status, C1.grid[8][4].status, C1.grid[8][3].status,
              C1.grid[3][8].status, C1.grid[4][8].status, C1.grid[5][8].status,
              C1.grid[0][3].status, C1.grid[0][4].status, C1.grid[0][5].status,
              C1.grid[5][0].status, C1.grid[4][0].status, C1.grid[3][0].status]

    status = status[3:] + status[0:3]

    C1.grid[8][5].status, C1.grid[8][4].status, C1.grid[8][3].status, \
        C1.grid[3][8].status, C1.grid[4][8].status, C1.grid[5][8].status, \
        C1.grid[0][3].status, C1.grid[0][4].status, C1.grid[0][5].status, \
        C1.grid[5][0].status, C1.grid[4][0].status, C1.grid[3][0].status = status

    cube_updater()
    pass


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

######################################
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:  # If user wants to perform an action
            if event.key == pygame.K_w:
                C1.reset(cube_map)
            if event.key == pygame.K_t:
                rotate_u_white()
            if event.key == pygame.K_g:
                rotate_u_yellow()
            if event.key == pygame.K_r:
                rotate_u_red()
            if event.key == pygame.K_y:
                rotate_u_orange()
            if event.key == pygame.K_f:
                rotate_u_blue()
            if event.key == pygame.K_h:
                rotate_ugreen()
            if event.key == pygame.K_s:
                scramble()
            if event.key == pygame.K_q:
                solve()

    C1.display_cube(screen)
    # Limit to 50 frames per second
    clock.tick(50)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# If you forget this line, the program will 'hang' on exit.
pygame.quit()
