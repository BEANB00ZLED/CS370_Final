import pygame
import numpy as np

class Grid:
    occupied_coords = []
    
    # uselss constructor
    def __init__(self):
        pass

    # draws the grid
    def drawGrid(self, w, rows, surface):
        # calculates the size between squares
        size_between = w // rows
        # draws the lines
        for i in range(0, w, size_between):
            x, y = i, i
            pygame.draw.line(surface, 'black', (x, 0), (x, w))
            pygame.draw.line(surface, 'black', (0, y), (w, y))

    #calculates the size between squares.
    def sizeBetween(self, w, rows):
        size_between = w // rows
        return size_between
    
    #Removes coordinate from 
    def removePoint(self, x, y):
        if [x, y] in Grid.occupied_coords:
          Grid.occupied_coords.remove([x, y])  

    #grabs size between, rounds x and y to nearest grid and returns x and y
    def computeSnap(self, x, y):
        grid_square_size = self.sizeBetween(1050, 10)
        x = ((round(x / grid_square_size)) * grid_square_size)
        y = ((round(y / grid_square_size)) * grid_square_size)
        if [x, y] not in Grid.occupied_coords:
            Grid.occupied_coords.append([x, y])
        print(Grid.occupied_coords)
        return x, y
