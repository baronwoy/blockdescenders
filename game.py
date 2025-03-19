from blocks import *
from grid import grid
import random
import pygame as py
import copy

class game:
    def __init__(self):
        self.grid = grid()
        self.blocks = [iblock(), jblock(), lblock(), oblock(), sblock(), tblock(), zblock()]
        self.currentblock = self.getrandomblock()
        self.nextblock = [self.getrandomblock() for i in range(3)]
        self.gameover = False
        self.score = 0
        self.lines = 0
        self.lv = 1
        self.totallines = 0
        self.interval = 175
        self.canhold = True
        self.hblock = initholdblock()

    def getrandomblock(self):
        if len(self.blocks) == 0:
            self.blocks = [iblock(), jblock(), lblock(), oblock(), sblock(), tblock(), zblock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def updatescore(self, num):
        if num == 1:
            self.score += 100 * self.lv + 1
        if num == 2:
            self.score += 300 * self.lv + 1
        if num == 3:
            self.score += 500 * self.lv + 1
        if num == 4:
            self.score += 800 * self.lv + 1
        else:
            self.score += 1

    def updatelevel(self):
            self.lv += 1
            if self.lv > 16:
                self.lv = 16
            self.updateinterval()

    def move_left(self):
        self.currentblock.move(0, -1)
        if self.blockinside(self.currentblock) == False or self.blockfits(self.currentblock) == False:
            self.currentblock.move(0, 1)

    def move_right(self):
        self.currentblock.move(0, 1)
        if self.blockinside(self.currentblock) == False or self.blockfits(self.currentblock) == False:
            self.currentblock.move(0, -1)

    def move_down(self):
        self.currentblock.move(1, 0)
        if self.blockinside(self.currentblock) == False or self.blockfits(self.currentblock) == False:
            self.currentblock.move(-1, 0)
            self.lockblock()

    def lockblock(self):
        tiles = self.currentblock.getcellpositions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.currentblock.id
        self.currentblock = self.nextblock.pop(0)
        self.nextblock.append(self.getrandomblock())
        numrows = self.grid.clearfullrow()
        self.totallines += numrows
        self.updatescore(numrows)
        if numrows:
            if self.totallines % 2 == 0:
                self.updatelevel()
        if self.blockfits(self.currentblock) == False:
            self.gameover = True
        self.canhold = True

    def reset(self):
        self.grid.reset()
        self.blocks = [iblock(), jblock(), lblock(), oblock(), sblock(), tblock(), zblock()]
        self.currentblock = self.getrandomblock()
        self.nextblock = [self.getrandomblock() for i in range(3)]
        self.gameover = False
        self.score = 0
        self.lines = 0
        self.lv = 1
        self.totallines = 0
        self.interval = 175
        self.canhold = True
        self.hblock = initholdblock()

    def blockfits(self, piece):
        tiles = piece.getcellpositions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.currentblock.rotate()
        if self.blockinside(self.currentblock) == False or self.blockfits(self.currentblock) == False:
            self.currentblock.undo_rotation()

    def rotateCCW(self):
        self.currentblock.rotateCCW()
        if self.blockinside(self.currentblock) == False or self.blockfits(self.currentblock) == False:
            self.currentblock.undo_rotation()

    def blockinside(self, piece):
        tiles = piece.getcellpositions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def ui(self, surface):
        my_font = py.font.SysFont('', 30)
        my_font2 = py.font.SysFont('', 25)
        score = self.score
        if score < 10:
            scoreval = "00000" + str(score)
        elif score < 100:
            scoreval = "0000" + str(score)
        elif score < 1000:
            scoreval = "000" + str(score)
        elif score < 10000:
            scoreval = "00" + str(score)
        elif score < 100000:
            scoreval = "0" + str(score)
        else:
            scoreval = str(score)

        lines = self.totallines
        linesval = str(lines)
        lv = self.lv
        lvval = str(lv)
        text_hold = my_font.render('HOLD', False, (0, 0, 0))
        surface.blit(text_hold, (70, 52))
        text_next = my_font.render('NEXT', False, (0, 0, 0))
        surface.blit(text_next, (470, 52))
        text_score = my_font.render('SCORE:', False, (0, 0, 0))
        surface.blit(text_score, (175, 20))
        text_scorenum = my_font.render(scoreval, False, (0, 0, 0))
        surface.blit(text_scorenum, (265, 20))
        text_lines = my_font2.render('Lines:', False, (0, 0, 0))
        surface.blit(text_lines, (65, 443))
        if lines < 10:
            text_linesval = my_font2.render(linesval, False, (0, 0, 0))
            surface.blit(text_linesval, (135, 443))
        else:
            text_linesval = my_font2.render(linesval, False, (0, 0, 0))
            surface.blit(text_linesval, (130, 443))

        text_lv = my_font2.render('Lv:', False, (0, 0, 0))
        surface.blit(text_lv, (65, 517))
        if lv < 10:
            text_lvval = my_font2.render(lvval, False, (0, 0, 0))
            surface.blit(text_lvval, (135, 517))
        else:
            text_lvval = my_font2.render(lvval, False, (0, 0, 0))
            surface.blit(text_lvval, (130, 517))

    def otherui(self, surface):
        hold = py.Rect(25, 50, 150, (400/3))
        py.draw.rect(surface, "black", hold, width=1)
        holdb = py.Rect(25, 50, 150, 25)
        py.draw.rect(surface, "black", holdb, width=1)
        next = py.Rect(425, 50, 150, 400)
        py.draw.rect(surface, "black", next, width=1)
        nextb = py.Rect(425, 50, 150, 25)
        py.draw.rect(surface, "black", nextb, width=1)
        py.draw.circle(surface, (0, 0, 0), (140, 450), 20, width=1)
        py.draw.circle(surface, (0, 0, 0), (140, 525), 20, width=1)

    def draw(self, screen):
        self.grid.draw(screen, 175, 50)
        g = self.getghostpos()
        g.id = 8
        g.draw(screen, 175, 50)
        self.currentblock.draw(screen,175,50)
        if self.hblock.id != -1:
            if self.hblock.id == 4:
                self.hblock.draw(screen,75,100)
            elif self.hblock.id == 3:
                self.hblock.draw(screen,50, 80)
            else:
                self.hblock.draw(screen, 62.5, 100)
        if self.nextblock[0].id == 3 or self.nextblock[0].id == 4:
            self.nextblock[0].draw(screen,375,100)
        else:
            self.nextblock[0].draw(screen,387.5,100)
        if self.nextblock[1].id == 3 or self.nextblock[1].id == 4:
            self.nextblock[1].draw(screen,375,(400/3 + 175/2))
        else:
            self.nextblock[1].draw(screen,387.5,(400/3 + 175/2))
        if self.nextblock[2].id == 3 or self.nextblock[2].id == 4:
            self.nextblock[2].draw(screen,375,(400/3 + 200))
        else:
            self.nextblock[2].draw(screen,387.5,(400/3 + 200))


    def getinterval(self):
        return self.interval

    def updateinterval(self):
        self.interval -= 10
        if self.interval < 25:
            self.interval = 25
        print(self.interval)

    def holdblock(self):
        if not self.canhold:
            return
        else:
            if self.hblock.id == -1:
                self.hblock = self.currentblock
                self.currentblock = self.nextblock.pop(0)
                self.nextblock.append(self.getrandomblock())
                self.reset_position()
            else:
                tempblock = self.currentblock
                self.currentblock = self.hblock
                self.hblock = tempblock
                self.reset_position()
            self.hblock.rowoffset = 0
            self.hblock.columnoffset = 0
            self.hblock.rotation_state = 0
            self.canhold = False


    def reset_position(self):
        if self.currentblock.id == 3:
            self.currentblock.rowoffset = -1
            self.currentblock.columnoffset = 3
        elif self.currentblock.id == 4:
            self.currentblock.rowoffset = 0
            self.currentblock.columnoffset = 4
        else:
            self.currentblock.rowoffset = 0
            self.currentblock.columnoffset = 3
        self.currentblock.rotation_state = 0

    def getghostpos(self):
        ghost = self.copy()
        while self.blockinside(ghost) == True and self.blockfits(ghost) == True:
            ghost.move(1, 0)
        ghost.move(-1, 0)
        return ghost


    def dropblock(self):
        while self.blockinside(self.currentblock) == True and self.blockfits(self.currentblock) == True:
            self.currentblock.move(1, 0)
        self.currentblock.move(-1, 0)
        self.lockblock()

    def copy(self):
        return copy.deepcopy(self.currentblock)


















