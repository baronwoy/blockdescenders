import pygame as py
from colors import colors

class grid:
    def __init__(self):
        self.rows = 20
        self.cols = 10
        self.cell_size = 25
        self.grid = [[0] * self.cols for i in range(self.rows)]
        self.colors = colors.get_cell_colors()

    def is_inside(self, row, column):
        if row >= 0 and row < self.rows and column >= 0 and column < self.cols:
            return True
        return False

    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    def is_row_full(self, row):
        for column in range(self.cols):
            if self.grid[row][column] == 0:
                return False
        return True

    def moverowdown(self, row, numrows):
        for column in range(self.cols):
            self.grid[row+numrows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    def clearfullrow(self):
        completed = 0
        for row in range(self.rows-1, 0, -1):
            if self.is_row_full(row):
                self.clearrow(row)
                completed += 1
            elif completed > 0:
                self.moverowdown(row, completed)
        return completed

    def reset(self):
        for row in range(self.rows):
            for column in range(self.cols):
                self.grid[row][column] = 0


    def clearrow(self, row):
        for column in range(self.cols):
            self.grid[row][column] = 0


    def draw(self, screen, offsetx, offsety):
        for row in range(self.rows):
            for column in range(self.cols):
                cellvalue = self.grid[row][column]
                cell_rect = py.Rect(column*self.cell_size + offsetx , row*self.cell_size + offsety , self.cell_size , self.cell_size )
                py.draw.rect(screen, self.colors[cellvalue], cell_rect)
