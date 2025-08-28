import sys
import consts
import main
import pygame
import donation_choice
from button import Button
from donation_choice import donation_choice
import db

pygame.init()

import sys
import pygame

#
pygame.init()
def donator():
    donor_name = ""
    donor_phone = ""
    donor_city = ""
    active_field = None

    while True:
        main.SCREEN.fill("white")
        PLAY_MOUSE_POS = pygame.mouse.get_pos()


        donator_text = main.get_font(45).render(
            "Choose your desired organisation: ", True,
            "black")
        main.SCREEN.blit(donator_text, donator_text.get_rect(center=(640, 60)))


        font = main.get_font(30)
        name_label = font.render("Your Name:", True, "black")
        phone_label = font.render("Phone:", True, "black")
        city_label = font.render("Your city:", True, "black")
        main.SCREEN.blit(name_label, (200, 200))
        main.SCREEN.blit(phone_label, (200, 300))
        main.SCREEN.blit(city_label , (200, 400))
        input_boxes = {
            "name": pygame.Rect(500, 190, 400, 40),
            "phone": pygame.Rect(500, 290, 400, 40),
            "city" : pygame.Rect(500, 390, 400, 40),
        }
        pygame.draw.rect(main.SCREEN, "white", input_boxes["name"])
        pygame.draw.rect(main.SCREEN, "white", input_boxes["phone"])
        pygame.draw.rect(main.SCREEN, "white", input_boxes["city"])
        main.SCREEN.blit(font.render(donor_name, True, "black"), (510, 195))
        main.SCREEN.blit(font.render(donor_phone, True, "black"), (510, 295))
        main.SCREEN.blit(font.render(donor_city, True, "black"), (510, 395))


        back_btn = Button(image=None, pos=(400, 500),
                          text_input="BACK", font=main.get_font(40),
                          base_color="black", hovering_color="green")
        next_btn = Button(image=None, pos=(800, 500),
                          text_input="NEXT", font=main.get_font(40),
                          base_color="black", hovering_color="green")

        for btn in [back_btn, next_btn]:
            btn.changeColor(PLAY_MOUSE_POS)
            btn.update(main.SCREEN)

        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.checkForInput(PLAY_MOUSE_POS):
                    main.main_menu()
                if next_btn.checkForInput(PLAY_MOUSE_POS):
                    for ngo in db.db["ngos"].values():
                        ngo["donors"].append({
                            "name": donor_name,
                            "phone": donor_phone,
                            "city": donor_city
                    })
                    import donation_choice
                    donation_choice.donation_choice()
                for key, rect in input_boxes.items():
                    color = "black" if active_field == key else "gray"
                    pygame.draw.rect(main.SCREEN, "white", rect)
                    pygame.draw.rect(main.SCREEN, color, rect, 2)

                    if rect.collidepoint(event.pos):
                        active_field = key
            if event.type == pygame.KEYDOWN and active_field:
                if event.key == pygame.K_BACKSPACE:
                    if active_field == "name":
                        donor_name = donor_name[:-1]
                    elif active_field == "phone":
                        donor_phone = donor_phone[:-1]
                    elif active_field == "city":
                        donor_city = donor_phone[:-1]

                else:
                    if active_field == "name":
                        donor_name += event.unicode
                    elif active_field == "phone":
                        donor_phone += event.unicode
                    elif active_field == "city":
                        donor_city += event.unicode


        pygame.display.update()




