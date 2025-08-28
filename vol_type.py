import sys
import pygame
import main
from button import Button
from db import db

pygame.init()


def vol_type():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        main.SCREEN.fill("white")
        title = main.get_font(40).render("Choose your desired organisation:",
                                         True, "black")
        main.SCREEN.blit(title, title.get_rect(center=(640, 80)))
        buttons = []
        y = 160
        for ngo_name in db["ngos"].keys():
            btn = Button(
                    image=None,
                    pos=(640, y),
                    text_input=ngo_name,

                    font=main.get_font(30),

                    base_color="black",

                    hovering_color="green"

            )

            btn.changeColor(PLAY_MOUSE_POS)

            btn.update(main.SCREEN)

            buttons.append(btn)

            y += 60
        donator_back = Button(image=None, pos=(640, 660),
                              text_input="BACK", font=main.get_font(50),
                              base_color="black", hovering_color="green")

        donator_back.changeColor(PLAY_MOUSE_POS)
        donator_back.update(main.SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if donator_back.checkForInput(PLAY_MOUSE_POS):
                    main.main_menu()
                for btn in buttons:
                    if btn.checkForInput(PLAY_MOUSE_POS):
                        print(f"Selected NGO: {btn.text_input}")

        pygame.display.update()