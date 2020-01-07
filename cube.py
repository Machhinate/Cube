import pygame
import cubeclass
import random
import time



# Initialize pygame
pygame.init()

# Set the height and width of the screen
size = [300, 500]
screen = pygame.display.set_mode(size)
pause = 0
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

the_cube = cubeclass.Cube(cube_map)


def cube_updater():
    pygame.time.delay(pause)
    the_cube.display_cube(screen)
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

            if the_cube.grid[0][4].status == 'b':
                rotate_white()
                rotate_blue()
                rotate_uorange()

            if the_cube.grid[1][3].status == 'b':
                rotate_white()
                rotate_white()
                rotate_blue()
                rotate_orange()

            if the_cube.grid[1][5].status == 'b':
                rotate_blue()
                rotate_uorange()

            if the_cube.grid[2][4].status == 'b':
                rotate_uwhite()
                rotate_blue()
                rotate_orange()

            if the_cube.grid[3][1].status == 'b':
                rotate_uwhite()
                rotate_blue()

            if the_cube.grid[3][7].status == 'b':
                rotate_white()
                rotate_blue()

            if the_cube.grid[4][0].status == 'b':
                rotate_ublue()
                rotate_red()
                rotate_blue()
                rotate_uwhite()
                rotate_blue()

            if the_cube.grid[4][2].status == 'b':
                rotate_ublue()
                rotate_ured()
                rotate_blue()
                rotate_uwhite()
                rotate_blue()

            if the_cube.grid[4][6].status == 'b':
                rotate_orange()
                rotate_white()
                rotate_blue()

            if the_cube.grid[4][8].status == 'b':
                rotate_blue()
                rotate_orange()
                rotate_blue()
                rotate_uyellow()
                rotate_ublue()

            if the_cube.grid[5][1].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_yellow()
                rotate_ublue()

            if the_cube.grid[5][7].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_uyellow()
                rotate_ublue()

            if the_cube.grid[6][4].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_uyellow()
                rotate_blue()
                rotate_ured()
                rotate_blue()
                rotate_blue()

            if the_cube.grid[7][3].status == 'b':
                rotate_ublue()
                rotate_ured()
                rotate_blue()
                rotate_blue()

            if the_cube.grid[7][5].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_yellow()
                rotate_yellow()
                rotate_blue()
                rotate_ured()
                rotate_blue()
                rotate_blue()

            if the_cube.grid[8][4].status == 'b':
                rotate_blue()
                rotate_blue()
                rotate_yellow()
                rotate_blue()
                rotate_ured()
                rotate_blue()
                rotate_blue()

            if the_cube.grid[9][4].status == 'b':
                rotate_green()
                rotate_green()
                rotate_white()
                rotate_white()
                rotate_blue()

            if the_cube.grid[10][3].status == 'b':
                rotate_ugreen()
                rotate_white()
                rotate_white()
                rotate_blue()

            if the_cube.grid[10][5].status == 'b':
                rotate_green()
                rotate_white()
                rotate_white()
                rotate_blue()

            if the_cube.grid[11][4].status == 'b':
                rotate_white()
                rotate_white()
                rotate_blue()

            if (the_cube.grid[3][4].status == 'b' and the_cube.grid[4][3].status == 'b' and
                    the_cube.grid[4][5].status == 'b' and the_cube.grid[5][4].status == 'b'):
                print('cross')
                cross = True

        while cross and not cross_edges:
            if not the_cube.grid[2][4].status == 'w':
                if the_cube.grid[2][4].status == 'r':
                    rotate_white()
                    rotate_white()
                    rotate_green()
                    rotate_red()
                    rotate_red()
                    rotate_ugreen()
                    rotate_white()
                    rotate_white()
                elif the_cube.grid[2][4].status == 'o':
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

            if not the_cube.grid[4][2].status == 'r':
                if the_cube.grid[4][2].status == 'w':
                    rotate_red()
                    rotate_red()
                    rotate_ugreen()
                    rotate_white()
                    rotate_white()
                    rotate_green()
                    rotate_red()
                    rotate_red()
                elif the_cube.grid[4][2].status == 'o':
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

            if not the_cube.grid[6][4].status == 'y':
                if the_cube.grid[6][4].status == 'w':
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
                elif the_cube.grid[6][4].status == 'o':
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

            if not the_cube.grid[4][6].status == 'o':
                if the_cube.grid[4][6].status == 'w':
                    rotate_orange()
                    rotate_orange()
                    rotate_green()
                    rotate_white()
                    rotate_white()
                    rotate_ugreen()
                    rotate_orange()
                    rotate_orange()
                elif the_cube.grid[4][6].status == 'y':
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

            if (the_cube.grid[4][6].status == 'o' and the_cube.grid[6][4].status == 'y' and
                    the_cube.grid[4][2].status == 'r' and the_cube.grid[2][4].status == 'w'):

                cross_edges = True
                print("cross edges")

        pygame.time.delay(step_pause)

        while cross_edges and not first_layer:

            if the_cube.grid[0][3].status == 'b':
                if the_cube.grid[3][0].status == 'r':
                    rotate_white()
                    rotate_green()
                    rotate_uwhite()

                elif the_cube.grid[3][0].status == 'y':
                    rotate_green()
                    rotate_red()
                    rotate_green()
                    rotate_ured()

                elif the_cube.grid[3][0].status == 'o':
                    rotate_green()
                    rotate_green()
                    rotate_yellow()
                    rotate_green()
                    rotate_uyellow()

                elif the_cube.grid[3][0].status == 'w':
                    rotate_ugreen()
                    rotate_orange()
                    rotate_green()
                    rotate_uorange()

            if the_cube.grid[3][0].status == 'b':
                if the_cube.grid[11][3].status == 'r':
                    rotate_ured()
                    rotate_ugreen()
                    rotate_red()

                elif the_cube.grid[11][3].status == 'y':
                    rotate_green()
                    rotate_uyellow()
                    rotate_ugreen()
                    rotate_yellow()

                elif the_cube.grid[11][3].status == 'o':
                    rotate_green()
                    rotate_green()
                    rotate_uorange()
                    rotate_ugreen()
                    rotate_orange()

                elif the_cube.grid[11][3].status == 'w':
                    rotate_ugreen()
                    rotate_uwhite()
                    rotate_ugreen()
                    rotate_white()

            if the_cube.grid[11][3].status == 'b':
                if the_cube.grid[0][3].status == 'r':
                    rotate_white()
                    rotate_green()
                    rotate_green()
                    rotate_uwhite()
                    rotate_ugreen()
                    rotate_white()
                    rotate_green()
                    rotate_uwhite()

                if the_cube.grid[0][3].status == 'y':
                    rotate_green()
                    rotate_red()
                    rotate_green()
                    rotate_green()
                    rotate_ured()
                    rotate_ugreen()
                    rotate_red()
                    rotate_green()
                    rotate_ured()

                if the_cube.grid[0][3].status == 'o':
                    rotate_green()
                    rotate_green()
                    rotate_yellow()
                    rotate_green()
                    rotate_green()
                    rotate_uyellow()
                    rotate_ugreen()
                    rotate_yellow()
                    rotate_green()
                    rotate_uyellow()

                if the_cube.grid[0][3].status == 'w':
                    rotate_ugreen()
                    rotate_orange()
                    rotate_green()
                    rotate_green()
                    rotate_uorange()
                    rotate_ugreen()
                    rotate_orange()
                    rotate_green()
                    rotate_uorange()

            if (the_cube.grid[0][5].status == 'b' or the_cube.grid[11][5].status == 'b' or
                    the_cube.grid[3][8].status == 'b'):
                rotate_green()
                continue

            if (the_cube.grid[5][8].status == 'b' or the_cube.grid[8][5].status == 'b' or
                    the_cube.grid[9][5].status == 'b'):
                rotate_green()
                rotate_green()
                continue

            if (the_cube.grid[5][0].status == 'b' or the_cube.grid[8][3].status == 'b' or
                    the_cube.grid[9][3].status == 'b'):
                rotate_ugreen()
                continue

            if ((the_cube.grid[3][3].status == 'b' and the_cube.grid[3][2].status != 'r') or
                    the_cube.grid[2][3].status == 'b' or the_cube.grid[3][2].status == 'b'):
                rotate_white()
                rotate_green()
                rotate_uwhite()
                continue

            if ((the_cube.grid[3][5].status == 'b' and the_cube.grid[2][5].status != 'w') or
                    the_cube.grid[2][5].status == 'b' or the_cube.grid[3][6].status == 'b'):
                rotate_orange()
                rotate_green()
                rotate_uorange()
                continue

            if ((the_cube.grid[5][3].status == 'b' and the_cube.grid[6][3].status != 'y') or
                    the_cube.grid[6][3].status == 'b' or the_cube.grid[5][2].status == 'b'):
                rotate_red()
                rotate_green()
                rotate_ured()
                continue

            if ((the_cube.grid[5][5].status == 'b' and the_cube.grid[5][6].status != 'o') or
                    the_cube.grid[5][6].status == 'b' or the_cube.grid[6][5].status == 'b'):
                rotate_yellow()
                rotate_green()
                rotate_uyellow()
                continue

            if (the_cube.grid[3][3].status == 'b' and the_cube.grid[3][5].status == 'b' and
                    the_cube.grid[5][3].status == 'b' and the_cube.grid[5][5].status == 'b'):
                print("first layer")
                first_layer = True

        pygame.time.delay(step_pause)

        while first_layer and not second_layer:
            if the_cube.grid[11][4].status != 'g' and the_cube.grid[0][4].status != 'g':
                if the_cube.grid[11][4].status == 'r':
                    if the_cube.grid[0][4].status == 'y':
                        rotate_ugreen()
                        rotate_red()
                        rotate_ugreen()
                        rotate_ured()
                        rotate_green()
                        rotate_green()
                        rotate_uyellow()
                        rotate_green()
                        rotate_green()
                        rotate_yellow()

                        print('red yellow')

                    if the_cube.grid[0][4].status == 'w':
                        rotate_ugreen()
                        rotate_ured()
                        rotate_green()
                        rotate_red()
                        rotate_green()
                        rotate_white()
                        rotate_ugreen()
                        rotate_uwhite()
                        print('red white')

                if the_cube.grid[11][4].status == 'y':
                    if the_cube.grid[0][4].status == 'r':
                        rotate_uyellow()
                        rotate_green()
                        rotate_yellow()
                        rotate_green()
                        rotate_red()
                        rotate_ugreen()
                        rotate_ured()
                        print('yellow red')

                    if the_cube.grid[0][4].status == 'o':
                        rotate_yellow()
                        rotate_ugreen()
                        rotate_uyellow()
                        rotate_green()
                        rotate_green()
                        rotate_uorange()
                        rotate_green()
                        rotate_green()
                        rotate_orange()

                        print('yellow orange')

                if the_cube.grid[11][4].status == 'o':
                    if the_cube.grid[0][4].status == 'w':
                        rotate_green()
                        rotate_orange()
                        rotate_ugreen()
                        rotate_uorange()
                        rotate_green()
                        rotate_green()
                        rotate_uwhite()
                        rotate_green()
                        rotate_green()
                        rotate_white()
                        print('orange white')

                    if the_cube.grid[0][4].status == 'y':
                        rotate_green()
                        rotate_uorange()
                        rotate_green()
                        rotate_orange()
                        rotate_green()
                        rotate_green()
                        rotate_yellow()
                        rotate_green()
                        rotate_green()
                        rotate_uyellow()
                        print('orange yellow')

                if the_cube.grid[11][4].status == 'w':
                    if the_cube.grid[0][4].status == 'o':
                        rotate_green()
                        rotate_green()
                        rotate_uwhite()
                        rotate_green()
                        rotate_white()
                        rotate_green()
                        rotate_green()
                        rotate_orange()
                        rotate_green()
                        rotate_green()
                        rotate_uorange()
                        print('white orange')

                    if the_cube.grid[0][4].status == 'r':
                        rotate_green()
                        rotate_green()
                        rotate_white()
                        rotate_ugreen()
                        rotate_uwhite()
                        rotate_green()
                        rotate_green()
                        rotate_ured()
                        rotate_green()
                        rotate_green()
                        rotate_red()
                        print('white red')

            if the_cube.grid[10][5].status != 'g' and the_cube.grid[4][8].status != 'g':
                rotate_green()
                continue

            if the_cube.grid[9][4].status != 'g' and the_cube.grid[8][4].status != 'g':
                rotate_green()
                rotate_green()
                continue

            if the_cube.grid[10][3].status != 'g' and the_cube.grid[4][0].status != 'g':
                rotate_ugreen()
                continue

            if the_cube.grid[3][1].status != 'r' or the_cube.grid[1][3].status != 'w':
                rotate_white()
                rotate_ugreen()
                rotate_uwhite()
                rotate_red()
                rotate_uwhite()
                rotate_ured()
                rotate_white()
                print('3,1;1,3')
                continue
            if the_cube.grid[5][7].status != 'o' or the_cube.grid[7][5].status != 'y':
                rotate_yellow()
                rotate_ugreen()
                rotate_uyellow()
                rotate_orange()
                rotate_uyellow()
                rotate_uorange()
                rotate_yellow()
                print('5,7;7,5')
                continue
            if the_cube.grid[7][3].status != 'y' or the_cube.grid[5][1].status != 'r':
                rotate_red()
                rotate_ugreen()
                rotate_ured()
                rotate_yellow()
                rotate_ured()
                rotate_uyellow()
                rotate_red()
                print('7,3;5,1')
                continue
            if the_cube.grid[3][7].status != 'o' or the_cube.grid[1][5].status != 'w':
                rotate_orange()
                rotate_ugreen()
                rotate_uorange()
                rotate_white()
                rotate_uorange()
                rotate_uwhite()
                rotate_orange()
                print('3,7;1,5')
                continue

            second_layer = True
            print('second layer')

        pygame.time.delay(step_pause)

        while second_layer and not top_cross:

            if (the_cube.grid[10][3].status == 'g' and the_cube.grid[11][4].status == 'g' and
                    the_cube.grid[10][5].status == 'g' and the_cube.grid[9][4].status == 'g'):
                top_cross = True
                print("top_cross")
                continue

            elif (the_cube.grid[10][3].status == 'g' and the_cube.grid[11][4].status != 'g' and
                    the_cube.grid[10][5].status != 'g' and the_cube.grid[9][4].status == 'g'):
                rotate_white()
                rotate_green()
                rotate_orange()
                rotate_ugreen()
                rotate_uorange()
                rotate_uwhite()
                continue

            elif (the_cube.grid[10][3].status == 'g' and the_cube.grid[11][4].status != 'g' and
                    the_cube.grid[10][5].status == 'g' and the_cube.grid[9][4].status != 'g'):
                rotate_white()
                rotate_orange()
                rotate_green()
                rotate_uorange()
                rotate_ugreen()
                rotate_uwhite()
                continue

            elif (the_cube.grid[10][3].status != 'g' and the_cube.grid[11][4].status == 'g' and
                    the_cube.grid[10][5].status != 'g' and the_cube.grid[9][4].status == 'g'):
                rotate_orange()
                rotate_yellow()
                rotate_green()
                rotate_uyellow()
                rotate_ugreen()
                rotate_uorange()
                continue

            elif (the_cube.grid[10][3].status == 'g' and the_cube.grid[11][4].status == 'g' and
                    the_cube.grid[10][5].status != 'g' and the_cube.grid[9][4].status != 'g'):
                rotate_orange()
                rotate_green()
                rotate_yellow()
                rotate_ugreen()
                rotate_uyellow()
                rotate_uorange()
                continue

            elif (the_cube.grid[10][3].status != 'g' and the_cube.grid[11][4].status == 'g' and
                    the_cube.grid[10][5].status == 'g' and the_cube.grid[9][4].status != 'g'):
                rotate_yellow()
                rotate_green()
                rotate_red()
                rotate_ugreen()
                rotate_ured()
                rotate_uyellow()
                continue

            elif (the_cube.grid[10][3].status != 'g' and the_cube.grid[11][4].status != 'g' and
                    the_cube.grid[10][5].status == 'g' and the_cube.grid[9][4].status == 'g'):
                rotate_red()
                rotate_green()
                rotate_white()
                rotate_ugreen()
                rotate_uwhite()
                rotate_ured()
                continue

            else:
                rotate_red()
                rotate_green()
                rotate_white()
                rotate_ugreen()
                rotate_uwhite()
                rotate_ured()

        pygame.time.delay(step_pause)

        while top_cross and not top_face:

            if (the_cube.grid[9][3].status == 'g' and the_cube.grid[9][5].status == 'g' and
                    the_cube.grid[11][3].status == 'g' and the_cube.grid[11][5].status == 'g'):
                top_face = True
                print('top face')
                continue

            elif (the_cube.grid[9][3].status == 'g' and the_cube.grid[9][5].status != 'g' and
                    the_cube.grid[11][3].status != 'g' and the_cube.grid[11][5].status != 'g'):
                rotate_green()
                continue

            elif (the_cube.grid[9][3].status != 'g' and the_cube.grid[9][5].status != 'g' and
                    the_cube.grid[11][3].status == 'g' and the_cube.grid[11][5].status != 'g'):
                rotate_green()
                rotate_green()
                continue

            elif (the_cube.grid[9][3].status != 'g' and the_cube.grid[9][5].status != 'g' and
                    the_cube.grid[11][3].status != 'g' and the_cube.grid[11][5].status == 'g'):
                rotate_ugreen()
                continue

            elif (the_cube.grid[9][3].status != 'g' and the_cube.grid[9][5].status == 'g' and
                  the_cube.grid[11][3].status != 'g' and the_cube.grid[11][5].status != 'g' and
                  the_cube.grid[3][8].status == 'g'):
                rotate_uwhite()
                rotate_ugreen()
                rotate_white()
                rotate_ugreen()
                rotate_uwhite()
                rotate_green()
                rotate_green()
                rotate_white()

            elif (the_cube.grid[9][3].status != 'g' and the_cube.grid[9][5].status != 'g' and
                  the_cube.grid[11][3].status != 'g' and the_cube.grid[11][5].status != 'g' and
                  (the_cube.grid[8][5].status == 'g' and the_cube.grid[8][3].status != 'g')):
                rotate_green()
                rotate_green()

            else:
                rotate_red()
                rotate_green()
                rotate_ured()
                rotate_green()
                rotate_red()
                rotate_green()
                rotate_green()
                rotate_ured()

        pygame.time.delay(step_pause)

        while top_face and not corners:

            if (the_cube.grid[0][3].status == the_cube.grid[0][5].status and
                    the_cube.grid[8][3].status == the_cube.grid[8][5].status):
                print('corners')
                corners = True
                continue

            if (the_cube.grid[0][3].status == the_cube.grid[0][5].status and
                    the_cube.grid[8][3].status != the_cube.grid[8][5].status):
                print('corner swap')
                rotate_ured()
                rotate_yellow()
                rotate_ured()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_uyellow()
                rotate_ured()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_red()

            elif (the_cube.grid[3][8].status == the_cube.grid[5][8].status or
                  the_cube.grid[8][3].status == the_cube.grid[8][5].status or
                  the_cube.grid[5][0].status == the_cube.grid[3][0].status):
                rotate_green()

            else:
                print('else corner swap')
                rotate_ured()
                rotate_yellow()
                rotate_ured()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_uyellow()
                rotate_ured()
                rotate_white()
                rotate_white()
                rotate_red()
                rotate_red()

        pygame.time.delay(step_pause)

        while corners and not top_layer:

            if (the_cube.grid[3][8].status == the_cube.grid[4][8].status and
                    the_cube.grid[8][3].status == the_cube.grid[8][4].status and
                    the_cube.grid[5][0].status == the_cube.grid[4][0].status and
                    the_cube.grid[0][3].status == the_cube.grid[0][4].status):
                top_layer = True
                print('top layer')
                continue

            if (the_cube.grid[3][8].status == the_cube.grid[4][8].status or
                    the_cube.grid[8][3].status == the_cube.grid[8][4].status or
                    the_cube.grid[5][0].status == the_cube.grid[4][0].status):
                rotate_green()
                continue

            else:
                rotate_yellow()
                rotate_yellow()
                rotate_green()
                rotate_ured()
                rotate_orange()
                rotate_yellow()
                rotate_yellow()
                rotate_red()
                rotate_uorange()
                rotate_green()
                rotate_yellow()
                rotate_yellow()

        pygame.time.delay(step_pause)

        while top_layer and not solved:
            if the_cube.grid[0][4].status == the_cube.grid[1][4].status:
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
            rotate_uyellow()
        elif move == 8:
            rotate_ublue()
        elif move == 9:
            rotate_ured()
        elif move == 10:
            rotate_uorange()
        else:
            rotate_uwhite()


def rotate_white(): #white
    # face corners

    hold = the_cube.grid[0][3].status
    the_cube.grid[0][3].status = the_cube.grid[2][3].status
    the_cube.grid[2][3].status = the_cube.grid[2][5].status
    the_cube.grid[2][5].status = the_cube.grid[0][5].status
    the_cube.grid[0][5].status = hold
    # face edges
    hold = the_cube.grid[0][4].status
    the_cube.grid[0][4].status = the_cube.grid[1][3].status
    the_cube.grid[1][3].status = the_cube.grid[2][4].status
    the_cube.grid[2][4].status = the_cube.grid[1][5].status
    the_cube.grid[1][5].status = hold
    # inside corners d
    hold = the_cube.grid[11][3].status
    the_cube.grid[11][3].status = the_cube.grid[3][2].status
    the_cube.grid[3][2].status = the_cube.grid[3][5].status
    the_cube.grid[3][5].status = the_cube.grid[3][8].status
    the_cube.grid[3][8].status = hold
    # outside corners d
    hold = the_cube.grid[11][5].status
    the_cube.grid[11][5].status = the_cube.grid[3][0].status
    the_cube.grid[3][0].status = the_cube.grid[3][3].status
    the_cube.grid[3][3].status = the_cube.grid[3][6].status
    the_cube.grid[3][6].status = hold
    # outside edges d
    hold = the_cube.grid[11][4].status
    the_cube.grid[11][4].status = the_cube.grid[3][1].status
    the_cube.grid[3][1].status = the_cube.grid[3][4].status
    the_cube.grid[3][4].status = the_cube.grid[3][7].status
    the_cube.grid[3][7].status = hold

    cube_updater()
    pass


def rotate_uwhite(): #uwhite
    status = [the_cube.grid[0][3].status, the_cube.grid[0][4].status, the_cube.grid[0][5].status,
              the_cube.grid[1][5].status, the_cube.grid[2][5].status, the_cube.grid[2][4].status,
              the_cube.grid[2][3].status, the_cube.grid[1][3].status]
    status = status[2:] + status[0:2]

    the_cube.grid[0][3].status, the_cube.grid[0][4].status, the_cube.grid[0][5].status, \
    the_cube.grid[1][5].status, the_cube.grid[2][5].status, the_cube.grid[2][4].status, \
    the_cube.grid[2][3].status, the_cube.grid[1][3].status = status

    status = [the_cube.grid[11][5].status, the_cube.grid[11][4].status, the_cube.grid[11][3].status,
              the_cube.grid[3][6].status, the_cube.grid[3][7].status, the_cube.grid[3][8].status,
              the_cube.grid[3][3].status, the_cube.grid[3][4].status, the_cube.grid[3][5].status,
              the_cube.grid[3][0].status, the_cube.grid[3][1].status, the_cube.grid[3][2].status]
    status = status[3:] + status[0:3]

    the_cube.grid[11][5].status, the_cube.grid[11][4].status, the_cube.grid[11][3].status, \
    the_cube.grid[3][6].status, the_cube.grid[3][7].status, the_cube.grid[3][8].status, \
    the_cube.grid[3][3].status, the_cube.grid[3][4].status, the_cube.grid[3][5].status, \
    the_cube.grid[3][0].status, the_cube.grid[3][1].status, the_cube.grid[3][2].status = status

    cube_updater()
    pass


def rotate_uyellow():  # yellow
    status = [the_cube.grid[6][3].status, the_cube.grid[6][4].status, the_cube.grid[6][5].status,
              the_cube.grid[7][5].status, the_cube.grid[8][5].status, the_cube.grid[8][4].status,
              the_cube.grid[8][3].status, the_cube.grid[7][3].status]
    status = status[2:] + status[0:2]

    the_cube.grid[6][3].status, the_cube.grid[6][4].status, the_cube.grid[6][5].status, \
    the_cube.grid[7][5].status, the_cube.grid[8][5].status, the_cube.grid[8][4].status, \
    the_cube.grid[8][3].status, the_cube.grid[7][3].status = status

    status = [the_cube.grid[5][5].status, the_cube.grid[5][4].status, the_cube.grid[5][3].status,
              the_cube.grid[5][8].status, the_cube.grid[5][7].status, the_cube.grid[5][6].status,
              the_cube.grid[9][3].status, the_cube.grid[9][4].status, the_cube.grid[9][5].status,
              the_cube.grid[5][2].status, the_cube.grid[5][1].status, the_cube.grid[5][0].status]

    status = status[3:] + status[0:3]

    the_cube.grid[5][5].status, the_cube.grid[5][4].status, the_cube.grid[5][3].status, \
    the_cube.grid[5][8].status, the_cube.grid[5][7].status, the_cube.grid[5][6].status, \
    the_cube.grid[9][3].status, the_cube.grid[9][4].status, the_cube.grid[9][5].status, \
    the_cube.grid[5][2].status, the_cube.grid[5][1].status, the_cube.grid[5][0].status = status

    cube_updater()
    pass


def rotate_yellow():  # yellow
    #face corners d
    hold = the_cube.grid[6][3].status
    the_cube.grid[6][3].status = the_cube.grid[8][3].status
    the_cube.grid[8][3].status = the_cube.grid[8][5].status
    the_cube.grid[8][5].status = the_cube.grid[6][5].status
    the_cube.grid[6][5].status = hold
    #face edges d
    hold = the_cube.grid[6][4].status
    the_cube.grid[6][4].status = the_cube.grid[7][3].status
    the_cube.grid[7][3].status = the_cube.grid[8][4].status
    the_cube.grid[8][4].status = the_cube.grid[7][5].status
    the_cube.grid[7][5].status = hold
    # inside corners d
    hold = the_cube.grid[9][5].status
    the_cube.grid[9][5].status = the_cube.grid[5][6].status
    the_cube.grid[5][6].status = the_cube.grid[5][3].status
    the_cube.grid[5][3].status = the_cube.grid[5][0].status
    the_cube.grid[5][0].status = hold
    # outside corners d
    hold = the_cube.grid[9][3].status
    the_cube.grid[9][3].status = the_cube.grid[5][8].status
    the_cube.grid[5][8].status = the_cube.grid[5][5].status
    the_cube.grid[5][5].status = the_cube.grid[5][2].status
    the_cube.grid[5][2].status = hold
    # outside edges d
    hold = the_cube.grid[9][4].status
    the_cube.grid[9][4].status = the_cube.grid[5][7].status
    the_cube.grid[5][7].status = the_cube.grid[5][4].status
    the_cube.grid[5][4].status = the_cube.grid[5][1].status
    the_cube.grid[5][1].status = hold

    cube_updater()
    pass


def rotate_red():  # red
    #face corners d
    hold = the_cube.grid[3][0].status
    the_cube.grid[3][0].status = the_cube.grid[5][0].status
    the_cube.grid[5][0].status = the_cube.grid[5][2].status
    the_cube.grid[5][2].status = the_cube.grid[3][2].status
    the_cube.grid[3][2].status = hold
    #face edges
    hold = the_cube.grid[3][1].status
    the_cube.grid[3][1].status = the_cube.grid[4][0].status
    the_cube.grid[4][0].status = the_cube.grid[5][1].status
    the_cube.grid[5][1].status = the_cube.grid[4][2].status
    the_cube.grid[4][2].status = hold
    # inside corners
    hold = the_cube.grid[2][3].status
    the_cube.grid[2][3].status = the_cube.grid[11][3].status
    the_cube.grid[11][3].status = the_cube.grid[8][3].status
    the_cube.grid[8][3].status = the_cube.grid[5][3].status
    the_cube.grid[5][3].status = hold
    # outside corners
    hold = the_cube.grid[0][3].status
    the_cube.grid[0][3].status = the_cube.grid[9][3].status
    the_cube.grid[9][3].status = the_cube.grid[6][3].status
    the_cube.grid[6][3].status = the_cube.grid[3][3].status
    the_cube.grid[3][3].status = hold
    # outside edges
    hold = the_cube.grid[1][3].status
    the_cube.grid[1][3].status = the_cube.grid[10][3].status
    the_cube.grid[10][3].status = the_cube.grid[7][3].status
    the_cube.grid[7][3].status = the_cube.grid[4][3].status
    the_cube.grid[4][3].status = hold

    cube_updater()
    pass


def rotate_ured():
    status = [the_cube.grid[3][0].status, the_cube.grid[3][1].status, the_cube.grid[3][2].status,
              the_cube.grid[4][2].status, the_cube.grid[5][2].status, the_cube.grid[5][1].status,
              the_cube.grid[5][0].status, the_cube.grid[4][0].status]
    status = status[2:] + status[0:2]

    the_cube.grid[3][0].status, the_cube.grid[3][1].status, the_cube.grid[3][2].status, \
    the_cube.grid[4][2].status, the_cube.grid[5][2].status, the_cube.grid[5][1].status, \
    the_cube.grid[5][0].status, the_cube.grid[4][0].status = status

    status = [the_cube.grid[2][3].status, the_cube.grid[1][3].status, the_cube.grid[0][3].status,
              the_cube.grid[5][3].status, the_cube.grid[4][3].status, the_cube.grid[3][3].status,
              the_cube.grid[8][3].status, the_cube.grid[7][3].status, the_cube.grid[6][3].status,
              the_cube.grid[11][3].status, the_cube.grid[10][3].status, the_cube.grid[9][3].status]

    status = status[3:] + status[0:3]

    the_cube.grid[2][3].status, the_cube.grid[1][3].status, the_cube.grid[0][3].status, \
    the_cube.grid[5][3].status, the_cube.grid[4][3].status, the_cube.grid[3][3].status, \
    the_cube.grid[8][3].status, the_cube.grid[7][3].status, the_cube.grid[6][3].status, \
    the_cube.grid[11][3].status, the_cube.grid[10][3].status, the_cube.grid[9][3].status = status

    cube_updater()
    pass


def rotate_orange():  # orange
    #face corners d
    hold = the_cube.grid[3][6].status
    the_cube.grid[3][6].status = the_cube.grid[5][6].status
    the_cube.grid[5][6].status = the_cube.grid[5][8].status
    the_cube.grid[5][8].status = the_cube.grid[3][8].status
    the_cube.grid[3][8].status = hold
    #face edges
    hold = the_cube.grid[3][7].status
    the_cube.grid[3][7].status = the_cube.grid[4][6].status
    the_cube.grid[4][6].status = the_cube.grid[5][7].status
    the_cube.grid[5][7].status = the_cube.grid[4][8].status
    the_cube.grid[4][8].status = hold
    # inside corners
    hold = the_cube.grid[2][5].status
    the_cube.grid[2][5].status = the_cube.grid[5][5].status
    the_cube.grid[5][5].status = the_cube.grid[8][5].status
    the_cube.grid[8][5].status = the_cube.grid[11][5].status
    the_cube.grid[11][5].status = hold
    # outside corners
    hold = the_cube.grid[0][5].status
    the_cube.grid[0][5].status = the_cube.grid[3][5].status
    the_cube.grid[3][5].status = the_cube.grid[6][5].status
    the_cube.grid[6][5].status = the_cube.grid[9][5].status
    the_cube.grid[9][5].status = hold
    # outside edges
    hold = the_cube.grid[1][5].status
    the_cube.grid[1][5].status = the_cube.grid[4][5].status
    the_cube.grid[4][5].status = the_cube.grid[7][5].status
    the_cube.grid[7][5].status = the_cube.grid[10][5].status
    the_cube.grid[10][5].status = hold

    cube_updater()
    pass


def rotate_uorange():
    status = [the_cube.grid[3][6].status, the_cube.grid[3][7].status, the_cube.grid[3][8].status,
              the_cube.grid[4][8].status, the_cube.grid[5][8].status, the_cube.grid[5][7].status,
              the_cube.grid[5][6].status, the_cube.grid[4][6].status]
    status = status[2:] + status[0:2]

    the_cube.grid[3][6].status, the_cube.grid[3][7].status, the_cube.grid[3][8].status, \
    the_cube.grid[4][8].status, the_cube.grid[5][8].status, the_cube.grid[5][7].status, \
    the_cube.grid[5][6].status, the_cube.grid[4][6].status = status

    status = [the_cube.grid[0][5].status, the_cube.grid[1][5].status, the_cube.grid[2][5].status,
              the_cube.grid[9][5].status, the_cube.grid[10][5].status, the_cube.grid[11][5].status,
              the_cube.grid[6][5].status, the_cube.grid[7][5].status, the_cube.grid[8][5].status,
              the_cube.grid[3][5].status, the_cube.grid[4][5].status, the_cube.grid[5][5].status]

    status = status[3:] + status[0:3]

    the_cube.grid[0][5].status, the_cube.grid[1][5].status, the_cube.grid[2][5].status, \
    the_cube.grid[9][5].status, the_cube.grid[10][5].status, the_cube.grid[11][5].status, \
    the_cube.grid[6][5].status, the_cube.grid[7][5].status, the_cube.grid[8][5].status, \
    the_cube.grid[3][5].status, the_cube.grid[4][5].status, the_cube.grid[5][5].status = status

    cube_updater()
    pass


def rotate_blue():  # blue
    # face corners d
    hold = the_cube.grid[3][3].status
    the_cube.grid[3][3].status = the_cube.grid[5][3].status
    the_cube.grid[5][3].status = the_cube.grid[5][5].status
    the_cube.grid[5][5].status = the_cube.grid[3][5].status
    the_cube.grid[3][5].status = hold
    # face edges
    hold = the_cube.grid[3][4].status
    the_cube.grid[3][4].status = the_cube.grid[4][3].status
    the_cube.grid[4][3].status = the_cube.grid[5][4].status
    the_cube.grid[5][4].status = the_cube.grid[4][5].status
    the_cube.grid[4][5].status = hold
    # inside corners
    hold = the_cube.grid[2][3].status
    the_cube.grid[2][3].status = the_cube.grid[5][2].status
    the_cube.grid[5][2].status = the_cube.grid[6][5].status
    the_cube.grid[6][5].status = the_cube.grid[3][6].status
    the_cube.grid[3][6].status = hold
    # outside corners
    hold = the_cube.grid[3][2].status
    the_cube.grid[3][2].status = the_cube.grid[6][3].status
    the_cube.grid[6][3].status = the_cube.grid[5][6].status
    the_cube.grid[5][6].status = the_cube.grid[2][5].status
    the_cube.grid[2][5].status = hold
    # outside edges
    hold = the_cube.grid[2][4].status
    the_cube.grid[2][4].status = the_cube.grid[4][2].status
    the_cube.grid[4][2].status = the_cube.grid[6][4].status
    the_cube.grid[6][4].status = the_cube.grid[4][6].status
    the_cube.grid[4][6].status = hold

    cube_updater()
    pass

def rotate_ublue():
    status = [the_cube.grid[3][3].status, the_cube.grid[3][4].status, the_cube.grid[3][5].status,
              the_cube.grid[4][5].status, the_cube.grid[5][5].status, the_cube.grid[5][4].status,
              the_cube.grid[5][3].status, the_cube.grid[4][3].status]
    status = status[2:] + status[0:2]

    the_cube.grid[3][3].status, the_cube.grid[3][4].status, the_cube.grid[3][5].status, the_cube.grid[4][5].status, \
    the_cube.grid[5][5].status, the_cube.grid[5][4].status, the_cube.grid[5][3].status, the_cube.grid[4][3].status \
        = status

    status = [the_cube.grid[2][5].status, the_cube.grid[2][4].status, the_cube.grid[2][3].status,
              the_cube.grid[5][6].status, the_cube.grid[4][6].status, the_cube.grid[3][6].status,
              the_cube.grid[6][3].status, the_cube.grid[6][4].status, the_cube.grid[6][5].status,
              the_cube.grid[3][2].status, the_cube.grid[4][2].status, the_cube.grid[5][2].status]

    status = status[3:] + status[0:3]

    the_cube.grid[2][5].status, the_cube.grid[2][4].status, the_cube.grid[2][3].status, \
    the_cube.grid[5][6].status, the_cube.grid[4][6].status, the_cube.grid[3][6].status, \
    the_cube.grid[6][3].status, the_cube.grid[6][4].status, the_cube.grid[6][5].status, \
    the_cube.grid[3][2].status, the_cube.grid[4][2].status, the_cube.grid[5][2].status = status

    cube_updater()
    pass


def rotate_green():  # green
    # face corners d
    hold = the_cube.grid[9][3].status
    the_cube.grid[9][3].status = the_cube.grid[11][3].status
    the_cube.grid[11][3].status = the_cube.grid[11][5].status
    the_cube.grid[11][5].status = the_cube.grid[9][5].status
    the_cube.grid[9][5].status = hold
    # face edges
    hold = the_cube.grid[9][4].status
    the_cube.grid[9][4].status = the_cube.grid[10][3].status
    the_cube.grid[10][3].status = the_cube.grid[11][4].status
    the_cube.grid[11][4].status = the_cube.grid[10][5].status
    the_cube.grid[10][5].status = hold
    # inside corners d
    hold = the_cube.grid[8][3].status
    the_cube.grid[8][3].status = the_cube.grid[3][0].status
    the_cube.grid[3][0].status = the_cube.grid[0][5].status
    the_cube.grid[0][5].status = the_cube.grid[5][8].status
    the_cube.grid[5][8].status = hold
    # outside corners d
    hold = the_cube.grid[8][5].status
    the_cube.grid[8][5].status = the_cube.grid[5][0].status
    the_cube.grid[5][0].status = the_cube.grid[0][3].status
    the_cube.grid[0][3].status = the_cube.grid[3][8].status
    the_cube.grid[3][8].status = hold
    # outside edges d
    hold = the_cube.grid[8][4].status
    the_cube.grid[8][4].status = the_cube.grid[4][0].status
    the_cube.grid[4][0].status = the_cube.grid[0][4].status
    the_cube.grid[0][4].status = the_cube.grid[4][8].status
    the_cube.grid[4][8].status = hold

    cube_updater()
    pass


def rotate_ugreen():
    status = [the_cube.grid[9][3].status, the_cube.grid[9][4].status, the_cube.grid[9][5].status,
              the_cube.grid[10][5].status, the_cube.grid[11][5].status, the_cube.grid[11][4].status,
              the_cube.grid[11][3].status, the_cube.grid[10][3].status]
    status = status[2:] + status[0:2]

    the_cube.grid[9][3].status, the_cube.grid[9][4].status, the_cube.grid[9][5].status, \
    the_cube.grid[10][5].status, the_cube.grid[11][5].status, the_cube.grid[11][4].status, \
    the_cube.grid[11][3].status, the_cube.grid[10][3].status = status

    status = [the_cube.grid[8][5].status, the_cube.grid[8][4].status, the_cube.grid[8][3].status,
              the_cube.grid[3][8].status, the_cube.grid[4][8].status, the_cube.grid[5][8].status,
              the_cube.grid[0][3].status, the_cube.grid[0][4].status, the_cube.grid[0][5].status,
              the_cube.grid[5][0].status, the_cube.grid[4][0].status, the_cube.grid[3][0].status]

    status = status[3:] + status[0:3]

    the_cube.grid[8][5].status, the_cube.grid[8][4].status, the_cube.grid[8][3].status, \
    the_cube.grid[3][8].status, the_cube.grid[4][8].status, the_cube.grid[5][8].status, \
    the_cube.grid[0][3].status, the_cube.grid[0][4].status, the_cube.grid[0][5].status, \
    the_cube.grid[5][0].status, the_cube.grid[4][0].status, the_cube.grid[3][0].status = status

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
            if event.key == pygame.K_p:
                the_cube.reset(cube_map)
            if event.key == pygame.K_u:
                rotate_uwhite()
            if event.key == pygame.K_d:
                rotate_uyellow()
            if event.key == pygame.K_l:
                rotate_ured()
            if event.key == pygame.K_r:
                rotate_uorange()
            if event.key == pygame.K_f:
                rotate_ublue()
            if event.key == pygame.K_b:
                rotate_ugreen()
            if event.key == pygame.K_s:
                scramble()
            if event.key == pygame.K_q:
                solve()

    the_cube.display_cube(screen)
    # Limit to 50 frames per second
    clock.tick(50)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# If you forget this line, the program will 'hang' on exit.
pygame.quit()
