first_ngo = next(
                        iter(db["ngos"].values()))  # לוקח את המילון הראשון
                    first_ngo["donors"].append({
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