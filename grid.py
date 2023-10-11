import pygame


class Grid:

    # uselss constructor
    def __int__(self):
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

    def sizeBetween(self, w, rows):
        size_between = w // rows
        return size_between
