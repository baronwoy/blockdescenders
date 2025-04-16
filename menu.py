import pygame as py

# home screen ui
class menu():
    def menuui(self, screen):
        screen.fill((100, 100, 100))
        menufont = py.font.Font(None, 110)
        textfont = py.font.Font(None, 35)
        headertext1 = menufont.render("BLOCK", False, (0, 0, 0))
        headertext2 = menufont.render("DESCENDERS", False, (0, 0, 0))
        instrtext1 = textfont.render("GAME", False, (0, 0, 0))
        screen.blit(instrtext1, (261, 412))
        instrtext2 = textfont.render("INSTRUCTIONS", False, (0, 0, 0))
        screen.blit(instrtext2, (207, 439))
        instrtext3 = textfont.render("START", False, (0, 0, 0))
        screen.blit(instrtext3, (262, 524))
        screen.blit(headertext1, (170, 30))
        screen.blit(headertext2, (43, 110))
        button = py.Rect((200, 400), (200, 75))
        button2 = py.Rect((200, 510), (200, 50))
        py.draw.rect(screen, (0, 0, 0), button, width=1)
        py.draw.rect(screen, (0, 0, 0), button2, width=1)
        return button, button2
