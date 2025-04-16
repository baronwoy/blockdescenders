import pygame as py

# class to display the game over UI
class gameover():
    def gameoveruitypebeat(self,thing, surface, my_font):
        score = thing.score
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

        lines = thing.totallines
        linesval = str(lines)
        lv = thing.lv
        lvval = str(lv)
        text_score = my_font.render('SCORE:', False, (255, 255, 255))
        surface.blit(text_score, (40, 220))
        text_scorenum = my_font.render(scoreval, False, (255, 255, 255))
        surface.blit(text_scorenum, (130, 220))
        text_lines = my_font.render('LINES:', False, (255, 255, 255))
        surface.blit(text_lines, (420, 220))
        text_linesval = my_font.render(linesval, False, (255, 255, 255))
        surface.blit(text_linesval, (500, 220))
        text_lv = my_font.render('LEVEL:', False, (255, 255, 255))
        surface.blit(text_lv, (250, 220))
        text_lvval = my_font.render(lvval, False, (255, 255, 255))
        surface.blit(text_lvval, (330, 220))


    def gameoverscreen(self,text, font, text_col, x, y, screen):
        img = font.render(text, False, text_col)
        screen.blit(img, (x, y))
