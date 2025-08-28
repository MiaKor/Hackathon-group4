import main
import pygame
import sys
import org
from button import Button
import donator

def donation_choice():
    while True:
        main.SCREEN.blit(main.BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = main.get_font(100).render("Please choose your type of contribution", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        donation_button = Button(image=pygame.image.load("assets/Play Rect.png"),
                                pos=(400, 400),
                                text_input="donation", font=main.get_font(75),
                                base_color="#d7fcd4", hovering_color="White")

        volunteer_button = Button(image=pygame.image.load("assets/Play Rect.png"),
                                pos=(400, 400),
                                text_input="volunteer", font=main.get_font(75),
                                base_color="#d7fcd4", hovering_color="White")

        contr_button = Button(image=pygame.image.load("assets/Play Rect.png"),
                                pos=(400, 400),
                                text_input="donate groceries", font=main.get_font(75),
                                base_color="#d7fcd4", hovering_color="White")

        # OPTIONS_BUTTON = Button(
        #     image=pygame.image.load("assets/Play Rect.png"), pos=(800, 400),
        #     text_input="ORG", font=main.get_font(75), base_color="#d7fcd4",
        #     hovering_color="White")

        main.SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [donation_button, contr_button, volunteer_button]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(main.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if donation_button.checkForInput(MENU_MOUSE_POS):
                    pass
                if volunteer_button.checkForInput(MENU_MOUSE_POS):
                    pass
                if contr_button.checkForInput(MENU_MOUSE_POS):
                    pass

        pygame.display.update()