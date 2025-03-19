import pygame as py
import mysql.connector
from game import game
from leaderboard import leaderboard

def gameoveruitypebeat(self, surface, my_font):
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
    text_score = my_font.render('SCORE:', False, (255, 255, 255))
    surface.blit(text_score, (175, 20))
    text_scorenum = my_font.render(scoreval, False, (255, 255, 255))
    surface.blit(text_scorenum, (265, 20))
    text_lines = my_font.render('Lines:', False, (255, 255, 255))
    surface.blit(text_lines, (65, 443))
    text_linesval = my_font.render(linesval, False, (255, 255, 255))
    surface.blit(text_linesval, (135, 443))
    text_lv = my_font.render('Lv:', False, (255, 255, 255))
    surface.blit(text_lv, (65, 517))
    text_lvval = my_font.render(lvval, False, (255, 255, 255))
    surface.blit(text_lvval, (135, 517))

py.init()
white = (255, 255, 255)
screen = py.display.set_mode((600, 600))
py.display.set_caption("Block Descenders")
moveleft = False
moveright = False
movedown = False
clock = py.time.Clock()
inputbox = py.Rect(100, 100, 100, 30)
color_inactive = py.Color('lightskyblue3')
color_active = py.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
my_font = py.font.Font(None, 30)
leaderboardvisibility = False

game = game()
leaderboard = leaderboard()
updateflag = False
gameupdate = py.USEREVENT
def gameoverscreen(text, font, text_col, x, y):
    img = font.render(text, False, text_col)
    screen.blit(img, (x,y))

while True:

    for event in py.event.get():
        py.time.set_timer(gameupdate, game.getinterval())
        if event.type == py.QUIT:
            py.quit()
        if leaderboardvisibility == True and game.gameover == True:
            if updateflag == True:
                leaderboard.insert(text, game.lv, game.totallines, game.score)
                updateflag = False
            leaderboard.display(screen)
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    game.reset()
                    leaderboardvisibility = False
                    text = ''
            py.display.flip()
            clock.tick(60)


        if game.gameover == True and leaderboardvisibility == False:
            screen.fill((0,0,0))
            gameoverscreen("GAME OVER", my_font, (255,255,255), 0, 0)
            gameoveruitypebeat(game, screen, my_font)
            if event.type == py.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == py.KEYDOWN:
                if active:
                    if event.key == py.K_RETURN:
                        print(text)
                        active = False
                        leaderboardvisibility = True
                        updateflag = True
                    elif event.key == py.K_BACKSPACE:
                        text = text[:-1]
                    elif len(text) > 4:
                        text = text[:-1]
                    else:
                        text += event.unicode
            texts = my_font.render(text, False, color)
            width = max(200, texts.get_width()+10)
            inputbox.w = width
            screen.blit(texts, (inputbox.x +5, inputbox.y + 5))
            py.draw.rect(screen, color, inputbox, 2)
            py.display.flip()
            clock.tick(60)

        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT and game.gameover == False:
                moveleft = True
            elif event.key == py.K_RIGHT and game.gameover == False:
                moveright = True
            elif event.key == py.K_DOWN and game.gameover == False:
                movedown = True
            elif event.key == py.K_UP and game.gameover == False:
                game.rotate()
            elif event.key == py.K_z and game.gameover == False:
                game.rotate()
            elif event.key == py.K_SPACE and game.gameover == False:
                game.dropblock()
            elif event.key == py.K_c and game.gameover == False:
                game.holdblock()
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                moveleft = False
            elif event.key == py.K_RIGHT:
                moveright = False
            elif event.key == py.K_DOWN:
                movedown = False
        if event.type == gameupdate and game.gameover == False:
            game.move_down()
        if moveleft == True:
            game.move_left()
        if moveright == True:
            game.move_right()
        if movedown == True:
            game.move_down()

    if game.gameover == False:
        screen.fill(white)
        game.draw(screen)
        game.ui(screen)
        game.otherui(screen)
        py.display.update()
        clock.tick(60)





