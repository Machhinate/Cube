import pygame
import random

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255,   255, 0)
orange = (255, 100, 0)
blue = (0, 0, 255)


class Cubie:
    def __init__(self, status):
        self.status = status


class Cube:
    def __init__(self, cubegrid):
        self.rows = len(cubegrid)
        self.columns = len(cubegrid[0])
        self.grid = []
        for row in range(self.rows):
            self.grid.append([])
            for column in range(self.columns):
                new_cubie = Cubie(cubegrid[row][column])
                self.grid[row].append(new_cubie)
             
    def reset(self, cube_grid):
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid[row][column] = Cubie(cube_grid[row][column])

    def display_cube(self, screen):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[row][column].status == '0':
                    self.draw_plain_square(screen, row, column)
                elif self.grid[row][column].status == 'b':
                    self.draw_blue(screen, row, column)
                elif self.grid[row][column].status == 'g':
                    self.draw_green(screen, row, column)
                elif self.grid[row][column].status == 'y':
                    self.draw_yellow(screen, row, column)
                elif self.grid[row][column].status == 'w':
                    self.draw_white(screen, row, column)
                elif self.grid[row][column].status == 'o':
                    self.draw_orange(screen, row, column)
                else:
                    self.draw_red(screen, row, column)

    def draw_plain_square(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, black, [j * (300 / columns), i * (400 / rows),
                                         (300 / columns), (400 / rows)])
        
    def draw_orange(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, orange, [j * (300 / columns), i * (400 / rows),
                                          (300 / columns), (400 / rows)])
       
    def draw_green(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, green, [j * (300 / columns), i * (400 / rows),
                                         (300 / columns), (400 / rows)])
     
    def draw_yellow(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, yellow, [j * (300 / columns), i * (400 / rows),
                                          (300 / columns), (400 / rows)])

    def draw_blue(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, blue, [j * (300 / columns), i * (400 / rows),
                                        (300 / columns), (400 / rows)])

    def draw_red(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, red, [j * (300 / columns), i * (400 / rows),
                                       (300 / columns), (400 / rows)])
    
    def draw_white(self, screen, i, j):
        rows = self.rows
        columns = self.columns
        pygame.draw.rect(screen, white, [j * (300 / columns), i * (400 / rows),
                                         (300 / columns), (400 / rows)])

