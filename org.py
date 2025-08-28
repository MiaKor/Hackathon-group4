import sys

import main

import pygame

from button import Button

from amuta import amuta

pygame.init()


def org():
    while True:

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        main.SCREEN.fill("white")

        # org_text = main.get_font(45).render("This is a blank screen.", True,

        #                                    "Black")

        # org_rect = org_text.get_rect(center=(640, 260))

        # main.SCREEN.blit(org_text, org_rect)

        my_name = "hello"

        my_data = {"hello": [["ori", "058", "rishon"], ["dana", "069", "nes"]]}

        amuta(my_name, my_data)

        org_back = Button(image=None, pos=(640, 460),

                          text_input="BACK", font=main.get_font(75),

                          base_color="Black", hovering_color="Green")

        org_back.changeColor(OPTIONS_MOUSE_POS)

        org_back.update(main.SCREEN)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if org_back.checkForInput(OPTIONS_MOUSE_POS):
                    main.main_menu()

        pygame.display.update()
