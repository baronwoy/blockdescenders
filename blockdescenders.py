# ~ Import libraries ~ #
import pygame as py
import pygame_menu as pym

# ~ Display the Menu and initalise globals
py.init()
surface = py.display.set_mode((500, 600))
clock = py.time.Clock()

# ~ Game Function
def start_the_game():
    pass

# ~ Game Instructions Page initialisation ~ #
instr_menu = pym.Menu(
height = 600,
width = 500,
title = 'Game Instructions',
theme = pym.themes.THEME_DARK,
)

# ~ Game Instruction Table
instr_table = instr_menu.add.table("Instructions Table")
instr_table.add_row(("Left and Right arrow keys", "Move Left and Right"), cell_font_size=20, cell_padding=5,
                    cell_border_width=0)
instr_table.add_row(("Down arrow", "Speed Up Block"), cell_font_size=20, cell_padding=5, cell_border_width=0)
instr_table.add_row(("Up arrow", "Rotate Clockwise"), cell_font_size=20, cell_padding=5, cell_border_width=0)
instr_table.add_row(("Space", "Hard Drop"), cell_font_size=20, cell_padding=5, cell_border_width=0)
instr_table.add_row(("C", "Hold"), cell_font_size=20, cell_padding=5, cell_border_width=0)
instr_table.add_row(("Z", "Rotate Anti-Clockwise"), cell_font_size=20, cell_padding=5, cell_border_width=0)
instr_table.resize(500, 600)

# ~ Display the GUI of the Main menu
TITLE = "BLOCK " + "\n" + "DESCENDERS"
menu = pym.Menu('Block Descenders', 500, 600,
                theme=pym.themes.THEME_DARK)

menu.add.label(TITLE, font_size=55, )
menu.add.image("boy.png")  # Placeholder
menu.add.button('Game Instructions', instr_menu)
menu.add.button('Start', start_the_game)
menu.add.button('Quit', pym.events.EXIT)

menu.mainloop(surface)
