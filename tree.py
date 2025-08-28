
import consts
import main
import pygame

def tree(num):
    if num == 0:
        img=pygame.image.load("assets/TREE0.webp")
        main.SCREEN.blit(img, (consts.SCREEN_WIDTH / 2+100, consts.SCREEN_HEIGHT / 2))
    if num==1:
        img = pygame.image.load( "assets/TREE1.png")
        main.SCREEN.blit(img, (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2))

    if num==2:
        img = pygame.image.load("assets/TREE2.png")
        main.SCREEN.blit(img, (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2-100))

    if num==3:
        img = pygame.image.load("assets/TREE3.png")
        main.SCREEN.blit(img, (consts.SCREEN_WIDTH/2, consts.SCREEN_HEIGHT/2-100))



def get_num(num):
    my_num=num
    return my_num
