import main
import pygame
import sys
import org
from button import Button
import donator

def donate_amuta ():
    while True:
        main.SCREEN.blit(main.BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = main.get_font(100).render("choose you desired organization:", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))



