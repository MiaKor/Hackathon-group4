
import consts
import main
import pygame

def tree(num):
    if num==1:
        img = pygame.image.load( "assets/TREE1.png")
    if num==2:
        img = pygame.image.load("assets/TREE2.png")
    if num==3:
        img = pygame.image.load("assets/TREE3.png")
    main.SCREEN.blit(img, (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2))

