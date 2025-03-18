import pygame as py
from game import game

py.init()
white = (255, 255, 255)
screen = py.display.set_mode((600, 600))
py.display.set_caption("Block Descenders")
moveleft = False
moveright = False
movedown = False
clock = py.time.Clock()

game = game()
gameupdate = py.USEREVENT


while True:
    for event in py.event.get():
        py.time.set_timer(gameupdate, game.getinterval())
        if event.type == py.QUIT:
            py.quit()
        if event.type == py.KEYDOWN:
            if game.gameover == True:
                game.gameover = False
                game.reset()
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

    screen.fill(white)
    game.draw(screen)
    game.ui(screen)
    game.otherui(screen)


    py.display.update()
    clock.tick(60)

