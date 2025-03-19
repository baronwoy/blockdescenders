import pygame as py
from game import game
from leaderboard import leaderboard
from menu import menu
from instructions import instructions
from gameover import gameover

py.init()
white = (255, 255, 255)
screen = py.display.set_mode((600, 600))
py.display.set_caption("Block Descenders")
moveleft = False
moveright = False
movedown = False
clock = py.time.Clock()
inputbox = py.Rect(200, 150, 100, 30)
color_inactive = py.Color('lightskyblue3')
color_active = py.Color('dodgerblue2')
color = color_inactive
active = False
text = ''
my_font = py.font.Font(None, 30)
leaderboardvisibility = False
menuvisible = True
gameinstructions = False

game = game()
leaderboard = leaderboard()
menu = menu()
instructions = instructions()
gameover = gameover()
updateflag = False
gameupdate = py.USEREVENT

while True:

    for event in py.event.get():
        py.time.set_timer(gameupdate, game.getinterval())
        if event.type == py.QUIT:
            py.quit()
        if menuvisible == True and gameinstructions == False:
            button, button2 = menu.menuui(screen)
            py.display.update()
            clock.tick(60)
            if event.type == py.MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    gameinstructions = True
                elif button2.collidepoint(event.pos):
                    menuvisible = False
                else:
                    pass
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
            bigfont = py.font.Font(None, 50)
            gameover.gameoverscreen("GAME OVER", bigfont, (white), 190, 60, screen)
            promptname = my_font.render("Enter name for leaderboard:", False, white)
            screen.blit(promptname, (150,110))
            gameover.gameoveruitypebeat(game, screen, my_font)
            if event.type == py.MOUSEBUTTONDOWN:
                if inputbox.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == py.KEYDOWN:
                if active:
                    if event.key == py.K_RETURN:
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
            if event.key == py.K_LEFT and game.gameover == False and menuvisible == False:
                moveleft = True
            elif event.key == py.K_RIGHT and game.gameover == False and menuvisible == False:
                moveright = True
            elif event.key == py.K_DOWN and game.gameover == False and menuvisible == False:
                movedown = True
            elif event.key == py.K_UP and game.gameover == False and menuvisible == False:
                game.rotate()
            elif event.key == py.K_z and game.gameover == False and menuvisible == False:
                game.rotateCCW()
            elif event.key == py.K_SPACE and game.gameover == False and menuvisible == False:
                game.dropblock()
            elif event.key == py.K_c and game.gameover == False and menuvisible == False:
                game.holdblock()
        if event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                moveleft = False
            elif event.key == py.K_RIGHT:
                moveright = False
            elif event.key == py.K_DOWN:
                movedown = False
        if event.type == gameupdate and game.gameover == False and menuvisible == False:
            game.move_down()
        if moveleft == True:
            game.move_left()
        if moveright == True:
            game.move_right()
        if movedown == True:
            game.move_down()

    if game.gameover == False and menuvisible == False:
        screen.fill(white)
        game.draw(screen)
        game.ui(screen)
        game.otherui(screen)
        py.display.update()
        clock.tick(60)


    if gameinstructions == True and menuvisible == True:
        exitbox = instructions.instructionsui(screen)
        if event.type == py.MOUSEBUTTONDOWN:
            if exitbox.collidepoint(event.pos):
                gameinstructions = False
        py.display.update()
        clock.tick(60)




