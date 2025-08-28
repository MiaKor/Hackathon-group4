import pygame

import consts

screen = pygame.display.set_mode(

        (consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


def draw_message(message, font_size, color, location):
    font = pygame.font.SysFont(consts.FONT_PATH, font_size)

    text_img = font.render(message, True, color)

    screen.blit(text_img, location)
