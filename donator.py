import sys

import main
import pygame

from button import Button

pygame.init()
def donator():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        main.SCREEN.fill("white")

        donator_text = main.get_font(45).render("choose your desired organisation: ", True,
                                        "black")
        donator_rect = donator_text.get_rect(center=(640, 260))
        main.SCREEN.blit(donator_text, donator_rect)

        donator_back = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=main.get_font(75),
                              base_color="White", hovering_color="Green")

        donator_back.changeColor(PLAY_MOUSE_POS)
        donator_back.update(main.SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if donator_back.checkForInput(PLAY_MOUSE_POS):
                    main.main_menu()

        pygame.display.update()