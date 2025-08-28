import sys

import consts
import main
import pygame
import donation_choice
from button import Button
from donation_choice import donation_choice

pygame.init()


def donator():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        main.SCREEN.fill("white")

        donator_text = main.get_font(45).render(
            "choose your desired organisation: ", True,
            "black")
        donator_rect = donator_text.get_rect(center=(640, 260))
        main.SCREEN.blit(donator_text, donator_rect)

        donator_submit = Button(image=None, pos=(400, 500),
                                text_input="submit", font=main.get_font(75),
                                base_color="black", hovering_color="Green")
        donator_back = Button(image=None, pos=(600, 500),
                              text_input="BACK", font=main.get_font(75),
                              base_color="black", hovering_color="Green")

        for button in [donator_back, donator_submit]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(main.SCREEN)

        donator_back.update(main.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if donator_back.checkForInput(PLAY_MOUSE_POS):
                    main.main_menu()
                if donator_submit.checkForInput(PLAY_MOUSE_POS):
                    donation_choice()
        pygame.display.update()
