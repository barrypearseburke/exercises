__author__ = 'Barry'
"""
import pygame
pygame.init()


pygame.display.set_caption("pygame hello world")

#background.fill(255,0,0)
screen = pygame.display.set_mode(size)

"""

import pygame

background_colour = (55,125,72)
size =width,height =1280,720

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)

pygame.display.flip()
#this keeps the window open
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False