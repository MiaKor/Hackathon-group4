import pygame
import sys

import org
from button import Button
import donator

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background1.jpg")
BG= pygame.transform.scale(BG, (1280, 720))



def get_font(size):
    return pygame.font.Font("assets/font.otf", size)



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("Welcome to ConTreebute", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        donator_button = Button(image=pygame.image.load("assets/Play Rect.png"),
                             pos=(400, 400),
                             text_input="donator", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(
            image=pygame.image.load("assets/Play Rect.png"), pos=(800, 400),
            text_input="ORG", font=get_font(75), base_color="#d7fcd4",
            hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"),
                             pos=(640, 550),
                             text_input="QUIT", font=get_font(75),
                             base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [donator_button, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if donator_button.checkForInput(MENU_MOUSE_POS):
                    donator.donator()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    org.org()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

if __name__ == "__main__":
    main_menu()