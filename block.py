from colors import colors
import pygame as py
from position import Position


class block:
    # declares the properties of the block class
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 25
        self.rowoffset = 0
        self.columnoffset = 0
        self.rotation_state = 0
        self.colors = colors.get_cell_colors()

    # moves the block by a row offset or column offset in the grid
    def move(self, rows, columns):
        self.rowoffset += rows
        self.columnoffset += columns

    def getcellpositions(self):
        tiles = self.cells[self.rotation_state]
        movedtiles = []
        for position in tiles:
            position = Position(position.row + self.rowoffset, position.column + self.columnoffset)
            movedtiles.append(position)
        return movedtiles

    # cycles through a blocks rotation states clockwise
    def  rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    # same as above but in the opposite direction
    def  rotateCCW(self):
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1
        else:
            self.rotation_state -= 1

    # undoes the rotation state
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == -1:
            self.rotation_state = len(self.cells) - 1

    # displays the block on the screen
    def draw(self, screen, offsetx, offsety):
        tiles = self.getcellpositions()
        for tile in tiles:
            tile_rect = py.Rect(tile.column * self.cell_size + offsetx, tile.row * self.cell_size + offsety , self.cell_size , self.cell_size)
            py.draw.rect(screen, self.colors[self.id], tile_rect)

